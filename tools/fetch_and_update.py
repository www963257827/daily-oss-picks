#!/usr/bin/env python3
"""
在 GitHub Actions 中自动更新知识库 Pages：
拉取 GitHub Trending → GitHub Models 翻译 → 构建 HTML → 由 Workflow push。

依赖：pip install httpx beautifulsoup4 pypinyin
环境变量：GITHUB_TOKEN（Actions 自动提供）
"""

from __future__ import annotations

import json
import os
import re
import sys
import datetime as dt
from pathlib import Path

import httpx

WORKSPACE = Path(__file__).resolve().parent.parent
DATA_DIR = WORKSPACE / "data"
ENTRIES = DATA_DIR / "entries.jsonl"
BUILD_SCRIPT = WORKSPACE / "tools" / "build_kb.py"

GITHUB_TOKEN = os.environ.get("GITHUB_TOKEN", "")
MODELS_URL = "https://models.github.ai/inference/chat/completions"
MODEL_NAME = "openai/gpt-4o-mini"

# 分类规则（与本地 CAT_RULES 一致，简化版）
CAT_RULES = [
    (2,  r"mobile|android|\bios\b|手机自动化"),
    (3,  r"memory that|agent.?memory|记忆|蒸馏"),
    (4,  r"humaniz|写作|writing style"),
    (6,  r"\bcad\b|diagram|专利|patent|spreadsheet|office sdk"),
    (10, r"\btts\b|speech|语音|asr|voice"),
    (11, r"fine.?tun|从零|train.*llm|llm训练|lora"),
    (12, r"inference|quantiz|量化|推理引擎|vllm"),
    (13, r"diffusion|stable.?diffusion|文生|music|音乐生成|image.?gen"),
    (5,  r"视频|video edit|剪辑|film|movie"),
    (7,  r"security|pentest|vulnerab|渗透|逆向|reverse|hack|exploit"),
    (9,  r"code.?review|代码审查|rag|知识图谱"),
    (16, r"wpf|winui|avalonia|xaml|ui.?framework|component|控件"),
    (17, r"windows|taskbar|explorer|壁纸|桌面工具|desktop utility"),
    (18, r"file.?manag|download manag|photo manag|相册|文件管理"),
    (19, r"player|播放器|viewer|图片查看|media play"),
    (20, r"短视频|notification|数字人"),
    (21, r"password|投屏|screen.?cast|remote.?desktop"),
    (22, r"\bgis\b|地图|geospatial"),
    (14, r"gateway|网关|self.?hosted|多模型|proxy"),
    (15, r"推荐|情报|monitor|盯盘|dashboard"),
    (8,  r"skill.?(collection|market)|plugin.?market|注册中心"),
    (1,  r"\bagent|\bskill\b|\bmcp\b|claude|harness|cursor|codex|copilot"),
    (25, r"\bgit\b|ci/?cd|devops|runner|action"),
    (24, r"awesome|curated|interview|面试|exercises|book|教程|learn"),
]


def guess_category(name: str, desc: str) -> int:
    hay = f"{name} {desc}".lower()
    for cid, pat in CAT_RULES:
        if re.search(pat, hay):
            return cid
    return 24


def translate_batch(texts: list[str]) -> list[str]:
    """用 GitHub Models 批量翻译。"""
    if not GITHUB_TOKEN:
        print("[翻译] 无 GITHUB_TOKEN，跳过翻译（保留英文）")
        return texts

    prompt = "将以下英文技术项目描述翻译成简洁中文（每条一两句话，忠实原意）。"
    prompt += "按编号返回翻译结果，格式：1. 翻译内容。不要其他解释。\n\n"
    for i, t in enumerate(texts, 1):
        prompt += f"{i}. {t[:200]}\n"

    try:
        resp = httpx.post(
            MODELS_URL,
            headers={
                "Authorization": f"Bearer {GITHUB_TOKEN}",
                "Content-Type": "application/json",
            },
            json={
                "model": MODEL_NAME,
                "messages": [
                    {"role": "system", "content": "你是技术翻译，输出简洁准确的中文。"},
                    {"role": "user", "content": prompt},
                ],
                "max_tokens": 2000,
                "temperature": 0.3,
            },
            timeout=60,
        )
        resp.raise_for_status()
        content = resp.json()["choices"][0]["message"]["content"]
        # 解析编号结果
        results = {}
        for line in content.split("\n"):
            m = re.match(r"(\d+)[.、\s]+(.+)", line.strip())
            if m:
                results[int(m.group(1))] = m.group(2).strip()
        return [results.get(i, texts[i-1]) for i in range(1, len(texts) + 1)]
    except Exception as exc:
        print(f"[翻译] 失败：{exc}，保留英文", file=sys.stderr)
        return texts


