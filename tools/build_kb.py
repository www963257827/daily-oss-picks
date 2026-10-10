#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
知识库构建脚本：从单一数据源生成全部索引产物。

数据源（唯一需要手工/由 AI 维护的地方）：
    knowledge-base/data/entries.jsonl    每行一条收录内容
    knowledge-base/data/categories.json  分区定义
    knowledge-base/data/meta.json        杂项字符串
    knowledge-base/data/header.md        顶部标题 + 使用说明
    knowledge-base/data/inbox.md         待整理区正文
    knowledge-base/data/footer.md        总结与趋势观察正文
    knowledge-base/data/usermarks.json   收藏(star)与置顶(pin)，按条目 id 绑定

产物（全部自动生成，不要手工编辑）：
    knowledge-base.html                 门户级本地看板（在根目录，双击即开）
    knowledge-base/我的知识库.md          主索引（锚点目录 + 置顶/收藏标记 + 分区图标）
    knowledge-base/标签索引.md            按标签反查
    knowledge-base/时间线.md              按收录日期倒序

安全护栏：
    构建前校验《我的知识库.md》的 SHA256 是否等于上一次构建/迁移时记录的值。
    若不一致，说明有其他人或其它对话改过该文件，脚本会拒绝覆盖，
    需要先执行 `python tools/migrate_to_jsonl.py --force` 吸收改动再构建。

用法：
    python tools/build_kb.py                # 构建全部产物
    python tools/build_kb.py --dry-run      # 只在终端打印统计，不写文件
    python tools/build_kb.py --no-guard     # 跳过哈希护栏（明确知道自己在做什么时）
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

WORKSPACE = Path(__file__).resolve().parent.parent
DATA_DIR = WORKSPACE / "data"                 # 仓库内 data/ 目录
OUT_DIR = WORKSPACE / "docs"                  # GitHub Pages 目录
KB_MD = OUT_DIR / "README_CH.md"             # 中文版
KB_HTML = OUT_DIR / "index.html"              # GitHub Pages 入口

ENTRIES = DATA_DIR / "entries.jsonl"
CATEGORIES = DATA_DIR / "categories.json"
META = DATA_DIR / "meta.json"
MARKS_FILE = DATA_DIR / "usermarks.json"
HASH_FILE = DATA_DIR / "source_hash.txt"

ARCH_CAP = 6000          # 嵌入看板的单篇归档正文字数上限

# Gitee 合规过滤：命中的条目不进入 Gitee 版产物（本地与 GitHub 版不受影响）
# 词表按上下文精修：避免误伤协议名（BitTorrent）、快捷键说明（Cheat Sheet）、
# 无害的"逆向案例"等；真正的安全类条目由 渗透/反编译/pentest 等词兜住。
SENS_RE_GITEE = re.compile(
    r"激活工具|激活码|数字权利|破解|防撤回|盗版|外挂|翻墙|科学上网|v2ray|shadowsocks"
    r"|种子站|渗透|反编译|crack|keygen|exploit|pentest|hacking"
    r"|wifite|cheat.?engine|unlock", re.I)

# 英文阅读版：分区标题（渲染层内容，随代码走）
CAT_TITLES_EN = {
    1: "AI Coding Agents · Runtimes & Methodologies",
    2: "Mobile Automation Agents",
    3: "Agent Memory & Knowledge Distillation",
    4: "Writing & Text-Style Skills",
    5: "Video Creation Skills",
    6: "Domain Skills (Diagrams / CAD / Research / Patents / Office)",
    7: "Security · Audit & Reverse Engineering",
    8: "Skill Collections & Ecosystem",
    9: "Code Intelligence / RAG / Code Review",
    10: "Speech & TTS",
    11: "Model Training & Fine-tuning",
    12: "Local Inference Engines & Optimization",
    13: "Image / Video / Music Generation",
    14: "AI Infrastructure · Gateways & Self-hosted Platforms",
    15: "Content Discovery & Intelligence",
    16: "WPF / .NET UI Frameworks & Control Libraries",
    17: "System Tools & Desktop Productivity",
    18: "Files · Downloads · Photo Management",
    19: "Image Viewers & Media Players",
    20: "AI Desktop Apps",
    21: "Cross-device Tools",
    22: "GIS",
    23: "Articles / AI News",
    24: "Developer Resources & Curated Lists",
    25: "DevOps / Developer Tools",
}

TRANS_FILE = DATA_DIR / "translation-en.json"   # 条目 id -> 英文定位一行（英文阅读版用）
TAGS_EN_FILE = DATA_DIR / "tags-en.json"        # 中文标签 -> 英文标签（英文阅读版用）


def load_tags_en():
    if not TAGS_EN_FILE.exists():
        return {}
    return json.loads(TAGS_EN_FILE.read_text(encoding="utf-8"))


def en_tags(tags, tags_en):
    """英文阅读版的标签：中文标签查映射表转英文，映射后去重保序。"""
    out, seen = [], set()
    for t in tags:
        t2 = tags_en.get(t, t)
        if t2 not in seen:
            seen.add(t2)
            out.append(t2)
    return out
CAT_ICONS = {            # 分区图标（渲染层内容，随代码走，不进数据）
    1: "🤖", 2: "📱", 3: "🧠", 4: "✍️", 5: "🎬", 6: "🧰", 7: "🔐", 8: "🧩", 9: "💻",
    10: "🎙️", 11: "🔧", 12: "⚡", 13: "🎨", 14: "🏗️", 15: "🛰️", 16: "🖼️", 17: "🛠️",
    18: "📁", 19: "▶️", 20: "✨", 21: "🔗", 22: "🗺️", 23: "📰", 24: "📚", 25: "🚀",
}


# ---------------------------------------------------------------- 数据加载

def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def load():
    if not ENTRIES.exists():
        sys.exit(f"[错误] 缺少数据源 {ENTRIES}，请先运行 tools/migrate_to_jsonl.py")
    entries = [json.loads(l) for l in ENTRIES.read_text(encoding="utf-8").splitlines() if l.strip()]
    categories = json.loads(CATEGORIES.read_text(encoding="utf-8"))
    meta = json.loads(META.read_text(encoding="utf-8"))
    header = (DATA_DIR / "header.md").read_text(encoding="utf-8").rstrip()
    inbox = (DATA_DIR / "inbox.md").read_text(encoding="utf-8").rstrip()
    footer = (DATA_DIR / "footer.md").read_text(encoding="utf-8").rstrip()
    marks = load_marks()
    return entries, categories, meta, header, inbox, footer, marks


def load_marks() -> dict:
    if not MARKS_FILE.exists():
        return {"star": [], "pin": []}
    m = json.loads(MARKS_FILE.read_text(encoding="utf-8"))
    return {"star": list(m.get("star", [])), "pin": list(m.get("pin", []))}


def load_archive_text(rel: str) -> str:
    """读取归档正文嵌入看板（全文检索与详情展开用），超长截断。"""
    if not rel:
        return ""
    p = WORKSPACE / rel
    if not p.exists():
        return ""
    try:
        t = p.read_text(encoding="utf-8", errors="replace").strip()
    except OSError:
        return ""
    if len(t) > ARCH_CAP:
        t = t[:ARCH_CAP] + "\n…（超长截断，完整内容见归档文件）"
    return t


# ---------------------------------------------------------------- 名称排序与引用渲染

# 名称排序键：英文名按字母序，中文名按拼音（pypinyin 可用时）；装不上则退回码点序
try:
    from pypinyin import lazy_pinyin

    def name_sort_key(name: str) -> str:
        return "".join(lazy_pinyin(name or "")).casefold()
except ImportError:
    def name_sort_key(name: str) -> str:
        return (name or "").casefold()


RE_REF = re.compile(r"\[\[e(\d+)\]\]")
_REF_STOP = "、（），。；！？ \n"


def resolve_refs(text: str, ref_map: dict) -> str:
    """把 [[e编号]] 渲染为可点击链接：token 后跟的名称片段（全名或仓库短名）原样作为
    链接文本，保持原文观感；没跟名称的用条目全名。migrate_to_jsonl.py 吸收产物时按
    「url 命中条目且链接文本是条目名的一部分」反推回 [[e编号]]，保证回环无损。
    未知编号原样保留（lint W7 会抓）。"""
    if not text or "[[e" not in text:
        return text
    out, i = [], 0
    while True:
        m = RE_REF.search(text, i)
        if not m:
            out.append(text[i:])
            break
        out.append(text[i:m.start()])
        info = ref_map.get(int(m.group(1)))
        if info is None:
            out.append(m.group(0))
            i = m.end()
            continue
        name, url = info
        k = m.end()
        if k < len(text) and text[k] == " ":
            k += 1
        j = k
        while j < len(text) and text[j] not in _REF_STOP:
            j += 1
        seg = text[k:j]
        if seg and (seg in name or name in seg):
            out.append(f"[{seg}]({url})")
            i = j
        else:
            out.append(f"[{name}]({url})")
            i = m.end()
    return "".join(out)


# ---------------------------------------------------------------- Markdown 生成

def render_bullets(entry, ref_map=None) -> str:
    out = []
    for b in entry["bullets"]:
        text = resolve_refs(b["text"], ref_map) if ref_map else b["text"]
        out.append(f"- **{b['label']}**：{text}")
    return "\n".join(out)


def render_entry(entry, ref_map=None, star=False, pin=False) -> str:
    prefix = ("📌" if pin else "") + ("⭐" if star else "")
    head = f"### {prefix}{' ' if prefix else ''}[{entry['name']}]({entry['url']})"
    body = render_bullets(entry, ref_map)
    return f"{head}\n{body}" if body else head


def build_markdown(entries, categories, meta, header, inbox, footer, marks, today) -> str:
    ref_map = {e["id"]: (e["name"], e["url"]) for e in entries}
    star_set = set(marks["star"])
    pin_order = {i: n for n, i in enumerate(marks["pin"])}
    by_cat = defaultdict(list)
    for e in entries:
        by_cat[e["category"]].append(e)
    for v in by_cat.values():
        v.sort(key=lambda x: name_sort_key(x["name"]))            # 名称序
        v.sort(key=lambda x: pin_order.get(x["id"], 10 ** 9))     # 置顶最前（稳定排序）

    articles = sum(1 for e in entries if e.get("type") == "article")
    projects = len(entries) - articles
    total = len(entries)

    stat = (f"> 📅 最后更新：{today} ｜ 共收录 **{total}** 条内容"
            f"（{projects} {meta.get('project_word', '个项目')} + "
            f"{articles} {meta.get('article_word', '篇精选文章')}）")

    rows = ["| 分区 | 内容说明 | 数量 |", "|-|-|-|"]
    for c in categories:
        rows.append(f"| [{c['numeral']}、{c['title']}](#sec-{c['id']}) "
                    f"| {c['index_desc']} | {len(by_cat[c['id']])} |")
    rows.append(f"| 待整理区 | {meta.get('inbox_row_desc', '新收藏内容暂存处')} | — |")
    dir_block = "## 📑 目录索引\n\n" + "\n".join(rows)

    parts = [header + "\n" + stat, dir_block]

    for c in categories:
        if c.get("sep"):
            parts.append("---")
        icon = CAT_ICONS.get(c["id"], "")
        parts.append(f'<a id="sec-{c["id"]}"></a>')
        block = f"## {icon} {c['numeral']}、{c['title']}（{len(by_cat[c['id']])}）"
        if c.get("intro"):
            block += "\n\n" + c["intro"]
        for e in by_cat[c["id"]]:
            block += "\n\n" + render_entry(e, ref_map,
                                           star=e["id"] in star_set,
                                           pin=e["id"] in pin_order)
        parts.append(block)

    parts.append("---")
    parts.append(inbox)
    parts.append("---")
    parts.append(footer)

    return "\n\n".join(parts) + "\n"