def fetch_trending() -> list[dict]:
    """抓取 GitHub Trending 页面。"""
    print("[拉取] GitHub Trending...")
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        "Accept": "text/html",
    }
    resp = httpx.get("https://github.com/trending", headers=headers, timeout=30, follow_redirects=True)
    resp.raise_for_status()

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(resp.text, "html.parser")
    repos = []

    for article in soup.select("article.Box-row"):
        # 仓库名
        h2 = article.select_one("h2 a")
        if not h2:
            continue
        href = h2.get("href", "")
        parts = href.strip("/").split("/")
        if len(parts) < 2:
            continue
        name = f"{parts[0]}/{parts[1]}"

        # 描述
        p = article.select_one("p")
        desc = p.get_text(strip=True) if p else ""

        # Stars
        star_el = article.select_one("a.Link--muted[href$='/stargazers']")
        stars_text = star_el.get_text(strip=True).replace(",", "") if star_el else "0"
        try:
            stars = int(stars_text)
        except ValueError:
            stars = 0

        # 今日 stars
        today_el = article.select_one("span.d-inline-block.float-sm-right")
        today_text = today_el.get_text(strip=True) if today_el else ""
        today_match = re.search(r"(\d+)", today_text.replace(",", ""))
        today = int(today_match.group(1)) if today_match else 0

        # 语言
        lang_el = article.select_one("[itemprop='programmingLanguage']")
        lang = lang_el.get_text(strip=True) if lang_el else ""

        repos.append({
            "name": name,
            "url": f"https://github.com/{name}",
            "desc": desc,
            "stars": stars,
            "today": today,
            "language": lang,
        })

    print(f"[拉取] 共 {len(repos)} 个仓库")
    return repos


def load_entries():
    if ENTRIES.exists():
        return [json.loads(l) for l in ENTRIES.read_text(encoding="utf-8").splitlines() if l.strip()]
    return []


def save_entries(entries):
    ENTRIES.parent.mkdir(parents=True, exist_ok=True)
    with ENTRIES.open("w", encoding="utf-8") as f:
        for e in sorted(entries, key=lambda x: (x["category"], x["id"])):
            f.write(json.dumps(e, ensure_ascii=False) + "\n")


def main():
    trending = fetch_trending()
    if not trending:
        print("[无数据] Trending 页面解析为空")
        return 1

    entries = load_entries()
    known = {(e.get("url") or "").rstrip("/").lower() for e in entries}
    known |= {e["name"].lower() for e in entries}
    new_repos = [r for r in trending if r["url"].rstrip("/").lower() not in known and r["name"].lower() not in known]
    print(f"[查重] 新增 {len(new_repos)} 个仓库（跳过 {len(trending) - len(new_repos)} 个已在库）")

    if not new_repos:
        print("[完成] 无新增，仅重建 HTML")
        os.system(f"python {BUILD_SCRIPT}")
        return 0

    # 批量翻译
    descs = [r["desc"] or r["name"] for r in new_repos]
    translated = translate_batch(descs)

    # 归档日期
    today = dt.date.today()
    folder = f"{today.year}.{today.month}.{today.day}"

    # 添加新条目
    next_id = max([e["id"] for e in entries], default=0) + 1
    for i, r in enumerate(new_repos):
        zh = translated[i] if i < len(translated) else r["desc"]
        entry = {
            "id": next_id,
            "category": guess_category(r["name"], r["desc"]),
            "type": "project",
            "name": r["name"],
            "url": r["url"],
            "bullets": [
                {"label": "定位", "text": zh[:60]},
                {"label": "简介", "text": f"{zh}（GitHub Trending {today.isoformat()}：★{r['stars']}，今日 +{r['today']}）"},
                {"label": "归档", "text": f"`开源项目介绍/{folder}/{r['name'].split('/')[-1]}.md`"},
                {"label": "标签", "text": f"`#{r['language'].lower()}`"},
            ],
            "tags": [r["language"].lower()] if r["language"] else ["github"],
            "archive": "",
            "positioning": zh[:60],
            "summary": f"{zh}（GitHub Trending {today.isoformat()}：★{r['stars']}，今日 +{r['today']}）",
            "extra": {},
            "added": today.isoformat(),
            "key": "",
        }
        entry["key"] = f"{entry['category']}-{entry['id']}"
        entries.append(entry)
        next_id += 1
        print(f"  [新增] #{entry['id']} {r['name']} -> 分区 {entry['category']}")

    save_entries(entries)
    print(f"[入库] 新增 {len(new_repos)} 条，共 {len(entries)} 条")

    # 构建 HTML
    print("[构建] 生成 HTML...")
    result = os.system(f"python {BUILD_SCRIPT}")
    if result != 0:
        print(f"[错误] 构建失败（退出码 {result}）")
        return 1

    print("[完成] HTML 已生成，等待 Workflow push")
    return 0


if __name__ == "__main__":
    sys.exit(main())