# ---------------------------------------------------------------- 附属索引

def build_tag_index(entries) -> str:
    tag_map = defaultdict(list)
    for e in entries:
        for t in e.get("tags", []):
            tag_map[t].append(e)
    lines = ["# 标签索引", "",
             f"> 自动生成于 {dt.date.today().isoformat()}，请勿手工编辑。"
             f"共 {len(tag_map)} 个标签，覆盖 {len(entries)} 条内容。", ""]
    for tag, items in sorted(tag_map.items(), key=lambda kv: (-len(kv[1]), kv[0])):
        lines.append(f"## `#{tag}`（{len(items)}）")
        lines.append("")
        for e in sorted(items, key=lambda x: (x["category"], name_sort_key(x["name"]))):
            lines.append(f"- [{e['name']}]({e['url']})")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


def build_timeline(entries) -> str:
    ref_map = {e["id"]: (e["name"], e["url"]) for e in entries}
    groups = defaultdict(list)
    for e in entries:
        groups[e.get("added") or "日期未知"].append(e)
    lines = ["# 收录时间线", "",
             f"> 自动生成于 {dt.date.today().isoformat()}，请勿手工编辑。按收录日期倒序。", ""]
    for day in sorted(groups, reverse=True):
        items = groups[day]
        lines.append(f"## {day}（{len(items)} 条）")
        lines.append("")
        for e in sorted(items, key=lambda x: (x["category"], x["id"])):
            pos = e.get("positioning") or ""
            pos = resolve_refs(pos, ref_map) if pos else ""
            pos = f" — {pos}" if pos else ""
            lines.append(f"- [{e['name']}]({e['url']}){pos}")
        lines.append("")
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------- Gitee 合规版 / 英文阅读版

def is_sensitive_gitee(e) -> bool:
    hay = (e["name"] + " " + (e.get("positioning") or "") + " " + (e.get("summary") or "") +
           " " + " ".join(e.get("tags", [])))
    return bool(SENS_RE_GITEE.search(hay))


def build_gitee_markdown(entries, categories, meta, header, inbox, footer, marks, today):
    """Gitee 合规版：条目级过滤敏感内容、跳过空分区，其余与主索引同构。
    返回 (md, 被过滤条数)。本地与 GitHub 版不受影响。"""
    kept = [e for e in entries if not is_sensitive_gitee(e)]
    dropped = len(entries) - len(kept)
    used_cats = [c for c in categories if any(e["category"] == c["id"] for e in kept)]
    md = build_markdown(kept, used_cats, meta, header, inbox, footer, marks, today)
    note = (f"> ⚠️ **Gitee 合规版**：已按平台内容要求隐藏 {dropped} 条敏感条目，"
            f"完整版见 GitHub 镜像。\n\n")
    md = md.replace("## 📑 目录索引", note + "## 📑 目录索引", 1)
    md = re.sub(r"^> 🌐 \*\*English edition\*\*:.*\n?", "", md, flags=re.M)   # Gitee 无英文版
    return md, dropped


def load_translations():
    if not TRANS_FILE.exists():
        return {}
    return json.loads(TRANS_FILE.read_text(encoding="utf-8"))


def build_english_markdown(entries, categories, trans, today, ref_map=None, tags_en=None):
    """英文阅读版（索引式，GitHub 默认首页）：每条 = 名称链接 + 英文定位一行 + 英文标签/日期。
    定位优先取 data/translation-en.json（键为条目 id），标签经 data/tags-en.json 转英文。"""
    if ref_map is None:
        ref_map = {e["id"]: (e["name"], e["url"]) for e in entries}
    tags_en = tags_en or {}
    articles = sum(1 for e in entries if e.get("type") == "article")
    by_cat = defaultdict(list)
    for e in entries:
        by_cat[e["category"]].append(e)
    used = [c for c in categories if by_cat.get(c["id"])]
    lines = [
        "# Daily Curated Open-Source Projects Knowledge Base",
        "",
        "> 🤖 Auto-updated every day at 06:00 from the GitHub Trending digest mail — "
        "collected, translated (Chinese) and curated.",
        "> 📖 **Full Chinese edition with complete descriptions: [README_CH.md](README_CH.md)** · "
        "this file is the English digest edition (repo default).",
        "",
        f"> Last updated: {today} ｜ **{len(entries)}** entries "
        f"({len(entries) - articles} projects + {articles} articles) ｜ {len(used)} categories",
        "",
        "| # | Category | Count |", "|:-:|-|-|",
    ]
    for c in used:
        lines.append(f"| {c['id']} | {CAT_TITLES_EN.get(c['id'], c['title'])} | {len(by_cat[c['id']])} |")
    lines.append("")
    for c in used:
        lines.append(f"## {c['numeral']}. {CAT_TITLES_EN.get(c['id'], c['title'])} ({len(by_cat[c['id']])})")
        lines.append("")
        for e in sorted(by_cat[c["id"]], key=lambda x: name_sort_key(x["name"])):
            en = (trans.get(str(e["id"])) or "").strip()
            if not en:
                en = resolve_refs(e.get("positioning") or e["name"], ref_map)
            lines.append(f"### [{e['name']}]({e['url']})")
            meta_bits = []
            etags = en_tags(e.get("tags", []), tags_en)
            if etags:
                meta_bits.append(" ".join(f"`#{t}`" for t in etags))
            if e.get("added"):
                meta_bits.append(e["added"])
            if meta_bits:
                lines.append(" · ".join(meta_bits))
            lines.append(en)
            lines.append("")
    lines.append("---")
    lines.append("*English digest auto-generated by `tools/build_kb.py` — one-line positioning per entry. "
                 "Full descriptions live in the Chinese edition and local archives.*")
    return "\n".join(lines).rstrip() + "\n"


# ---------------------------------------------------------------- HTML 看板

HTML_TEMPLATE = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>__TITLE__</title>
<style>
:root{
  --bg:#F5F6FA; --surface:#FFFFFF; --surface2:#EDEFF5; --text:#1A1B25; --muted:#5A5D6E;
  --border:rgba(26,27,37,.10); --brand:#4B3FE3; --brand-soft:#EEF0FF; --brand-strong:#DDE2FF;
  --brand-text:#2A2790; --radius:10px; --radius-card:14px;
  --shadow:0 1px 2px rgba(26,27,37,.05),0 8px 24px rgba(26,27,37,.07);
  --shadow-hover:0 4px 12px rgba(26,27,37,.10),0 18px 44px rgba(26,27,37,.14);
  --font:"Noto Sans CJK SC","WenQuanYi Micro Hei","Microsoft YaHei","PingFang SC",system-ui,-apple-system,"Segoe UI",sans-serif;
  --mono:"JetBrains Mono",ui-monospace,"SF Mono",Menlo,Consolas,monospace;
}
@media (prefers-color-scheme: dark){
  :root{ --bg:#0F0F13; --surface:#17171C; --surface2:#222228; --text:#E6E6E8; --muted:#9C9FA8;
         --border:rgba(230,230,232,.13); --brand:#8B80FF; --brand-soft:#231F52; --brand-strong:#3C2ECA; --brand-text:#CFD8FF; }
}
*{box-sizing:border-box}
body{margin:0;background:var(--bg);color:var(--text);font:400 14px/21px var(--font);-webkit-font-smoothing:antialiased}
.wrap{max-width:min(1840px,calc(100vw - 72px));margin:0 auto;padding:24px 32px 80px}
a{color:inherit}
header.top{margin-bottom:16px}
header.top h1{font:700 26px/34px var(--font);margin:0 0 4px;letter-spacing:.5px}
header.top .sub{color:var(--muted);font:400 13px/20px var(--font);margin-bottom:16px}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(130px,1fr));gap:10px;margin-bottom:16px}
.stat{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius);
      padding:10px 14px;box-shadow:var(--shadow);cursor:pointer;user-select:none;
      transition:transform .15s,border-color .15s,background .15s}
.stat:hover{transform:translateY(-2px);border-color:var(--brand)}
.stat.on{border-color:var(--brand);background:var(--brand-soft)}
.stat b{display:block;font:600 22px/28px var(--mono);color:var(--brand)}
.stat span{color:var(--muted);font:500 12px/16px var(--font)}
.tabs{display:flex;gap:8px;margin:0 0 16px}
.tab{background:var(--surface);border:1px solid var(--border);border-radius:999px;padding:8px 20px;
     font:600 14px/20px var(--font);color:var(--muted);cursor:pointer;box-shadow:var(--shadow)}
.tab:hover{border-color:var(--brand);color:var(--brand)}
.tab.on{background:var(--brand);border-color:var(--brand);color:#fff}
.panel{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-card);
       padding:14px;margin-bottom:12px;box-shadow:var(--shadow);position:sticky;top:0;z-index:20}
.row{display:flex;flex-wrap:wrap;gap:8px;align-items:center}
input[type=search]{flex:1 1 300px;min-width:220px;background:var(--surface2);border:1px solid var(--border);
  border-radius:var(--radius);padding:9px 14px;color:var(--text);font:400 14px/20px var(--font);outline:none}
input[type=search]:focus{border-color:var(--brand)}
select{background:var(--surface2);border:1px solid var(--border);border-radius:var(--radius);
  padding:9px 10px;color:var(--text);font:400 13px/20px var(--font);outline:none;cursor:pointer}
.iconbtn{background:var(--surface2);border:1px solid var(--border);border-radius:var(--radius);
  padding:8px 12px;cursor:pointer;font:500 13px/18px var(--font);color:var(--muted)}
.iconbtn:hover{border-color:var(--brand);color:var(--brand)}
.chips{display:flex;flex-wrap:wrap;gap:6px;margin-top:10px}
.chip{background:var(--surface2);border:1px solid var(--border);border-radius:999px;
  padding:3px 12px;font:500 12px/18px var(--font);color:var(--muted);cursor:pointer;user-select:none}
.chip:hover{border-color:var(--brand);color:var(--brand)}
.chip.on{background:var(--brand-strong);border-color:var(--brand);color:var(--brand-text)}
.catnav{display:flex;flex-wrap:wrap;gap:6px;padding:4px 2px 10px;margin-bottom:6px}
.catnav .chip{white-space:nowrap}
.count{margin:0 2px 12px;display:none}
.count.on{display:flex;gap:8px;align-items:center}
.resetbtn{background:var(--brand-soft);border:1px solid var(--brand);color:var(--brand-text);
  border-radius:999px;padding:5px 16px;font:500 12px/18px var(--font);cursor:pointer}
.resetbtn:hover{background:var(--brand-strong)}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(430px,1fr));gap:14px}
@media (max-width:900px){.cards{grid-template-columns:1fr}}
.card{position:relative;background:var(--surface);border:1px solid var(--border);
      border-radius:var(--radius-card);padding:16px 16px 14px 22px;margin-bottom:0;
      box-shadow:var(--shadow);transition:transform .15s,box-shadow .15s,border-color .15s;overflow:hidden}
.card::before{content:"";position:absolute;left:0;top:0;bottom:0;width:5px;
      background:var(--cat,#888);opacity:.9}
.card:hover{transform:translateY(-2px);box-shadow:var(--shadow-hover);border-color:var(--cat,#888)}
.card.flash{animation:flash 1.6s ease}
@keyframes flash{0%,60%{box-shadow:0 0 0 3px var(--brand)}100%{box-shadow:var(--shadow)}}
.chead{display:flex;flex-wrap:wrap;gap:8px;align-items:baseline;margin-bottom:6px}
.pinflag{font-size:15px}
.name{font:600 16px/24px var(--font);color:var(--text);text-decoration:none;flex:1 1 auto;min-width:200px}
.name:hover{color:var(--brand);text-decoration:underline}
.cat{background:var(--brand-soft);border:1px solid var(--brand);border-radius:999px;
  padding:1px 10px;font:500 11px/17px var(--font);color:var(--brand-text);white-space:nowrap;max-width:46%;
  overflow:hidden;text-overflow:ellipsis}
.date{font:400 12px/17px var(--mono);color:var(--muted);white-space:nowrap}
.pos{margin:0 0 8px;font:400 14px/21px var(--font);color:var(--text)}
.sum{margin:0;font:400 13px/20px var(--font);color:var(--muted);
     display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.sum.open{-webkit-line-clamp:unset;display:block;max-height:160px;overflow-y:auto}
.archhit{display:inline-block;background:var(--brand-soft);border:1px solid var(--brand);
  border-radius:6px;padding:0 8px;font:500 11px/17px var(--font);color:var(--brand-text);margin-top:6px}
.more{margin-top:6px;background:none;border:none;padding:0;color:var(--brand);
  font:500 12px/18px var(--font);cursor:pointer;position:sticky;bottom:0;z-index:3;
  background:var(--surface);border:1px solid var(--border);border-radius:6px;padding:4px 12px;margin-top:8px}
.detail{display:none;margin-top:10px;border-top:1px dashed var(--border);padding-top:10px}
.detail.open{display:block}
.detail .arch{max-height:280px;overflow-y:auto;padding-right:6px;font:400 13px/20px var(--font)}
.detail .arch h1,.detail .arch h2,.detail .arch h3,.detail .arch h4{font:600 14px/22px var(--font);margin:10px 0 4px}
.detail .arch table{border-collapse:collapse;margin:6px 0;font-size:12px;line-height:18px;max-width:100%;display:block;overflow-x:auto}
.detail .arch th,.detail .arch td{border:1px solid var(--border);padding:3px 8px;text-align:left}
.detail .arch th{background:var(--surface2)}
.detail .arch blockquote{border-left:3px solid var(--brand);margin:6px 0;padding:2px 10px;color:var(--muted)}
.detail .arch code{font-family:var(--mono);background:var(--surface2);border-radius:4px;padding:0 5px}
.detail .arch hr{border:none;border-top:1px solid var(--border);margin:10px 0}
.openfile{display:inline-block;margin-top:8px;color:var(--brand);font:500 12px/18px var(--font)}
.meta{display:flex;flex-wrap:wrap;gap:6px;align-items:center;margin-top:10px}
.tag{background:var(--surface2);border:1px solid var(--border);border-radius:6px;
  padding:1px 8px;font:500 12px/18px var(--font);color:var(--muted);cursor:pointer}
.tag:hover{border-color:var(--brand);color:var(--brand)}
.markbtn{margin-left:auto;display:flex;gap:4px}
.markbtn button{background:none;border:1px solid var(--border);border-radius:6px;cursor:pointer;
  font-size:14px;line-height:20px;padding:1px 8px;opacity:.55}
.markbtn button:hover{opacity:1;border-color:var(--brand)}
.markbtn button.on{opacity:1;border-color:var(--brand);background:var(--brand-soft)}
.empty{grid-column:1/-1;padding:60px;text-align:center;color:var(--muted);background:var(--surface);
  border:1px dashed var(--border);border-radius:var(--radius-card)}
.intref{color:var(--brand);cursor:pointer;text-decoration:underline dotted}
/* ---- 总览 ---- */
.ovgrid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
@media (max-width:1100px){.ovgrid{grid-template-columns:repeat(2,minmax(0,1fr))}}
@media (max-width:640px){.ovgrid{grid-template-columns:1fr}}
.ovcard{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-card);
        padding:16px;box-shadow:var(--shadow);min-width:0;overflow:hidden}
.ovcard h3{margin:0 0 12px;font:600 15px/22px var(--font)}
.bar-row{display:grid;grid-template-columns:minmax(80px,130px) 1fr 30px;gap:6px;align-items:center;
         margin:4px 0;cursor:pointer}
.bar-row:hover .bar-label{color:var(--brand)}
.bar-label{font:500 12px/17px var(--font);color:var(--text);white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.bar-track{background:var(--surface2);border-radius:6px;height:14px;overflow:hidden}
.bar{height:100%;border-radius:6px;transition:width .4s}
.bar-num{font:600 12px/17px var(--mono);color:var(--muted);text-align:right}
.trendsvg{width:100%;height:auto;display:block}
.tline{fill:none;stroke:var(--brand);stroke-width:2.5;stroke-linejoin:round;stroke-linecap:round}
.tarea{fill:var(--brand);opacity:.10}
.tdot{fill:var(--brand);stroke:var(--surface);stroke-width:1.5;opacity:.9;cursor:default}
.tdot:hover{opacity:1}
.tgrid{stroke:var(--border);stroke-dasharray:3 4;stroke-width:1}
.tlabel{font:400 9px var(--mono);fill:var(--muted)}
.tval{font:400 9px var(--mono);fill:var(--muted)}
.cloud{display:flex;flex-wrap:wrap;gap:6px 10px;align-items:baseline}
.cloud .ctag{cursor:pointer;color:var(--brand);font-weight:600;opacity:.85}
.cloud .ctag:hover{opacity:1;text-decoration:underline}
.recent{list-style:none;margin:0;padding:0}
.recent li{padding:7px 4px;border-bottom:1px dashed var(--border);cursor:pointer;display:flex;gap:8px;align-items:baseline}
.recent li:last-child{border-bottom:none}
.recent li:hover .rname{color:var(--brand)}
.rdate{font:400 11px/16px var(--mono);color:var(--muted);white-space:nowrap}
.rname{font:500 13px/19px var(--font)}
.rpos{color:var(--muted);font:400 12px/17px var(--font);overflow:hidden;text-overflow:ellipsis;white-space:nowrap;flex:1}
footer{margin-top:28px;color:var(--muted);font:400 12px/18px var(--font)}
mark{background:var(--brand-strong);color:var(--brand-text);border-radius:2px;padding:0 1px}
/* ---- AI 问答 ---- */
#aiview .cfgrow{display:none;gap:8px;flex-wrap:wrap;margin-top:10px}
#aiview .panel.cfgopen .cfgrow{display:flex}
#aiview .cfgrow input{flex:1 1 200px;min-width:150px;background:var(--surface2);border:1px solid var(--border);
  border-radius:var(--radius);padding:8px 12px;color:var(--text);font:400 13px/18px var(--font);outline:none}
#aiview .cfgrow input:focus{border-color:var(--brand)}
#ai-cfgmsg{color:var(--brand);font:500 12px/18px var(--font)}
.aihint{color:var(--muted);font:400 11px/16px var(--font);margin-top:8px}
.chatlog{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-card);
  padding:16px;min-height:160px;max-height:calc(100vh - 440px);overflow-y:auto;box-shadow:var(--shadow)}
.chatlog .msg{margin-bottom:12px;max-width:88%}
.chatlog .msg.user{margin-left:auto;background:var(--brand);color:#fff;border-radius:12px 12px 2px 12px;
  padding:8px 14px;font:500 14px/22px var(--font);width:fit-content}
.chatlog .msg.ai{background:var(--surface2);border-radius:12px 12px 12px 2px;padding:10px 14px}
.chatlog .msg.ai .msginfo{color:var(--muted);font:400 11px/15px var(--font);margin-bottom:4px}
.chatlog .msg.ai .msgbody{font:400 14px/22px var(--font)}
.chatlog .msgbody p{margin:0 0 6px}
.chatlog .msgbody h4{font:600 14px/22px var(--font);margin:8px 0 4px}
.chatlog .msgbody ul{margin:4px 0;padding-left:20px}
.chatlog .msgbody table{border-collapse:collapse;margin:6px 0;font-size:12px;max-width:100%;display:block;overflow-x:auto}
.chatlog .msgbody th,.chatlog .msgbody td{border:1px solid var(--border);padding:3px 8px;text-align:left}
.chatlog .msgbody code{font-family:var(--mono);background:var(--surface);border-radius:4px;padding:0 5px}
.chatlog .msgbody blockquote{border-left:3px solid var(--brand);margin:6px 0;padding:2px 10px;color:var(--muted)}
.chatlog .aierr{color:#d64545;font:500 13px/20px var(--font)}
.chatlog .aierr2{color:var(--muted);font:400 12px/18px var(--font)}
.chatquick{display:flex;flex-wrap:wrap;gap:6px;margin:10px 0}
.chatinput{background:var(--surface);border:1px solid var(--border);border-radius:var(--radius-card);
  padding:10px;box-shadow:var(--shadow)}
.chatinput input{flex:1 1 260px;min-width:200px;background:var(--surface2);border:1px solid var(--border);
  border-radius:var(--radius);padding:10px 14px;color:var(--text);font:400 14px/20px var(--font);outline:none}
.chatinput input:focus{border-color:var(--brand)}
/* ---- 手机适配（视口 ≤768px 自动切换为移动布局） ---- */
@media (max-width:768px){
  .wrap{padding:14px 12px 56px}
  header.top h1{font:700 20px/28px var(--font)}
  header.top .sub{font-size:11px;line-height:16px}
  .stats{grid-template-columns:repeat(4,1fr);gap:6px}
  .stat{padding:8px 4px;text-align:center;border-radius:8px}
  .stat b{font-size:16px;line-height:20px}
  .stat span{font-size:10px;line-height:13px}
  .tabs{margin-bottom:10px}
  .tab{padding:7px 16px;font-size:13px}
  .panel{padding:10px}
  .row{gap:6px}
  input[type=search]{flex:1 1 100%;min-width:0;padding:9px 12px}
  select{flex:1 1 30%;min-width:0;padding:8px 4px;font-size:12px}
  .iconbtn{padding:8px 12px}
  .chips{gap:5px;margin-top:8px}
  .chip{padding:4px 12px}
  .catnav{padding:2px 0 8px}
  .ovgrid{grid-template-columns:1fr;gap:10px}
  .ovcard{padding:12px}
  .ovcard h3{font-size:14px}
  .cards{grid-template-columns:1fr;gap:10px}
  .card{padding:12px 12px 10px 18px}
  .name{font-size:15px;min-width:140px}
  .cat{max-width:100%}
  .pos{font-size:13px}
  .sum{font-size:12.5px}
  .sum.open{max-height:120px}
  .detail .arch{max-height:220px}
  .tag{padding:2px 10px}
  .markbtn button{padding:2px 10px;font-size:15px}
  .recent li{padding:6px 2px}
  #aiview .cfgrow input{flex:1 1 100%}
  .chatlog{max-height:56vh;padding:10px}
  .chatlog .msg{max-width:96%}
  footer{margin-top:20px;font-size:11px}
}
</style>
</head>
<body>
<div class="wrap">
<header class="top">
  <h1>__TITLE__</h1>
  <div class="sub">本地知识库门户 · 检索 / 全文 / 收藏 / 置顶 · 按 <b>/</b> 聚焦搜索</div>
  <div class="stats" id="stats"></div>
  <div class="tabs">
    <button class="tab" id="tab-ov" data-tab="overview">📊 总览</button>
    <button class="tab" id="tab-list" data-tab="list">🗂 条目</button>
    <button class="tab" id="tab-ai" data-tab="ai">🤖 问答</button>
  </div>
</header>

<div id="overview" hidden></div>

<div id="listview">
  <div class="panel">
    <div class="row">
      <input type="search" id="q" placeholder="搜索名称 / 定位 / 简介 / 标签 / 归档全文……">
      <select id="cat"><option value="">全部分区</option></select>
      <select id="type">
        <option value="">全部类型</option>
        <option value="project">项目</option>
        <option value="article">文章</option>
      </select>
      <select id="sort">
        <option value="date">按收录日期</option>
        <option value="name">按名称</option>
        <option value="cat">按分区</option>
        <option value="seq">按收录序号</option>
      </select>
      <button class="iconbtn" id="random" title="随机看一条">🎲</button>
    </div>
    <div class="chips" id="chips"></div>
  </div>
  <div class="catnav" id="catnav"></div>
  <div class="count" id="count"></div>
  <div class="cards" id="list"></div>
</div>

<div id="aiview" hidden>
  <div class="panel" id="aicfgpanel">
    <div class="row">
      <button class="iconbtn" id="ai-editcfg" title="展开/收起模型配置">⚙️ 模型配置</button>
      <span id="ai-cfgmsg"></span>
    </div>
    <div class="cfgrow">
      <input id="ai-base" placeholder="API 地址（OpenAI 兼容），如 https://api.deepseek.com">
      <input id="ai-key" type="password" placeholder="API Key（仅存本机浏览器）">
      <input id="ai-model" placeholder="模型名，如 deepseek-chat">
      <button class="iconbtn" id="ai-save">保存</button>
      <button class="iconbtn" id="ai-test">测试连接</button>
    </div>
    <div class="aihint">接入任意 OpenAI 兼容接口（DeepSeek / GLM / Kimi / 本地 Ollama 等）。密钥只保存在
      本机浏览器 localStorage，不会写进知识库文件、也不会上传到 Gitee。若报跨域(CORS)错误，请换支持
      浏览器调用的服务，或本地 Ollama 启动时设置 OLLAMA_ORIGINS=*。</div>
  </div>
  <div class="chatlog" id="chatlog"></div>
  <div class="chatquick" id="chatquick"></div>
  <div class="chatinput row">
    <input id="ai-q" placeholder="问知识库：推荐剪视频的工具？总结最近收录？分析某个分区？">
    <button class="iconbtn" id="ai-send">发送</button>
    <button class="iconbtn" id="ai-clear" title="清空对话">🗑</button>
  </div>
</div>

<footer>由 tools/build_kb.py 从 knowledge-base/data/ 生成（含归档正文检索） · __BUILT__ · 请勿手工编辑本文件</footer>
</div>

<script type="application/json" id="kb-data">__DATA__</script>
<script>
(function(){
"use strict";
var root = document.getElementById('kb-data');
var DATA = JSON.parse(root.textContent);
var entries = DATA.entries, cats = DATA.categories, EMBED = DATA.marks;
var catName = {}, catIcon = {}, catHue = {};
cats.forEach(function(c){ catName[c.id] = c.numeral + '、' + c.title;
                          catIcon[c.id] = c.icon || ''; catHue[c.id] = (c.id * 137) % 360; });

/* ---------- 收藏/置顶：数据源为永久层，localStorage 为本地叠加层 ---------- */
var LS_KEY = 'kbmarks-v1';
function lsGet(){ try{ return JSON.parse(localStorage.getItem(LS_KEY)) || {}; }catch(e){ return {}; } }
function lsSave(o){ try{ localStorage.setItem(LS_KEY, JSON.stringify(o)); }catch(e){} }
var ls = lsGet();
function inArr(a, i){ return a && a.indexOf(i) >= 0; }
function isStar(e){ return !inArr(ls.starDel, e.id) && (inArr(EMBED.star, e.id) || inArr(ls.starAdd, e.id)); }
function isPin(e){  return !inArr(ls.pinDel, e.id)  && (inArr(EMBED.pin, e.id)  || inArr(ls.pinAdd, e.id)); }
function toggleMark(kind, id){
  var addK = kind + 'Add', delK = kind + 'Del';
  var marked = kind === 'star' ? isStarById(id) : isPinById(id);
  if (marked){
    if (inArr(EMBED[kind], id)) { ls[delK] = ls[delK] || []; ls[delK].push(id); ls[addK] = remove(ls[addK], id); }
    else { ls[addK] = remove(ls[addK], id); }
  } else {
    if (inArr(EMBED[kind], id)) { ls[delK] = remove(ls[delK], id); }
    else { ls[addK] = ls[addK] || []; ls[addK].push(id); ls[delK] = remove(ls[delK], id); }
  }
  lsSave(ls);
}
function isStarById(i){ var e = byId[i]; return e ? isStar(e) : false; }
function isPinById(i){ var e = byId[i]; return e ? isPin(e) : false; }
function remove(a, i){ return (a || []).filter(function(x){ return x !== i; }); }

/* ---------- 状态与 URL hash ---------- */
var state = {tab:'overview', q:'', cat:'', type:'', sort:'date', tag:'', staronly:false,
             pinonly:false, recentonly:false};
function readHash(){
  var h = decodeURIComponent(location.hash || '');
  if (h.indexOf('#') !== 0) return;
  h.slice(1).split('&').forEach(function(kv){
    var p = kv.split('=');
    if (p[0] in state){
      var v = p.slice(1).join('=');
      state[p[0]] = (p[0] === 'staronly') ? v === '1' : v;
    }
  });
}
function writeHash(){
  try{
    var parts = [];
    Object.keys(state).forEach(function(k){
      var v = state[k];
      if (v === '' || v === false) return;
      parts.push(k + '=' + encodeURIComponent(v === true ? '1' : v));
    });
    history.replaceState(null, '', parts.length ? '#' + parts.join('&') : location.pathname);
  }catch(e){}
}

/* ---------- 工具 ---------- */
var byId = {};
entries.forEach(function(e){ byId[e.id] = e; });
function esc(s){ return String(s == null ? '' : s).replace(/[&<>"']/g, function(c){
  return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]; }); }
function href(u){ if(!u) return '#'; return /^https?:/i.test(u) ? u : encodeURI(u); }
function isLocalHost(){
    return location.protocol === 'file:' ||
           location.hostname === 'localhost' ||
           location.hostname === '127.0.0.1' ||
           location.hostname === '0.0.0.0';
}
function hueColor(cid, l){ return 'hsl(' + catHue[cid] + ',62%,' + l + '%)'; }
function hl(text){
  var safe = esc(text);
  if (!state.q) return safe;
  var ws = state.q.toLowerCase().split(/\s+/).filter(Boolean);
  if (!ws.length) return safe;
  var re = new RegExp('(' + ws.map(function(w){ return w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|') + ')', 'gi');
  return safe.replace(re, '<mark>$1</mark>');
}
/* 正文格式化：先抽出链接占位 → 转义/搜索高亮/加粗 → 还原为真实链接（库内条目变内部跳转） */
function fmtText(text){
  if (!text) return '';
  var links = [];
  var t = String(text).replace(/\[([^\]]+)\]\(([^)]+)\)/g, function(m, txt, url){
    links.push({ txt: txt, url: url });
    return '\x00' + (links.length - 1) + '\x00';
  });
  t = esc(t);
  if (state.q){
    var ws = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    if (ws.length){
      var re = new RegExp('(' + ws.map(function(w){ return w.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }).join('|') + ')', 'gi');
      t = t.replace(re, '<mark>$1</mark>');
    }
  }
  t = t.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
  t = t.replace(/\x00(\d+)\x00/g, function(m, i){
    var L = links[+i];
    if (byUrl[L.url]) return '<span class="intref" data-goto="' + byUrl[L.url] + '">' + esc(L.txt) + '</span>';
    return '<a href="' + esc(L.url) + '" target="_blank" rel="noopener">' + esc(L.txt) + '</a>';
  });
  return t;
}

/* ---------- 迷你 Markdown 渲染（归档正文预览） ---------- */
function inline(s){
  var t = esc(s);
  t = t.replace(/`([^`]+)`/g, '<code>$1</code>');
  t = t.replace(/\*\*([^*]+)\*\*/g, '<b>$1</b>');
  t = t.replace(/\[([^\]]+)\]\(([^)]+)\)/g, function(m, txt, url){
    if (byUrl[url]) return '<span class="intref" data-goto="' + byUrl[url] + '">' + txt + '</span>';
    return '<a href="' + url + '" target="_blank" rel="noopener">' + txt + '</a>';
  });
  return t;
}
var byUrl = {};
entries.forEach(function(e){ if (e.url) byUrl[e.url] = e.id; });
function md2html(src){
  if (!src) return '';
  var lines = String(src).split(/\r?\n/), out = [], i, m;
  var listOpen = false, tableRows = [];
  function closeList(){ if (listOpen){ out.push('</ul>'); listOpen = false; } }
  function flushTable(){
    if (!tableRows.length) return;
    var head = tableRows[0], body = tableRows.slice(2);
    var h = '<table><tr>' + head.map(function(c){ return '<th>' + inline(c) + '</th>'; }).join('') + '</tr>';
    body.forEach(function(r){ h += '<tr>' + r.map(function(c){ return '<td>' + inline(c) + '</td>'; }).join('') + '</tr>'; });
    out.push(h + '</table>'); tableRows = [];
  }
  for (i = 0; i < lines.length; i++){
    var line = lines[i].trim();
    if (/^\|.*\|$/.test(line)){ closeList(); tableRows.push(line.slice(1, -1).split('|').map(function(x){ return x.trim(); })); continue; }
    flushTable();
    if (!line){ closeList(); continue; }
    m = line.match(/^(#{1,6})\s+(.*)$/);
    if (m){ closeList(); out.push('<h4>' + inline(m[2]) + '</h4>'); continue; }
    if (/^(-{3,}|_{3,})$/.test(line)){ closeList(); out.push('<hr>'); continue; }
    m = line.match(/^>\s?(.*)$/);
    if (m){ closeList(); out.push('<blockquote>' + inline(m[1]) + '</blockquote>'); continue; }
    m = line.match(/^[-*+]\s+(.*)$/);
    if (m){ if (!listOpen){ out.push('<ul>'); listOpen = true; } out.push('<li>' + inline(m[1]) + '</li>'); continue; }
    closeList();
    out.push('<p>' + inline(line) + '</p>');
  }
  closeList(); flushTable();
  return out.join('\n');
}

/* ---------- 匹配与排序 ---------- */
function hay(e){
  return (e.name + ' ' + (e.positioning || '') + ' ' + (e.summary || '') + ' ' +
          (e.tags || []).join(' ') + ' ' + (e.archive || '') + ' ' + e.key).toLowerCase();
}
function match(e){
  if (state.cat !== '' && String(e.category) !== String(state.cat)) return false;
  if (state.type && e.type !== state.type) return false;
  if (state.tag && (e.tags || []).indexOf(state.tag) < 0) return false;
  if (state.staronly && !isStar(e)) return false;
  if (state.pinonly && !isPin(e)) return false;
  if (state.recentonly && !isRecent(e)) return false;
  if (state.q){
    var hayFull = hay(e) + ' ' + (e.arch_text || '').toLowerCase();
    var ws = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    for (var k = 0; k < ws.length; k++){ if (hayFull.indexOf(ws[k]) < 0) return false; }
  }
  return true;
}
function archHit(e){
  if (!state.q || !e.arch_text) return false;
  var ws = state.q.toLowerCase().split(/\s+/).filter(Boolean), t = e.arch_text.toLowerCase(), i;
  for (i = 0; i < ws.length; i++){ if (t.indexOf(ws[i]) < 0) return false; }
  return true;
}
var catOrder = {};
cats.forEach(function(c, i){ catOrder[c.id] = i; });
function cmp(a, b){
  var pa = isPin(a) ? 0 : 1, pb = isPin(b) ? 0 : 1;
  if (pa !== pb) return pa - pb;
  if (state.sort === 'name') return a.name.localeCompare(b.name, 'zh');
  if (state.sort === 'seq') return a.id - b.id;
  if (state.sort === 'cat') return (catOrder[a.category] - catOrder[b.category]) || (a.id - b.id);
  return (b.added || '').localeCompare(a.added || '') || (b.id - a.id);
}

/* ---------- 头部统计 ---------- */
/* ---------- 头部统计（可点击的过滤器） ---------- */
function renderStats(){
  var a = entries.filter(function(e){ return e.type === 'article'; }).length;
  var tags = {};
  entries.forEach(function(e){ (e.tags || []).forEach(function(t){ tags[t] = 1; }); });
  var starN = entries.filter(isStar).length, pinN = entries.filter(isPin).length;
  var days = recentDays();
  var items = [
    { label: '总计', val: entries.length, act: 'reset', on: false,
      tip: '清空全部过滤，显示所有内容' },
    { label: '项目', val: entries.length - a, act: 'type', v: 'project', on: state.type === 'project' },
    { label: '文章', val: a, act: 'type', v: 'article', on: state.type === 'article' },
    { label: '⭐ 收藏', val: starN, act: 'staronly', on: state.staronly },
    { label: '📌 置顶', val: pinN, act: 'pinonly', on: state.pinonly },
    { label: '分区', val: cats.length, act: 'catview', on: false,
      tip: '跳到条目列表，按分区浏览' },
    { label: '标签', val: Object.keys(tags).length, act: 'tagview', on: false,
      tip: '跳到条目列表，点标签过滤' },
    { label: '近 7 天', val: days.length, act: 'recentonly', on: state.recentonly },
  ];
  document.getElementById('stats').innerHTML = items.map(function(x){
    return '<div class="stat' + (x.on ? ' on' : '') + '" data-action="' + x.act + '"' +
           (x.v ? ' data-value="' + x.v + '"' : '') +
           (x.tip ? ' title="' + esc(x.tip) + '"' : '') + '>' +
           '<b>' + x.val + '</b><span>' + esc(x.label) + '</span></div>';
  }).join('');
}
function clearFilters(){
  state.q = ''; state.cat = ''; state.type = ''; state.tag = '';
  state.staronly = false; state.pinonly = false; state.recentonly = false;
}
function recentDays(){
  return entries.filter(isRecent)
                .sort(function(a, b){ return b.added.localeCompare(a.added); });
}
var RECENT_CUT = (function(){ var d = new Date(DATA.built); d.setDate(d.getDate() - 6); return d; })();
function isRecent(e){ return !!(e.added && new Date(e.added) >= RECENT_CUT); }

/* ---------- 总览 ---------- */
function renderOverview(){
  var html = '<div class="ovgrid">';
  html += '<div class="ovcard"><h3>🗂 分区分布（点击过滤）</h3>' + catBars() + '</div>';
  html += '<div class="ovcard"><h3>🏷 高频标签（点击过滤）</h3><div class="cloud">' + cloud() + '</div></div>';
  html += '<div class="ovcard"><h3>🆕 最近 7 天收录</h3><ul class="recent">' + recent() + '</ul></div>';
  html += '<div class="ovcard"><h3>📈 收录趋势（按月）</h3>' + trend() + '</div>';
  html += '</div>';
  document.getElementById('overview').innerHTML = html;
}
function catBars(){
  var counts = cats.map(function(c){
    return {c: c, n: entries.filter(function(e){ return e.category === c.id; }).length};
  });
  var max = Math.max.apply(null, counts.map(function(x){ return x.n; }));
  return counts.map(function(x){
    var w = max ? Math.round(x.n / max * 100) : 0;
    return '<div class="bar-row" data-cat="' + x.c.id + '">' +
      '<span class="bar-label" title="' + esc(catName[x.c.id]) + '">' + x.c.icon + ' ' + esc(catName[x.c.id]) + '</span>' +
      '<div class="bar-track"><div class="bar" style="width:' + w + '%;background:' + hueColor(x.c.id, 55) + '"></div></div>' +
      '<span class="bar-num">' + x.n + '</span></div>';
  }).join('');
}
function trend(){
  /* 纵向排版：时间自上而下（旧→新），数量横向伸展 */
  var bym = {};
  entries.forEach(function(e){
    var m = (e.added || '').slice(0, 7);
    if (m) bym[m] = (bym[m] || 0) + 1;
  });
  var ms = Object.keys(bym).sort().slice(-24);
  if (!ms.length) return '<div style="color:var(--muted);padding:20px 0;text-align:center">暂无数据</div>';
  var max = Math.max.apply(null, ms.map(function(m){ return bym[m]; }));
  var W = 300, H = 400, PL = 52, PR = 56, PT = 26, PB = 18;
  var iw = W - PL - PR, ih = H - PT - PB;
  var step = ms.length > 1 ? ih / (ms.length - 1) : 0;
  var pts = ms.map(function(m, i){
    return { x: PL + (max ? bym[m] / max * iw : 0),
             y: PT + (ms.length > 1 ? i * step : ih / 2),
             m: m, n: bym[m] };
  });
  var line = pts.map(function(p){ return p.x.toFixed(1) + ',' + p.y.toFixed(1); }).join(' ');
  var area = PL + ',' + pts[0].y.toFixed(1) + ' ' + line + ' ' + PL + ',' +
             pts[pts.length - 1].y.toFixed(1);
  var dots = pts.map(function(p){
    return '<circle class="tdot" cx="' + p.x.toFixed(1) + '" cy="' + p.y.toFixed(1) + '" r="4">' +
           '<title>' + p.m + '：' + p.n + ' 条</title></circle>';
  }).join('');
  var rows = pts.map(function(p){
    return '<text class="tlabel" x="' + (PL - 8) + '" y="' + (p.y + 3).toFixed(1) + '" text-anchor="end">' +
           esc(p.m.slice(2)) + '</text>' +
           '<text class="tval" x="' + (p.x + 10).toFixed(1) + '" y="' + (p.y + 3).toFixed(1) + '">' + p.n + '</text>';
  }).join('');
  var grid = [1, .5, 0].map(function(f){
    var x = (PL + iw * f).toFixed(1);
    var v = Math.round(max * f);
    return '<line class="tgrid" x1="' + x + '" y1="' + PT + '" x2="' + x + '" y2="' + (H - PB) + '"/>' +
           '<text class="tval" x="' + x + '" y="' + (PT - 9) + '" text-anchor="middle">' + v + '</text>';
  }).join('');
  return '<svg class="trendsvg" viewBox="0 0 ' + W + ' ' + H + '" role="img">' +
         '<polygon class="tarea" points="' + area + '"/>' +
         '<polyline class="tline" points="' + line + '"/>' +
         grid + dots + rows + '</svg>';
}
function cloud(){
  var tc = {};
  entries.forEach(function(e){ (e.tags || []).forEach(function(t){ tc[t] = (tc[t] || 0) + 1; }); });
  var top = Object.keys(tc).sort(function(a, b){ return tc[b] - tc[a] || a.localeCompare(b); }).slice(0, 30);
  if (!top.length) return '无';
  var max = tc[top[0]], min = tc[top[top.length - 1]];
  return top.map(function(t){
    var size = Math.round(12 + (tc[t] - min) / Math.max(1, max - min) * 14);
    return '<span class="ctag" data-tag="' + esc(t) + '" style="font-size:' + size + 'px">#' + esc(t) + '</span>';
  }).join('');
}
function recent(){
  var days = recentDays();
  if (!days.length) return '<li><span class="rname">近 7 天没有新收录</span></li>';
  return days.slice(0, 12).map(function(e){
    return '<li data-goto="' + e.id + '"><span class="rdate">' + esc(e.added) + '</span>' +
           '<span class="rname">' + esc(e.name) + '</span>' +
           '<span class="rpos">' + esc(e.positioning || '') + '</span></li>';
  }).join('');
}

/* ---------- 条目渲染 ---------- */
function renderList(){
  var list = entries.filter(match);
  list.sort(cmp);
  /* 过滤状态行：无过滤时整行隐藏；有过滤时是「⟲ 清除全部」胶囊按钮 */
  var filtered = !!(state.q || state.cat !== '' || state.type || state.tag ||
                    state.staronly || state.pinonly || state.recentonly);
  var cbox = document.getElementById('count');
  if (!filtered){
    cbox.className = 'count';
    cbox.innerHTML = '';
  } else {
    var desc = [];
    if (state.q) desc.push('关键词「' + state.q + '」');
    if (state.cat !== '') desc.push('分区 ' + catName[state.cat]);
    if (state.type) desc.push(state.type === 'project' ? '仅项目' : '仅文章');
    if (state.tag) desc.push('#' + state.tag);
    if (state.staronly) desc.push('⭐ 只看收藏');
    if (state.pinonly) desc.push('📌 只看置顶');
    if (state.recentonly) desc.push('近 7 天');
    cbox.className = 'count on';
    cbox.innerHTML = '<button class="resetbtn" title="清空全部过滤条件">⟲ 清除全部 —— ' +
                      '显示 ' + list.length + ' / ' + entries.length + ' 条 ｜ ' +
                      esc(desc.join(' · ')) + '</button>';
  }
  var box = document.getElementById('list');
  if (!list.length){
    box.innerHTML = '<div class="empty">没有匹配的条目 —— 换个关键词，或清空过滤条件试试</div>';
    return;
  }
  var frag = [];
  list.forEach(function(e){
    frag.push(cardHtml(e));
  });
  box.innerHTML = frag.join('');
}
function cardHtml(e){
  var star = isStar(e), pin = isPin(e);
  var flags = (pin ? '<span class="pinflag" title="置顶">📌</span>' : '') +
              (star ? '<span class="pinflag" title="收藏">⭐</span>' : '');
  var sum = e.summary || '';
  var sumHtml = sum ? '<p class="sum">' + fmtText(sum) + '</p><button class="more" type="button">展开全文</button>' : '';
      var arch = e.arch_text ? '<div class="detail"><div class="arch">' + md2html(e.arch_text) + '</div>' +
      (isLocalHost() ? '<a class="openfile" href="' + href(e.archive) + '" target="_blank">📄 打开归档文件</a>' : '') + '</div>' : '';
  var tags = (e.tags || []).map(function(t){
    return '<span class="tag" data-tag="' + esc(t) + '">#' + esc(t) + '</span>';
  }).join('');
  var hit = '';
  if (state.q){
    var ws = state.q.toLowerCase().split(/\s+/).filter(Boolean);
    var hv = hay(e);
    var inHay = ws.every(function(w){ return hv.indexOf(w) >= 0; });
    if (!inHay) hit = archHit(e) ? '<span class="archhit">📄 正文命中</span>' : '';
  }
  return '<article class="card" data-id="' + e.id + '" style="--cat:' + hueColor(e.category, 55) + '">' +
    '<div class="chead">' + flags +
      '<a class="name" href="' + href(e.url) + '" target="_blank" rel="noopener">' + hl(e.name) + '</a>' +
      '<span class="cat" title="' + esc(catName[e.category]) + '">' + esc(catIcon[e.category] + ' ' + catName[e.category]) + '</span>' +
      (e.added ? '<span class="date">' + esc(e.added) + '</span>' : '') +
    '</div>' +
    (e.positioning ? '<p class="pos">' + fmtText(e.positioning) + '</p>' : '') +
    sumHtml + hit + arch +
    '<div class="meta">' + tags +
      '<span class="markbtn">' +
        '<button data-mark="star" class="' + (star ? 'on' : '') + '" title="收藏（长期生效请告诉 AI 写入数据源）">⭐</button>' +
        '<button data-mark="pin" class="' + (pin ? 'on' : '') + '" title="置顶">📌</button>' +
        '<button data-mark="copy" title="复制 [名称](链接)">⧉</button>' +
      '</span>' +
    '</div>' +
  '</article>';
}

/* ---------- 分区导航 / chips ---------- */
function renderCatnav(){
  var nav = document.getElementById('catnav');
  var html = '<span class="chip' + (state.cat === '' ? ' on' : '') + '" data-cat="">全部 ' + entries.length + '</span>';
  cats.forEach(function(c){
    var n = entries.filter(function(e){ return e.category === c.id; }).length;
    html += '<span class="chip' + (String(state.cat) === String(c.id) ? ' on' : '') + '" data-cat="' + c.id + '">' +
            c.icon + ' ' + esc(c.title) + ' ' + n + '</span>';
  });
  nav.innerHTML = html;
}
function renderChips(){
  var tc = {};
  entries.forEach(function(e){ (e.tags || []).forEach(function(t){ tc[t] = (tc[t] || 0) + 1; }); });
  var top = Object.keys(tc).sort(function(a, b){ return tc[b] - tc[a] || a.localeCompare(b); }).slice(0, 28);
  var box = document.getElementById('chips');
  var html = '<span class="chip' + (state.staronly ? ' on' : '') + '" id="starchip">⭐ 只看收藏</span>';
  html += top.map(function(t){
    return '<span class="chip' + (state.tag === t ? ' on' : '') + '" data-tag="' + esc(t) + '">#' + esc(t) + ' ' + tc[t] + '</span>';
  }).join('');
  box.innerHTML = html;
}

/* ---------- 跳转与交互 ---------- */
function setTab(tab){
  state.tab = tab;
  document.getElementById('overview').hidden = (tab !== 'overview');
  document.getElementById('listview').hidden = (tab !== 'list');
  document.getElementById('aiview').hidden = (tab !== 'ai');
  document.getElementById('tab-ov').classList.toggle('on', tab === 'overview');
  document.getElementById('tab-list').classList.toggle('on', tab === 'list');
  document.getElementById('tab-ai').classList.toggle('on', tab === 'ai');
  writeHash();
}
function gotoEntry(id){
  var e = byId[id];
  if (!e) return;
  if (!match(e)){ clearFilters(); syncControls(); }
  setTab('list');
  renderList(); renderCatnav(); renderChips();
  var el = document.querySelector('.card[data-id="' + id + '"]');
  if (el){
    el.scrollIntoView({behavior: 'smooth', block: 'center'});
    el.classList.remove('flash'); void el.offsetWidth; el.classList.add('flash');
    var d = el.querySelector('.detail');
    if (d && !d.classList.contains('open')){ d.classList.add('open'); }
  }
}
function randomOne(){
  var pool = entries.filter(match);
  if (!pool.length) pool = entries;
  gotoEntry(pool[Math.floor(Math.random() * pool.length)].id);
}
function copyRef(e, btn){
  var text = '[' + e.name + '](' + e.url + ')';
  function done(){ btn.textContent = '✓'; setTimeout(function(){ btn.textContent = '⧉'; }, 1200); }
  if (navigator.clipboard && navigator.clipboard.writeText){
    navigator.clipboard.writeText(text).then(done, function(){ fallback(); });
  } else fallback();
  function fallback(){
    var ta = document.createElement('textarea');
    ta.value = text; document.body.appendChild(ta); ta.select();
    try{ document.execCommand('copy'); done(); }catch(err){}
    document.body.removeChild(ta);
  }
}
function syncControls(){
  document.getElementById('q').value = state.q;
  document.getElementById('cat').value = String(state.cat);
  document.getElementById('type').value = state.type;
  document.getElementById('sort').value = state.sort;
}

/* ---------- 事件绑定 ---------- */
document.getElementById('tab-ov').addEventListener('click', function(){ setTab('overview'); });
document.getElementById('tab-list').addEventListener('click', function(){ setTab('list'); });
document.getElementById('stats').addEventListener('click', function(ev){
  var el = ev.target.closest('.stat'); if (!el) return;
  var act = el.dataset.action, val = el.dataset.value || '';
  if (act === 'catview'){                 // 分区卡：跳条目区，按分区浏览
    clearFilters(); state.sort = 'cat';
  } else if (act === 'tagview'){          // 标签卡：跳条目区（点标签 chip 过滤）
    clearFilters();
  } else if (act === 'reset'){
    clearFilters();
  } else {
    /* 单选语义：先记住是否已激活 → 清空全部 → 未激活才生效（激活中再点=取消） */
    var was = false;
    if (act === 'type') was = (state.type === val);
    else if (act === 'staronly') was = state.staronly;
    else if (act === 'pinonly') was = state.pinonly;
    else if (act === 'recentonly') was = state.recentonly;
    clearFilters();
    if (!was){
      if (act === 'type') state.type = val;
      else if (act === 'staronly') state.staronly = true;
      else if (act === 'pinonly') state.pinonly = true;
      else if (act === 'recentonly') state.recentonly = true;
    }
  }
  setTab('list'); syncControls(); renderStats();
  renderList(); renderChips(); renderCatnav(); writeHash();
});
document.getElementById('count').addEventListener('click', function(){
  clearFilters(); syncControls(); setTab('list');
  renderStats(); renderList(); renderChips(); renderCatnav(); writeHash();
});
document.getElementById('random').addEventListener('click', randomOne);
document.getElementById('q').addEventListener('input', function(ev){
  state.q = ev.target.value.trim(); renderList(); renderChips(); writeHash();
});
document.getElementById('cat').addEventListener('change', function(ev){
  state.cat = ev.target.value; renderList(); renderCatnav(); writeHash();
});
document.getElementById('type').addEventListener('change', function(ev){
  state.type = ev.target.value; renderStats(); renderList(); writeHash();
});
document.getElementById('sort').addEventListener('change', function(ev){
  state.sort = ev.target.value; renderList(); writeHash();
});
document.getElementById('catnav').addEventListener('click', function(ev){
  var el = ev.target.closest('.chip'); if (!el) return;
  var cat = el.dataset.cat === '' ? '' : String(el.dataset.cat);
  var was = (state.cat === cat);
  clearFilters();
  if (!was) state.cat = cat;
  setTab('list'); syncControls(); renderStats();
  renderList(); renderCatnav(); renderChips(); writeHash();
});
document.getElementById('chips').addEventListener('click', function(ev){
  var el = ev.target.closest('.chip'); if (!el) return;
  if (el.id === 'starchip'){
    var wasStar = state.staronly;
    clearFilters();
    if (!wasStar) state.staronly = true;
  } else if (el.dataset.tag){
    var wasTag = (state.tag === el.dataset.tag);
    clearFilters();
    if (!wasTag) state.tag = el.dataset.tag;
  }
  renderStats(); renderList(); renderChips(); renderCatnav(); writeHash();
});
document.getElementById('overview').addEventListener('click', function(ev){
  var bar = ev.target.closest('.bar-row');
  if (bar){
    var cat = String(bar.dataset.cat), wasCat = (state.cat === cat);
    clearFilters();
    if (!wasCat) state.cat = cat;
    setTab('list'); syncControls(); renderStats();
    renderList(); renderCatnav(); renderChips(); writeHash(); return;
  }
  var ct = ev.target.closest('.ctag');
  if (ct){
    var tg = ct.dataset.tag, wasTag = (state.tag === tg);
    clearFilters();
    if (!wasTag) state.tag = tg;
    setTab('list'); syncControls(); renderStats();
    renderList(); renderCatnav(); renderChips(); writeHash(); return;
  }
  var li = ev.target.closest('li[data-goto]');
  if (li){ gotoEntry(parseInt(li.dataset.goto, 10)); }
});
document.getElementById('list').addEventListener('click', function(ev){
  var more = ev.target.closest('.more');
  if (more){
    var card = more.closest('.card');
    var s = more.previousElementSibling;
    var d = card.querySelector('.detail');
    s.classList.toggle('open');
    if (d) d.classList.toggle('open');
    more.textContent = s.classList.contains('open') ? '收起' : '展开全文';
    return;
  }
  var mark = ev.target.closest('[data-mark]');
  if (mark){
    var card = ev.target.closest('.card');
    var e = byId[parseInt(card.dataset.id, 10)];
    if (mark.dataset.mark === 'copy'){ copyRef(e, mark); return; }
    var kind = mark.dataset.mark;
    toggleMark(kind, e.id);
    if (kind === 'pin'){
      var sc = window.scrollY;
      renderStats(); renderList(); renderCatnav(); renderChips();
      window.scrollTo(0, sc);
    } else {
      mark.classList.toggle('on', kind === 'star' ? isStar(e) : isPin(e));
      renderStats();
    }
    return;
  }
  var tag = ev.target.closest('.tag');
  if (tag){ state.tag = tag.dataset.tag; renderList(); renderChips(); writeHash(); return; }
  var ir = ev.target.closest('.intref');
  if (ir){ ev.preventDefault(); gotoEntry(parseInt(ir.dataset.goto, 10)); return; }
});
document.addEventListener('keydown', function(ev){
  if (ev.key === '/' && document.activeElement.tagName !== 'INPUT'){
    ev.preventDefault(); setTab('list'); document.getElementById('q').focus();
  }
  if (ev.key === 'Escape' && document.activeElement.tagName === 'INPUT'){
    state.q = ''; syncControls(); renderList(); renderChips(); writeHash();
  }
});

/* ---------- AI 问答（用户自配 OpenAI 兼容接口，密钥仅存本机 localStorage） ---------- */
var AI_CFG_KEY = 'kbai-config-v1', aiBusy = false, aiHistory = [];
function aiCfg(){ try{ return JSON.parse(localStorage.getItem(AI_CFG_KEY)) || {}; }catch(e){ return {}; } }
function aiCfgOk(){ var c = aiCfg(); return !!(c.base && c.model); }
function flashCfg(t){
  var el = document.getElementById('ai-cfgmsg');
  el.textContent = t;
  setTimeout(function(){ el.textContent = ''; }, 5000);
}
function renderAiPanel(){
  var c = aiCfg();
  document.getElementById('ai-base').value = c.base || '';
  document.getElementById('ai-key').value = c.key || '';
  document.getElementById('ai-model').value = c.model || '';
  document.getElementById('aicfgpanel').classList.toggle('cfgopen', !aiCfgOk());
}
function aiSaveCfg(){
  var c = { base: document.getElementById('ai-base').value.trim(),
            key: document.getElementById('ai-key').value.trim(),
            model: document.getElementById('ai-model').value.trim() };
  if (!c.base || !c.model){ flashCfg('接口地址与模型名必填'); return; }
  try{ localStorage.setItem(AI_CFG_KEY, JSON.stringify(c)); }catch(e){}
  renderAiPanel();
  flashCfg('已保存（密钥仅存本机浏览器）');
}
/* ---- 上下文脱敏：发给模型的索引里隐藏安全/激活类条目（库与看板不受影响），默认开 ---- */
var SAN_KEY = 'kbai-sanitize';
function sanitizeOn(){ try{ return localStorage.getItem(SAN_KEY) !== '0'; }catch(e){ return true; } }
function toggleSanitize(){
  try{ localStorage.setItem(SAN_KEY, sanitizeOn() ? '0' : '1'); }catch(e){}
  renderQuick();
}
var SENS_RE = /激活|破解|防撤回|渗透|逆向|漏洞|盗版|外挂|crack|exploit|pentest|hacking|wifite|reverse|vulnerab|patch|keygen|bypass/i;
function ctxEntries(){
  if (!sanitizeOn()) return { list: entries, hidden: 0 };
  var list = entries.filter(function(e){
    return !SENS_RE.test(e.name + ' ' + (e.positioning || ''));
  });
  return { list: list, hidden: entries.length - list.length };
}
function kbStatsText(list){
  var a = list.filter(function(e){ return e.type === 'article'; }).length;
  return '共 ' + list.length + ' 条（项目 ' + (list.length - a) + ' / 文章 ' + a + '），' + cats.length + ' 个分区' +
         (sanitizeOn() ? '' : '：' + cats.map(function(c){ return c.numeral + '、' + c.title; }).join('；'));
}
function kbIndexText(list){
  return list.map(function(e){
    return '- ' + e.name + '（' + catName[e.category] + '）：' + (e.positioning || '');
  }).join('\n');
}
function retrieve(question, list){
  var hays = list.map(function(e){
    return (e.name + ' ' + (e.positioning || '') + ' ' + (e.summary || '') +
            ' ' + (e.tags || []).join(' ')).toLowerCase();
  });
  function scoreAll(terms){
    var scored = list.map(function(e, i){
      var s = 0;
      terms.forEach(function(t){ if (hays[i].indexOf(t) >= 0) s += t.length; });
      return { e: e, s: s };
    }).filter(function(x){ return x.s > 0; });
    scored.sort(function(a, b){ return b.s - a.s; });
    return scored;
  }
  var toks = question.toLowerCase()
    .split(/[\s，。？！、；：,.?!;:（）()\-]+/).filter(function(t){ return t.length >= 2; });
  var scored = scoreAll(toks);
  if (!scored.length){                      // 整块未命中：中文 3 字滑窗再试一次
    var win = [], m, re = /[\u4e00-\u9fff]{3,}/g;
    while ((m = re.exec(question))){
      for (var i = 0; i + 3 <= m[0].length; i++) win.push(m[0].slice(i, i + 3));
    }
    if (win.length) scored = scoreAll(win);
  }
  return scored.slice(0, 10).map(function(x){ return x.e; });
}
function buildMessages(q){
  var ctx = ctxEntries();
  var sys = '你是用户的个人开源知识库助手，用户会就知识库内容提问。\n' +
    '【知识库概况】' + kbStatsText(ctx.list) + '\n【全部条目索引（名称｜分区｜定位）】\n' + kbIndexText(ctx.list) +
    '\n\n回答要求：用中文；引用具体项目时写成 Markdown 链接 [名称](链接) 以便用户跳转；' +
    '优先依据知识库内容回答，库里没有的可以说明后基于常识补充；分析与推荐要条理清晰。';
  var rel = retrieve(q, ctx.list);
  if (rel.length){
    sys += '\n\n【与本次问题最相关的条目详情】\n' + rel.map(function(e){
      return '### ' + e.name + '\n链接：' + e.url + ' ｜ 分区：' + catName[e.category] +
             (e.tags && e.tags.length ? ' ｜ 标签：' + e.tags.join(',') : '') +
             '\n简介：' + (e.summary || '（无）').slice(0, 500);
    }).join('\n\n');
  }
  var msgs = [{ role: 'system', content: sys }];
  aiHistory.slice(-6).forEach(function(h){ msgs.push(h); });
  msgs.push({ role: 'user', content: q });
  return { msgs: msgs, rel: rel, hidden: ctx.hidden };
}
async function callAI(messages, onDelta){
  var c = aiCfg();
  var url = c.base.replace(/\/+$/, '') + '/chat/completions';
  var res = await fetch(url, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', 'Authorization': 'Bearer ' + (c.key || '') },
    body: JSON.stringify({ model: c.model, messages: messages, stream: true })
  });
  if (!res.ok){
    var t = '';
    try{ t = await res.text(); }catch(e){}
    throw new Error('HTTP ' + res.status + (t ? '：' + t.slice(0, 200) : ''));
  }
  var reader = res.body.getReader();
  var dec = new TextDecoder(), buf = '', full = '';
  while (true){
    var r = await reader.read();
    if (r.done) break;
    buf += dec.decode(r.value, { stream: true });
    var lines = buf.split('\n');
    buf = lines.pop();
    for (var i = 0; i < lines.length; i++){
      var l = lines[i].trim();
      if (l.indexOf('data:') !== 0) continue;
      var d = l.slice(5).trim();
      if (!d || d === '[DONE]') continue;
      try{
        var j = JSON.parse(d);
        var delta = j.choices && j.choices[0] && j.choices[0].delta && j.choices[0].delta.content;
        if (delta){ full += delta; onDelta(full); }
      }catch(e){}
    }
  }
  return full;
}
function chatBubble(role, html){
  var log = document.getElementById('chatlog');
  var div = document.createElement('div');
  div.className = 'msg ' + role;
  div.innerHTML = html;
  log.appendChild(div);
  log.scrollTop = log.scrollHeight;
  return div;
}
async function aiAsk(){
  if (aiBusy) return;
  var input = document.getElementById('ai-q');
  var q = input.value.trim();
  if (!q) return;
  if (!aiCfgOk()){
    setTab('ai');
    document.getElementById('aicfgpanel').classList.add('cfgopen');
    document.getElementById('ai-base').focus();
    flashCfg('请先在上方配置接口地址与模型，然后保存');
    return;
  }
  input.value = '';
  chatBubble('user', esc(q));
  var built = buildMessages(q);
  var info = built.rel.length ?
    '已附带：全部条目索引 ＋ ' + built.rel.length + ' 条相关详情' : '已附带：全部条目索引';
  if (built.hidden){
    info += '（🛡 已脱敏隐藏 ' + built.hidden + ' 条敏感条目）';
  }
  var holder = chatBubble('ai', '<div class="msginfo">' + esc(info) + '</div>' +
                          '<div class="msgbody">思考中…</div>');
  var body = holder.querySelector('.msgbody');
  aiBusy = true;
  document.getElementById('ai-send').disabled = true;
  try{
    var ans = await callAI(built.msgs, function(full){
      body.innerHTML = md2html(full);
      var log = document.getElementById('chatlog');
      log.scrollTop = log.scrollHeight;
    });
    body.innerHTML = md2html(ans || '（空回复）');
    aiHistory.push({ role: 'user', content: q }, { role: 'assistant', content: ans });
    if (aiHistory.length > 12) aiHistory = aiHistory.slice(-12);
  }catch(err){
    var em = String(err.message);
    if (/违规|敏感|sensitive|risk|1301|filter|审查|banned|blocked|content.?poli/i.test(em)){
      body.innerHTML = '<span class="aierr">模型服务商的内容风控拦截了这次请求（不是知识库或页面的问题）。</span><br>' +
        '<span class="aierr2">知识库里的安全研究/工具类条目（渗透、逆向、激活等）容易被风控词库误判。' +
        '可依次尝试：① 确认输入框上方「🛡 脱敏上下文」开关已打开后重新提问；' +
        '② 换用 DeepSeek 或本地 Ollama 等更宽容的接口；③ 换个问法。</span>';
    } else {
      body.innerHTML = '<span class="aierr">请求失败：' + esc(err.message) + '</span><br>' +
        '<span class="aierr2">常见原因：地址/密钥/模型名错误、服务不支持流式，或该接口不允许浏览器跨域' +
        '（CORS）——可换 DeepSeek / GLM / Kimi 等支持浏览器调用的服务，或本地 Ollama 设 OLLAMA_ORIGINS=*。</span>';
    }
  }
  aiBusy = false;
  document.getElementById('ai-send').disabled = false;
}
function renderQuick(){
  var on = sanitizeOn();
  document.getElementById('chatquick').innerHTML =
    '<span class="chip' + (on ? ' on' : '') + '" id="sanchip" ' +
    'title="开启后，发给模型的上下文会自动隐藏安全/激活类敏感条目（知识库本身不受影响），避免被服务商风控误拦">' +
    '🛡 脱敏上下文 ' + (on ? '开' : '关') + '</span>' +
    [
      ['总结最近 7 天收录', '总结最近 7 天收录的内容，按分区归纳并点出亮点'],
      ['分析知识库结构', '分析这个知识库的分区结构和标签分布，指出盲区和值得补充的方向'],
      ['推荐剪视频工具', '我想用 AI 剪视频，从库里推荐最合适的工具并说明理由'],
    ].map(function(x){
      return '<span class="chip" data-q="' + esc(x[1]) + '">' + esc(x[0]) + '</span>';
    }).join('');
}

/* ---------- 事件绑定 ---------- */
document.getElementById('tab-ai').addEventListener('click', function(){ setTab('ai'); });
document.getElementById('ai-editcfg').addEventListener('click', function(){
  document.getElementById('aicfgpanel').classList.toggle('cfgopen');
});
document.getElementById('ai-save').addEventListener('click', aiSaveCfg);
document.getElementById('ai-send').addEventListener('click', aiAsk);
document.getElementById('ai-q').addEventListener('keydown', function(ev){
  if (ev.key === 'Enter'){ ev.preventDefault(); aiAsk(); }
});
document.getElementById('ai-clear').addEventListener('click', function(){
  aiHistory = [];
  document.getElementById('chatlog').innerHTML = '';
});
document.getElementById('chatquick').addEventListener('click', function(ev){
  var c = ev.target.closest('.chip'); if (!c) return;
  if (c.id === 'sanchip'){ toggleSanitize(); return; }
  document.getElementById('ai-q').value = c.dataset.q;
  aiAsk();
});
document.getElementById('chatlog').addEventListener('click', function(ev){
  var ir = ev.target.closest('.intref');
  if (ir){ ev.preventDefault(); gotoEntry(parseInt(ir.dataset.goto, 10)); }
});
document.getElementById('ai-test').addEventListener('click', function(){
  aiSaveCfg();
  var msg = document.getElementById('ai-cfgmsg');
  msg.textContent = '测试中…';
  callAI([{ role: 'user', content: '回复「连接成功」四个字即可' }], function(){}).then(
    function(ans){ msg.textContent = '✓ 连接成功：' + (ans || '').slice(0, 40); },
    function(err){ msg.textContent = '✗ ' + String(err.message).slice(0, 90); });
  setTimeout(function(){ if (msg.textContent !== '测试中…') msg.textContent = ''; }, 9000);
});

/* ---------- 启动 ---------- */
readHash();
syncControls();
renderStats();
renderOverview();
renderChips();
renderCatnav();
renderList();
renderAiPanel();
renderQuick();
setTab(state.tab || 'overview');
})();
</script>
</body>
</html>
"""


def build_html(entries, categories, meta, marks, today) -> str:
    ref_map = {e["id"]: (e["name"], e["url"]) for e in entries}
    star_set, pin_set = set(marks["star"]), set(marks["pin"])
    cat_order = {c["id"]: i for i, c in enumerate(categories)}
    ordered = sorted(entries, key=lambda x: (cat_order.get(x["category"], 99),
                                              name_sort_key(x["name"])))
    payload = {
        "built": today,
        "marks": {"star": marks["star"], "pin": marks["pin"]},
        "categories": [{"id": c["id"], "numeral": c["numeral"], "title": c["title"],
                        "icon": CAT_ICONS.get(c["id"], "")} for c in categories],
        "entries": [{
            "seq": i + 1,
            "id": e["id"],
            "key": e.get("key") or f"{e['category']}-{e['id']}",
            "name": e["name"],
            "url": e["url"],
            "category": e["category"],
            "type": e.get("type", "project"),
            "positioning": resolve_refs(e.get("positioning", ""), ref_map),
            "summary": resolve_refs(e.get("summary", ""), ref_map),
            "tags": e.get("tags", []),
            "archive": e.get("archive", ""),
            "arch_text": load_archive_text(e.get("archive", "")),
            "added": e.get("added", ""),
        } for i, e in enumerate(ordered)],
    }
    blob = json.dumps(payload, ensure_ascii=False).replace("</", "<\\/")
    title = html.escape(meta.get("title", "我的知识库"))
    return (HTML_TEMPLATE
            .replace("__TITLE__", title)
            .replace("__BUILT__", today)
            .replace("__DATA__", blob))


# ---------------------------------------------------------------- 主流程

def verify_outputs(entries, categories) -> list:
    """构建后自检：确认产物真的写对了。返回问题列表，空列表表示通过。"""
    import re as _re
    problems = []
    md = KB_MD.read_text(encoding="utf-8")
    found = _re.findall(r"^### (?:[📌⭐]+\s+)?\[", md, _re.M)
    if len(found) != len(entries):
        problems.append(f"md 条目数 {len(found)} != 数据源 {len(entries)}")
    for c in categories:
        if f"{c['numeral']}、{c['title']}（" not in md:
            problems.append(f"md 缺少分区标题：{c['numeral']}、{c['title']}")

    h = KB_HTML.read_text(encoding="utf-8")
    m = _re.search(r'<script type="application/json" id="kb-data">(.*?)</script>', h, _re.S)
    if not m:
        problems.append("看板缺少内嵌数据块")
    else:
        try:
            d = json.loads(m.group(1).replace("<\\/", "</"))
            if len(d["entries"]) != len(entries):
                problems.append(f"看板条目数 {len(d['entries'])} != 数据源 {len(entries)}")
            if len(d["categories"]) != len(categories):
                problems.append("看板分区数与数据源不符")
        except json.JSONDecodeError as exc:
            problems.append(f"看板内嵌 JSON 解析失败：{exc}")
    for token in ("__TITLE__", "__DATA__", "__BUILT__"):
        if token in h:
            problems.append(f"看板残留占位符 {token}")
    return problems


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true", help="只打印统计，不写文件")
    ap.add_argument("--no-guard", action="store_true", help="跳过哈希护栏")
    args = ap.parse_args()

    entries, categories, meta, header, inbox, footer, marks = load()
    today = dt.date.today().isoformat()

    # 护栏：确认主索引没有被其它会话改动
    if KB_MD.exists() and HASH_FILE.exists() and not args.no_guard:
        recorded = HASH_FILE.read_text(encoding="utf-8").strip()
        actual = sha256(KB_MD)
        if recorded and recorded != actual:
            print("[中止] 检测到《我的知识库.md》在上次构建后被修改过（可能是其它对话正在编辑）。",
                  file=sys.stderr)
            print("       请先运行：python tools/migrate_to_jsonl.py --force  吸收改动，再重新构建。",
                  file=sys.stderr)
            return 3

    keys = [e.get("key") or f"{e['category']}-{e['id']}" for e in entries]
    dup = [k for k, n in Counter(keys).items() if n > 1]
    if dup:
        print(f"[中止] 唯一键重复：{sorted(dup)}", file=sys.stderr)
        return 4

    md = build_markdown(entries, categories, meta, header, inbox, footer, marks, today)
    gitee_md, n_filtered = build_gitee_markdown(entries, categories, meta, header, inbox, footer, marks, today)
    trans = load_translations()
    md_en = build_english_markdown(entries, categories, trans, today, tags_en=load_tags_en())
    n_en = sum(1 for e in entries if ((trans.get(str(e["id"])) or "").strip()))
    tag_md = build_tag_index(entries)
    tl_md = build_timeline(entries)
    html_out = build_html(entries, categories, meta, marks, today)

    per_cat = Counter(e["category"] for e in entries)
    n_art = sum(1 for e in entries if e.get("type") == "article")
    print(f"[统计] 共 {len(entries)} 条 ｜ 项目 {len(entries) - n_art} ｜ 收藏文章 {n_art} ｜ "
          f"⭐ {len(set(marks['star']) & {e['id'] for e in entries})} ｜ 📌 {len(marks['pin'])}")
    for c in categories:
        print(f"   {CAT_ICONS.get(c['id'], '')} {c['numeral']}、{c['title']}: {per_cat[c['id']]}")
    print(f"[体积] 我的知识库.md {len(md.encode('utf-8')) / 1024:.1f} KB ｜ "
          f"看板 {len(html_out.encode('utf-8')) / 1024:.1f} KB")
    print(f"[Gitee版] 过滤 {n_filtered} 条敏感条目 ｜ [英文版] 已译 {n_en}/{len(entries)} 条定位")

    if args.dry_run:
        print("[dry-run] 未写入任何文件")
        return 0

    KB_MD.parent.mkdir(parents=True, exist_ok=True)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    KB_MD.write_text(md, encoding="utf-8")
    KB_HTML.write_text(html_out, encoding="utf-8")
    # README.md（英文版，仓库首页自动渲染）
    (WORKSPACE / "README.md").write_text(md_en, encoding="utf-8")
    # README_CH.md（中文完整版，放 docs/）
    KB_MD.write_text(md, encoding="utf-8")
    # 其他索引放 docs/
    (OUT_DIR / "标签索引.md").write_text(tag_md, encoding="utf-8")
    (OUT_DIR / "时间线.md").write_text(tl_md, encoding="utf-8")
    DATA_DIR.mkdir(parents=True, exist_ok=True)

    # 回写各分区的实际条目数，保持 categories.json 与产物一致
    for c in categories:
        c["declared_count"] = per_cat[c["id"]]
    CATEGORIES.write_text(json.dumps(categories, ensure_ascii=False, indent=2) + "\n",
                          encoding="utf-8")

    HASH_FILE.write_text(sha256(KB_MD), encoding="utf-8")

    problems = verify_outputs(entries, categories)
    if problems:
        print("[自检失败] 产物与数据源不一致：", file=sys.stderr)
        for p in problems:
            print(f"   - {p}", file=sys.stderr)
        return 5

    print(f"[完成] 已写入 {KB_MD.name} / knowledge-base.html / 标签索引.md / 时间线.md"
          f" / 我的知识库-gitee.md / 我的知识库-EN.md")
    print("[自检] 通过（条目数、分区标题、看板内嵌数据均一致）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
