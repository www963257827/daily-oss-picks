# 我的知识库

> 📌 **知识库使用说明**：本地 Markdown 版个人知识库，用于收藏和整理各类优质开源项目、工具、学习资源。新增内容直接发给 AI（ZCode）即可——单条或多条链接都行，AI 会自动查重、写归档、录入、体检并同步；查询时说"库里有没有 X"即可。定期由 AI 复核整理归类。
> 🌐 **English edition**: [README.md](README.md)（GitHub 镜像默认页）
>
> 📅 最后更新：2026-10-11 ｜ 共收录 **408** 条内容（400 个项目 + 8 篇精选文章）

## 📑 目录索引

| 分区 | 内容说明 | 数量 |
|-|-|-|
| [一、AI 编码 Agent · 运行时与方法论](#sec-1) | 终端编码 Agent、Agent 运行时与桌面宿主、Harness 增强系统、开发方法论（TDD/规格驱动/敏捷 AI 开发） | 28 |
| [二、手机自动化 Agent](#sec-2) | 视觉多模态手机操控、ADB/MCP 驱动、iOS/Android 真机与模拟器自动化 | 7 |
| [三、Agent 记忆与知识蒸馏](#sec-3) | 跨工具长期记忆、会学习反思的记忆系统、书籍与数字痕迹蒸馏为 Skill | 9 |
| [四、写作与文本风格 Skills](#sec-4) | AI 文本去痕、中文润色、清除写作套路、输出去客套化 | 5 |
| [五、视频创作 Skills](#sec-5) | 视频理解、对话式剪辑、AI 影视制作管线 | 6 |
| [六、专业领域 Skills](#sec-6) | 图表与架构图、CAD 建模、科研技能合集、专利交底、Office 套件与 SDK | 22 |
| [七、安全 · 审计与逆向](#sec-7) | 多阶段安全审计 Skill、逆向工程路由包、渗透测试工具集 | 22 |
| [八、Skill 合集与生态](#sec-8) | 官方规范与示例、工程实践集、安全策展注册中心、超大规模技能库、多宿主插件市场、MCP 服务器目录 | 31 |
| [九、代码智能 / RAG / 代码审查](#sec-9) | 代码知识图谱、检索增强生成、AI 代码审查 CLI | 13 |
| [十、语音与 TTS](#sec-10) | 低延迟语音流水线、本地语音工作室、零样本多语种语音克隆 | 6 |
| [十一、模型训练与微调](#sec-11) | 本地训练平台、从零训 LLM 教学、低显存 LoRA 微调 | 5 |
| [十二、本地推理引擎与优化](#sec-12) | 层流式推理、边缘小模型、MoE 引擎、量化压缩、模型选型 | 15 |
| [十三、图像 / 视频 / 音乐生成](#sec-13) | 生成 WebUI、扩散模型 C++ 推理、音乐生成模型 | 7 |
| [十四、AI 基础设施 · 网关与自托管平台](#sec-14) | 多模型路由网关、Agent 专用浏览器、自托管 AI 平台、AIGC SaaS 底座、多智能体编排 | 25 |
| [十五、内容发现与情报](#sec-15) | 跨平台内容推荐、全球情报仪表盘、短视频采集下载、AI 盯盘、群体智能预测 | 15 |
| [十六、WPF / .NET UI 框架与控件库](#sec-16) | 跨平台 .NET UI 框架（Avalonia/MAUI）、WPF Fluent 控件库/主题引擎（wpfui、MahApps、HandyControl、MaterialDesign、ModernWpf 等） | 23 |
| [十七、系统工具与桌面效率](#sec-17) | 动态壁纸、浮出控件、硬件工具箱、系统清理、便签、快速预览、资源管理器增强、格式转换、防撤回、Linux 桌面 | 47 |
| [十八、文件 · 下载 · 照片管理](#sec-18) | 现代文件管理器、下载工具、自托管照片库、本地相册 | 20 |
| [十九、图片查看与媒体播放](#sec-19) | 跨平台图片查看器、Fluent 媒体播放器、语言学习播放器、媒体查重 | 9 |
| [二十、AI 桌面应用](#sec-20) | 图像转 3D、AI 短视频生成、AI 通知指挥中心、设计转代码、编码 Agent 配额管理 | 8 |
| [二十一、跨设备工具](#sec-21) | 密码管理、iPhone 投屏、跨平台远程桌面 | 10 |
| [二十二、地理信息 / GIS](#sec-22) | 云原生 GIS 平台 | 1 |
| [二十三、文章收藏 / AI 动态](#sec-23) | 公众号精选文章、模型发布动态、技术选型指南 | 8 |
| [二十四、开发者资源 / 精选合集](#sec-24) | 免费公共 API、AI Agent 教材、应用示例合集、开源游戏清单、提示词模板库 | 39 |
| [二十五、DevOps / 开发者工具](#sec-25) | CI/CD Runner、Git GUI、worktree 管理、密钥与敏感数据管理 | 27 |
| 待整理区 | 新收藏内容暂存处 | — |

---

<a id="sec-1"></a>

## 🤖 一、AI 编码 Agent · 运行时与方法论（28）

编码 Agent 本体、它们的运行时与宿主，以及让 Agent 按工程方法论干活的框架。

### [affaan-m/ECC](https://github.com/affaan-m/ECC)
- **定位**：Agent Harness 性能优化系统（68 agents + 292 skills + 记忆 + 安全扫描）
- **简介**：你的 Agent 会写代码，但 **ECC 给它一套协同的工程系统和工具箱**：先规划再动手、用测试验证改动、从全新上下文里审查自己的产出、记住重要的事、把重复的成功沉淀成可复用的 skill 和 workflow。核心循环 `plan → test → implement → review → verify → remember → improve`——**装一次，让它成为你 Agent 的工作方式**，不必在每个 prompt 里重建。设计口号很精辟：**「Optimize the context window. Persist everything else.」**（优化上下文窗口，其余一切都持久化）。开箱含量惊人：**68 个 agents**（规划/审查/构建修复/安全/架构/领域）、**292 个 skills**（TDD/调研/安全/文档/前端/数据/ML/运维）、**94 个 commands**（legacy shim，正转向 skills-first）、Hooks 与 Memory 运行时（强制执行、会话摘要、持续学习、instincts、上下文控制）、按语言/项目选装的 Rules，以及 **AgentShield** 安全扫描（扫 prompts、hooks、MCP 配置、权限、密钥和 agent 文件）。平台支持分级明确：**与 Claude Code 配合最好**，Codex 有受支持的同步路径，Cursor / OpenCode / Gemini / Zed / Copilot / Antigravity / Qwen 是**能力受限的适配器**——别假设功能对等。安装 `npx ecc-universal@2.2.2 setup`（需 Node 18+，Claude 插件还需 Git 与 Claude Code 2.1+），引导式安装与原生插件命令装的是同一个 `ecc@ecc` 插件，**二选一别叠加**。⚠️ **只从官方渠道安装**（GitHub 仓库 / npm `ecc-universal`+`ecc-agentshield` / GitHub App / slug `ecc@ecc` / ecc.tools），第三方镜像可能含恶意软件。商业模式：**仓库永久 MIT 免费**，ECC Pro 是面向私有仓库的托管 GitHub App（App 免费装，私有仓库 $19/席位/月起）——这就是为什么单个维护者能每周在 7 个 harness 上发版。赞助商含 CodeRabbit、Greptile、Moonshot AI (Kimi)、SerpApi。README 13 种语言。MIT，**265,392 stars** / 39,651 forks，2026-01 创建——八个月冲到 26 万星，是本次收录中体量最大的项目。
- **归档**：`开源项目介绍/2026.9.23/ECC.md`
- **标签**：`#harness` `#skill` `#记忆` `#安全扫描` `#claude-code` `#跨平台`

### [agegr/pi-web](https://github.com/agegr/pi-web)
- **定位**：pi 编码 Agent 的本地 Web UI
- **简介**：读取本地 pi 会话文件，提供浏览器工作区：会话浏览、实时聊天、模型配置、技能管理、项目文件预览。结构化展示工具调用和 Markdown 结果，解决终端会话中难以回溯和定位问题的痛点。Next.js + React 实现，91 issues、53 PRs，MIT 协议。
- **归档**：`开源项目介绍/2026.9.6/pi-web.md`
- **标签**：`#agent` `#webui` `#nextjs`

### [agent0ai/agent-zero](https://github.com/agent0ai/agent-zero)
- **定位**：Agent Zero：通用型 AI Agent 框架，可自建、自学习、自主执行任务。
- **简介**：Agent Zero：通用型 AI Agent 框架，可自建、自学习、自主执行任务。（GitHub 每日趋势 2026-09-29：★19330，当日 +22）
- **归档**：`开源项目介绍/2026.9.29/agent-zero.md`
- **标签**：`#python`

### [agno-agi/agno](https://github.com/agno-agi/agno)
- **定位**：构建、运行和管理 Agent 平台的全栈框架。
- **简介**：构建、运行和管理 Agent 平台的全栈框架。（GitHub 每日趋势 2026-10-03：★42529，当日 +41）
- **归档**：`开源项目介绍/2026.10.4/agno.md`
- **标签**：`#python`

### [anomalyco/opencode](https://github.com/anomalyco/opencode)
- **定位**：开源 AI 编码 Agent · 终端 UI
- **简介**：MIT 协议的开源 AI 编码 Agent，以终端 TUI 形式运行。多平台安装：`curl | bash` 一键安装、npm/bun/pnpm/yarn 全局安装、Windows (scoop/choco)、macOS/Linux (Homebrew)。多语言支持（README 20+ 种语言），Monorepo 架构（Turborepo + Bun），内置 VS Code 扩展 SDK、Nix 支持、`.zed` 配置。15,679 commits、4.2k issues、1.5k PRs，活跃度极高。
- **归档**：`开源项目介绍/2026.9.6/opencode.md`
- **标签**：`#编码agent` `#tui` `#开源` `#跨平台`

### [anthropics/claude-code](https://github.com/anthropics/claude-code)
- **定位**：Anthropic 官方终端编码 Agent（本库大量 Skill 项目的宿主平台）
- **简介**：一个**住在你终端里的 agentic 编码工具**——理解你的代码库，通过自然语言命令帮你更快写代码：执行例行任务、解释复杂代码、处理 git 工作流。三种用法：终端 · IDE · 在 GitHub 上 `@claude`。这是知识库里 ECC、agent-skills、video-use、OfficeCLI、security-audit-skill、open-code-review 等一大票项目的**共同宿主**，它们几乎都围绕 Claude Code 的 skill/plugin 机制构建。⚠️ **npm 安装方式已弃用**，推荐：macOS/Linux `curl -fsSL https://claude.ai/install.sh | bash`、Windows `irm https://claude.ai/install.ps1 | iex`，也可 `brew install --cask claude-code` 或 `winget install Anthropic.ClaudeCode`。仓库内含官方 plugins 目录（自定义命令 + agents）。报 bug 用内置 `/bug` 命令或提 issue。**数据政策明确**：会收集使用数据（代码接受/拒绝）、关联对话数据和 `/bug` 反馈；保护措施包括敏感信息有限留存期、会话数据访问受限、**明确不用反馈数据训练模型**。TypeScript / Node.js 18+，仓库未声明标准 License，**147,649 stars** / 24,132 forks / 12,225 open issues，Anthropic 官方维护。
- **归档**：`开源项目介绍/2026.9.23/claude-code.md`
- **标签**：`#编码agent` `#cli` `#anthropic` `#官方` `#plugin`

### [anthropics/claude-code-action](https://github.com/anthropics/claude-code-action)
- **定位**：Anthropic 官方的 Claude Code GitHub Action 集成，把 Claude 用于 PR 审查
- **简介**：Anthropic 官方的 Claude Code GitHub Action 集成，把 Claude 用于 PR 审查与议题处理等工作流。（GitHub 每日趋势 2026-09-26：★9012，当日 +15）
- **归档**：`开源项目介绍/2026.9.27/claude-code-action.md`
- **标签**：`#typescript`

### [bmad-code-org/BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD)
- **定位**：多 Agent 敏捷 AI 开发方法论框架，用专家角色编排 AI 交付
- **简介**：**BMAD-METHOD**（Breakthrough Method for Agile AI-Driven Development）是**敏捷 AI 驱动开发（AiDD）**的开源方法论框架：AI 编码助手擅长实现却常把未言明的假设直接写成代码，BMad 用**拟人化专家 Agent 角色 + 结构化工作流**让重要决策显式化、上下文持续传递，覆盖 Clarify→Plan→Build→Review→Learn 的完整交付环，流程按需伸缩——小改动直接 Build，复杂工作才走深度规划。协议为 **MIT + 商标条款**（BMad™ 等是 BMad Code, LLC 商标，MIT 不授予商标权，GitHub API 因此标 NOASSERTION），官方承诺永久免费、无付费墙工作流。**Agent 角色体系**（v6 以技能形式提供，可点名唤起）：**Mary**（Business Analyst）、**John**（Product Manager，PRD 与需求发现）、**Winston**（System Architect，偏好「无聊技术」）、**Amelia**（Senior Software Engineer，测试先行 red-green-refactor）、**Sally**（UX Designer）；工作流技能含 brainstorming、prd、prfaq、product-brief、architecture、spec、ux、**bmad-build（唯一官方实现路径）**、build-auto（基于 spec-frontmatter 状态机的无人值守 worker）、code-review、bmad-review、deep-recon、retrospective、party-mode 等；v6.11 起核心技能从 14 个精简到 8 个，Phase 4 定型为单链 `sprint-planning→build→code-review`。**版本演进**：v1.0.0（2025-04-06）敏捷 persona + 模板 → v2 模板与 Agent 解耦 → v3 引入 **BMad Orchestrator** 超级 Agent → v4（06-20）架构大改：NPM 包 `npx bmad-method install`、`.bmad-core` 模块化、多 IDE、YAML 化定义、扩展包架构 → **v6.0.0 正式版（2026-02-17）**全面转向 skills 体系 → v6.10（2026-07-03）**bmad-loop** 成为可安装模块 → **v6.12.0（2026-09-03）**：Build 先调查再决定流程仪式量、评审 triage 为每条发现记录判决与证据；breaking 变更含 persistent_facts 默认空、{diff_output}→{diff_file}、垫片改为 `--shims` 显式开启、bmad-checkpoint-preview 更名 bmad-walkthrough。规模：创建 **2025-04-13**，截至 2026-09-27 约 **53,508 Stars / 6,025 Forks / 160 位贡献者 / 2,257 commits / 165 tags**，9-26 仍在推送，Open Issues 仅 46。生态模块：BMad Builder、Test Architect、Creative Intelligence Suite、BMad Loop、Game Dev Studio（Unity/Unreal/Godot/Phaser）。安装：`npx skills add bmad-code-org/BMAD-METHOD` 或 Claude Code / Codex 插件市场。注意事项：v4→v6 是破坏性重构（agents/tasks 换成 skills），旧教程不通用；文档站 docs.bmad-method.org。
- **关联**：库内 [obra/superpowers](https://github.com/obra/superpowers)、[github/spec-kit](https://github.com/github/spec-kit)（同属方法论驱动的 Agent 开发框架）
- **归档**：`开源项目介绍/2026.9.27/BMAD-METHOD.md`
- **标签**：`#ai-agent` `#multi-agent` `#agile` `#methodology` `#workflow` `#context-engineering`

### [bytedance/deer-flow](https://github.com/bytedance/deer-flow)
- **定位**：字节跳动开源的长程 SuperAgent Harness：会研究、会写码、会创作，配沙箱/记忆/技能/子代理。
- **简介**：字节跳动开源的长程 SuperAgent Harness：会研究、会写码、会创作，配沙箱/记忆/技能/子代理。（GitHub 每日趋势 2026-09-30：★83220，当日 +79）
- **归档**：`开源项目介绍/2026.9.30/deer-flow.md`
- **标签**：`#python`

### [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates)
- **定位**：Claude Code 的配置与监控 CLI 工具（含 Agent 仪表盘模板）。
- **简介**：Claude Code 的配置与监控 CLI 工具（含 Agent 仪表盘模板）。（GitHub 每日趋势 2026-09-26：★31789，当日 +91）
- **归档**：`开源项目介绍/2026.9.28/claude-code-templates.md`
- **标签**：`#python`

### [earendil-works/pi](https://github.com/earendil-works/pi)
- **定位**：通用 AI Agent 工具箱 · 编码 Agent 运行时
- **简介**：TypeScript Monorepo（爆火的 OpenClaw 即基于此开发），由 mitsuhiko（Flask 作者）等人维护。四大核心包：统一多厂商 LLM API（pi-ai）、Agent 运行时（pi-agent-core）、交互式编码 Agent CLI（pi-coding-agent）、差分渲染终端 UI 库（pi-tui）。支持模型轮换、扩展思考、会话分支、HTML 导出、包管理器。55.6k stars、4,288 commits、222 releases（v0.75.5），MIT 协议。强调供应链安全：精确版本固定、shrinkwrap 传递依赖锁定、CI 审计签名。配套 OSS 会话数据共享计划，助力开源编码 Agent 改进。
- **归档**：`开源项目介绍/2026.9.6/pi.md`
- **标签**：`#agent` `#typescript` `#编码agent` `#monorepo`

### [Fosowl/agenticSeek](https://github.com/Fosowl/agenticSeek)
- **定位**：100% 本地运行的开源 Manus AI 替代品，自主浏览网页、写代码、做任务规划
- **简介**：agenticSeek 是 Fosowl 于 **2025-02-19** 发起的开源项目，定位 **Manus AI 的 100% 本地替代品**——不用云端 API、不产生月度账单，"只花电费"就能得到一个会思考、会浏览网页、会写代码的自主 Agent，文件、对话与搜索记录全部留在本机。核心能力由五类 Agent 构成（CasualAgent、CoderAgent、FileAgent、PlannerAgent、BrowserAgent），由仓库内 `llm_router/`（依赖 adaptive-classifier）按 query 自动分派；BrowserAgent 基于 Selenium + undetected-chromedriver + selenium-stealth 做隐身浏览、信息抽取与表单填写，CoderAgent 可无人监督地编写、调试并运行 Python/C/Go/Java 程序，PlannerAgent 负责把复合任务拆步执行。语音链路由本地 Vosk（STT）与 Kokoro（TTS）组成，靠唤醒词（即 `agent_name`）触发，但语音输入目前仅限 CLI 模式且只支持英文。技术栈：**Python（FastAPI + uvicorn + Celery，broker 用 Valkey/Redis）后端 + React 19（CRA）前端 + Docker Compose**，一键拉起 SearxNG 元搜索、Redis、前后端四个服务；`sources/` 内含 agents、browser、llm_provider、workspace、api_auth（Token 鉴权）等模块，另有 `prompts/`、`crx/` 扩展目录。模型侧本地支持 ollama / lm-studio / OpenAI 兼容端点（llama.cpp、vLLM、LM Studio），云端可选 OpenAI、Google、DeepSeek、Hugging Face、TogetherAI、OpenRouter、MiniMax；README 明确提示复杂浏览与规划任务不要用 gpt-4o，因为提示词是针对 DeepSeek 类推理模型调优的。硬件门槛：14B/12GB VRAM 勉强可用，32B/24GB+ 多数任务可行，70B+/48GB 最佳。协议 **GPL-3.0**；规模 **27,306 stars / 3,061 forks / 177 watchers / 992 commits / 44 位贡献者**，仓库约 27 MB，README 提供含简繁中文在内的 8 种语言版本。注意事项：项目**从未发布任何 Release 或 tag**（shields、badgen、GitHub Releases API 三方确认为 0），只能跟 `main` 滚动使用；作者自述这是"零路线图、零融资"的副业项目，并声明除 @Martin993886460 外的 agenticSeek X 账号均为假冒；`pushed_at` 为 2026-09-24，但默认分支最后一次提交约在 2026-09-13，主干节奏放缓；表单填写与语音仍标注为实验性。三大高频坑：ChromeDriver 与 Chrome 版本必须匹配、Docker 内访问宿主 Ollama 需设 `OLLAMA_HOST=0.0.0.0`、SearxNG 基址在 Web 与 CLI 模式下取值不同。社区入口为 GitHub Discussions 与 Discord。
- **归档**：`开源项目介绍/2026.9.25/agenticSeek.md`
- **标签**：`#ai-agent` `#本地大模型` `#browser-automation` `#manus-alternative` `#voice-assistant` `#docker`

### [github/spec-kit](https://github.com/github/spec-kit)
- **定位**：开源规范驱动开发（Spec-Driven Development）工具包，适配任意 AI 编码 Agent
- **简介**：GitHub 官方开源，核心理念「先定义要构建什么，再开始构建」——让规范变得可执行、直接生成实现。提供 specify-cli（Python）与 /speckit.* 系列命令（constitution → specify → plan → tasks → implement → converge，另含 clarify/analyze/checklist），支持 30+ AI 编码 Agent（Claude Code、Codex CLI、Copilot CLI、Command Code 等）。四级定制系统：项目本地覆盖 → Presets → Extensions → 核心模板。1,807 commits，社区活跃（含中文 README）。
- **归档**：`开源项目介绍/2026.8.18/spec-kit.md`
- **标签**：`#spec-driven` `#ai-coding` `#github` `#cli`

### [google/ax](https://github.com/google/ax)
- **定位**：谷歌开源的 Agent 编排运行时。
- **简介**：谷歌开源的 Agent 编排运行时。（GitHub 每日趋势 2026-09-26：★11252，当日 +1386）
- **归档**：`开源项目介绍/2026.9.28/ax.md`
- **标签**：`#go`

### [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman)
- **定位**：原始人语录省 token：让编码 Agent 像原始人一样说话，削减 65% token（病毒式 Skill＋代理）。
- **简介**：原始人语录省 token：让编码 Agent 像原始人一样说话，削减 65% token（病毒式 Skill＋代理）。（GitHub 每日趋势 2026-10-03：★108963，当日 +271）
- **归档**：`开源项目介绍/2026.10.3/caveman.md`
- **标签**：`#go`

### [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux)
- **定位**：cmux：基于 Ghostty 的 macOS 终端，带垂直标签页与 AI Agent 通知，专为多任务设计。
- **简介**：cmux：基于 Ghostty 的 macOS 终端，带垂直标签页与 AI Agent 通知，专为多任务设计。（GitHub 每日趋势 2026-10-08：★27774，当日 +96）
- **归档**：`开源项目介绍/2026.10.8/cmux.md`
- **标签**：`#swift`

### [microsoft/agent-framework](https://github.com/microsoft/agent-framework)
- **定位**：微软官方 Agent 框架：构建、编排与部署 AI Agent 和多 Agent 工作流（支持 Python 与 .NE
- **简介**：微软官方 Agent 框架：构建、编排与部署 AI Agent 和多 Agent 工作流（支持 Python 与 .NET）。（GitHub 每日趋势 2026-10-09：★14017，当日 +24）
- **归档**：`开源项目介绍/2026.10.9/agent-framework.md`
- **标签**：`#python`

### [mksglu/context-mode](https://github.com/mksglu/context-mode)
- **定位**：AI 编码 Agent 的上下文窗口优化：沙箱化工具输出（缩减 98%）、持久会话记忆、强制轮转策略。
- **简介**：AI 编码 Agent 的上下文窗口优化：沙箱化工具输出（缩减 98%）、持久会话记忆、强制轮转策略。（GitHub 每日趋势 2026-10-01：★24385，当日 +88）
- **归档**：`开源项目介绍/2026.10.1/context-mode.md`
- **标签**：`#typescript`

### [mvschwarz/openrig](https://github.com/mvschwarz/openrig)
- **定位**：把 Claude Code 与 Codex 等多个编码 Agent 作为一个系统协同运行的多智能体 Harness。
- **简介**：把 Claude Code 与 Codex 等多个编码 Agent 作为一个系统协同运行的多智能体 Harness。（GitHub 每日趋势 2026-09-28：★744，当日 +114）
- **归档**：`开源项目介绍/2026.9.28/openrig.md`
- **标签**：`#typescript`

### [NVIDIA/OpenShell](https://github.com/NVIDIA/OpenShell)
- **定位**：英伟达出品：面向自主 AI Agent 的安全私有运行时。
- **简介**：英伟达出品：面向自主 AI Agent 的安全私有运行时。（GitHub 每日趋势 2026-09-30：★10312，当日 +978）
- **归档**：`开源项目介绍/2026.9.30/OpenShell.md`
- **标签**：`#rust`

### [obra/superpowers](https://github.com/obra/superpowers)
- **定位**：为编码智能体提供可组合技能库与完整软件开发方法论的 Agent 技能框架
- **简介**：**Superpowers** 是 Jesse Vincent（obra）与 Prime Radiant 团队打造的**智能体技能框架与软件开发方法论**，MIT 协议，主语言 Shell，创建于 2025-10-09。其核心理念是让编码智能体不再直接跳进代码：先经 **brainstorming** 技能苏格拉底式提问提炼规格，再用 **writing-plans** 把工作拆成 2-5 分钟的细粒度任务，随后以 **subagent-driven-development（SDD）**派发全新子代理逐任务实现并做两阶段评审，或以 v6.4.1 重建的 **executing-plans 原生内联模式**在当前会话跑完全部任务、最后做一次全分支评审（最省钱路径）；全程强制 **RED-GREEN-REFACTOR 的 TDD 纪律**（先于测试写的代码会被删除，以项目整体测试套件定义"绿"）、git worktree 隔离与代码评审门禁。**差异化优势**在于跨 Harness 通用：同一套技能可安装到 Claude Code、Codex App/CLI、Cursor、Gemini CLI、GitHub Copilot CLI、OpenCode（含 2.0 原生 API）、Qwen Code、Devin CLI、Factory Droid、Grok Build CLI、Kimi Code、Antigravity、Pi、Hermes Agent、Muse 等十余种编码智能体，通过 SessionStart 钩子在会话启动与上下文压缩后自动注入引导指令，技能自动触发无需手动调用。v6.4.1（2026-09-19）还新增 **diagnosing-superpowers** 会话诊断技能，可读取转录给出 path:line 级证据并生成脱敏报告包；SDD 支持同名计划独立工作区、review-package 拒绝空 BASE..HEAD 范围、控制器下沉嵌套子代理省约一半成本。**规模数据**：约 291,172 Stars、26,049 Forks、401 开放 Issues、1,087 Watchers、约 682 commits、37 位贡献者、35 个 tags，最近推送 2026-09-22，是 Agent 技能生态中增长最猛的项目之一。**注意事项**：官方一般不接受新技能贡献，技能修改须兼容所有受支持的智能体；brainstorming 可视化伴侣含可选遥测（仅版本号，可用 SUPERPOWERS_DISABLE_TELEMETRY 关闭）；企业支持走 Prime Radiant 商业服务；社区渠道为 Discord 与 GitHub Issues。
- **归档**：`开源项目介绍/2026.9.25/superpowers.md`
- **标签**：`#agent-skill` `#sdd` `#tdd` `#claude-code` `#methodology` `#plugin`

### [omnigent-ai/omnigent](https://github.com/omnigent-ai/omnigent)
- **定位**：Omnigent：开源 AI Agent 框架与元 Harness——编排 Claude Code/Codex/Curs
- **简介**：Omnigent：开源 AI Agent 框架与元 Harness——编排 Claude Code/Codex/Cursor/Pi 与自定义 Agent。（GitHub 每日趋势 2026-10-07：★10621，当日 +50）
- **归档**：`开源项目介绍/2026.10.8/omnigent.md`
- **标签**：`#python`

### [openclaw/openclaw](https://github.com/openclaw/openclaw)
- **定位**：真正能干活的 AI，任意系统任意平台——龙虾之道（基于 pi 框架的明星项目）。
- **简介**：真正能干活的 AI，任意系统任意平台——龙虾之道（基于 pi 框架的明星项目）。（GitHub 每日趋势 2026-10-01：★390908，当日 +136）
- **归档**：`开源项目介绍/2026.10.1/openclaw.md`
- **标签**：`#typescript`

### [openclaw/openclaw-windows-node](https://github.com/openclaw/openclaw-windows-node)
- **定位**：OpenClaw 的 Windows 伴侣套件。
- **简介**：OpenClaw 的 Windows 伴侣套件。（GitHub 每日趋势 2026-10-02：★2133，当日 +2）
- **归档**：`开源项目介绍/2026.10.2/openclaw-windows-node.md`
- **标签**：`#csharp`

### [pingdotgg/t3code](https://github.com/pingdotgg/t3code)
- **定位**：T3 堆栈的 AI 编码助手（Theo 出品，T3Chat 作者的终端 Agent）。
- **简介**：T3 堆栈的 AI 编码助手（Theo 出品，T3Chat 作者的终端 Agent）。（GitHub 每日趋势 2026-10-03：★24487，当日 +251）
- **归档**：`开源项目介绍/2026.10.4/t3code.md`
- **标签**：`#typescript`

### [pydantic/pydantic-ai](https://github.com/pydantic/pydantic-ai)
- **定位**：Python 的 AI 之道：Agent、实时语音、图像生成、嵌入——任意模型、任意接口、端到端类型安全。
- **简介**：Python 的 AI 之道：Agent、实时语音、图像生成、嵌入——任意模型、任意接口、端到端类型安全。（GitHub 每日趋势 2026-10-01：★20292，当日 +24）
- **归档**：`开源项目介绍/2026.10.1/pydantic-ai.md`
- **标签**：`#python`

### [strands-agents/harness-sdk](https://github.com/strands-agents/harness-sdk)
- **定位**：面向生产级 AI Agent 的开源 Harness SDK（Python/TypeScript），任意模型任意云，可端
- **简介**：面向生产级 AI Agent 的开源 Harness SDK（Python/TypeScript），任意模型任意云，可端到端构建与掌控 Agent。（GitHub 每日趋势 2026-09-26：★8445，当日 +251）
- **归档**：`开源项目介绍/2026.9.27/harness-sdk.md`
- **标签**：`#python`

### [vastsa/PI-Desktop](https://github.com/vastsa/PI-Desktop)
- **定位**：AI Agent 的模块化桌面工作空间（本地优先 · 模型无关 · 插件驱动）
- **简介**：**把项目、Agent、模型、插件和工作流带进一个持久的桌面环境**——macOS / Windows / Linux。核心主张三句话：**Your projects stay local · Your models stay replaceable · Your workspace stays yours**（项目留在本地、模型随时可换、工作空间归你所有）。定位很清晰：终端 Agent 擅长执行，IDE Agent 擅长住在编辑器里，PI-Desktop 再往前走一步——**给 AI Agent 一个属于它们自己的、持久的、独立的、可扩展的桌面工作空间**。四大支柱：**独立工作空间**（不依赖任何特定 IDE 或终端，项目/会话/审查/预览/agent 都活在自己的空间里）· **插件驱动**（插件扩展的**不只是 agent**，可以添加面板、视图、小组件、工具、MCP 服务器、主题和后台服务）· **Agent 编排**（一个 agent 往往不够，可委派给 **Subagent** 或并行协调整整的 **Worker Session**）· **模型自由**（云端模型、本地模型、自定义网关、兼容 API，**换模型不用重建工作流**）。技术架构是 **Electron + Rust host core + pi Agent Harness + 用户可安装插件**，前端 React + TypeScript，走 MCP 协议，带 i18n（含简体中文 README）。当前发布线 **0.15.x（Early Preview）**。LGPL-3.0，5,206 stars / 435 forks / 139 open issues，文档站 [pi-docs.aiuo.net](https://pi-docs.aiuo.net/)，社区 [r/AIUO](https://www.reddit.com/r/AIUO/)，2026-09-22 仍在推送。
- **归档**：`开源项目介绍/2026.9.23/PI-Desktop.md`
- **标签**：`#agent宿主` `#electron` `#rust` `#插件` `#本地优先` `#mcp`

<a id="sec-2"></a>

## 📱 二、手机自动化 Agent（7）

### [droidrun/mobilerun](https://github.com/droidrun/mobilerun)
- **定位**：AI 控制手机 · Android/iOS 自动化 Agent 框架（原 droidrun）
- **简介**：基于 AI 大模型的 Android/iOS 自动化 Agent 框架（GitHub 6.2K Star，仓库已更名为 mobilerun）。核心理念「将思考交给 AI、将执行交给框架」，打破传统自动化脚本对特定 UI 控件的强依赖。1,153 commits、86 tags、25 branches，compat 层提供向后兼容，2026-05 最新更新。
- **归档**：`开源项目介绍/2026.9.6/mobilerun.md`
- **标签**：`#agent` `#手机自动化` `#跨平台`

### [IPADS-SAI/MobiAgent](https://github.com/IPADS-SAI/MobiAgent)
- **定位**：AI 控制手机 · 可定制移动智能体框架（IPADS 实验室）
- **简介**：三位一体系统：**MobiMind 模型家族** + **AgentRR 加速框架** + **MobiFlow 基准测试平台**。Planner 制定整体计划、Decider 判断每一步点击位置、Grounder 精准定位屏幕坐标。2026 年新增 **MobiMem 画像记忆系统**（两篇论文：arXiv 2509.00531 + 2512.15784）、**移动端独立部署**、**多模型适配器**（stepfun 等）、**UI 语义自动采集**。覆盖小红书、高德、饿了么、淘宝等 10+ 主流 App，Apache-2.0 协议，216 commits，持续活跃更新（2026-07 最新提交）。
- **归档**：`开源项目介绍/2026.9.6/MobiAgent.md`
- **标签**：`#agent` `#手机自动化` `#多模态` `#学术研究`

### [minitap-ai/mobile-use](https://github.com/minitap-ai/mobile-use)
- **定位**：AI 控制手机 · Python 库（Minitap AI）
- **简介**：Python 库（约 1.8K Star），支持安卓和 iOS。截取屏幕图像 + 用户指令 → 多模态模型分析返回坐标/操作 → 转换为 ADB 命令执行，完成后再次截图确认，直至任务完成。集成 Maestro 移动测试框架作为底层交互引擎，支持 OpenAI API 与本地部署等多种模型后端。v2 新增 **MCP Server**，有完整文档站（docs.minitap.ai）和学术论文（arXiv 2602.07787）。Apache-2.0 协议。
- **归档**：`开源项目介绍/2026.9.6/mobile-use.md`
- **标签**：`#agent` `#手机自动化` `#python` `#mcp`

### [mobile-next/mobile-mcp](https://github.com/mobile-next/mobile-mcp)
- **定位**：让 AI Agent 驱动 iOS/Android 真机与模拟器的 MCP 服务器
- **简介**：mobile-next/mobile-mcp 是一个 **模型上下文协议（MCP）服务器**，把 iOS/Android 原生操作以结构化工具暴露给 LLM/Agent，让 AI 无需懂 XCUITest/Espresso 即可驱动模拟器、仿真器与真机。**Apache-2.0** 协议，主语言 **TypeScript**，官网 mobilenext.ai。最大差异化是**「可访问性优先」**：默认基于原生 accessibility tree 读取真实 UI 元素驱动应用，**不需视觉模型、不消耗图像 token**，必要时才回退截图+坐标，因而更快、更省、更确定；一套 API 横跨 iOS/Android × 模拟器/仿真器/真机。能力覆盖点击/滑动/手势、应用安装卸载启动终止、录屏、硬件按键、深链、屏幕方向、剪贴板、GPS 定位覆盖、设备日志与崩溃报告，并有 `mobile_batch_commands` 一次调用串联多工具；可 stdio 或 `--listen` 起 Streamable HTTP（无状态、可水平扩展）；配合 Mobile Next Cloud 调度远程真机池。自 **1.0.0（2026-08-02，BREAKING）** 起后端切换为通用设备 CLI **mobilecli**（替代旧 TS 实现，可用 MOBILEMCP_LEGACY_ROBOT 临时回退），iOS 用开源 Device Kit 取代 WebdriverAgent，Android 内嵌 agent 免装 APK。兼容 Claude Code、Codex、Gemini、Copilot、Antigravity、Cursor、Cline、Goose、Kiro、opencode、Windsurf、Amp，安装 `npx -y @mobilenext/mobile-mcp@latest`，环境变量控制鉴权与关遥测。规模数据（2026-09-27）：Stars ~7,305、Forks 640、Open Issues 43、Commits 438，创建 2025-03-28，最近推送 2026-09-23，最新版本 1.0.4（2026-09-13）。注意事项：需 Node v20+ 与 Xcode/Android 平台工具；贡献者精确值与 tags 总数因 API 限流未获取到。
- **关联**：库内 [MobiAgent](https://github.com/IPADS-SAI/MobiAgent)、[MobileAgent](https://github.com/X-PLUG/MobileAgent)、[mobile-use](https://github.com/minitap-ai/mobile-use)（同为 AI 操控手机，本项走 MCP + 可访问性树而非视觉截图）
- **归档**：`开源项目介绍/2026.9.27/mobile-mcp.md`
- **标签**：`#mcp` `#手机自动化` `#ios` `#android` `#ai-agent`

### [TencentQQGYLab/AppAgent](https://github.com/TencentQQGYLab/AppAgent)
- **定位**：AI 控制手机 · 腾讯多模态智能体（CHI 2025）
- **简介**：「Multimodal Agents as Smartphone Users」：通过 ADB 获取屏幕截图 → 多模态大模型分析 UI 元素 → 决定点击坐标或滑动，实现真正的视觉交互。模仿人类学习新软件的过程，自主探索或观察演示后为每个 App 生成使用文档（Knowledge Base），执行任务时精准调用。MIT 协议，CHI 2025 论文，33 commits。**下一代 AppAgentX** 已发布，引入进化机制。
- **归档**：`开源项目介绍/2026.9.6/AppAgent.md`
- **标签**：`#agent` `#手机自动化` `#知识库` `#学术研究`

### [trycua/cua](https://github.com/trycua/cua)
- **定位**：cua：用开源驱动、跨 OS 机群与基准测试规模化 Computer-Use 2.0。
- **简介**：cua：用开源驱动、跨 OS 机群与基准测试规模化 Computer-Use 2.0。（GitHub 每日趋势 2026-10-08：★28665，当日 +229）
- **归档**：`开源项目介绍/2026.10.8/cua.md`
- **标签**：`#rust`

### [X-PLUG/MobileAgent](https://github.com/X-PLUG/MobileAgent)
- **定位**：AI 控制手机 · 阿里 X-PLUG 多模态智能体
- **简介**：能看见屏幕、能点击按钮、能像人一样跨 APP 操作，不依赖系统后台接口。AI 识别屏幕上所有图标、文字和按钮（纯图标也能靠视觉理解），生成逐步计划，通过 ADB 发送点击/滑动/输入指令，每步截图确认并自我修正。已迭代至 **v3.5 版本**（v1→v2→v3→v3.5），含 Mobile-Agent-E 变体和 GUI-Critic-R1 评估模型。420 commits、191 issues，2026-08 最新更新。
- **归档**：`开源项目介绍/2026.9.6/MobileAgent.md`
- **标签**：`#agent` `#手机自动化` `#adb` `#多模态`

<a id="sec-3"></a>

## 🧠 三、Agent 记忆与知识蒸馏（9）

### [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)
- **定位**：AI 编码 Agent 长期记忆 · 跨工具跨机器共享
- **简介**：为 **20+ 编码 Agent**（Claude Code、Codex、Cursor、OpenCode、Grok、Devin、Kimi、Pi、OpenClaw 等）提供统一的长期记忆层。在 Claude Code 中途离开，到 Codex 里打开同一目录就能无缝接手——进度、失败尝试、开放问题全部自动传递。记忆是 **git 备份的纯 Markdown wiki**，可 grep、可 Obsidian 打开、可手动编辑、随时从文件重建索引。**默认零 LLM 调用**，捕获/搜索/交接全不用 API Key。支持团队共享（多用户认证、审计日志内置，不是付费层）。Rust 单体二进制，~700/s 写入上限，MIT 协议。
- **归档**：`开源项目介绍/2026.9.16/ai-memory.md`
- **标签**：`#agent` `#记忆` `#rust` `#跨工具` `#团队协作`

### [kangarooking/cangjie-skill](https://github.com/kangarooking/cangjie-skill)
- **定位**：「仓颉 Skill」知识精馏工具
- **简介**：将书籍、视频等深度知识蒸馏为可被 AI 调用的结构化 Skill。采用六阶段知识精馏法，提炼可执行的方法论、决策规则和框架；2.0 版本支持蒸馏视频。**v2.5.0 于 2026 年 8 月底发布**，新增 DeepSeek Harness 支持。包含示例 Skill（如 naval-almanack-skill《纳瓦尔宝典》蒸馏）和基准测试。58 commits，持续活跃更新。
- **归档**：`开源项目介绍/2026.9.6/cangjie-skill.md`
- **标签**：`#skill` `#知识蒸馏` `#方法论`

### [mem0ai/mem0](https://github.com/mem0ai/mem0)
- **定位**：AI Agent 的记忆层：可插拔的记忆基础设施，上下文持久化、面向生产环境。
- **简介**：AI Agent 的记忆层：可插拔的记忆基础设施，上下文持久化、面向生产环境。（GitHub 每日趋势 2026-09-30：★66314，当日 +119）
- **归档**：`开源项目介绍/2026.9.30/mem0.md`
- **标签**：`#python`

### [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem)
- **定位**：为每个 Agent 提供跨会话持久上下文：捕获会话中的所有操作，AI 压缩后自动恢复。
- **简介**：为每个 Agent 提供跨会话持久上下文：捕获会话中的所有操作，AI 压缩后自动恢复。（GitHub 每日趋势 2026-10-03：★95363，当日 +115）
- **归档**：`开源项目介绍/2026.10.4/claude-mem.md`
- **标签**：`#typescript`

### [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill)
- **定位**：数字痕迹蒸馏 Skill —— 已升级为 dot-skill，可蒸馏任何人（同事 / 关系 / 名人）
- **简介**：原「同事.Skill」已升级为 **dot-skill**（2026.08 突破 20K ⭐）：将数字痕迹（聊天记录、文档、邮件、截图）蒸馏为可独立运行的 AI Skill。从「蒸馏同事」扩展为蒸馏任何人：**colleague**（Work Skill + Persona 双层架构，含技术规范/流程/知识库）、**relationship**（伴侣/家人/朋友，表达 DNA + 情绪触发点）、**celebrity**（名人/小说角色，六维度研究工具链：字幕下载→文稿清洗→研究合并→质量检查）。五端通用：Claude Code / Hermes / OpenClaw / Codex / DeepSeek Harness。数据源支持飞书/钉钉/Slack 自动采集、微信聊天记录（SQLite）、PDF/邮件/Markdown。人格画像 6 层性格结构，支持增量 merge 与对话纠正。技术报告：COLLEAGUE.SKILL（arXiv 2605.31264），上海 AI Lab · AI Safety Center 支持，MIT 协议，109 commits。
- **归档**：`开源项目介绍/2026.9.6/dot-skill.md`（早期版本另存于 `开源项目介绍/2026.8.18/dot-skill-colleague-skill.md`）
- **标签**：`#skill` `#知识蒸馏` `#dot-skill`

### [topoteretes/cognee](https://github.com/topoteretes/cognee)
- **定位**：开源 AI 记忆平台：给 Agent 装上持久化长期记忆，小模型即可免费运行。
- **简介**：开源 AI 记忆平台：给 Agent 装上持久化长期记忆，小模型即可免费运行。（GitHub 每日趋势 2026-09-29：★31128，当日 +103）
- **归档**：`开源项目介绍/2026.9.29/cognee.md`
- **标签**：`#python`

### [vectorize-io/hindsight](https://github.com/vectorize-io/hindsight)
- **定位**：会学习与反思的 Agent 长期记忆系统，LongMemEval 基准 SOTA
- **简介**：**Hindsight** 是 Vectorize.io 开源的 Agent 记忆系统（MIT 协议，主语言 Python），定位 "Agent Memory That Learns"——重点不是复述对话历史，而是让 Agent 随时间积累认知。核心为三大操作：**retain**（LLM 抽取事实/实体/关系/时序并归一化入库）、**recall**（语义向量 + BM25 + 图谱 + 时间四路并行检索，RRF 融合与 cross-encoder 重排）、**reflect**（跨记忆深度反思形成新关联）。记忆采用仿生分层：世界事实、经验、观察（带证据引用与证明计数、增量精炼而非覆盖的信念）、心智模型与知识页（后台自动重写的活文档），按 bank 严格隔离并可携带性格特质（怀疑度、字面化、同理心）。官方称在 **LongMemEval** 基准达到 SOTA，成绩由 Virginia Tech Sanghani 中心与《华盛顿邮报》独立复现，已被财富 500 强生产使用，论文见 arXiv:2512.12818。接入方式极丰富：两行代码的 LLM Wrapper（基于 LiteLLM 覆盖 100+ 模型，可直接复用 ChatGPT/Claude/Cursor/Copilot 订阅免 API Key）、60+ 框架与应用集成（LangGraph、CrewAI、n8n、Dify、Obsidian 等）、每个 server 内置 **MCP** 端点、为 Claude Code/Codex/Cursor CLI 等十余种编码代理一键安装按仓库划分的长期项目记忆。部署支持 Docker、pip、Helm/K8s、pg0 内嵌无服务器模式与托管 Hindsight Cloud；存储为 PostgreSQL+pgvector 或 Oracle AI Database 23ai。安全侧有 Memory Defense（45 种密钥/PII 模式脱敏或拦截），多语言端到端保留原文。规模：**27,656 stars / 2,676 forks / 244 贡献者 / 3,178 commits / 268 tags**，创建于 2025-10-30，最新 v0.10.1（2026-09-21），最近推送 2026-09-24。注意：retain/recall 依赖外部 LLM 提供商；Cloud 为按用量付费托管；Intel Mac 需装 hindsight-all-slim。
- **关联**：库内 [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory)（同为 Agent 长期记忆方案，体量更轻）
- **归档**：`开源项目介绍/2026.9.25/hindsight.md`
- **标签**：`#agent-memory` `#mcp` `#llm` `#rag` `#python`

### [VictorTaelin/OptMem](https://github.com/VictorTaelin/OptMem)
- **定位**：AI Agent 的永久记忆：426 token 的提示词＋一个脚本，即插即用。
- **简介**：AI Agent 的永久记忆：426 token 的提示词＋一个脚本，即插即用。（GitHub 每日趋势 2026-10-06：★1962，当日 +85）
- **归档**：`开源项目介绍/2026.10.8/OptMem.md`
- **标签**：`#python`

### [virgiliojr94/book-to-skill](https://github.com/virgiliojr94/book-to-skill)
- **定位**：技术书自动转 Agent Skill
- **简介**：将技术书（PDF/EPUB/DOCX 等）自动转化为核心 SKILL.md（心智模型）+ 按章节拆分的 Markdown 文件，Agent 按需加载对应章节，避免全文塞入上下文。支持 Claude Code、Copilot CLI、Amp 等。176 commits，Python 实现，含评估测试和工具脚本。
- **归档**：`开源项目介绍/2026.9.6/book-to-skill.md`
- **标签**：`#skill` `#书籍` `#知识蒸馏`

<a id="sec-4"></a>

## ✍️ 四、写作与文本风格 Skills（5）

### [ayghri/i-have-adhd](https://github.com/ayghri/i-have-adhd)
- **定位**：一份 SKILL.md，让编码 Agent 别把答案埋在客套话里
- **简介**：副标题「ADHD-friendly outputs. No ADHD diagnosis needed!」点明定位——**这不是医疗工具，而是一种更好的默认输出风格**。它解决的痛点极具普遍性：AI 答案是对的，但被埋住了——「Great question!」开场、三层背景铺垫、真正的命令藏在第四段、末尾「Hope this helps!」。做法不调模型、不写后处理，只把 ADHD 友好沟通原则编码成 Skill。**10 条硬规则**：首行必须是可执行动作 · 多步必编号且单步内不许出现两次「and then」· 结尾只给一个 2 分钟内能做的事 · 旁支必须先完成当前再作为独立问句抛出 · 每轮重述「第 3 步/共 5 步」· **时间估计必须给具体单位**（「a bit」和「a few hours」在 ADHD 脑中等价）· 成果要可验证地展示 · 报错禁用「Uh oh」只讲原因与修法 · 列表每组封顶 5 项（**但明确声明只约束呈现、不得限制分析与搜索**）· 禁开场白禁复述禁收尾客套。真正值得研究的是它的严谨度：规则建立在 **5 条明确认知模型**上（工作记忆小、知道≠做到、启动最难、时间感扁平、多巴胺稀缺）；有 **6 条「破例条款」**——用户要求 explain 时充分展开、**破坏性操作前必须确认（安全高于简洁）**、连续三轮 still broken 就停止改码转而质疑前提、真实歧义时问一句胜过猜错重写、规则与任务冲突时任务赢、规则与 Agent 宿主冲突时 system prompt 赢；还有发送前自检清单，最后验证「**只读首行和末行能否知道下一步做什么、刚发生了什么**」。frontmatter 设 `disable-model-invocation: true`，只能用户显式 `/i-have-adhd` 触发，规则整会话持续生效、说 stop adhd mode 才关闭。MIT，Python（仓库仅 416KB），**50,303 stars** / 2,902 forks / 71 open issues，README 提供 10 种语言（含简中/日/韩/波斯/泰/阿），2026-05 创建。**star/fork 比高达 17:1**——绝大多数人是认同理念顺手点星，这是对「AI 太啰嗦」这一痛点最强的投票。
- **归档**：`开源项目介绍/2026.9.23/i-have-adhd.md`
- **标签**：`#skill` `#输出风格` `#提示词工程` `#adhd` `#开发者体验`

### [blader/humanizer](https://github.com/blader/humanizer)
- **定位**：去除 AI 生成文本痕迹的 Agent Skill
- **简介**：基于 Wikipedia「AI 写作迹象」指南，识别并修正 **35 种** 典型 AI 写作模式（夸大重要性、AI 词汇滥用、三段式强迫症、破折号泛滥、假深层真理、聊天机器人语气等六大类），两轮改写 + 模式自检，让文本更自然更像人写的，不改变原意、不编造事实。支持提供写作样本匹配个人语气，可直接处理文件（不动代码/frontmatter/链接）。MIT 协议，版本 v2.11.2，54 commits，兼容所有支持 Agent Skills 标准的工具。
- **归档**：`开源项目介绍/2026.9.6/humanizer.md`
- **标签**：`#skill` `#写作` `#ai文本去痕` `#维基百科`

### [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail)
- **定位**：让你的 AI Agent 像最懒的资深工程师一样思考——最好的代码是从没写过的代码。
- **简介**：让你的 AI Agent 像最懒的资深工程师一样思考——最好的代码是从没写过的代码。（GitHub 每日趋势 2026-10-01：★148891，当日 +865）
- **归档**：`开源项目介绍/2026.10.1/ponytail.md`
- **标签**：`#javascript`

### [op7418/Humanizer-zh](https://github.com/op7418/Humanizer-zh)
- **定位**：Claude Code 中文文本润色 Skill，消除文本中 AI 生成痕迹
- **简介**：**Humanizer-zh** 是 blader/humanizer（v3.0.0）的汉化版本，以纯 Markdown 提示词文档（SKILL.md）形态运行的 **Claude Code Skill**，核心能力是编辑文章、评论、文档中的空话、重复与模板化表达，同时严格保留事实、确定程度和作者声音，默认只交付最终改写稿，没问题的句子可以不改。它维护 **31 个检查点**，沿用 A–F 六大分类：A 铺垫代替陈述（假对比、戏剧性碎片、伪深度等）、B 公式化节奏（强凑三段式、万能破折号、限定堆叠等）、C 拔高与借权威（空泛高频词、意义拔高、权威背书等）、D 公式化排版（无效粗体、装饰性标题）、E 聊天与草稿残留（客服腔、重复免责）、F **中文补充检查**（长定语、"进行＋动词"、被字句堆叠、四字词排比、万能背景、套话收尾）。**差异化**：一是深度中文化并新增 F 类中文专属检查点；二是 2026-09-23 修订强调"克制"——普通排比、破折号、连接词不再一律修改，不编造功能/数据/来源/第一人称经历，"可能"不变"确定"、"计划"不变"已经"；三是边界清晰：它是给 Agent 执行的编辑指导而非检测程序，作者明确声明不能证明文章由谁撰写、不保证通过任何 AI 检测器。**技术栈**：无运行时代码，SKILL.md+README 结构（GitHub 主语言显示 Python 来自结构检查脚本）；安装支持 npx skills add 一键、git clone 到 ~/.claude/skills/ 或手动复制，/humanizer-zh 调用；来源含本仓库 PR #39/#34、stop-slop、Wikipedia「Signs of AI writing」；tests/ 提供 18 个短文本案例、Markdown 样例与结构检查脚本。**协议** MIT。**规模与时间线**：2026-01-19 创建，最近推送 2026-09-23；**Stars 18,392、Forks 1,198**、Open Issues 31、Watchers 30；Commits 仅 7、贡献者 3，无正式 Release/Tag，属"文档即产品"的轻量维护模式，大版本迭代经由大型 PR 重写完成。**注意事项**：润色效果依赖宿主 Agent 的执行质量；文件编辑默认保留代码、命令、路径、YAML 与锚点；不可将其用作 AI 写作检测或作者身份判定依据。
- **关联**：库内 [blader/humanizer](https://github.com/blader/humanizer)（英文原版，本仓库为其汉化版）
- **归档**：`开源项目介绍/2026.9.25/Humanizer-zh.md`
- **标签**：`#claude-code` `#agent-skill` `#chinese` `#写作` `#humanizer`

### [petergyang/no-ai-slop](https://github.com/petergyang/no-ai-slop)
- **定位**：清除 20+ 种 AI 味写作套路、同时保留作者个人声音的 Agent 写作净化 Skill
- **简介**：Creator Economy newsletter 主理人 Peter Yang 出品，**约 2 个月破万 star 的「Skill 即产品」现象级案例**。识别并清除 AI 生成文本的套路化表达：**二元对比**（"It's not X. It's Y."）、**清嗓开场**（"Here's the thing"）、**伪洞察铺垫**（"What nobody tells you"）、**冒号揭晓**、**戏剧性断句**、**重要性吹捧**（"a testament to"）、**含糊引用**（"experts agree"）、**同义词轮换**、**假深刻结尾**等 20+ 种模式，同时检查观点先行、主动语态、具体细节等写作基本功。**三种用法**：`/no-ai-slop` 编辑并列出改动 · **检测模式**只逐条引用命中的模式而**不断言「是否 AI 所写」**（回避 AI 检测器准确率争议的克制设计）· 反向生成 slop 讽刺文。安装零门槛：一句话丢给 ChatGPT / Claude Code / Codex，或 `npx skills add` 全局安装，另有 ChatGPT 插件形态。**设计洞察**：`eval.md` 让技能自带输出自检清单，是提示词工程里少见的「**评估内置**」实践；与多数会把文字磨平的 AI 润色工具相反，它以「**去 slop 但不扁平化个人风格**」为核心卖点。可与库里的 blader/humanizer（35 种 AI 写作模式，基于维基百科指南）对照阅读——一个偏模式清单工程化，一个偏创作者语感。MIT，核心资产为 Markdown 提示词（构建脚本 Python），**11,040 stars** / 747 forks，2026-07 创建。
- **归档**：`开源项目介绍/2026.9.23/no-ai-slop.md`
- **标签**：`#skill` `#写作` `#ai文本去痕` `#提示词工程` `#chatgpt插件`

<a id="sec-5"></a>

## 🎬 五、视频创作 Skills（6）

### [bradautomates/claude-video](https://github.com/bradautomates/claude-video)
- **定位**：让 Claude 具备「观看视频」能力
- **简介**：通过 /watch 指令优先获取字幕、按需下载视频、抽取关键帧、生成带时间戳的转录文本（Whisper 兜底），再将帧与对齐文本交给 Claude 逐帧分析。支持 YouTube、Loom 及本地视频。同时兼容 Claude Code 和 Codex 双插件（.claude-plugin + .codex-plugin），以及 Agent Skills 标准。39 issues、117 PRs，社区贡献活跃。
- **归档**：`开源项目介绍/2026.9.6/claude-video.md`
- **标签**：`#skill` `#视频理解` `#多模态`

### [browser-use/video-use](https://github.com/browser-use/video-use)
- **定位**：用编码 Agent 剪视频（对话式剪辑 Skill，100% 开源）
- **简介**：browser-use 团队出品。把原始素材丢进文件夹，和 Claude Code 聊几句，拿回 `final.mp4`——没有预设、没有菜单、没有时间轴 GUI，适配任何有 shell 权限的 agent（Claude Code / Codex / Hermes / Openclaw）。自动剪掉 `umm`/`uh`/口误重开与镜头间死区、逐段调色（暖调电影感 / 中性增强 / 自定义 ffmpeg 链）、每个切点做 **30ms 音频淡入淡出**防爆音、烧录字幕（默认 2 词大写分块，可定制）、通过 HyperFrames / Remotion / Manim / PIL 生成动画叠层（**并行 sub-agent，一个动画一个 agent**）。**最关键的设计：LLM 从不"看"视频，它"读"视频**——Layer 1 用 ElevenLabs Scribe 拿词级时间戳 + 说话人分离 + 音频事件标注（`(laughter)`/`(applause)`/`(sigh)`），所有 take 打包成约 **12KB** 的 `takes_packed.md` 作主阅读视图；Layer 2 的 `timeline_view` 按需生成「胶片条 + 波形 + 词标签 + 静音切点候选」PNG，只在歧义停顿、重拍对比、切点核查等决策点调用。对比朴素做法的 30,000 帧 × 1,500 token = **4500 万 token 噪音**，这是数量级的成本差。管线为 `Transcribe → Pack → LLM Reasons → EDL → Render → Self-Eval`，自评回路在**渲染产物**上逐切点检查画面跳变/爆音/字幕遮挡，不通过就修复重渲染（最多 3 次），通过了才给你看预览。会话记忆持久化到 `project.md`，下次开新会话能接着走。五条设计原则：文本+按需视觉、音频为主画面跟随、询问→确认→执行→自评→持久化、对内容类型零假设、12 条硬规则其余留给审美自由。所有输出落在 `<videos_dir>/edit/`，skill 目录保持干净。依赖 Python + ffmpeg（必需）、yt-dlp（可选）、ElevenLabs API key（必需）。MIT，**25.8k stars** / 3.1k forks / 115 open issues，2026-04 创建。
- **归档**：`开源项目介绍/2026.9.23/video-use.md`
- **标签**：`#视频剪辑` `#skill` `#claude-code` `#ffmpeg` `#browser-use` `#低成本`

### [calesthio/OpenMontage](https://github.com/calesthio/OpenMontage)
- **定位**：全球首个开源 Agentic 视频生产系统：12 条制作管线、100+ 工具、700+ Agent 技能。
- **简介**：全球首个开源 Agentic 视频生产系统：12 条制作管线、100+ 工具、700+ Agent 技能。（GitHub 每日趋势 2026-10-03：★62616，当日 +328）
- **归档**：`开源项目介绍/2026.10.4/OpenMontage.md`
- **标签**：`#python`

### [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)
- **定位**：写 HTML 即渲染视频，为 Agent 而设计（HeyGen 出品）。
- **简介**：写 HTML 即渲染视频，为 Agent 而设计（HeyGen 出品）。（GitHub 每日趋势 2026-10-01：★54566，当日 +352）
- **归档**：`开源项目介绍/2026.10.1/hyperframes.md`
- **标签**：`#typescript`

### [OpenCut-app/OpenCut](https://github.com/OpenCut-app/OpenCut)
- **定位**：开源版剪映（CapCut 替代品），浏览器视频剪辑。
- **简介**：开源版剪映（CapCut 替代品），浏览器视频剪辑。（GitHub 每日趋势 2026-10-03：★91435，当日 +234）
- **归档**：`开源项目介绍/2026.10.4/OpenCut.md`
- **标签**：`#typescript`

### [smallc/Kinema](https://gitee.com/smallc/Kinema)
- **定位**：AI 影视制作管线 · 给一个主题，出一条成片
- **简介**：把检索、文案、分镜、角色设定、生图、配音、字幕、特效和合成串成**一条完整管线**，解决传统 AI 视频创作要在多工具间来回切换、设定散落在不同会话、改一处就得重做的痛点。**长篇小说创作**（十章一批，自动跑七项复核：设定一致性/人设/情节连贯/AI 腔/文风/伏笔/节奏）→ 小说改剧本、剧本拆分镜（一章一集，双语提示词，开拍前零成本静态体检标出运镜雷同与景别单调）→ **3D 导演台**（灰模走位调度，30+ 运镜预设）→ **简笔分镜板**（镜头切成逐秒铅笔草图 + 时间轴）→ **深度捕捉**（实拍片本机 CPU 提取深度浮雕+骨骼控制视频，框 4~15 秒绑到镜头）。资产管理是核心：角色三区两视设定图、道具三视图、场景主视觉按出场逐镜自动挂载，固定 seed + 资产血缘追踪，一张脸在几十个镜头里稳住。40+ 画风档（赛博朋克/新海诚/吉卜力/国漫仙侠/皮克斯/水墨/粘土定格等），三种渲染模式（kenburns 零成本 / dubbed / native 原生音画）。成本可控：`--dry-run` 逐镜报价、超预算事前闸拦截、已完成的镜锁定不可覆盖。代码绑定**能力**而非厂商，`models.yaml` 换模型不改管线（图像 Seedream/通义万相，视频 Seedance/Veo，语音 seed-audio，音乐 ElevenLabs）。制作流程整理为**能力包**放在 `.claude/skills/`，斜杠调用 `/kn-cyberpunk`、`/kn-anime`；`AGENTS.md` 统一支持 Claude Code、Codex、Cursor、Copilot、Windsurf、Aider、Zed。本地只做 FFmpeg 合成字幕运镜，**纯 CPU 无需显卡**，重活全在云端 API，密钥自管、成片归你。AGPL-3.0，14 commits，BladeX 作者 smallchill 出品，密集迭代中。
- **归档**：`开源项目介绍/2026.9.22/Kinema.md`
- **标签**：`#ai视频` `#制作管线` `#skill` `#分镜` `#深度捕捉` `#gitee`

<a id="sec-6"></a>

## 🧰 六、专业领域 Skills（22）

### [anthropics/financial-services](https://github.com/anthropics/financial-services)
- **定位**：Anthropic 面向金融服务行业的官方示例与参考实现集合。
- **简介**：Anthropic 面向金融服务行业的官方示例与参考实现集合。（GitHub 每日趋势 2026-09-26：★37504，当日 +279）
- **归档**：`开源项目介绍/2026.9.28/financial-services.md`
- **标签**：`#python`

### [AssetRipper/AssetRipper](https://github.com/AssetRipper/AssetRipper)
- **定位**：分析游戏文件的 GUI 应用（Unity 资产提取）。
- **简介**：分析游戏文件的 GUI 应用（Unity 资产提取）。（GitHub 每日趋势 2026-10-09：★8511，当日 +8）
- **归档**：`开源项目介绍/2026.10.9/AssetRipper.md`
- **标签**：`#csharp`

### [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)
- **定位**：专业级图表生成 Skill
- **简介**：为 Claude Code / Codex / Pi / Factory Droid 等提供专业级图表生成能力，内置 **39 种编辑级图表类型**（架构图、流程图、时序图、状态机、ER 图、时间线、泳道图、象限图、雷达图、甘特图、Sankey、鱼骨图、Wardley Map、看板、用户旅程、UML 类图、数据库 schema 等），输出自包含 HTML+SVG，支持品牌自动适配（从网站提取配色和字体）。v2.5.10 新增 10 种布局语法，v2.0 引入飞轮自改进循环，可重绘 draw.io/Mermaid 源。MIT 协议，135 commits。
- **归档**：`开源项目介绍/2026.9.6/diagram-design.md`
- **标签**：`#skill` `#图表` `#可视化` `#svg`

### [CoplayDev/unity-mcp](https://github.com/CoplayDev/unity-mcp)
- **定位**：连接 AI 助手与 Unity 编辑器的 MCP 桥，让 AI 直接操作 Unity 项目。
- **简介**：连接 AI 助手与 Unity 编辑器的 MCP 桥，让 AI 直接操作 Unity 项目。（GitHub 每日趋势 2026-09-28：★14531，当日 +23）
- **归档**：`开源项目介绍/2026.9.28/unity-mcp.md`
- **标签**：`#csharp`

### [cyanfish/naps2](https://github.com/cyanfish/naps2)
- **定位**：尽可能简单地扫描文档为 PDF 等。
- **简介**：尽可能简单地扫描文档为 PDF 等。（GitHub 每日趋势 2026-10-03：★4577，当日 +5）
- **归档**：`开源项目介绍/2026.10.4/naps2.md`
- **标签**：`#csharp`

### [datalab-to/chandra](https://github.com/datalab-to/chandra)
- **定位**：处理复杂表格、表单、手写体的 OCR 模型，带完整版面理解。
- **简介**：处理复杂表格、表单、手写体的 OCR 模型，带完整版面理解。（GitHub 每日趋势 2026-10-03：★12395，当日 +20）
- **归档**：`开源项目介绍/2026.10.4/chandra.md`
- **标签**：`#python`

### [dream-num/univer](https://github.com/dream-num/univer)
- **定位**：面向 AI Agent 的开源 Office SDK，六大编辑器同构单一运行时
- **简介**：**Univer** 是 DreamNum（梦数科技）开源的 Office SDK（Apache-2.0，TypeScript），官方定位 "The Office Harness for AI Agents"。2026-09-24 当天连发 **v1.0.0/v1.0.1/v1.0.2**，正式把 Sheets、Docs、Slides、Boards、Bases、PDF 六大编辑器统一进一个可编程运行时，共享插件与命令系统并为每个编辑器提供 Facade API。核心差异化是**同构架构**：同一套代码既在浏览器渲染 Canvas UI，也能在 Node.js（≥18.17）无头运行，为 Agent 提供服务端文档处理、程序化编辑、渲染截图与布局诊断的输出验证、Worktree 隔离草稿的人机协同评审；**插件优先**，一切能力皆插件，可增删替换懒加载，提供 Plugin/Preset/Headless 三种集成模式；**性能**面向大型文档表面，Canvas 渲染引擎 + 独立公式引擎，1.0 改进了大表格计算、长文档布局与 Office 文件兼容性及移动端编辑。AI 生态完善：AI SDK、univer-mcp（自然语言驱动 Sheets）、univer-sdk-skills（Agent 技能）、univer-cli、开源参考实现 Univer Workspace（Agent 可生成绑定单元格的表格 mini-app 仪表盘）。开源与商业边界清晰：实时协作、编辑历史、导入导出、打印、图表、透视表、服务端计算等属 **Univer Pro** 商业层，OSS 包独立可用。兼容性：Chrome/Edge 88+、Firefox 90+、Safari 14.1+、Electron 12+，React 18/19（最低 16.9+）、Vue、Web Components，依赖 Intl.Segmenter（可 polyfill），构建推荐 Vite/esbuild/Webpack 5，开发需 Node ≥22.18 + pnpm ≥11。规模：**17,458 stars / 1,510 forks / 68 贡献者 / 5,808 commits / 149 tags**，仓库创建于 2022-09-29，最近推送 2026-09-24；社区有 Discord、GitHub Discussions、Twitter/X 与 Open Collective 赞助。注意：1.0 为含 API 移除与包变更的大版本，从 0.25 升级须按迁移指南操作；@univerjs/* 各包必须保持同一协调发布线同版本混用。
- **关联**：库内 [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)（AI 侧 Office 自动化的另一条路线）
- **归档**：`开源项目介绍/2026.9.25/univer.md`
- **标签**：`#office-sdk` `#spreadsheet` `#typescript` `#canvas` `#ai-agent`

### [earthtojake/text-to-cad](https://github.com/earthtojake/text-to-cad)
- **定位**：AI 智能体 CAD 建模技能
- **简介**：通过自然语言或参考图片生成、修改、校验工业级三维 CAD 模型，基于 build123d + OpenCascade，输出 STEP/STL/3MF/GLB/URDF 等格式。含本地 CAD 查看器，支持参数化建模与迭代设计。v0.3.2（2026-06），226 commits、22 tags。支持 Claude Code 和 Codex 双插件。
- **归档**：`开源项目介绍/2026.9.6/text-to-cad.md`
- **标签**：`#skill` `#cad` `#生成式设计` `#3d`

### [gumyr/build123d](https://github.com/gumyr/build123d)
- **定位**：Python CAD 编程库（参数化建模，OCC 内核）。
- **简介**：Python CAD 编程库（参数化建模，OCC 内核）。（GitHub 每日趋势 2026-10-06：★3318，当日 +19）
- **归档**：`开源项目介绍/2026.10.8/build123d.md`
- **标签**：`#python`

### [handsomestWei/patent-disclosure-skill](https://github.com/handsomestWei/patent-disclosure-skill)
- **定位**：中国专利点挖掘与交底书编写 Agent Skill
- **简介**：MIT 协议的专利 Agent Skill（5.4k stars），解决「有代码有设计但专利点不会挖、交底书写不出」的痛点。核心能力：**专利交底书编写**（发明/实用/外观全覆盖，从项目材料梳出专利点、查新脱敏、成稿迭代、输出可改 Word，支持外观线稿/实用结构线稿/CAD三维投影自动出图）；**专利通俗解读**（读成通俗笔记与图谱，入库 Obsidian 形成个人专利知识库，可扩展同族对照/技术路线/差异分析）；政策动向嗅探、审查答复辅助。让真正干活的研发人员也能写出可交付的专利交底书。**🔄 2026-09-23 复核更新**：stars **5.4k → 10,001（正式破万）** / 1,033 forks / 11 open issues，commits 31 → 53（2026-04-07 建仓，2026-09-20 最近推送，**无 release/tag**）。**架构已重组为 8 个子技能**：交底书编写、**申请文件**、案卷会稿、通俗解读、**专利地图**、审查答复辅助、**著录检索**、政策简报。新增能力里最值得一提的是**专利地图**（语义地形沙盘、申请人四象限、同族引证网络、技术功效矩阵，**本地私有化运行**）与**申请文件生成**（把交底直接改写为权要/说明书/摘要/附图），支持**保护型 1+N 专利布局**；审查答复升级为 **RAG 检索增强**，著录检索支持按图/权要倒推检索式。仓库主页已指向 skillhub.cn 收录页。
- **归档**：`开源项目介绍/2026.9.6/patent-disclosure-skill.md`（2026-09-23 已复核更新）
- **标签**：`#skill` `#专利` `#交底书` `#知识产权`

### [hiroi-sora/Umi-OCR](https://github.com/hiroi-sora/Umi-OCR)
- **定位**：开源免费的离线 OCR 软件：截屏/批量图片/PDF 识别，排除水印，内置多国语言库。
- **简介**：开源免费的离线 OCR 软件：截屏/批量图片/PDF 识别，排除水印，内置多国语言库。（GitHub 每日趋势 2026-10-10：★47727，当日 +51）
- **归档**：`开源项目介绍/2026.10.10/Umi-OCR.md`
- **标签**：`#python`

### [HKUDS/CLI-Anything](https://github.com/HKUDS/CLI-Anything)
- **定位**：为任意软件自动生成 Agent 原生 CLI 的自动化框架
- **简介**：**CLI-Anything** 是**港大数据智能实验室（HKUDS）**的开源项目，口号「Making ALL Software Agent-Native」，配套技术报告 **arXiv:2606.03854**《CLI-Anything: Towards Agent-Native Computer Use》。核心论点：GUI 自动化脆弱、API 覆盖有限、重写实现丢失九成功能，而 CLI 是人与 Agent 的通用接口——结构化、可组合、自描述（--help）、确定性强。核心能力两条线：其一，**CLI-Hub 包管理器**（`pip install cli-anything-hub`），一条命令 list/search/install/update/uninstall/launch 社区 CLI harness，v0.4.0 新增 **CLI-Matrix** 命令族，把多 CLI 工作流矩阵按能力一键安装（`cli-hub can <task>` 按任务查能力、preflight 校验覆盖、matrix install 整套供给，支持 dry-run 与断点续装）；其二，**7 阶段全自动生成流水线**（Analyze→Design→Implement→Plan Tests→Write Tests→Document→Publish），在 Claude Code、Cursor、Codex、Pi、OpenCode、Goose 等平台装入插件后对任意代码库跑 `/cli-anything`，产出带 **REPL、--json 结构化输出、undo/redo 与完整测试**的 Click CLI，Phase 6.5 自动生成 SKILL.md 供 `npx skills` 直接消费，`:refine` 按覆盖率差距做增量非破坏扩展。差异化亮点：**真实软件集成、零妥协**——CLI 生成合法工程文件（ODF/MLT XML/SVG）后委托真实软件执行（LibreOffice 出 PDF、Blender 渲 3D、Audacity 走 sox），后端缺失时**测试 fail 而非 skip**，杜绝玩具实现；全仓 **2,461+ 测试 100% 通过**（1,732 单元 + 579 E2E + 19 Node.js），覆盖 18 个主要应用；生态含 Blender、GIMP、FreeCAD（258 命令）、QGIS、Godot、s&box、OBS、Zoom、Zotero、Calibre、ComfyUI、Ollama 乃至激光切割（MeerK40t）等数十个 harness。规模与时间线：创建 **2026-03-08**，截至 2026-09-27 约 **50,637 Stars / 4,631 Forks / 145 位贡献者 / 893 commits / 3 个 tag**；已发布 v0.2.0、v0.3.0、v0.4.0（2026-06-25）；**Apache-2.0**，Python ≥3.10 + Click ≥8.0，方法论唯一事实源为 HARNESS.md。注意事项：部分 harness 需另装上游桌面软件才能完整工作；Windows 下 Claude Code 走 bash，需 Git for Windows 或 WSL 以避免 cygpath 报错；仓库未设置 topics。
- **关联**：库内 [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)（Office 侧的 Agent 原生 CLI）
- **归档**：`开源项目介绍/2026.9.27/CLI-Anything.md`
- **标签**：`#cli` `#ai-agent` `#agent-native` `#skill` `#自动化` `#hkuds`

### [hugohe3/ppt-master](https://github.com/hugohe3/ppt-master)
- **定位**：AI 把文档或主题变成真正的原生 PPT——原生形状、转场动画、数据图表（非截图拼贴）。
- **简介**：AI 把文档或主题变成真正的原生 PPT——原生形状、转场动画、数据图表（非截图拼贴）。（GitHub 每日趋势 2026-10-10：★58684，当日 +308）
- **归档**：`开源项目介绍/2026.10.10/ppt-master.md`
- **标签**：`#python`

### [iOfficeAI/OfficeCLI](https://github.com/iOfficeAI/OfficeCLI)
- **定位**：为 AI Agent 而生的 Office 套件（Word / Excel / PowerPoint）
- **简介**：自称「世界上第一个也是最好的、为 AI Agent 设计的 Office 套件」——给任何 Agent 完整控制 Word/Excel/PPT 的能力，**一行代码**。开源、单一二进制、**不需要安装 Office**、零依赖、全平台（.NET 运行时内嵌）。真正的杀手锏是**内置高保真 HTML 渲染引擎**：把 `.docx`/`.xlsx`/`.pptx` 渲染成 HTML 或 PNG，闭合「渲染 → 看 → 修」循环——**这才是给 AI 装上了眼睛**，Agent 不再猜 DOM 而是真看到渲染结果。覆盖形状、图表（趋势线/误差线/瀑布图/K线/迷你图）、公式（OMML→LaTeX 用 KaTeX 渲染）、3D `.glb`（Three.js）、morph 切换、逐页 PNG 截图。接入极简：把 `curl -fsSL https://officecli.ai/SKILL.md` 粘进 Agent 对话即自动装好；或 `officecli install` 会**自动检测已装的编码 Agent**（Claude Code / Cursor / Windsurf / Copilot 等）并把 skill 装进去。支持 `officecli watch` 实时预览（localhost:26315），每个 add/set/remove 都即时刷新浏览器。能力面深得离谱：Word 有完整 i18n/RTL、LaTeX 公式、mermaid→原生可编辑形状、修订跟踪与按作者接受/拒绝；Excel 有 **350+ 函数自动求值**、溢出动态数组、透视表（多字段/日期分组/计算字段/缓存 CoW）、帕累托图、布尔 and/or 选择器 `row[Salary>5000 and Region=EMEA]`；PPT 有 15 种强调+16 种退出动画预设、morph 切换、3D 模型、幻灯片缩放、线程式批注往返。过去 50 行 python-pptx 现在一行命令。安装支持 brew / scoop / npm / 一行 curl。姊妹项目 [AionUi](https://github.com/iOfficeAI/AionUi) 提供 GUI 形态。Apache-2.0，**31,057 stars** / 2,119 forks，2026-03 创建，半年冲到 3 万星。
- **归档**：`开源项目介绍/2026.9.23/OfficeCLI.md`
- **标签**：`#office` `#ai-agent` `#skill` `#渲染引擎` `#cli` `#docx`

### [IvanMurzak/Unity-MCP](https://github.com/IvanMurzak/Unity-MCP)
- **定位**：Unity 引擎的 AI 技能、MCP 工具与 CLI：完整 AI 开发测试回路，CLI 快速安装、高效 token 用
- **简介**：Unity 引擎的 AI 技能、MCP 工具与 CLI：完整 AI 开发测试回路，CLI 快速安装、高效 token 用量。（GitHub 每日趋势 2026-10-01：★4367，当日 +9）
- **归档**：`开源项目介绍/2026.10.1/Unity-MCP.md`
- **标签**：`#csharp`

### [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills)
- **定位**：166 个科研 Agent Skill 合集（原 Claude Scientific Skills）
- **简介**：K-Dense 出品的 **147 个即用型科研技能**合集（MIT 协议，2025.10 改为允许商用），覆盖 17 大科学领域：生物信息学、化学信息学/药物发现、蛋白质组学、临床研究、医疗 AI、医学影像、机器学习、材料科学、物理天文学、工程仿真、数据可视化、地理空间、实验室自动化、科学传播、多组学、蛋白质工程、Agent 基础设施。支持任何兼容 [Agent Skills](https://agentskills.io/) 开放标准的 AI Agent（Cursor、Claude Code、Codex、Google Antigravity 等）。535 commits，90 tags（v2.37.1）。关联产品 **K-Dense BYOK**：桌面 AI 合作科学家，自带全部 147 技能 + 40+ 模型 + 100+ 科学数据库。**🔄 2026-09-23 复核更新**：技能数 **147 → 166**、commits **535 → 732**、tags **90 → 106**、版本 **v2.37.1 → v2.69.0**，**45,060 stars** / 4,087 forks / 仅 10 open issues（2025-10-19 建仓，2026-09-14 最近推送）。已发表 arXiv 论文《Scientific Agent Skills: A Library of Procedural Knowledge for Research Agents》（**arXiv:2609.00065**），官方称 **190,000+ 科研工作者**在用。领域扩至约 **20 个**，新增临床前研究与动物福利、监管与标准（ISO 13485/14971、ICH Q2(R2)/Q14）、研究方法论、神经科学与电生理；新增 AlphaGenome、OneKGPd（3,202 人 1000 Genomes 队列）、Paperclip（约 1,100 万篇全文论文）、GenSpectrum 病原监测等技能。安装新增 **`gh skill install`（可 `--pin` 固定版本）** 与 **Agent Plugins 1.0.0 整包加载**；治理侧有**每周 Cisco Skill Scanner 安全扫描 + CI 强制技能测试**——与库里的 tech-leads-club/agent-skills 同属「安全策展」路线。
- **归档**：`开源项目介绍/2026.9.6/scientific-agent-skills.md`（2026-09-23 已复核更新）
- **标签**：`#skill` `#科研` `#生物信息` `#药物发现` `#多领域`

### [mcneel/RhinoAI](https://github.com/mcneel/RhinoAI)
- **定位**：Rhino（犀牛）3D 的 AI 功能插件。
- **简介**：Rhino（犀牛）3D 的 AI 功能插件。（GitHub 每日趋势 2026-10-02：★335，当日 +5）
- **归档**：`开源项目介绍/2026.10.2/RhinoAI.md`
- **标签**：`#csharp`

### [mcp-servers-for-revit/mcp-servers-for-revit](https://github.com/mcp-servers-for-revit/mcp-servers-for-revit)
- **定位**：Revit（BIM）的 MCP 服务器——Sparx 分支版。
- **简介**：Revit（BIM）的 MCP 服务器——Sparx 分支版。（GitHub 每日趋势 2026-10-08：★366，当日 +5）
- **归档**：`开源项目介绍/2026.10.8/mcp-servers-for-revit.md`
- **标签**：`#csharp`

### [microsoft/markitdown](https://github.com/microsoft/markitdown)
- **定位**：微软出品的文件与 Office 文档转 Markdown 工具（★189K）。
- **简介**：微软出品的文件与 Office 文档转 Markdown 工具（★189K）。（GitHub 每日趋势 2026-10-08：★189000，当日 +193）
- **归档**：`开源项目介绍/2026.10.8/markitdown.md`
- **标签**：`#python`

### [Perfare/AssetStudio](https://github.com/Perfare/AssetStudio)
- **定位**：探索、提取和导出 Unity 资产与 AssetBundle 的工具。
- **简介**：探索、提取和导出 Unity 资产与 AssetBundle 的工具。（GitHub 每日趋势 2026-10-01：★15599，当日 +0）
- **归档**：`开源项目介绍/2026.10.1/AssetStudio.md`
- **标签**：`#csharp`

### [sbroenne/mcp-server-excel](https://github.com/sbroenne/mcp-server-excel)
- **定位**：通过 MCP 或 CLI 让 AI 操控真正的 Excel——Power Query、DAX、VBA、透视表、图表共 3
- **简介**：通过 MCP 或 CLI 让 AI 操控真正的 Excel——Power Query、DAX、VBA、透视表、图表共 326 种操作。（GitHub 每日趋势 2026-10-03：★799，当日 +6）
- **归档**：`开源项目介绍/2026.10.3/mcp-server-excel.md`
- **标签**：`#csharp`

### [tt-a1i/archify](https://github.com/tt-a1i/archify)
- **定位**：AI Agent 技能 · 自然语言生成架构图/流程图/时序图
- **简介**：可用于 Claude、Codex CLI 和 opencode 的 agent skill，用大白话描述系统或流程即可生成精细技术图（单文件 HTML）。支持五种图表类型：Architecture（架构图）、Workflow（流程图）、Sequence（时序图）、Data Flow（数据流图）、Lifecycle（生命周期图）。深色/浅色主题一键切换，导出最高 4× 原生光栅化 PNG/JPEG/WebP 或双主题自持 SVG（自动跟随系统深浅色），一键复制到剪贴板。内置质量闭环：JSON Schema 校验 → 布局检查 → HTML/SVG artifact 检查 → 定向迭代。支持语义技术标签（aws.lambda、postgres、redis 等），聊天迭代修改。**🔄 2026-09-23 复核更新**：版本已从 v2.10 前进到 **v2.16.0**（开发版 v2.17.0-dev.1），**69,271 stars** / 4,648 forks / 145 open issues，2026-09-01 登顶 **GitHub Trending 周榜全语言第一**并获量子位专题报道。**定位已从「技术图表」扩展为「任何交互式可视化」**——社区案例含上海 CityWalk 行程、合同评审、事故复盘，官方 Proof Lab 画廊收录 11 个可验证场景。新增 **Architecture Delta 对比**（Before/Delta/After + 机器回执）、**viewer 交互**（route/reach/lens/story/演示舞台 F 键）、Signal Flow / Blueprint / Classic 三种视觉预设、**1200×630 Share Card 导出**；CLI 新增 `preview`（loopback 预览 + last-good 保护）与 `deliver`（原子交付），安装面扩展到 Cursor / Raven / DeepSeek Harness，UI 支持 `meta.locale` 中英双语。MIT，JavaScript，2026-04-15 建仓，2026-09-22 最近推送。
- **归档**：`开源项目介绍/2026.8.29/Archify.md`（2026-09-23 已复核更新）
- **标签**：`#skill` `#图表` `#架构图` `#流程图`

<a id="sec-7"></a>

## 🔐 七、安全 · 审计与逆向（22）

### [0x4m4/hexstrike-ai](https://github.com/0x4m4/hexstrike-ai)
- **定位**：HexStrike AI：高级 MCP 服务器，让 Claude/GPT/Copilot 等 AI Agent 自主调度
- **简介**：HexStrike AI：高级 MCP 服务器，让 Claude/GPT/Copilot 等 AI Agent 自主调度 150+ 网络安全工具。（GitHub 每日趋势 2026-09-29：★12214，当日 +56）
- **归档**：`开源项目介绍/2026.9.29/hexstrike-ai.md`
- **标签**：`#python`

### [abrignoni/ALEAPP](https://github.com/abrignoni/ALEAPP)
- **定位**：Android 日志事件与 Protobuf 解析器（取证工具）。
- **简介**：Android 日志事件与 Protobuf 解析器（取证工具）。（GitHub 每日趋势 2026-10-09：★974，当日 +18）
- **归档**：`开源项目介绍/2026.10.9/ALEAPP.md`
- **标签**：`#python`

### [BitterSecurity/Decepticon](https://github.com/BitterSecurity/Decepticon)
- **定位**：红队自主攻击 Agent（Decepticon）。
- **简介**：红队自主攻击 Agent（Decepticon）。（GitHub 每日趋势 2026-10-11：★5805，当日 +80）
- **归档**：`开源项目介绍/2026.10.11/Decepticon.md`
- **标签**：`#python`

### [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)
- **定位**：Cloudflare 出品的多阶段安全审计 Skill（把 Agent 变成安全审计员）
- **简介**：编排一组**相互隔离**的 agent 走完六个阶段：① **侦察**（在 `architecture.md` + `coverage-ledger.json` 中测绘架构、信任边界、输入面、既有证据、确定性覆盖率）② **覆盖率驱动猎捕**（从账本单元分配隔离 hunter，用 coverage critic 找空白）③ **候选验证**（每个候选交给一个**全新的 verifier 去尝试证伪**）④ **结构化输出**（`confirmed`/`needs_validation`/`rejected` 写入 `findings.json` 并用 `report-schema.json` 校验）⑤ **独立记录核验**（全新 agent 核验源声明，**实质性替换再接受一次独立核验**）⑥ **目标中立报告**（推导 `REPORT.md`/`FINDINGS-DETAIL.md`/`NEEDS-VALIDATION.md`）。三种判决区分极严：`confirmed` 需完整源追溯 + 有界观测结果；`needs_validation` 有精确的未解决事实且**不给严重性评级**；`rejected` 记录已被证伪的候选。**多次运行是累加的**——利用先前账本瞄准空白、重验已变更源码、结转当前证据，但**绝不把过时或未解决的工作当作已覆盖**。这是**播种了 Cloudflare 漏洞发现 harness 的那个 skill**（那套 harness 后来长成多阶段、覆盖全机队的系统，本仓库是它的单仓库起点，见[官方博客](https://blog.cloudflare.com/build-your-own-vulnerability-harness)）。猎捕类别文档多达 11 个专项：内存安全与二进制、AI 与 LLM（提示注入/agent-tool/输出处理）、Web 协议与认证、客户端（DOM 注入/消息信任/UI 重定向/原型污染）、供应链与发布、云与部署、RPC 与消息、资源耗尽与可用性、数据隔离与生命周期、桌面移动与本地 IPC、攻击类别。校验器是**零依赖 `.cjs`** 脚本且自带测试。**五条设计原则**极值得抄：只确认已确立的边界失效 · **对抗式验证（检查发现的 agent 永远不是发现它的 agent）** · 严重性需要影响（可能性×影响，而非偏离清单的程度）· **纵深防御的缺口不是漏洞**（A 层已挡住，缺 B 层只是加固建议）· 多次运行提升覆盖率（**测试中单次运行只找到重复运行总计的约一半漏洞**）。安装 `npx skills add https://github.com/cloudflare/security-audit-skill --skill security-audit`（`--global` 装到用户级），说「security audit this codebase」即自动激活。前置要求三条：模型需支持 tool use 与并行 sub-agent、Node.js、以及**OS 级强制沙箱**（禁外网、净化白名单环境、资源限制、只允许写 scratch 路径）——**没有这些控制，工作流会把线索留为 `needs_validation` 而不执行目标代码**。MIT，**20,128 stars** / 1,140 forks，2026-06 创建。
- **归档**：`开源项目介绍/2026.9.23/cloudflare-security-audit-skill.md`
- **标签**：`#安全审计` `#skill` `#cloudflare` `#对抗验证` `#沙箱` `#覆盖率`

### [derv82/wifit3](https://github.com/derv82/wifit3)
- **定位**：仅 USB、跨平台版的 Wifite 无线安全测试工具。
- **简介**：仅 USB、跨平台版的 Wifite 无线安全测试工具。（GitHub 每日趋势 2026-09-26：★1118，当日 +409）
- **归档**：`开源项目介绍/2026.9.27/wifit3.md`
- **标签**：`#python`

### [elder-plinius/OBLITERATUS](https://github.com/elder-plinius/OBLITERATUS)
- **定位**：挣脱束缚你的枷锁（Pliny 逆向工程的越狱工具集）。
- **简介**：挣脱束缚你的枷锁（Pliny 逆向工程的越狱工具集）。（GitHub 每日趋势 2026-10-02：★8551，当日 +23）
- **归档**：`开源项目介绍/2026.10.2/OBLITERATUS.md`
- **标签**：`#python`

### [icsharpcode/ILSpy](https://github.com/icsharpcode/ILSpy)
- **定位**：老牌开源 .NET 反编译器，支持 PDB 生成与 ReadyToRun。
- **简介**：老牌开源 .NET 反编译器，支持 PDB 生成与 ReadyToRun。（GitHub 每日趋势 2026-09-26：★26139，当日 +7）
- **归档**：`开源项目介绍/2026.9.28/ILSpy.md`
- **标签**：`#csharp`

### [kaifcodec/user-scanner](https://github.com/kaifcodec/user-scanner)
- **定位**：二合一邮件与用户名 OSINT 套件，原生支持 MCP，从一个邮箱/用户名深挖数据。
- **简介**：二合一邮件与用户名 OSINT 套件，原生支持 MCP，从一个邮箱/用户名深挖数据。（GitHub 每日趋势 2026-10-03：★5194，当日 +70）
- **归档**：`开源项目介绍/2026.10.4/user-scanner.md`
- **标签**：`#python`

### [Mafifrizi/ARES](https://github.com/Mafifrizi/ARES)
- **定位**：ARES：授权红队交战自动化——仪表盘、活动范围、模块编排、OPSEC 控制、加密数据。
- **简介**：ARES：授权红队交战自动化——仪表盘、活动范围、模块编排、OPSEC 控制、加密数据。（GitHub 每日趋势 2026-10-01：★557，当日 +23）
- **归档**：`开源项目介绍/2026.10.1/ARES.md`
- **标签**：`#python`

### [MDX-Tom/gpt-instruct](https://github.com/MDX-Tom/gpt-instruct)
- **定位**：针对 GPT 系列的 Codex 破甲提示词与测试包。
- **简介**：针对 GPT 系列的 Codex 破甲提示词与测试包。（GitHub 每日趋势 2026-10-08：★9312，当日 +43）
- **归档**：`开源项目介绍/2026.10.8/gpt-instruct.md`
- **标签**：`#python`

### [morluto/rea](https://github.com/morluto/rea)
- **定位**：用 Agent 逆向一切——从应用行为到原生二进制。
- **简介**：用 Agent 逆向一切——从应用行为到原生二进制。（GitHub 每日趋势 2026-10-07：★8025，当日 +2963）
- **归档**：`开源项目介绍/2026.10.8/rea.md`
- **标签**：`#typescript`

### [mvt-project/mvt](https://github.com/mvt-project/mvt)
- **定位**：移动设备取证工具包（MVT），用于检测潜在的入侵痕迹（Amnesty International 出品）。
- **简介**：移动设备取证工具包（MVT），用于检测潜在的入侵痕迹（Amnesty International 出品）。（GitHub 每日趋势 2026-10-03：★15177，当日 +34）
- **归档**：`开源项目介绍/2026.10.4/mvt.md`
- **标签**：`#python`

### [NVIDIA/SkillSpector](https://github.com/NVIDIA/SkillSpector)
- **定位**：英伟达出品：AI Agent 技能的安全扫描器——检测漏洞、恶意模式、提示注入与数据外泄风险。
- **简介**：英伟达出品：AI Agent 技能的安全扫描器——检测漏洞、恶意模式、提示注入与数据外泄风险。（GitHub 每日趋势 2026-10-03：★19064，当日 +167）
- **归档**：`开源项目介绍/2026.10.3/SkillSpector.md`
- **标签**：`#python`

### [p-e-w/heretic](https://github.com/p-e-w/heretic)
- **定位**：语言模型的完全自动审查移除工具。
- **简介**：语言模型的完全自动审查移除工具。（GitHub 每日趋势 2026-10-03：★33008，当日 +233）
- **归档**：`开源项目介绍/2026.10.4/heretic.md`
- **标签**：`#python`

### [Perfare/Il2CppDumper](https://github.com/Perfare/Il2CppDumper)
- **定位**：Unity il2cpp 逆向工程工具。
- **简介**：Unity il2cpp 逆向工程工具。（GitHub 每日趋势 2026-10-05：★9454，当日 +4）
- **归档**：`开源项目介绍/2026.10.5/Il2CppDumper.md`
- **标签**：`#csharp`

### [SamboyCoding/Cpp2IL](https://github.com/SamboyCoding/Cpp2IL)
- **定位**：逆向 Unity IL2CPP 工具链的工具（开发中）。
- **简介**：逆向 Unity IL2CPP 工具链的工具（开发中）。（GitHub 每日趋势 2026-10-08：★2826，当日 +103）
- **归档**：`开源项目介绍/2026.10.8/Cpp2IL.md`
- **标签**：`#csharp`

### [samugit83/redamon](https://github.com/samugit83/redamon)
- **定位**：AI 驱动的攻击性红队框架：从侦察、利用到后渗透全程自动化执行。
- **简介**：AI 驱动的攻击性红队框架：从侦察、利用到后渗透全程自动化执行。（GitHub 每日趋势 2026-09-29：★2743，当日 +97）
- **归档**：`开源项目介绍/2026.9.29/redamon.md`
- **标签**：`#python`

### [smicallef/spiderfoot](https://github.com/smicallef/spiderfoot)
- **定位**：SpiderFoot：自动化 OSINT 威胁情报与攻击面测绘。
- **简介**：SpiderFoot：自动化 OSINT 威胁情报与攻击面测绘。（GitHub 每日趋势 2026-10-01：★22689，当日 +33）
- **归档**：`开源项目介绍/2026.10.1/spiderfoot.md`
- **标签**：`#python`

### [uber/ADR](https://github.com/uber/ADR)
- **定位**：Uber 的 ADR：通过可观测性、安全基准与威胁检测保护企业 AI Agent。
- **简介**：Uber 的 ADR：通过可观测性、安全基准与威胁检测保护企业 AI Agent。（GitHub 每日趋势 2026-10-08：★1876，当日 +36）
- **归档**：`开源项目介绍/2026.10.8/ADR.md`
- **标签**：`#python`

### [usestrix/strix](https://github.com/usestrix/strix)
- **定位**：开源 AI 渗透测试工具，自动发现并修复应用漏洞。
- **简介**：开源 AI 渗透测试工具，自动发现并修复应用漏洞。（GitHub 每日趋势 2026-09-26：★64951，当日 +208）
- **归档**：`开源项目介绍/2026.9.27/strix.md`
- **标签**：`#python`

### [Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool)
- **定位**：面向授权安全测试的 AI 引导式一体化渗透测试工具集
- **简介**：**hackingtool** 是 2020 年 4 月创建的开源一体化安全测试工具集，当前版本在单一终端控制台收录 **21 个分类、215 款精选工具**（信息收集、字典生成、无线、SQL 注入、钓鱼、Web 攻击、后渗透、取证、载荷生成、漏洞利用框架、逆向、DDoS、RAT、XSS、隐写、AD、云安全、移动安全、密码/哈希破解等），以 63 个固定标签检索，另有 59 个失修条目归档隐藏。改造后的核心差异化是 **AI 引导层**：裸文本或 /ai 将自然语言意图经固定标签分类法映射为真实工具（模型只能返回分类法内标签，不可能编造工具）；/goal 由 AI 一次调用生成真实命令计划（含每步理由与安装提示），确认目标授权后逐步执行（列表式 subprocess、不经 shell，工作区留存 plan.json/run.log/原始输出）；/find 先查本地目录再查 GitHub API、可解释排名、仅建议不安装不运行且零模型调用；无头模式 --engagement 产出统一 findings.json 并可选 AI 汇总与报告。AI 层**可选、自带密钥**（OpenAI 兼容端点或本地 Ollama），未配置时全部退化为标准库关键词匹配等确定性离线行为。安全设计：无 curl|bash、下载源固定+SHA-256 校验、不强制 sudo、API 密钥仅写入权限 600 的 .env、越界请求（信号干扰、DoS、大规模目标、恶意软件）在任何网络调用前即被拒绝。**技术栈**：Python 3.10+，仅支持 Linux/macOS（Windows 明确不支持）；prompt_toolkit 交互控制台（/ 命令、@ 工具与标签补全），非交互环境回退经典数字菜单；目录驱动架构，绝大多数工具只是 src/hackingtool/catalog/ 下的一个 YAML 条目；安装支持 pipx（推荐）/uv/venv/Docker；部分工具需 Go 1.21+/Ruby/tmux/Docker。**协议** MIT。**规模与时间线**：**Stars 79,695、Forks 9,036**、Open Issues 133、Watchers 1,484、Commits 340、贡献者 41、3 个 Tags，未发布正式 GitHub Release；2020-04-11 创建，最近推送 2026-08-23；曾登 Trendshift 趋势榜。**合规注意事项**：项目自我定位为仅服务授权安全测试（红队、蓝队/SOC、DFIR、OSINT、漏洞赏金、CTF），但收录 DDoS、RAT、钓鱼等攻击性工具，在中国及多数司法辖区对未授权目标使用属违法犯罪，仅限自有或书面授权系统在隔离环境中使用。
- **归档**：`开源项目介绍/2026.9.25/hackingtool.md`
- **标签**：`#security` `#pentest` `#hacking` `#linux` `#osint` `#cli`

### [zhaoxuya520/reverse-skill](https://github.com/zhaoxuya520/reverse-skill)
- **定位**：面向 AI 编码客户端的逆向工程与授权安全研究技能路由包，带合规门禁与证据链
- **简介**：**reverse-skill** 是一个"网络安全技能路由包"，MIT 协议（CTF-Sandbox-Orchestrator 子目录为 GPLv3），README 指向项目站 reverse.apivix.com，主语言 PowerShell。它解决的痛点很实际：AI 智能体遇到 APK、二进制、前端 JS 加密、CTF 题目或渗透测试目标时往往靠猜命令、选错工具，该包负责把任务路由到正确的方法论技能、探测并按需自举本机工具链，再执行可复现的工作流。**差异化亮点**：一是客户端无关——以 skills/config/routing.json 为路由唯一事实源，不绑定 Claude Code/Codex/Cursor/OpenCode/Kiro/Cline；二是合规设计突出——全局规则（RULES.md）要求先通过 scope 授权门禁才允许对目标采取任何 ACT 动作，case-init 生成案件目录（scope/timeline/workitems），全程留存 Evidence→Finding→Path 证据链并支持 SHA-256 完整性校验与只读 Case Review；三是工程化验证——170+ 条中英双语路由回归基准在 GitHub Actions Windows+Ubuntu 双平台跑回归、结构一致性、冒烟与 INDEX 漂移检查，且做供应链版本固定。场景覆盖 40+ 技能模块：Android/iOS 移动端、exe/dll/so/ELF 二进制（IDA Pro/radare2/Ghidra/Binary Ninja）、.NET、JS 加密参数、DSL 虚拟机、HTTP 抓包重放（Reqable MCP）、恶意软件/YARA、渗透扫描、攻击链编排、固件/IoT、补丁差分/N-day、Pwn、API/GraphQL、供应链 SBOM、LLM 安全、OLLVM 反混淆，另有含 42 个子技能的 CTF 沙箱编排器。技术栈：PowerShell 为主，配 Bash/Python/Node.js 脚本与 Markdown 技能文档；依赖 Java/JDK（jadx、apktool）、Node.js 22.12+、Python 3.x 与任一兼容 AI 客户端。规模数据：Stars 约 **37,991**、Forks 5,269、开放 issue 仅 22、贡献者 15、commits 约 181、tags 1，曾登 Trendshift 趋势榜。时间线：创建 2026-05-13，唯一 Release v1.0.1（2026-08-08），最近推送 2026-09-22，主分支已演进至 44 条路由规则。**注意事项（合规边界）**：项目免责声明明确仅限合法安全研究、教育、CTF 及自有或获明确授权系统的测试，严禁未经授权的访问、扫描、利用与数据获取；README 各处对规则数与基准数的口径不一致（44/175、43/173、41/163），档案中已如实分别标注。
- **关联**：库内 [cloudflare/security-audit-skill](https://github.com/cloudflare/security-audit-skill)、[Z4nzu/hackingtool](https://github.com/Z4nzu/hackingtool)
- **归档**：`开源项目介绍/2026.9.27/reverse-skill.md`
- **标签**：`#skill` `#reverse-engineering` `#security-research` `#ai-agent` `#pentest`

<a id="sec-8"></a>

## 🧩 八、Skill 合集与生态（31）

### [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- **定位**：面向 AI 编码 Agent 的生产级工程技能（25 skills + 9 斜杠命令）
- **简介**：Addy Osmani（Google Chrome 团队）出品。**Skill 把资深工程师构建软件时使用的工作流、质量关卡和最佳实践编码下来**，打包成 AI Agent 能在开发每个阶段一致遵循的形式。9 个斜杠命令对应完整生命周期 `DEFINE → PLAN → BUILD → VERIFY → REVIEW → SHIP`，每个命令自动激活合适的 skill：`/spec`（**Spec before code**）· `/plan`（小而原子的任务）· `/build`（一次一个切片）· `/test`（**测试即证明**）· `/constraints`（决定一次、处处强制）· `/review`（改善代码健康度）· `/webperf`（**优化前先测量**）· `/code-simplify`（**清晰胜过聪明**）· `/ship`（**更快就是更安全**）。想少点手工？**`/build auto`** 生成计划并在一次批准的流程中实现每个任务——你只批准一次计划然后它自主跑完；它移除的是**任务之间**的人工介入而非验证：每个任务依然测试驱动、独立提交，遇到失败或有风险的步骤会**暂停**。Skill 也会按你在做的事自动激活（设计 API → `api-and-interface-design`，构建 UI → `frontend-ui-engineering`）。安装最快路径是开放的 [skills CLI](https://github.com/vercel-labs/skills)，可装进 **70+ 个 agent**：`npx skills add addyosmani/agent-skills`（`--list` 先浏览、`--skill <name>` 只取单个）。也支持 Claude Code plugin marketplace（`/plugin marketplace add addyosmani/agent-skills` + `/plugin install agent-skills@addy-agent-skills`）。⚠️ 两个坑记录在案：**按 skill 安装不会拷仓库级 `references/` 目录**（skill 可用但共享清单路径失效，issue #361 跟踪）；marketplace 走 SSH clone，没配 key 时用完整 HTTPS URL，或 `git config --global url."https://github.com/".insteadOf git@github.com:` 一次性重写。MIT，**98,442 stars** / 10,342 forks，2026-02 创建，Trendshift 上榜，官网 [skills.addy.ie](https://skills.addy.ie)。
- **归档**：`开源项目介绍/2026.9.23/agent-skills.md`
- **标签**：`#skill` `#工程实践` `#tdd` `#斜杠命令` `#claude-code` `#addyosmani`

### [AgriciDaniel/claude-seo](https://github.com/AgriciDaniel/claude-seo)
- **定位**：Claude Code 通用 SEO 技能：26 个子技能＋19 个子代理，覆盖技术 SEO、E-E-A-T、Schem
- **简介**：Claude Code 通用 SEO 技能：26 个子技能＋19 个子代理，覆盖技术 SEO、E-E-A-T、Schema、GEO/AEO。（GitHub 每日趋势 2026-10-01：★18022，当日 +72）
- **归档**：`开源项目介绍/2026.10.1/claude-seo.md`
- **标签**：`#python`

### [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)
- **定位**：规模最大的开源 Agent Skills 库：388 个技能、20 个领域、96 个插件，一套 SKILL.md 服务 13 种编码 Agent
- **简介**：claude-skills 是 Alireza Rezvani 于 **2025-10-19** 创建的 MIT 协议技能库，从单个 `content-creator` 营销技能起步，十个月长成 **388 个生产级技能、20 个领域、118 个 Agent、7 个 Persona、150 条斜杠命令、96 个插件市场条目**，是当前最大的开源 Claude Code / Agent Skills 集合：**26,405 stars / 3,718 forks / 242 watchers / 1,499 commits / 46 位贡献者 / 7 个 tag / 6 个 Release**，仓库约 22 MB、10 种语言。每个技能是一个含 `SKILL.md`（YAML frontmatter + 指令）加可选 `scripts/`、`references/`、`assets/` 的目录，遵循 agentskills.io 标准，因此**一个仓库同时服务 13 种编码 Agent**：Claude Code、OpenAI Codex、Gemini CLI、OpenClaw 原生，Hermes Agent 与 Mistral Vibe 走 BYO-sync，Cursor / Aider / Windsurf / Kilo Code / OpenCode / Augment / Antigravity 由 `scripts/convert.sh --tool all` 转换后 `install.sh` 落地；Claude Code 侧用 `/plugin marketplace add alirezarezvani/claude-skills` 按领域安装。领域分布为工程核心 53 + 工程 POWERFUL 93、市场 49+7、C-Level 咨询 46 + C-Level Agents 22、监管与质量 19、产品 17、生产力 12、学术研究 10、合规 OS 9、项目管理 9、商业 8、业务运营 7、Agent Launcher 6、金融 5、Research Ops 5、Markdown→HTML 5、Loop Library 1。差异化不在数量而在**工程治理**：对外计数全部由 `scripts/derive_counters.py --check` 派生并被 CI 锁定；设有技能名与内置命令冲突（#885）、frontmatter YAML（G10）、退役模型（G7）、路径（G1）、脚本冒烟（G8）、`plugin.json` 非法键（#954）等阻断式门禁；对引入的上游能力保留公开 `audit/` 审计记录（如审计 petergyang/human-review 后判定"不 vendor、只借鉴模式"，据此重写为零网络的 `engineering/human-gate`）；706+ 个 Python 工具全部 **stdlib-only、零 pip 依赖**，另配 823 份参考文档。前沿模块包括 `agent-memory`（L0–L3 四级、靠跨会话跨天复现晋升、未经人工 adopt 不进 CLAUDE.md）、`memory-engineering`（记忆写路径成本定价与遗忘策略）、`skillopt-sleep`（vendor 自 microsoft/SkillOpt 的夜间门控自进化）、`agent-harness` 与 `agent-launcher`（把目标编译成 `max_iterations` 钳制在 1..20 的有界 grade→iterate 循环或 POSIX cron 定时部署）、`skill-security-auditor`（安装前扫命令注入/提权/数据外泄，输出 PASS/WARN/FAIL）。时间线：**v2.12.0**（2026-08-24/25）是自 v2.9.0 以来首个打 tag 的 Release，合并了此前只写进 README 却未打 tag 的 v2.10.0–v2.11.2，并把 17 个 open issue 全部推进终态；此前有 v2.9.0（2026-05-28）、v2.0.0（2026-03-04，86 skills / 9 domains）。最近推送 2026-08-30，主干已约一个月未动。注意事项：README 计数自相矛盾（首页 388 skills，多工具章节写 345，校验期望 346），"5,200+ stars"引用块严重过时；Windows 必须 `git clone -c core.symlinks=true`（开发者模式）并设 `PYTHONUTF8=1`，否则镜像树会退化为一行指针文本；v2.12.0 前有 39 个 `plugin.json` 因非规范键导致约 40% 市场插件无法安装，建议升级。文档站 alirezarezvani.github.io/claude-skills。
- **关联**：库内 [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)、[tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills)（另两个 Skill 合集）
- **归档**：`开源项目介绍/2026.9.25/claude-skills.md`
- **标签**：`#claude-code` `#agent-skill` `#plugin` `#提示词工程` `#codex` `#cursor`

### [anthropics/claude-plugins-official](https://github.com/anthropics/claude-plugins-official)
- **定位**：Anthropic 官方维护的高质量 Claude Code 插件目录。
- **简介**：Anthropic 官方维护的高质量 Claude Code 插件目录。（GitHub 每日趋势 2026-09-26：★37045，当日 +283）
- **归档**：`开源项目介绍/2026.9.27/claude-plugins-official.md`
- **标签**：`#python`

### [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins)
- **定位**：Anthropic 官方知识工作者插件库（Claude Cowork 用）。
- **简介**：Anthropic 官方知识工作者插件库（Claude Cowork 用）。（GitHub 每日趋势 2026-10-07：★26322，当日 +124）
- **归档**：`开源项目介绍/2026.10.8/knowledge-work-plugins.md`
- **标签**：`#python`

### [anthropics/skills](https://github.com/anthropics/skills)
- **定位**：Anthropic 官方 Agent Skills 示例合集、规范与技能模板仓库
- **简介**：**anthropics/skills** 是 Anthropic 官方的 Agent Skills 公共仓库（描述 "Public repository for Agent Skills"），创建于 **2025-09-22**，一年内即获约 **177,818 Stars、21,067 Forks**，是 Skills 生态最受关注的参考仓库。Skill 是自包含文件夹：SKILL.md 携带 YAML frontmatter（仅需 name、description 两个字段）与指令正文，辅以脚本和资源，由 Claude 按需动态加载，以可复现方式教会模型完成按品牌规范生成文档、按组织流程分析数据、自动化个人任务等专门工作。仓库收录 **19 个官方示例技能**，覆盖创意设计、开发技术、企业沟通与文档处理四大类：algorithmic-art、canvas-design、frontend-design、theme-factory、slack-gif-creator（创意），mcp-builder、webapp-testing、web-artifacts-builder、claude-api、skill-creator（开发），brand-guidelines、internal-comms、doc-coauthoring、academy-guide、discernment-nudge（企业），以及 **docx/pdf/pptx/xlsx** 四个生产级文档技能——后者正是驱动 Claude 官方 Create Files 能力的真实实现，以 source-available（非开源）方式发布供参考复杂技能写法；多数示例技能为 **Apache 2.0**，仓库级无统一 LICENSE（GitHub API license 为 null）。仓库同时托管 **Agent Skills 规范**（spec/agent-skills-spec.md，标准站点 agentskills.io）与**技能模板**（template/SKILL.md），并通过 .claude-plugin/marketplace.json 注册为 Claude Code 插件市场：`/plugin marketplace add anthropics/skills` 后可安装 document-skills 或 example-skills 插件，对话中提及即可调用；Claude.ai 付费计划内置全部示例技能，Claude API 提供 Skills 接口支持预置与自定义技能；README 还展示 Notion 等合作伙伴技能。规模数据：主语言 **Python**，默认分支 main，**commits 56、贡献者 15（含匿名 16）、无 Tag、无 Release**，约 4.7MB、419 个文件；open issues 1,274，watchers 1,130，Discussions 开启，最近推送 2026-09-22。注意事项：官方免责声明指出技能仅供演示与教育目的，Claude 实际行为可能与技能所示不同，关键任务前须自行充分测试；docx/pdf/pptx/xlsx 为 source-available 许可，二次分发需留意条款。
- **归档**：`开源项目介绍/2026.9.25/skills.md`
- **标签**：`#agent-skill` `#claude` `#anthropic` `#skill-md` `#plugin-marketplace`

### [aws/agent-toolkit-for-aws](https://github.com/aws/agent-toolkit-for-aws)
- **定位**：AWS 官方的 MCP 服务器、技能与插件合集，帮 AI Agent 在 AWS 上构建。
- **简介**：AWS 官方的 MCP 服务器、技能与插件合集，帮 AI Agent 在 AWS 上构建。（GitHub 每日趋势 2026-10-01：★2762，当日 +10）
- **归档**：`开源项目介绍/2026.10.1/agent-toolkit-for-aws.md`
- **标签**：`#python`

### [cloudflare/cloudflare-os](https://github.com/cloudflare/cloudflare-os)
- **定位**：基于 Cloudflare Workers 的 Agent 工作空间：创建文档、构建应用、运行 Agent，带着企业上下
- **简介**：基于 Cloudflare Workers 的 Agent 工作空间：创建文档、构建应用、运行 Agent，带着企业上下文。（GitHub 每日趋势 2026-10-03：★10457，当日 +84）
- **归档**：`开源项目介绍/2026.10.4/cloudflare-os.md`
- **标签**：`#typescript`

### [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills)
- **定位**：精选的 Claude Skills、资源与工具合集，用于定制 Claude AI 工作流。
- **简介**：精选的 Claude Skills、资源与工具合集，用于定制 Claude AI 工作流。（GitHub 每日趋势 2026-10-01：★76040，当日 +118）
- **归档**：`开源项目介绍/2026.10.1/awesome-claude-skills.md`
- **标签**：`#python`

### [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills)
- **定位**：面向 Claude Code 和 AI Agent 的营销技能集：CRO、文案、SEO、分析与增长工程。
- **简介**：面向 Claude Code 和 AI Agent 的营销技能集：CRO、文案、SEO、分析与增长工程。（GitHub 每日趋势 2026-10-03：★52311，当日 +139）
- **归档**：`开源项目介绍/2026.10.3/marketingskills.md`
- **标签**：`#javascript`

### [cursor/plugins](https://github.com/cursor/plugins)
- **定位**：Cursor 插件规范与官方插件合集。
- **简介**：Cursor 插件规范与官方插件合集。（GitHub 每日趋势 2026-10-02：★9281，当日 +157）
- **归档**：`开源项目介绍/2026.10.2/plugins.md`
- **标签**：`#typescript`

### [CursorTouch/Windows-MCP](https://github.com/CursorTouch/Windows-MCP)
- **定位**：Windows 计算机使用的 MCP 服务器（让 AI 控制电脑）。
- **简介**：Windows 计算机使用的 MCP 服务器（让 AI 控制电脑）。（GitHub 每日趋势 2026-10-09：★8299，当日 +411）
- **归档**：`开源项目介绍/2026.10.9/Windows-MCP.md`
- **标签**：`#python`

### [dotnet/skills](https://github.com/dotnet/skills)
- **定位**：.NET 官方的 AI 编码技能（skills）仓库。
- **简介**：.NET 官方的 AI 编码技能（skills）仓库。（GitHub 每日趋势 2026-09-26：★5485，当日 +5）
- **归档**：`开源项目介绍/2026.9.27/skills.md`
- **标签**：`#csharp`

### [garrytan/gstack](https://github.com/garrytan/gstack)
- **定位**：Garry Tan 的 Claude Code 完整配置：23 个定制工具分别扮演 CEO、设计师、工程经理、发布经理、
- **简介**：Garry Tan 的 Claude Code 完整配置：23 个定制工具分别扮演 CEO、设计师、工程经理、发布经理、文档工程师等角色。（GitHub 每日趋势 2026-10-05：★135060，当日 +121）
- **归档**：`开源项目介绍/2026.10.5/gstack.md`
- **标签**：`#typescript`

### [google/skills](https://github.com/google/skills)
- **定位**：面向 Google 产品与技术的 Agent Skills 官方仓库。
- **简介**：面向 Google 产品与技术的 Agent Skills 官方仓库。（GitHub 每日趋势 2026-10-02：★20557，当日 +33）
- **归档**：`开源项目介绍/2026.10.2/skills.md`
- **标签**：`#python`

### [hashgraph-online/awesome-codex-plugins](https://github.com/hashgraph-online/awesome-codex-plugins)
- **定位**：精选的 OpenAI Codex / ChatGPT 插件、技能与资源合集（#1 Codex 市场）。
- **简介**：精选的 OpenAI Codex / ChatGPT 插件、技能与资源合集（#1 Codex 市场）。（GitHub 每日趋势 2026-10-02：★1135，当日 +19）
- **归档**：`开源项目介绍/2026.10.2/awesome-codex-plugins.md`
- **标签**：`#python`

### [ifixai-ai/iFixAi](https://github.com/ifixai-ai/iFixAi)
- **定位**：AI Agent 的独立审计：人类或 Agent 自己运行，回答 Agent 经济中最关键的问题——这件事 Agent
- **简介**：AI Agent 的独立审计：人类或 Agent 自己运行，回答 Agent 经济中最关键的问题——这件事 Agent 真做对了吗？（GitHub 每日趋势 2026-10-01：★17122，当日 +250）
- **归档**：`开源项目介绍/2026.10.1/iFixAi.md`
- **标签**：`#python`

### [mattpocock/skills](https://github.com/mattpocock/skills)
- **定位**：Matt Pocock（TypeScript 名师）的实战工程技能集，直接来自其 .agents 目录。
- **简介**：Matt Pocock（TypeScript 名师）的实战工程技能集，直接来自其 .agents 目录。（GitHub 每日趋势 2026-09-26：★269532，当日 +671）
- **归档**：`开源项目介绍/2026.9.28/skills.md`
- **标签**：`#shell`

### [microsoft/mcp](https://github.com/microsoft/mcp)
- **定位**：微软官方 MCP 服务器实现目录与 Azure/Fabric 服务器统一工程仓库
- **简介**：**microsoft/mcp** 是微软官方的 **MCP（Model Context Protocol）服务器目录仓库**，描述为 "Catalog of official Microsoft MCP server implementations for AI-powered data access and tool integration"，**MIT** 协议，创建于 **2025-04-09**，主语言 **C#**（.NET）。MCP 是标准化应用向大模型提供上下文的开放协议，采用 Host—Client—Server 架构。仓库双重定位：其一，托管在本仓库内构建的两个核心服务器源码——**Azure MCP Server**（将全部 Azure MCP 工具聚合于单一服务器，实现 AI 智能体与 Azure 服务的无缝连接，可独立使用或配合 VS Code 的 GitHub Copilot for Azure 扩展）与 **Microsoft Fabric MCP Server**（Public Preview，local-first，为 AI 智能体提供 Fabric 公共 API、item 定义与最佳实践的完整访问，无需连接实时环境）；其二，作为微软全系 MCP 服务器官方目录，按云与基础设施、开发者工具、生产力、数据分析、安全五类收录 Foundry、Azure Resource Manager、Azure DevOps、AKS、Binlog、GitHub、Markitdown、M365 系列（Calendar/Mail/Teams/Word/Copilot Chat/User/Admin Center/OneDrive & SharePoint）、Learn、Enterprise（Entra）、Sentinel、SQL、Dataverse、Dev Box、Fabric RTI、Clarity、NuGet、Playwright、Wassette 等 20 余个服务器，区分 Local（stdio）与 Remote（HTTP 端点如 mcp.ai.azure.com、mcp.management.azure.com、learn.microsoft.com/api/mcp）两种类型，并提供 VS Code / VS Code Insiders / Visual Studio / IntelliJ / Eclipse / Claude Code 一键安装徽章，另可经 `microsoft/skills` 市场安装 Azure 插件接入 Copilot CLI 与 Claude Code。工程层面沉淀了微软各 MCP 服务器共用的核心库、测试框架、工程系统与 CI 流水线；发布由 azure-sdk-automation 机器人按服务器独立打 tag 滚动进行，产物含 **.mcpb 桌面扩展包**与 linux-arm64/x64/musl、Windows、macOS 多平台 zip（单资产最大约 205MB）。规模数据：**Stars 3,708、Forks 628、open issues 308、watchers 45**；**commits 2,458、贡献者 166（含匿名 168）、Tags 163、Releases 158**；最新版本 **Azure.Mcp.Server 3.0.0-beta.46**（2026-09-22 发布，prerelease），最近推送 2026-09-24，仓库体量约 312MB，迭代极为活跃。注意事项：Azure MCP 3.0 仍处 beta 通道，Fabric MCP 为 Public Preview，接口可能变动；M365 agent365 系列 Remote 端点需 Entra 租户 ID 与订阅授权；贡献需签署 Microsoft CLA；仓库未设 Topics、Discussions 未开启，文档主阵地为 Microsoft Learn 及各服务器 README/CHANGELOG。
- **归档**：`开源项目介绍/2026.9.25/mcp.md`
- **标签**：`#mcp` `#azure` `#微软` `#fabric` `#csharp`

### [microsoft/SkillOpt](https://github.com/microsoft/SkillOpt)
- **定位**：微软出品的文本空间优化器：用轨迹驱动编辑+验证门控，为冻结 LLM 训练可复用的自然语言技能。
- **简介**：微软出品的文本空间优化器：用轨迹驱动编辑+验证门控，为冻结 LLM 训练可复用的自然语言技能。（GitHub 每日趋势 2026-09-29：★17790，当日 +111）
- **归档**：`开源项目介绍/2026.9.29/SkillOpt.md`
- **标签**：`#python`

### [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills)
- **定位**：MiniMax 官方 Agent Skills 仓库。
- **简介**：MiniMax 官方 Agent Skills 仓库。（GitHub 每日趋势 2026-10-11：★13684，当日 +9）
- **归档**：`开源项目介绍/2026.10.11/skills.md`
- **标签**：`#csharp`

### [modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)
- **定位**：MCP 官方 C# SDK，用于构建 Model Context Protocol 服务端与客户端。
- **简介**：MCP 官方 C# SDK，用于构建 Model Context Protocol 服务端与客户端。（GitHub 每日趋势 2026-09-28：★4549，当日 +2）
- **归档**：`开源项目介绍/2026.9.28/csharp-sdk.md`
- **标签**：`#csharp`

### [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)
- **定位**：Model Context Protocol 官方 Python SDK（服务端与客户端）。
- **简介**：Model Context Protocol 官方 Python SDK（服务端与客户端）。（GitHub 每日趋势 2026-10-03：★24471，当日 +20）
- **归档**：`开源项目介绍/2026.10.4/python-sdk.md`
- **标签**：`#python`

### [modelcontextprotocol/servers](https://github.com/modelcontextprotocol/servers)
- **定位**：Model Context Protocol 官方服务器合集（MCP 参考实现库）。
- **简介**：Model Context Protocol 官方服务器合集（MCP 参考实现库）。（GitHub 每日趋势 2026-10-01：★90757，当日 +48）
- **归档**：`开源项目介绍/2026.10.1/servers.md`
- **标签**：`#typescript`

### [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents)
- **定位**：指尖上的完整 AI 代理公司：从前端巫师到 Reddit 社区忍者、从创意注入器到现实检查员。
- **简介**：指尖上的完整 AI 代理公司：从前端巫师到 Reddit 社区忍者、从创意注入器到现实检查员。（GitHub 每日趋势 2026-10-06：★157412，当日 +744）
- **归档**：`开源项目介绍/2026.10.8/agency-agents.md`
- **标签**：`#shell`

### [multica-ai/andrej-karpathy-skills](https://github.com/multica-ai/andrej-karpathy-skills)
- **定位**：一个 CLAUDE.md 文件改进 Claude Code 行为——源自 Andrej Karpathy 对 LLM 编
- **简介**：一个 CLAUDE.md 文件改进 Claude Code 行为——源自 Andrej Karpathy 对 LLM 编码陷阱的观察（★218K）。（GitHub 每日趋势 2026-10-11：★218010，当日 +279）
- **归档**：`开源项目介绍/2026.10.11/andrej-karpathy-skills.md`
- **标签**：`#开源`

### [pbakaus/impeccable](https://github.com/pbakaus/impeccable)
- **定位**：让 AI Harness 更懂设计的设计语言与规范。
- **简介**：让 AI Harness 更懂设计的设计语言与规范。（GitHub 每日趋势 2026-09-26：★71027，当日 +326）
- **归档**：`开源项目介绍/2026.9.28/impeccable.md`
- **标签**：`#javascript`

### [Q00/ouroboros](https://github.com/Q00/ouroboros)
- **定位**：Agent OS：Agent 自我变强，人类只守底线——面试门控、分级评估、预算化进化循环，含 MCP 服务器与 14
- **简介**：Agent OS：Agent 自我变强，人类只守底线——面试门控、分级评估、预算化进化循环，含 MCP 服务器与 14 种运行时。（GitHub 每日趋势 2026-09-30：★6138，当日 +11）
- **归档**：`开源项目介绍/2026.9.30/ouroboros.md`
- **标签**：`#python`

### [tech-leads-club/agent-skills](https://github.com/tech-leads-club/agent-skills)
- **定位**：面向专业编码 Agent 的**安全策展** Skill 注册中心 · 一份技能装到 17 个 Agent
- **简介**：Tech Leads Club 社区维护的**经安全验证**的 Skill 库与分发工具链。核心切入点是 Skill 生态的安全痛点——引用 Snyk 报告「**开放市场 13.4% 的技能含严重漏洞**」，并用四道防线做差异化：**100% 开源无二进制** · **CI 静态分析** · **锁文件 + 内容哈希** · **Snyk Agent Scan 发布前扫描**。支持三级梯队约 **17 个 Agent**（Claude Code、Cursor、Copilot、Windsurf、Codex、TRAE、Antigravity、Amazon Q 等），`npx @tech-leads-club/agent-skills` 交互向导一键安装。精选技能含 **tlc-spec-driven**（四阶段规格驱动开发，与库里的 github/spec-kit 属同一思路）、aws-advisor、playwright-skill、figma 设计转代码等。附带 **MCP Server** 以**渐进式披露**暴露目录（search → read → fetch），避免上下文膨胀。**协议设计是内容型开源仓库的规范范本**：MIT（代码）+ CC-BY-4.0（官方 SKILL.md 内容），清晰区分「引擎」与「知识内容」的授权边界。TypeScript 100%，**5,770 stars** / 503 forks，2026-01 创建，2026-09-12 最近推送。与库里的 addyosmani/agent-skills（个人工程实践集）互补——**这个卖的是「安全策展 + 多 Agent 分发」**。
- **归档**：`开源项目介绍/2026.9.23/tech-leads-agent-skills.md`
- **标签**：`#skill` `#注册中心` `#安全扫描` `#mcp` `#typescript`

### [twostraws/SwiftUI-Agent-Skill](https://github.com/twostraws/SwiftUI-Agent-Skill)
- **定位**：SwiftUI Agent 技能，适配 Claude Code、Codex 等 AI 工具（Paul Hudson 出品
- **简介**：SwiftUI Agent 技能，适配 Claude Code、Codex 等 AI 工具（Paul Hudson 出品）。（GitHub 每日趋势 2026-10-10：★5329，当日 +88）
- **归档**：`开源项目介绍/2026.10.10/SwiftUI-Agent-Skill.md`
- **标签**：`#开源`

### [wshobson/agents](https://github.com/wshobson/agents)
- **定位**：面向 Claude Code 等七大宿主的多宿主 Agent 插件市场
- **简介**：wshobson/agents 自称 **Agentic Plugin Marketplace**，用一套 Markdown 源（plugins/）沉淀生产可用的工作流积木——**94 插件、202 子代理、183 技能、105 斜杠命令、16 多代理编排器**，原生分发到 **Claude Code、Codex CLI、Cursor、OpenCode、Antigravity CLI、GitHub Copilot、Pi 七大宿主**。**MIT** 协议，主语言 **Python**（构建/生成/评测工具链），维护者 Seth Hobson。核心差异化是**「单一事实源、按宿主原生适配」**：每个宿主拿到符合自身习惯的原生产物而非最小公分母降级翻译，安装某插件只加载其组件而非整个市场；Codex/Cursor 从已提交注册表直装，Antigravity/OpenCode/Pi 经 clone+`make generate`，技能可用 `gh skill install`/`npx skills add` 单独安装免 clone。自带**分层模型策略**（Tier0 Fable 5 最长时程、Tier1 Opus 架构/安全/审查、Tier2 inherit、Tier3 Sonnet 文档/测试、Tier4 Haiku 快速运维）与 **plugin-eval** 三层质量评测（静态 lint / LLM judge / Monte Carlo）；工程化命令 make generate-all/validate/garden；外部集成 Pensyve（记忆）与 HOL Guard（安全，锁定 commit、需批准安装）。内容覆盖架构、语言、基础设施、安全、数据、ML、文档、商业、SEO 等领域。规模数据（2026-09-27）：Stars ~40,000、Forks ~4,267、Subscribers 316、Commits 592，创建 2025-07-24，最近推送 2026-09-26，无正式 GitHub Release。注意事项：本库数据来源分歧最大——api.github.com 快照滞后（pushed_at 09-21），故 stars/forks/推送以 ungh.cc、badgen.net 实时值为准；open_issues 的 api 快照（15）与 badgen（125）口径不同，两值均如实保留；贡献者与 tags 精确值因限流未获取到。
- **关联**：库内 [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills)、[anthropics/skills](https://github.com/anthropics/skills)、[addyosmani/agent-skills](https://github.com/addyosmani/agent-skills)
- **归档**：`开源项目介绍/2026.9.27/agents.md`
- **标签**：`#claude-code` `#ai-agent` `#subagents` `#skill` `#mcp`

<a id="sec-9"></a>

## 💻 九、代码智能 / RAG / 代码审查（13）

### [alibaba/open-code-review](https://github.com/alibaba/open-code-review)
- **定位**：阿里巴巴开源的 AI 代码审查 CLI（确定性工程 × Agent 混合架构）
- **简介**：起源于**阿里巴巴集团内部的官方 AI 代码审查助手**——过去两年服务**数万名开发者**、识别**数百万个代码缺陷**，经大规模验证后孵化开源。**只需配置一个模型端点即可开始**。它读 Git diff，通过具备 tool-use 能力的 agent 把变更发给可配置 LLM，生成**行级精度**的结构化评论；agent 能读完整文件、搜索代码库、检查其他变更文件以获得上下文，产出**深度审查而非表面 diff 反馈**。另有 `ocr scan` 审查整个文件，用于审计**没有有意义 diff 的陌生代码库**。**核心洞察：通用 Agent 做代码审查有三大痛点**——大变更集时会「偷懒」漏文件（覆盖不完整）、报告位置与实际代码对不上（位置漂移）、prompt 稍改质量就大幅波动（质量不稳定），**根因是纯语言驱动的架构对审查过程缺乏硬约束**。解法是让两者各做擅长的事：**确定性工程提供硬约束**（精确文件选择确保不漏、智能文件打包把相关文件如 `message_en.properties` + `message_zh.properties` 归为一个单元并让每个 bundle 作为 **sub-agent 在隔离上下文运行**、基于模板引擎的细粒度规则匹配从源头消除信息噪声、外置的评论定位与反思模块系统性提升位置与内容准确度）；**Agent 负责动态决策**（场景调优的 prompt 降 token、从大规模生产数据 tool-call trace 蒸馏出的场景调优工具集）。**Benchmark 很硬**：基于 50 个热门开源仓库、200 个真实 PR、10 种语言，由 80+ 位资深工程师交叉验证出 1,505 条 ground-truth 问题（数据集已开源为 [AACR-Bench](https://huggingface.co/datasets/Alibaba-Aone/aacr-bench)）。用**同一底层模型**对比 Claude Code，Precision 和 F1 显著更高、**只消耗约 1/9 的 token**、审查更快；Recall 较低是**刻意用召回换精度**以减少噪声。支持 Windows/macOS/Linux，agent 集成 Claude Code / Codex / Cursor / Kimi Code，模型走 OpenAI 与 Anthropic 兼容接口，内置 NPE/线程安全/XSS/SQL 注入等多语言规则集。**OpenSSF Best Practices Gold** 认证，README 5 种语言，npm 包 `@alibaba-group/open-code-review`。Go 语言，Apache-2.0，**39,711 stars** / 2,851 forks，2026-05 创建——四个月近 4 万星，Trendshift 日/周/月榜（Go 分类）。
- **归档**：`开源项目介绍/2026.9.23/open-code-review.md`
- **标签**：`#代码审查` `#阿里巴巴` `#go` `#混合架构` `#行级评论` `#benchmark`

### [allenai/olmocr](https://github.com/allenai/olmocr)
- **定位**：AllenAI 出品：将 PDF 线性化为 LLM 训练数据集的工具箱。
- **简介**：AllenAI 出品：将 PDF 线性化为 LLM 训练数据集的工具箱。（GitHub 每日趋势 2026-10-08：★19723，当日 +22）
- **归档**：`开源项目介绍/2026.10.8/olmocr.md`
- **标签**：`#python`

### [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph)
- **定位**：预索引的代码知识图谱，代码变更自动同步；支持 Claude Code/Codex/Gemini/Cursor 等主流编码
- **简介**：预索引的代码知识图谱，代码变更自动同步；支持 Claude Code/Codex/Gemini/Cursor 等主流编码 Agent。（GitHub 每日趋势 2026-10-01：★72521，当日 +159）
- **归档**：`开源项目介绍/2026.10.1/codegraph.md`
- **标签**：`#c`

### [google/langextract](https://github.com/google/langextract)
- **定位**：谷歌出品：用 LLM 从非结构化文本中提取结构化信息的 Python 库。
- **简介**：谷歌出品：用 LLM 从非结构化文本中提取结构化信息的 Python 库。（GitHub 每日趋势 2026-09-26：★38847，当日 +154）
- **归档**：`开源项目介绍/2026.9.28/langextract.md`
- **标签**：`#python`

### [headroomlabs-ai/headroom](https://github.com/headroomlabs-ai/headroom)
- **定位**：Headroom：压缩工具输出、日志、文件与 RAG 块再给 LLM——编码 Agent 省 20% token，RAG
- **简介**：Headroom：压缩工具输出、日志、文件与 RAG 块再给 LLM——编码 Agent 省 20% token，RAG 场景省 60-95%。（GitHub 每日趋势 2026-10-10：★74820，当日 +120）
- **归档**：`开源项目介绍/2026.10.10/headroom.md`
- **标签**：`#python`

### [Robbyant/lingbot-map](https://github.com/Robbyant/lingbot-map)
- **定位**：ECCV 2026 最佳论文候选：LingBot-Map，几何上下文 Transformer 做流式 3D 重建。
- **简介**：ECCV 2026 最佳论文候选：LingBot-Map，几何上下文 Transformer 做流式 3D 重建。（GitHub 每日趋势 2026-10-10：★17618，当日 +109）
- **归档**：`开源项目介绍/2026.10.10/lingbot-map.md`
- **标签**：`#python`

### [sqlfluff/sqlfluff](https://github.com/sqlfluff/sqlfluff)
- **定位**：模块化 SQL Linter 与自动格式化器，支持多方言与模板化代码。
- **简介**：模块化 SQL Linter 与自动格式化器，支持多方言与模板化代码。（GitHub 每日趋势 2026-10-03：★9916，当日 +9）
- **归档**：`开源项目介绍/2026.10.4/sqlfluff.md`
- **标签**：`#python`

### [t8y2/dbx](https://github.com/t8y2/dbx)
- **定位**：25 MB 的轻量跨平台数据库客户端，支持 100+ 种数据库（MySQL/PostgreSQL/SQLite/Redi
- **简介**：25 MB 的轻量跨平台数据库客户端，支持 100+ 种数据库（MySQL/PostgreSQL/SQLite/Redis/MongoDB 等）。（GitHub 每日趋势 2026-09-30：★21810，当日 +349）
- **归档**：`开源项目介绍/2026.9.30/dbx.md`
- **标签**：`#rust`

### [tester-army/e2e](https://github.com/tester-army/e2e)
- **定位**：面向 Web 与移动应用的下一代端到端测试框架。
- **简介**：面向 Web 与移动应用的下一代端到端测试框架。（GitHub 每日趋势 2026-10-05：★2677，当日 +344）
- **归档**：`开源项目介绍/2026.10.5/e2e.md`
- **标签**：`#typescript`

### [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph)
- **定位**：本地代码知识图谱 · AI 编码精准上下文
- **简介**：用 Tree-sitter 将代码库解析为结构图（函数/类/导入为节点，调用/继承/测试覆盖为边），增量跟踪变更，通过 MCP 给 AI 助手提供精准上下文，让它「只读该读的部分」。以 Flask 代码库为例：全文读取 143,594 tokens → 图谱查询 2,196 tokens，减少 **71 倍**。一条命令自动接入 **15+ AI 编码工具**（Codex、Claude Code、Cursor、Windsurf、Zed、Continue、OpenCode、Antigravity、Gemini CLI、Copilot 等），支持 Git/SVN 钩子、GitHub Action、对称卸载。MIT 协议，1,000 commits，5 种语言 README。
- **归档**：`开源项目介绍/2026.9.6/code-review-graph.md`
- **标签**：`#mcp` `#tree-sitter` `#token优化` `#代码审查`

### [VectifyAI/OpenKB](https://github.com/VectifyAI/OpenKB)
- **定位**：OpenKB：开源 LLM 知识库（VectifyAI 出品）。
- **简介**：OpenKB：开源 LLM 知识库（VectifyAI 出品）。（GitHub 每日趋势 2026-10-01：★4671，当日 +46）
- **归档**：`开源项目介绍/2026.10.1/OpenKB.md`
- **标签**：`#python`

### [VectifyAI/PageIndex](https://github.com/VectifyAI/PageIndex)
- **定位**：PageIndex：面向无向量、基于推理的 RAG 的文档索引。
- **简介**：PageIndex：面向无向量、基于推理的 RAG 的文档索引。（GitHub 每日趋势 2026-09-30：★37071，当日 +822）
- **归档**：`开源项目介绍/2026.9.30/PageIndex.md`
- **标签**：`#python`

### [vitali87/code-graph-rag](https://github.com/vitali87/code-graph-rag)
- **定位**：多语言代码知识图谱 RAG 系统
- **简介**：Tree-sitter 解析代码库 → 存入 Memgraph 图数据库 → 结合 Qdrant 向量库，支持自然语言查询代码结构与关系。支持 11 种编程语言，提供 MCP Server 集成。核心能力：死代码检测、AST 精准修补（diff 预览）、代码优化、ast-grep 模式搜索重写、增量索引更新。新增 TypeScript 分级验证、排除集处理、Windows 支持、补丁报告分级。MIT 协议，6,366 commits，社区非常活跃。
- **归档**：`开源项目介绍/2026.9.6/code-graph-rag.md`
- **标签**：`#rag` `#图数据库` `#代码分析` `#ast`

<a id="sec-10"></a>

## 🎙️ 十、语音与 TTS（6）

### [debpalash/VoiceStudio](https://github.com/debpalash/VoiceStudio)
- **定位**：本地语音工作室 · 开源版 ElevenLabs 替代 · 646 语言（原 OmniVoice-Studio）
- **简介**：全功能本地语音工作室——克隆声音、**声音设计**（用文字描述一个音色）、视频配音、听写（浮动小组件）、转写、有声书与批量任务，全部本地运行无需账号/API Key。集成 **16 个 TTS + 11 ASR 引擎**，覆盖 **646 种语言**，支持 CUDA / Apple Silicon MLX / ROCm / CPU / 远程 Worker。默认引擎为 VoiceStudio（由 k2-fsa/OmniVoice 驱动），也可换其他引擎。**Electron 桌面应用已正式落地**（不再只是「重写中」），另有 REST/SSE/WebSocket API、OpenAI 兼容音频 API、**MCP Server** 供 Agent 调用。macOS/Linux 一行安装：`curl -fsSL https://voicestudio.sh/install | sh`（`--version X.Y.Z` 指定版本、`--main` 从主干构建、`--uninstall` 卸载但保留数据），也可从 Releases 下载后按 macOS/Windows/Linux/Docker 平台指南安装。**支持「用 prompt 安装」**——把安装说明直接粘给 Claude Code / Codex / Cursor 让 Agent 自己装完。视频配音支持 YouTube 导入 + 定时语音，有声书支持多角色配音板和术语表管理。本地工作流跑在你自己的硬件上，远程服务是可选的，**使用分析需要明确同意**。README 提供简体中文版，官网 [voicestudio.sh](https://voicestudio.sh)，Trendshift 上榜。AGPL-3.0，**34,388 stars** / 4,052 forks，2026-04 创建，2026-09-22 仍在推送。
- **归档**：`开源项目介绍/2026.9.6/VoiceStudio.md`
- **标签**：`#tts` `#asr` `#语音克隆` `#mcp` `#本地优先` `#electron`

### [huggingface/speech-to-speech](https://github.com/huggingface/speech-to-speech)
- **定位**：低延迟语音 Agent 流水线 · OpenAI Realtime 兼容
- **简介**：HuggingFace 官方开源，全模块化语音对话流水线：VAD → STT → LLM → TTS，通过 OpenAI Realtime API（WebSocket + WebRTC）对外暴露，每个组件可替换。默认 Parakeet STT + Qwen3-TTS 本地运行，LLM 层兼容任何 OpenAI 协议（云端或本地 llama.cpp/vLLM）。已在 Reachy Mini 机器人生产环境服务数千台设备。含 OmniVoice、Pocket TTS 等技术，支持多语言、OpenAI Agents SDK。Apache-2.0 协议，1,063 commits。
- **归档**：`开源项目介绍/2026.9.6/speech-to-speech.md`
- **标签**：`#语音` `#huggingface` `#实时语音` `#realtime-api`

### [k2-fsa/OmniVoice](https://github.com/k2-fsa/OmniVoice)
- **定位**：支持 600+ 语言的 SOTA 零样本多语种语音克隆 TTS · RTF 低至 0.025（约 40 倍实时）
- **简介**：k2-fsa 团队（**Kaldi/Shark 生态，作者含 Daniel Povey**）开源的大规模多语种零样本 TTS，配套论文 arXiv:2604.00688。**600+ 语言覆盖是零样本 TTS 中最广**，采用「扩散语言模型风格」架构，输出 24 kHz 音频。**三种生成模式共用一个 `generate()` API**：① **语音克隆**（3-10 秒参考音频，`ref_text` 可省略由 Whisper 自动转写，克隆 prompt 可序列化 `.pt` **跨会话复用**）② **语音设计**（`instruct` 文本控制性别/年龄/音高/耳语/英美口音/**四川话等中文方言**）③ **自动音色**。**细粒度控制突出**：13 种非语言符号（`[laughter]`、`[sigh]` 等）、**中文拼音声调数字纠音**、英文 CMU 音素覆盖、数字文本归一化。**工程化程度是真正的差异化亮点**：支持 **CUDA / Apple MPS / Intel Arc XPU** 三后端，**FlashInfer 融合内核**（序列打包 CFG、融合 RMSNorm/RoPE/GEMM、CUDA Graph）带来 **2-2.9x 无损加速**——单卡 H100 fp16 下 batch=8 时 RTF 从 0.0298 降至 0.0115；提供 Gradio Demo、单条推理、多 GPU 批量推理三个 CLI，`examples/` 含完整训练微调流水线。⚠️ 语音设计模式**仅用中英数据训练**，低资源语言下克隆模式更稳；官方**明确禁止未授权克隆与冒充用途**。**这是库里 debpalash/VoiceStudio 的默认引擎**（VoiceStudio 默认引擎即「由 k2-fsa/OmniVoice 驱动」），两者是「模型层 + 产品层」的上下游关系。Apache-2.0，Python，**13,738 stars** / 2,067 forks，2026-03-31 开源，2026-09-21 最近推送。
- **归档**：`开源项目介绍/2026.9.23/OmniVoice.md`
- **标签**：`#tts` `#语音克隆` `#多语言` `#扩散模型` `#k2-fsa`

### [microsoft/VibeVoice](https://github.com/microsoft/VibeVoice)
- **定位**：微软开源的前沿语音 AI。
- **简介**：微软开源的前沿语音 AI。（GitHub 每日趋势 2026-10-03：★54602，当日 +36）
- **归档**：`开源项目介绍/2026.10.3/VibeVoice.md`
- **标签**：`#python`

### [openutau/OpenUtau](https://github.com/openutau/OpenUtau)
- **定位**：开源歌声合成平台，经典 UTAU 的现代后继者。
- **简介**：开源歌声合成平台，经典 UTAU 的现代后继者。（GitHub 每日趋势 2026-09-29：★4340，当日 +6）
- **归档**：`开源项目介绍/2026.9.29/OpenUtau.md`
- **标签**：`#csharp`

### [Tencent-Hunyuan/Hy-MT2](https://github.com/Tencent-Hunyuan/Hy-MT2)
- **定位**：腾讯混元翻译模型 Hy-MT2。
- **简介**：腾讯混元翻译模型 Hy-MT2。（GitHub 每日趋势 2026-10-10：★1176，当日 +147）
- **归档**：`开源项目介绍/2026.10.10/Hy-MT2.md`
- **标签**：`#python`

<a id="sec-11"></a>

## 🔧 十一、模型训练与微调（5）

（此「十一」为 2026-09-27 分区重组后的新编号，与已废弃的旧「十一、自撰稿件/推文库」无关，后者不再收录。）

### [jingyaogong/minimind](https://github.com/jingyaogong/minimind)
- **定位**：3 块钱成本、单卡 3090 约 2 小时，从零训练一个 64M 参数 LLM 的全流程教学项目
- **简介**：中文社区最具影响力的「从零训大模型」项目。主线 **minimind-3（64M Dense）/ minimind-3-moe（198M-A64M）**，结构对齐 Qwen3 生态：**Pre-Norm + RMSNorm、SwiGLU、RoPE + YaRN 外推、GQA（8q/4kv）、32768 max_pos**，自研仅 **6,400 词表**的小 tokenizer 以压缩 embedding 参数占比。**全阶段链路覆盖**：Pretrain → SFT → **LoRA（纯手写，非 peft）** → DPO → **PPO / GRPO / CISPO（RLAIF）** → **Agentic RL**（`train_agent.py` 多轮 Tool-Use）→ 黑盒/白盒蒸馏 → **自适应思考**（`open_thinking` 开关下沉到 chat_template），**所有算法从 0 实现，不依赖 trl/peft 封装**——这正是它的教学价值所在。全阶段数据开源（`pretrain_t2t_mini` 1.2GB + `sft_t2t_mini` 1.6GB 即可快速复现 Zero 模型），兼容 llama.cpp / vLLM / ollama 与 OpenAI API 协议服务端。**设计洞察**：针对 0.1B 小模型 RLAIF 的**奖励稀疏**问题，选用 InternLM2-1.8B-Reward 输出**连续分数**保证优势函数梯度非零；用 mini 数据集组合把「从零训 LLM」门槛压到 **3 元人民币**，教学叙事极具传播力。可与库里的 bojieli/ai-agent-book（第八章讲后训练原理）配套阅读——一个讲清楚「为什么」，一个让你亲手跑通「怎么做」。Apache-2.0，Python（PyTorch 原生），**60,900 stars** / 7,912 forks，2024-07 创建，2026-09-10 最近推送。
- **归档**：`开源项目介绍/2026.9.23/minimind.md`
- **标签**：`#llm训练` `#小模型` `#pytorch` `#强化学习` `#教程` `#moe`

### [MakazhanAlpamys/Soup](https://github.com/MakazhanAlpamys/Soup)
- **定位**：一份 YAML 微调 LLM，层流式加载让 4GB 显存训练 8B 模型
- **简介**：**Soup**（PyPI：`soup-cli`，官网 trysoup.dev）把 LLM 微调与后训练压缩成**一份 YAML + 一条命令**：`soup init --template chat` 生成配置、`soup train` 开训，批大小、GPU 检测、量化全自动，主打「零 SSH、零配置地狱」，**Apache-2.0** 协议。招牌技术 **layer streaming（层流式加载，BETA、opt-in `stream_layers: true`）**：冻结基座不驻留显存，从主机 RAM 按 decoder 层逐层喂给 GPU——**RTX 3050 Laptop 4GB** 上 Llama-3.1-8B + NF4 + LoRA 实测 **119.6 tok/s、峰值 3.32 GB**，与常规驻留运行 **bit-exact**，并在 H100 独立复现（113 tok/s、同 3.32 GB）；配套论文发表于 Zenodo（概念 DOI 10.5281/zenodo.21771064，v3 为 10.5281/zenodo.21918325），测量记录全公开含失败项，v3 主动撤回 v1「瓶颈在主机-设备传输」的未实测推断（实测删除全部 H2D 字节仅提速 1.4%，最大流式开销为每层 NF4 反量化 9.8%），并记录 NF4 单层超约 165MiB 时「前向 bit-exact 但梯度静默错误」缺陷的修复（#331）与「8 卡 ZeRO-3 慢于单卡驻留」的不利己对比。功能覆盖：训练任务含 **SFT、DPO/GRPO/PPO/KTO/ORPO/SimPO/IPO/BCO、RLHF、预训练、蒸馏、tool-calling、PRM、视觉/音频/TTS、unlearning、RAFT/RA-DIT**；PEFT 动物园（DoRA/LoRA+/rsLoRA/VeRA/PiSSA/ReLoRA/GaLore/NEFTune、YaRN/LongLoRA、packing）；三后端：transformers、Unsloth（快 2–5 倍）、MLX（Apple Silicon）；数据格式自动检测；导出 GGUF/ONNX/TensorRT/AWQ/GPTQ/BitNet；OpenAI 兼容 server、投机解码；`soup ui` Web 面板、`eval benchmark`、Elo 竞技场、autopilot、doctor 体检、100+ 现成 recipes 与数据飞轮（`soup loop`）；另有 HIPAA/SOC2/EU-AI-Act 合规模板与 BOM/签名/审计/airgap 供应链控制。VRAM 参考：8GB→7B、16GB→14B、24GB→34B、48GB→70B（QLoRA 4-bit）。规模与时间线：创建 **2026-02-20**，截至 2026-09-27 约 **7,296 Stars / 1,163 Forks / 74 位贡献者 / 1,481 commits / 179 tags**，9-26 仍在推送；最新 **v0.75.1**（2026-09-21），v0.75.0（09-12）落地「未知配置键拒绝加载」breaking 变更，v0.74.0（09-04）修复冻结基座一直按 fp32 加载的缺陷（H100 峰值显存 48,241→18,658 MiB）；社区高度外部驱动：v0.75.0 的 60 个 PR 全部来自 22 位外部贡献者。注意事项：仅支持 **Python 3.10–3.12**；README 性能数字测于 v0.72.2，4GB 卡复测在 #361 待办；维护者在单台 4GB 笔记本上开发维护。
- **关联**：库内 [unslothai/unsloth](https://github.com/unslothai/unsloth)（Soup 内置其后端）、[NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- **归档**：`开源项目介绍/2026.9.27/Soup.md`
- **标签**：`#llm` `#微调` `#lora` `#qlora` `#低显存` `#pytorch`

### [pytorch/pytorch](https://github.com/pytorch/pytorch)
- **定位**：主流深度学习框架：Python 张量与动态神经网络，GPU 加速强劲。
- **简介**：主流深度学习框架：Python 张量与动态神经网络，GPU 加速强劲。（GitHub 每日趋势 2026-09-28：★103408，当日 +56）
- **归档**：`开源项目介绍/2026.9.28/pytorch.md`
- **标签**：`#python`

### [tensorflow/tensorflow](https://github.com/tensorflow/tensorflow)
- **定位**：谷歌主导的开源机器学习框架，深度学习生态的事实标准，提供从训练到部署的完整工具链。
- **简介**：谷歌主导的开源机器学习框架，深度学习生态的事实标准，提供从训练到部署的完整工具链。（GitHub 每日趋势 2026-09-26：★200374，当日 +31）
- **归档**：`开源项目介绍/2026.9.27/tensorflow.md`
- **标签**：`#cpp`

### [unslothai/unsloth](https://github.com/unslothai/unsloth)
- **定位**：本地大模型运行/微调/部署一体化平台 · 首个既能跑又能训练模型的桌面应用
- **简介**：已演进为三位一体产品：**Unsloth Desktop**（Tauri 桌面应用）+ **Unsloth Studio**（Web UI）+ **Unsloth Core**（Python 库），运行并训练 LLM/扩散/嵌入/音频模型，训练快 2 倍、显存省 70%（Apache-2.0）。训练全面支持：LoRA/QLoRA/全量微调/预训练/RL/GRPO/DPO/FP8，MoE 训练快 12 倍省 35% 显存，新 Triton 内核 + Padding Free + Packing 再提速 3 倍，80GB GPU 可训超 500K 上下文。运行侧：OpenAI 兼容 API、`unsloth start claude/codex/opencode` 一条命令把本地模型接入编码 Agent（可作为子代理）、MCP 服务器与控制端点、私有搜索/深度研究/RAG、Cloudflare 安全 HTTPS 远程访问。硬件覆盖 CPU/NVIDIA/AMD/Intel/macOS(MLX)/Vulkan/多 GPU。GGUF/NVFP4/FP8 导出，Data Recipes 从 PDF/CSV/DOCX 构建数据集，7,374 commits 社区活跃。
- **归档**：`开源项目介绍/2026.8.29/unsloth.md`
- **标签**：`#微调` `#llm` `#本地部署` `#桌面应用`

<a id="sec-12"></a>

## ⚡ 十二、本地推理引擎与优化（15）

### [antirez/ds4](https://github.com/antirez/ds4)
- **定位**：antirez 出品：DeepSeek 4 Flash 与 PRO 的本地推理引擎（Metal/CUDA/ROCm）。
- **简介**：antirez 出品：DeepSeek 4 Flash 与 PRO 的本地推理引擎（Metal/CUDA/ROCm）。（GitHub 每日趋势 2026-10-05：★23339，当日 +211）
- **归档**：`开源项目介绍/2026.10.5/ds4.md`
- **标签**：`#c`

### [ashhart/TensorFold](https://github.com/ashhart/TensorFold)
- **定位**：Apple Silicon（MLX）上的快速精确 LLM 解码引擎，对外提供 OpenAI 兼容接口。
- **简介**：Apple Silicon（MLX）上的快速精确 LLM 解码引擎，对外提供 OpenAI 兼容接口。（GitHub 每日趋势 2026-09-29：★547，当日 +160）
- **归档**：`开源项目介绍/2026.9.29/TensorFold.md`
- **标签**：`#python`

### [cactus-compute/needle](https://github.com/cactus-compute/needle)
- **定位**：45M 参数超小型工具调用模型 · 14MB 单文件运行
- **简介**：边缘设备专用的工具调用/结构化提取模型（Apache-2.0），仅 45M 参数、14MB 单二进制文件，完整会话 ~28MB RAM。基于 Simple Attention Network 架构（Hadamard MLP + GQA + Engram KV 记忆 + 多通道超连接），CQ2-bit 量化（Cactus Quants）。核心特性：字节级语法约束输出（JSON 保证合法）、置信度门控、内置工具检索头（大目录自动选 top5）、256 token 滑动窗口 + KV sink 内存恒定。支持 LoRA 微调（JAX 训练，CUDA/Metal GPU 加速），微调后仍为单 .cact 文件。基准测试中与 FunctionGemma 270M 等模型互有胜负，但体积小 5-70 倍。含 6 个预置环境（智能家居、媒体播放器、可穿戴等）和 Playground Web UI。
- **归档**：`开源项目介绍/2026.8.29/needle.md`
- **标签**：`#小模型` `#工具调用` `#边缘计算` `#结构化提取`

### [deepseek-ai/DeepGEMM](https://github.com/deepseek-ai/DeepGEMM)
- **定位**：DeepSeek 出品：干净高效的 GPU BLAS 内核库（FP8 GEMM）。
- **简介**：DeepSeek 出品：干净高效的 GPU BLAS 内核库（FP8 GEMM）。（GitHub 每日趋势 2026-10-07：★8633，当日 +363）
- **归档**：`开源项目介绍/2026.10.8/DeepGEMM.md`
- **标签**：`#cuda`

### [FlashML-org/FreeToken](https://github.com/FlashML-org/FreeToken)
- **定位**：边缘原生 MoE 推理引擎 · 让 290B+ 前沿开源大模型跑在游戏 PC 上
- **简介**：把「数据中心级 MoE 服务」搬到桌面的推理引擎。它解决的核心矛盾是：**前沿模型越来越大，本地只有一张 24GB 消费卡**。答案不是砍模型，而是把 **GPU、CPU、主机内存、互连带宽当成统一弹性资源池**来调度。技术上最硬的三件事：① 论文提出的 **q⋆ 带宽自适应 CPU–GPU 协同执行策略**，配合**全层双缓冲 prefill 流式加载**和**全局 LRU 专家缓存**，把 PCIe 瓶颈藏起来；② 自研 **FTW 快速权重格式**；③ 运行时可在**专家缓存与 KV 内存之间动态重分配显存**，无需重启引擎、无需重载权重。**真正面向 Agent 时代的差异化设计是「语义感知缓存」**：为 recurrent state 与 KV cache 打**语义锚点检查点**，Agent 插入工具调用或思考块这类局部上下文编辑时**不必重算整段前缀**——这对 Codex、Claude Code 这类高频改上下文的编码 Agent 是实打实的延迟收益。模型侧支持 DeepSeek-V4-Flash、Qwen3.6-35B-A3B、GLM-5.2，覆盖 **MXFP4/NVFP4/FP8/BF16** 量化，原生支持 RTX 30/40/50 系，对外暴露 **Anthropic 与 OpenAI 双兼容 API**。**学术背书扎实**：arXiv 2608.16157 作者含 UC Berkeley 的 Keutzer 与 Stoica、MIT 的 Song Han、Databricks 的 Matei Zaharia；代码血缘继承 SGLang、vLLM、FlashInfer、llama.cpp。安装 `uv pip install "freetoken[accel]"`，另有 Windows/Linux 桌面 App。Apache-2.0，Python，**13,607 stars** / 1,337 forks / **335 open issues**，2026-07 建仓——**issue 密度说明是真有人在用，而非展示型项目**。可与库里的 lyogavin/airllm（层流式加载）对照：两者都在解「小显存跑大模型」，airllm 走通用分层，FreeToken 专攻 MoE + Agent 缓存语义。
- **归档**：`开源项目介绍/2026.9.23/FreeToken.md`
- **标签**：`#moe` `#推理引擎` `#本地大模型` `#kv-cache` `#边缘ai`

### [ggml-org/Llama-Windows](https://github.com/ggml-org/Llama-Windows)
- **定位**：Windows 桌面 Llama 应用伴侣（ggml 官方）。
- **简介**：Windows 桌面 Llama 应用伴侣（ggml 官方）。（GitHub 每日趋势 2026-10-08：★54，当日 +7）
- **归档**：`开源项目介绍/2026.10.8/Llama-Windows.md`
- **标签**：`#csharp`

### [huggingface/transformers](https://github.com/huggingface/transformers)
- **定位**：🤗 Transformers：最先进的机器学习模型定义框架，覆盖文本、视觉、音频与多模态（★167K）。
- **简介**：🤗 Transformers：最先进的机器学习模型定义框架，覆盖文本、视觉、音频与多模态（★167K）。（GitHub 每日趋势 2026-10-11：★167096，当日 +94）
- **归档**：`开源项目介绍/2026.10.11/transformers.md`
- **标签**：`#python`

### [lyogavin/airllm](https://github.com/lyogavin/airllm)
- **定位**：层流式大模型推理 · 单卡 4GB 跑 70B、8GB 跑 405B
- **简介**：内存优化推理框架（Apache-2.0），通过分层加载（layer-wise streaming）技术——一次只加载一层到 GPU，计算完卸载再加载下一层——实现极低显存运行超大规模模型，无需量化/蒸馏/剪枝。支持 MoE 模型逐专家流式加载：Kimi K3 (2.8T) 仅需 3.72GB、DeepSeek-V3 (671B) 约 12GB、Llama 3.1 405B 需 8GB、Qwen3-235B 约 3GB。可选 4bit/8bit 分块量化加速（最高 3x 提速，精度损失极小）。统一 AutoModel 接口自动识别模型架构，支持 Llama/DeepSeek/Qwen/Mistral/ChatGLM/Baichuan/InternLM/Phi/Gemma 等几乎所有主流模型。支持 CUDA/Linux、Apple Silicon macOS（MLX）、CPU 推理。含预取优化重叠加载与计算。
- **归档**：`开源项目介绍/2026.8.29/airllm.md`
- **标签**：`#推理优化` `#llm` `#低显存` `#moe`

### [magnitudedev/magnitude](https://github.com/magnitudedev/magnitude)
- **定位**：先测你的机器，再告诉你该跑什么模型的本地推理引擎
- **简介**：官方 FAQ 一句话讲清与 Ollama / LM Studio 的区别：「**它们负责跑你选的模型，Magnitude 负责帮你选。**」差异化洞察在于产品重心不是「推理更快」，而是**决策前置**——本地推理最大的隐性成本是**试错**：拉了 20GB 才发现只有 3 tok/s。Magnitude 先 **profile 硬件**，对目录中每个模型和每种量化**预估 tok/s**，按 **speed / accuracy / intelligence / memory 四维**排序，推荐偏好分 **fastest / faster / balanced / smarter / smartest 五档**；选定后再针对具体硬件从**上下文长度到 speculative decoding 端到端调优**。形态是 macOS/Windows/Linux 原生桌面应用，内置 `magnitude` CLI（无需 npm 安装），配置在 `~/.magnitude/config.json`。**CLI 命令体系完整分五组**：`hardware` 与 `catalog status/list/show/recommendations/pull/cancel/remove`（发现下载）· `models status/load/stop`（加载态）· `connections list/add/sync/remove`（**Agent 接入，支持 8 种 harness**：pi、opencode、hermes、openclaw、codex、claude-code、oh-my-pi、cline；`add` 可带 `--set-model` 与 `--install-skill`，Pi 的 Skill 自动安装）· `app open` 与 `service start/status/stop/install/uninstall`（后台常驻，uninstall 只关自启不删应用与模型）· `update check/status/download/install/discard`（桌面、内置服务与 CLI 一起升级）。硬件覆盖 **Apple Silicon、NVIDIA、AMD、纯 CPU**，并明确支持 **DGX Spark、Strix Halo** 这类统一内存设备。模型按需加载、**空闲或内存吃紧时自动卸载**，完全离线私有、无 token 费用无 API Key 无限流。Apache-2.0，TypeScript，**4,847 stars** / 369 forks / **仅 22 open issues**，2026-06 建仓，Discussions + Wiki + Discord + X @usemagnitude 齐备。**三个月近 5,000 star 配 22 个 open issue，维护极紧凑**——「帮你选模型」需要真实硬件 profile 数据积累，慢是正常的。
- **归档**：`开源项目介绍/2026.9.23/magnitude.md`
- **标签**：`#本地大模型` `#推理引擎` `#桌面应用` `#模型选型` `#ollama替代`

### [NVIDIA/Model-Optimizer](https://github.com/NVIDIA/Model-Optimizer)
- **定位**：NVIDIA 官方模型压缩库：量化、剪枝、蒸馏、投机解码加速推理
- **简介**：**NVIDIA Model Optimizer**（ModelOpt，Apache-2.0，Python）是 NVIDIA 官方的 SOTA 模型压缩与推理加速统一库，2025-01-28 开源，2025-12-08 由 TensorRT Model Optimizer 更名而来。覆盖六大技术：**后训练量化 PTQ**（NVFP4/FP8/INT8 等，模型压缩 2x–4x，支持 HF LLM/VLM、Megatron-Bridge、Diffusers、ONNX、Windows 路径）、**QAT/量化感知蒸馏 QAD**（如 Qwen3.6-35B W4A4 NVFP4+QAD 端到端教程：vLLM 吞吐较 BF16 提升 1.30x、检查点缩小 3.1x 并恢复精度）、**剪枝**（Minitron 与 Puzzletron 异构剪枝/NAS，客户案例 Domyn 355B→260B、Bielik 缩小 33% 提速 50% 保留 90% 质量）、**知识蒸馏**、**投机解码**（Medusa，Llama 3.1 最高 1.9x）、**稀疏化**。输入 Hugging Face/PyTorch/ONNX 模型，经统一 HF 导出 API（transformers+diffusers）产出检查点，直接部署到 **TensorRT-LLM、TensorRT、vLLM、SGLang**；与 Megatron-Bridge、Megatron-LM、HF Accelerate 深度集成（QAD 支持 FSDP2 多卡）。官方背书极强：Nemotron 3 Ultra 550B NVFP4（解码吞吐较 GLM-5.1 754B FP4 高至 5.9x）、Nemotron-3-Super FP8/NVFP4、DeepSeek-R1 FP4、Llama-3.1 405B FP4 等 Hugging Face 官方预量化检查点均出自该库，曾助 TensorRT-LLM 创 MLPerf 纪录，Adobe 用其降低扩散模型延迟 60%、TCO 40%。0.47.0 版新增 ONNX Autotune 量化、nvfp4_act_headroom 激活校准算法、Local-Hessian 权重尺度、AutoQuantize 自动混合精度、Kimi-K3 2.8T 免校准流式 NVFP4 转换器等；还提供 Claude Code/Codex 的 Agent 插件技能。安装：pip install -U nvidia-modelopt[all] 或 NVCR 容器预装。规模：**4,024 stars / 628 forks / 1,285 commits / 56 tags / 约 97 位贡献者**（抓取时 GitHub API 触发限流，commits 与贡献者数以 git 本地统计补齐），创建于 2024-04-23，最新 0.47.0（2026-09-23），最近推送 2026-09-24。注意：仍处 pre-1.0，小版本可能含破坏性变更，废弃特性仅 1 个发布（约 1 个月）迁移期；部分量化 Vision Encoder 导出要求推理运行时配套支持；仓库未设置 topics。
- **关联**：库内 [unslothai/unsloth](https://github.com/unslothai/unsloth)、[lyogavin/airllm](https://github.com/lyogavin/airllm)（微调与推理省显存的另两条路线）
- **归档**：`开源项目介绍/2026.9.25/modeloptimizer.md`
- **标签**：`#quantization` `#nvfp4` `#inference` `#pruning` `#pytorch`

### [raullenchai/Rapid-MLX](https://github.com/raullenchai/Rapid-MLX)
- **定位**：Rapid-MLX：基于 MLX 的 Apple Silicon LLM 推理服务器，兼容 OpenAI/Anthrop
- **简介**：Rapid-MLX：基于 MLX 的 Apple Silicon LLM 推理服务器，兼容 OpenAI/Anthropic API。（GitHub 每日趋势 2026-10-07：★3914，当日 +16）
- **归档**：`开源项目介绍/2026.10.8/Rapid-MLX.md`
- **标签**：`#python`

### [SemiAnalysisAI/InferenceX](https://github.com/SemiAnalysisAI/InferenceX)
- **定位**：开源推理研究平台标准。
- **简介**：开源推理研究平台标准。（GitHub 每日趋势 2026-09-30：★1785，当日 +8）
- **归档**：`开源项目介绍/2026.9.30/InferenceX.md`
- **标签**：`#python`

### [sgl-project/sglang](https://github.com/sgl-project/sglang)
- **定位**：SGLang：面向大模型与多模态模型的高性能推理服务框架。
- **简介**：SGLang：面向大模型与多模态模型的高性能推理服务框架。（GitHub 每日趋势 2026-10-02：★36697，当日 +39）
- **归档**：`开源项目介绍/2026.10.2/sglang.md`
- **标签**：`#python`

### [tile-ai/tilelang](https://github.com/tile-ai/tilelang)
- **定位**：面向 GPU/CPU/加速器高性能算子开发的领域专用语言（DSL）。
- **简介**：面向 GPU/CPU/加速器高性能算子开发的领域专用语言（DSL）。（GitHub 每日趋势 2026-10-02：★8036，当日 +157）
- **归档**：`开源项目介绍/2026.10.2/tilelang.md`
- **标签**：`#python`

### [vllm-project/vllm](https://github.com/vllm-project/vllm)
- **定位**：vLLM：高吞吐、高内存效率的 LLM 推理与服务引擎。
- **简介**：vLLM：高吞吐、高内存效率的 LLM 推理与服务引擎。（GitHub 每日趋势 2026-10-08：★93336，当日 +73）
- **归档**：`开源项目介绍/2026.10.8/vllm.md`
- **标签**：`#python`

<a id="sec-13"></a>

## 🎨 十三、图像 / 视频 / 音乐生成（7）

### [Friedrich-M/UniMate](https://github.com/Friedrich-M/UniMate)
- **定位**：SIGGRAPH Asia 2026 论文：一个统一模型驱动多种骨架动画。
- **简介**：SIGGRAPH Asia 2026 论文：一个统一模型驱动多种骨架动画。（GitHub 每日趋势 2026-10-02：★1010，当日 +225）
- **归档**：`开源项目介绍/2026.10.2/UniMate.md`
- **标签**：`#python`

### [leejet/stable-diffusion.cpp](https://github.com/leejet/stable-diffusion.cpp)
- **定位**：基于 ggml 的纯 C/C++ 扩散模型本地推理引擎，图像视频生成界的 llama.cpp
- **简介**：**stable-diffusion.cpp** 是 leejet 开发的**纯 C/C++ 扩散模型推理引擎**，MIT 协议，基于 ggml 张量库、与 llama.cpp 同一技术路线，超轻量且无外部依赖，创建于 2023-08-13，运行于 Linux、macOS、Windows 与 Android（Termux）。**核心能力**：覆盖图像生成（SD1.x/2.x/Turbo、SDXL、SD3/3.5、FLUX.1-dev/schnell、FLUX.2-dev/klein、Qwen Image 及 2.1、Z-Image、Chroma、Lens、Krea2、Ideogram4、LLaDA-Image、HiDream-O1、SenseNova U1.5 等）、图像编辑（FLUX.1-Kontext、Qwen Image Edit 系列）与视频生成（Wan2.1/2.2 含 Vace、MiniMax-H3、LTX-2.3/2.5、HunyuanVideo 1.5、LingBot-Video），生态特性齐备：LoRA（webui 语法）、ControlNet、IP-Adapter、PhotoMaker、ADetailer、LCM/LCM-LoRA、TAESD 低内存解码、ESRGAN 超分、Flash Attention、VAE tiling、GGUF 量化与 INT8 convrot、缓存加速，采样器含 Euler A/Heun/DPM++ 2M v2/ER-SDE/LCM 等。**差异化**：一是**新模型 Day-0/Day-1 支持**（2026-09-20 即支持 Qwen-Image-2.1、08-04 支持 MiniMax-H3）；二是**多后端**——CPU（AVX/AVX2/AVX512）、CUDA、Vulkan、Metal、OpenCL、SYCL，支持 RPC 与后端分区放置；三是直接读取 .ckpt/.safetensors/.gguf 三种权重并可互相转换量化；四是可复现 RNG（cuda 对齐 webui、cpu 对齐 ComfyUI）与 PNG 内嵌 webui 兼容生成参数；五是 2026-04 起内置全新嵌入式 Web UI，同时保留 sd-cli 一条命令出图。**下游生态**：LocalAI、KoboldCpp、GIMP 插件、Jellybox、sd.cpp-webui 等以其为后端，并有 Python、Go（3 个绑定）、C#、Rust、Flutter/Dart 语言封装。**规模数据**：约 7,216 Stars、811 Forks、269 开放 Issues、约 913 commits、109 位贡献者、694 个 tags，最近推送 2026-09-24，发布采用滚动 master 快照（最新 master-910-4dfe8f5）。**注意事项**：项目明确声明处于活跃开发期，**API 与命令行参数可能频繁变动**，无语义化版本号，升级集成需锁定 commit 并关注 CHANGELOG；未设官网，文档均在仓库 docs/ 目录。
- **关联**：库内 [mcmonkeyprojects/SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI)（上层 WebUI，可把此类引擎当后端）
- **归档**：`开源项目介绍/2026.9.25/stable-diffusion-cpp.md`
- **标签**：`#diffusion` `#ggml` `#cpp` `#图像生成` `#video-generation` `#quantization`

### [mcmonkeyprojects/SwarmUI](https://github.com/mcmonkeyprojects/SwarmUI)
- **定位**：模块化 AI 图像/视频生成 WebUI（前身 StableSwarmUI）
- **简介**：v0.9.8 Beta。模块化的 AI 生成 Web 界面，重点在**让强力工具变得易上手 + 高性能 + 可扩展**。支持面已远超图像：**AI 图像**（Krea 2、Stable Diffusion、Flux）、**AI 视频**（MiniMax H3、Wan、LTX-2）、**AI 音频**（ACE-Step），新模型公开发布后持续加入。双界面策略很聪明——新手用主 Generate 标签页轻松出图，进阶用户切到 **Comfy Workflow** 标签页拿无限制的原始节点图，但仍会为了便利特性（图像编辑器、自动工作流生成）和强力工具（Grid Generator）回到 Generate 页。官方定性为 **Almost-Release**：绝大多数任务的工具链已完备，只剩少数几处想再打磨；尚未实现的关键目标是原生 LLM 辅助提示词（目前有扩展）。**永远 100% 免费开源**，作者明确拒绝付费墙和塞广告，靠 Patreon 捐赠维持。部署方式齐全：Google Colab（⚠️ 免费账号不一定允许远程 WebUI）、Runpod / Vast.ai 云 GPU 模板、Windows（`install-windows.bat`，别放 `Program Files`；Win10 需手装 git + .NET 8 SDK，Win11 全自动；有时要跑两遍）、Linux（一键 `install-linux.sh`，Python 必须 3.11/3.12，**不要用 3.14+**）、macOS。无头服务器可 `--launch_mode none --host 0.0.0.0` 或走 cloudflared。技术栈 C#/.NET 8（将迁 .NET 10）+ JS 前端 + ComfyUI（Python）推理后端，默认端口 7801。MIT，4,589 stars / 458 forks，2024-06 创建，2026-09-22 仍在推送。
- **归档**：`开源项目介绍/2026.9.23/SwarmUI.md`
- **标签**：`#aigc` `#stable-diffusion` `#comfyui` `#文生视频` `#webui` `#本地部署`

### [meituan-longcat/LongCat-Video](https://github.com/meituan-longcat/LongCat-Video)
- **定位**：美团 LongCat 视频生成模型。
- **简介**：美团 LongCat 视频生成模型。（GitHub 每日趋势 2026-10-03：★8654，当日 +43）
- **归档**：`开源项目介绍/2026.10.4/LongCat-Video.md`
- **标签**：`#python`

### [microsoft/TRELLIS.2](https://github.com/microsoft/TRELLIS.2)
- **定位**：微软 TRELLIS 2：原生紧凑结构化潜码 3D 生成。
- **简介**：微软 TRELLIS 2：原生紧凑结构化潜码 3D 生成。（GitHub 每日趋势 2026-10-11：★11747，当日 +207）
- **归档**：`开源项目介绍/2026.10.11/TRELLIS.2.md`
- **标签**：`#python`

### [multimodal-art-projection/YuE](https://github.com/multimodal-art-projection/YuE)
- **定位**：YuE2 前沿音乐生成模型 · 符号规划 + 零样本翻唱 + Agent 化编辑
- **简介**：**「Compose in symbols. Create in sound.」**（用符号作曲，用声音创作。）YuE2 把前沿级歌曲质量带给音乐生成，同时给出**一份可编辑的乐谱**——给它歌词和风格提示，它先写出一份**旋律与和声计划**，再把计划实现为带人声与伴奏的完整歌曲。三大能力：① **前沿质量**——在 WildSongBench（192 条 prompt）上与 **Suno v5/v6 具竞争力**，YuE2 (best-of-8) 取得 **6.9632 SongBench Avg**，是所有被评估设置中观测到的最高均值；② **通过符号规划实现白盒生成**——渲染之前就能**读、弹、改**这份作品，旋律与和声成为显式控制项，人或 agent 都能检查并编辑；③ **零样本翻唱 + Agent 化编辑**——把转写下来的歌用新风格重新演绎，或通过一场关于乐谱/编曲/歌词的**对话**打磨歌曲，**全部用同一个生成 checkpoint**。三种创作模式：Create（歌词+风格→乐谱→完整歌曲）、Cover（源录音→旋律乐谱→全新演绎）、Edit with an agent（音乐反馈→乐谱/风格/歌词修订→新录音）；官方 agent 演示跟着《The Last Train》走了 **9 个步骤、14 个版本**，从华语流行到英语爵士配新和声与萨克斯独奏，每版都能试听并检查其对话/乐谱/prompt/歌词。**架构**：一个 **AR–NAR Mixture-of-Transformers** 主干自回归预测乐谱与语义 token，再用 **flow matching** 生成声学潜变量，由 **VAE** 解码为立体声音频；三种模式的区别只在于**乐谱从哪来**。分阶段 Python API：`plan() → generate_semantic() → synthesize() → decode()`。配套开源资产齐全：[YuE2-3B](https://huggingface.co/m-a-p/YuE2-3B) 主模型、MERT-v2-FullSong（音乐表征）、SheetSage2（乐谱）、WildSongBench（评测集）、公开盲听 [Music Arena](https://arena.3-148-255-99.sslip.io:8080)（与领先专有系统 A/B 对比，无需账号）。README 设有 **Agent skill** 章节，配合白盒符号规划可让 Agent 通过对话迭代改谱。参与机构：HKUST · M·A·P · Tokenwave.AI · NYU · Stanford · MBZUAI · NOIZ · ACE Studio。免费在线试用 [yue.noizai.net](https://yue.noizai.net/)（NOIZ 托管，无需安装）。原 YuE v1 保留在 `YuE-v1` 分支。Python，Apache-2.0，10,072 stars / 1,145 forks；榜单成绩亮眼：Trendshift GitHub Trending **#1 Repository of the Day**（2026-09-14 全语言）、HF 全球模型 Trending **#3**（09-17）、HF Text-to-Audio Trending **#1**（09-20）。
- **归档**：`开源项目介绍/2026.9.23/YuE.md`
- **标签**：`#音乐生成` `#符号规划` `#白盒` `#翻唱` `#apache2` `#huggingface`

### [storytold/artcraft](https://github.com/storytold/artcraft)
- **定位**：面向艺术家、设计师和电影人的有意图创作引擎。
- **简介**：面向艺术家、设计师和电影人的有意图创作引擎。（GitHub 每日趋势 2026-10-09：★7038，当日 +2510）
- **归档**：`开源项目介绍/2026.10.9/artcraft.md`
- **标签**：`#rust`

<a id="sec-14"></a>

## 🏗️ 十四、AI 基础设施 · 网关与自托管平台（25）

### [2dust/v2rayN](https://github.com/2dust/v2rayN)
- **定位**：跨平台代理 GUI 客户端（Windows/Linux/macOS），支持 Xray、sing-box 等内核。
- **简介**：跨平台代理 GUI 客户端（Windows/Linux/macOS），支持 Xray、sing-box 等内核。（GitHub 每日趋势 2026-09-26：★116982，当日 +123）
- **归档**：`开源项目介绍/2026.9.28/v2rayN.md`
- **标签**：`#csharp`

### [Alishahryar1/free-claude-code](https://github.com/Alishahryar1/free-claude-code)
- **定位**：多模型编码 Agent 网关 · 用 50 家提供商驱动 9 种编码 Agent
- **简介**：独立开源项目（MIT 协议），作为本地代理运行，统一接入 50 家 ToS 友好的 AI 提供商（每月 13 亿+ 免费 tokens），驱动 9 种编码 Agent：Claude Code、Codex、Pi、OpenCode、Cline、Hermes、DeepSeek Harness、Grok Build、Muse Code。核心能力：提供商故障自动转移（失败后自动试下一个模型）、终端输出 token 减少 90%（RTK 过滤 + 五项内置优化）、多端支持（终端/桌面/VS Code/JetBrains/Discord/Telegram）、语音输入（本地 Whisper / NVIDIA NIM 转录）、模型层级路由（Fable/Opus/Sonnet/Haiku 独立分配模型）、推理级别控制。支持本地模型（Ollama / LM Studio / llama.cpp）。含 Web Admin UI 统一管理提供商和模型配置。
- **归档**：`开源项目介绍/2026.8.29/free-claude-code.md`
- **标签**：`#网关` `#多模型` `#编码agent` `#本地代理`

### [arc53/DocsGPT](https://github.com/arc53/DocsGPT)
- **定位**：私有 AI 平台：Agent、助手与企业搜索，内置 Agent 构建器、深度研究与文档分析。
- **简介**：私有 AI 平台：Agent、助手与企业搜索，内置 Agent 构建器、深度研究与文档分析。（GitHub 每日趋势 2026-10-03：★18304，当日 +6）
- **归档**：`开源项目介绍/2026.10.4/DocsGPT.md`
- **标签**：`#python`

### [BerriAI/litellm](https://github.com/BerriAI/litellm)
- **定位**：LiteLLM：最快的 AI 网关。Rust 内核＋Python SDK，用 OpenAI 格式调 100+ LLM A
- **简介**：LiteLLM：最快的 AI 网关。Rust 内核＋Python SDK，用 OpenAI 格式调 100+ LLM API，带成本追踪与限流。（GitHub 每日趋势 2026-10-10：★60547，当日 +95）
- **归档**：`开源项目介绍/2026.10.10/litellm.md`
- **标签**：`#python`

### [block/buzz](https://github.com/block/buzz)
- **定位**：Rust 编写的「蜂群心智」通信平台，为多智能体与多人间的高频协同通信而生。
- **简介**：Rust 编写的「蜂群心智」通信平台，为多智能体与多人间的高频协同通信而生。（GitHub 每日趋势 2026-09-26：★34752，当日 +175）
- **归档**：`开源项目介绍/2026.9.27/buzz.md`
- **标签**：`#rust`

### [citrolabs/ego-lite](https://github.com/citrolabs/ego-lite)
- **定位**：专为 AI Agent 设计的并行浏览器 · 你和 Agent 共享同一浏览器
- **简介**：从内核级定制的 Chromium 浏览器（MIT 协议），让用户和 AI Agent 并行工作互不干扰。每个 Agent 拥有独立的「Space」隔离工作区，支持多 Space 并行任务（如同时抓取 10 个网站）。与传统浏览器自动化框架不同，ego lite 基于代码而非 CLI——Agent 将多步操作写成 JavaScript 片段一次性执行，复杂任务速度快 2.5 倍、token 消耗大幅减少。通过 `ego-browser` skill 暴露页内工具（snapshot、fill、click、wait、navigate、capture），支持 Claude Code、Codex、Cursor 等多种 Agent。可迁移 Chrome 数据（登录态/Cookie/扩展/书签），Agent 继承用户真实登录状态。页面 Snapshot 质量业界领先，可靠处理深层嵌套 iframe。macOS 可用，Windows/Linux 在路线图中。
- **归档**：`开源项目介绍/2026.8.29/ego-lite.md`
- **标签**：`#浏览器` `#agent` `#并行` `#自动化`

### [danny-avila/LibreChat](https://github.com/danny-avila/LibreChat)
- **定位**：增强版 ChatGPT 克隆 · 自托管多模型 AI 平台
- **简介**：老牌开源项目（2023-02 创建），为自托管而生的多模型聊天平台，与库里的 open-webui 属同类竞品。提供商覆盖面极广：Anthropic (Claude) · AWS Bedrock · OpenAI · Azure OpenAI · Google · Vertex AI · OpenAI Responses API（含 Azure），加**自定义端点**（任何 OpenAI 兼容 API 直接用、**无需代理**），以及 Ollama / AMD Lemonade / groq / Cohere / Mistral / Apple MLX / koboldcpp / together.ai / OpenRouter / Helicone / Perplexity / ShuttleAI / Deepseek / Qwen 等本地与远程提供商。**Code Interpreter API** 提供安全沙箱执行，支持 Python / Node.js (JS/TS) / Go / C/C++ / Java / PHP / Rust / Fortran 八种语言，可直接上传处理下载文件，由 ClickHouse/code-interpreter 驱动。**Agents 体系**已相当完整：无代码自定义助手、Agent Marketplace（发现并部署社区 agent）、按用户/组协作共享、MCP 服务器与工具集成、**Skills**（可复用的 `SKILL.md` 指令包，支持手动/自动/常驻三种触发）、**Agent Plugins**（实验性地把 Skills 与 MCP 服务器打包成启动时加载的包）、**Subagents**（委派给拥有**独立上下文窗口**的隔离子 agent）。v0.8.8-rc3 的重点全在工程化与治理：**Agent Management API**（beta，增删改查 Agent + 管理 Agent 文件与 Skills + 通过**部署绑定的 OIDC 身份**认证机器客户端）、**Attached workspaces**（高度实验，per-Agent 默认工作空间，Agent 可检查目录树/读写文件/在**有界超时**下跑 Bash，个人 worker 支持自助注册与 per-Agent Git 身份）、**Code approval controls**（文件写入与命令执行可选 Ask/Allow/Deny，含面向可信环境的 Full access 模式）、**Background tool controls**（可取消普通后台工具但保持 detached Subagent 独立）、**Manual context compaction**（上下文填满前主动发起「仅摘要」轮次）、**Context Usage**（检查对话/工具流量/Agent 指令/缓存/成本/runway 压力且**不重复计算类别子集**）、**Unified attachments**（上传一次由系统决定路由给模型还是抽取文本，**仅在需要时**才配置 File Search 与 Code 工具）、新增 **GPT-6 Astra**、**Observability**（OpenTelemetry 关联日志导出、Langfuse trace 白名单、客户端构建 ID 标记诊断、Insights 按授权 Agent 限定）、可靠性与安全性强化（Agent 续跑与检查点恢复、Redis 存活检测、DocumentDB 协调、OpenID 与 MCP OAuth 会话、共享链接限流、**租户隔离**、附件边界）。一键部署模板齐全：Railway / Zeabur / Sealos；翻译走 locize，有中文 README。TypeScript，MIT，**44,672 stars** / 9,171 forks / 780 open issues，官网 [librechat.ai](https://librechat.ai/)，2026-09-22 仍在高频推送。
- **归档**：`开源项目介绍/2026.9.23/LibreChat.md`
- **标签**：`#self-hosted` `#多模型` `#mcp` `#agent` `#代码解释器` `#chatgpt替代`

### [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute)
- **定位**：多 AI 提供商统一路由网关 · 编码 Agent 免费接入基础设施
- **简介**：通过单一 OpenAI 兼容端点接入 **341 家 AI 提供商、1,202 个模型**，聚合约 **15.1 亿/月免费 tokens**（90+ 免费层级）。19 种路由策略，四层自动降级（订阅→API→廉价→免费），熔断+密钥冷却+模型锁定三层弹性。RTK + Caveman 双层压缩节省 15%–95% token（工具密集会话平均 ~89%）。内置 MCP Server（109 工具）、A2A 协议、记忆系统、护栏、Vision 模态桥。兼容 33+ 编码 Agent，零配置安装即用（预装免费后端开箱即跑）。Electron 桌面应用 + Docker/Nix 部署，实时分析仪表盘。MIT 协议，7,062 commits、v3.8.50，500+ 贡献者，43 种语言。
- **归档**：`开源项目介绍/2026.9.6/OmniRoute.md`
- **标签**：`#网关` `#多模型` `#免费tokens` `#token压缩` `#mcp`

### [DuarteSantos8/openGym](https://github.com/DuarteSantos8/openGym)
- **定位**：自托管健身与体重追踪：规划例程、记录训练（超级组/热身/有氧）、查看肌群训练情况。
- **简介**：自托管健身与体重追踪：规划例程、记录训练（超级组/热身/有氧）、查看肌群训练情况。（GitHub 每日趋势 2026-10-06：★4537，当日 +1433）
- **归档**：`开源项目介绍/2026.10.8/openGym.md`
- **标签**：`#javascript`

### [experientiallabs/experiential](https://github.com/experientiallabs/experiential)
- **定位**：开源零标记网关：支持 BYOK、自托管与 1000+ 市场模型，从你的流量中学习。
- **简介**：开源零标记网关：支持 BYOK、自托管与 1000+ 市场模型，从你的流量中学习。（GitHub 每日趋势 2026-10-05：★8846，当日 +570）
- **归档**：`开源项目介绍/2026.10.5/experiential.md`
- **标签**：`#python`

### [getsentry/sentry](https://github.com/getsentry/sentry)
- **定位**：开发者优先的错误追踪与性能监控平台。
- **简介**：开发者优先的错误追踪与性能监控平台。（GitHub 每日趋势 2026-10-03：★44973，当日 +12）
- **归档**：`开源项目介绍/2026.10.3/sentry.md`
- **标签**：`#python`

### [LibreTranslate/LibreTranslate](https://github.com/LibreTranslate/LibreTranslate)
- **定位**：免费开源的机器翻译 API，自托管、可离线、部署简单。
- **简介**：免费开源的机器翻译 API，自托管、可离线、部署简单。（GitHub 每日趋势 2026-10-01：★16954，当日 +49）
- **归档**：`开源项目介绍/2026.10.1/LibreTranslate.md`
- **标签**：`#python`

### [likeadmin/likeadmin-aigc](https://gitee.com/likeadmin/likeadmin-aigc)
- **定位**：多租户 AIGC SaaS 平台 · AI 应用生产与商业化底座
- **简介**：面向 AI 时代的应用生产基础设施，把**模型能力、应用市场、租户运营、点数计费、内容生成和持续更新**整合到同一套系统。不是普通后台，而是可部署、可更新、可运营的 AI 商业底座——上游连接模型与算力，下游连接客户/场景/权益/收入，中间沉淀可复用的应用、数据、权限、账单和运营能力。核心能力：多租户 SaaS 架构（平台/租户/用户多角色协作）、内置图片/视频/**数字人**/智能画布/LLM 等 AIGC 应用、应用中心（启停 + 租户授权 + 菜单权限 + 前端入口管理）、点数计费与会员套餐充值消耗闭环、五端交付（平台后台 + 租户后台 + PC + H5 + 微信小程序）、云端系统更新（私有更新源 + 版本签名校验 + 长任务更新流程）、本地化部署便于企业掌控数据密钥与商业策略。技术栈 PHP 8+ / ThinkPHP / MySQL / Composer，Vue 前端编译产物已内置（源码预计 2.0 放出）。**Docker Compose 一键部署**：镜像内含全部编译资源，不需要前端源码仓库也不需装 Node.js；8 个容器分工（web/app/mysql/redis/ai-worker/canvas-worker/scheduler/initialize），PHP 镜像自带扩展、Composer 生产依赖和 FFmpeg。适用场景：AIGC 聚合平台、企业私有 AI 门户、行业模型应用市场、数字人生产平台、AI 内容商业化系统、会员制智能工具站，以及政企/教育/电商/传媒/本地生活的专属智能服务平台。Apache-2.0（允许商用，需保留版权 logo），579 commits，16 分支，最新版 1.0.349，迭代非常活跃。
- **归档**：`开源项目介绍/2026.9.22/likeadmin-aigc.md`
- **标签**：`#saas` `#aigc` `#多租户` `#thinkphp` `#docker` `#gitee`

### [microsoft/semantic-kernel](https://github.com/microsoft/semantic-kernel)
- **定位**：微软的 LLM 应用集成框架（Semantic Kernel）：快速把大模型接入 .NET/Python 应用。
- **简介**：微软的 LLM 应用集成框架（Semantic Kernel）：快速把大模型接入 .NET/Python 应用。（GitHub 每日趋势 2026-09-26：★28603，当日 +8）
- **归档**：`开源项目介绍/2026.9.28/semantic-kernel.md`
- **标签**：`#csharp`

### [oblien/openship](https://github.com/oblien/openship)
- **定位**：自托管部署平台。
- **简介**：自托管部署平台。（GitHub 每日趋势 2026-09-30：★13699，当日 +436）
- **归档**：`开源项目介绍/2026.9.30/openship.md`
- **标签**：`#typescript`

### [open-webui/open-webui](https://github.com/open-webui/open-webui)
- **定位**：自托管 AI 平台 · 全功能 WebUI
- **简介**：「AI 的家」——可扩展、功能丰富、用户友好的自托管 AI 平台，支持**完全离线运行**。同时接入 Ollama 本地模型和任何 OpenAI 兼容 API，提供商无关的统一界面。完整生态：核心 WebUI + Computer 编码 Agent + 终端环境 + 知识库 RAG + 桌面应用。5 类插件系统（Filters/Actions/Pipes/Tools/Skills），MCP/MCPO/OpenAPI 工具连接，持久记忆，9 种向量数据库，多模型对话 + 模型竞技场，Channels 团队协作，语音/视频通话，图片生成，企业级认证与可观测性。MIT 协议。
- **归档**：`开源项目介绍/2026.9.16/open-webui.md`
- **标签**：`#self-hosted` `#webui` `#多模型` `#rag` `#mcp`

### [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach)
- **定位**：给 AI Agent 一键装上互联网能力（一个 CLI，零 API 费用）
- **简介**：中文 Agent 基础设施里增长最猛的项目之一。解决的痛点很具体：Agent 能写代码改文档管项目，但让它上网找东西就抓瞎——YouTube 拿不到字幕、Twitter API 要付费、Reddit **403 封服务器 IP**、小红书必须登录、B 站把通用下载工具**全面风控拦截**、搜索要么付费要么质量差、网页抓回来一堆 HTML 标签没法读、GitHub 认证配置麻烦、RSS 要自己装库写代码。**这些不难实现，但每个平台都有自己的门槛，光让 Agent 能读个推特就得折腾半天。** Agent Reach 把这件事变成一句话——安装：`帮我安装 Agent Reach：https://raw.githubusercontent.com/Panniantong/agent-reach/main/docs/install.md`（复制给 Agent 即可，几分钟装完）；更新同样一句话指向 `docs/update.md`。**四个关键承诺**：💰 **完全免费**（所有工具开源、所有 API 免费，唯一可能花钱的是服务器代理 $1/月，**本地电脑不需要**）· 🔒 **隐私安全**（Cookie 只存本地，不上传不外传，代码全开源可审查）· 🔄 **持续换代**（每个平台都是「**首选 + 备选**」多后端路由，某接入方式失效就换下一个、**用户无感**；2026-06 实例：yt-dlp 被 B 站风控封死 → 已切 bili-cli，用户零操作）· 🤖 **兼容所有 Agent**（Claude Code / OpenClaw / Cursor / Windsurf，任何能跑命令行的都行）。自带诊断：`agent-reach doctor` 一条命令告诉你哪个通、哪个不通、怎么修。**这个「多后端路由 + 上游主动维护」的设计是它与普通爬虫库的本质区别**——平台封了他们修，有新渠道他们加，你不用自己盯。支持平台：Twitter/X · Reddit · YouTube（字幕）· GitHub（含 Issue）· Bilibili · 小红书 · 通用网页（清洗为可读文本）· RSS 订阅 · Web 搜索。README 4 种语言（简中主 + 英/日/韩）。Python 3.10+，MIT，**84,790 stars** / 7,446 forks，2026-02 创建——七个月 8.5 万星，Trendshift **GitHub Trending #1 Repository of the Day**。
- **归档**：`开源项目介绍/2026.9.23/Agent-Reach.md`
- **标签**：`#agent基础设施` `#爬虫` `#免费api` `#cli` `#多后端路由` `#中文项目`

### [paperclipai/paperclip](https://github.com/paperclipai/paperclip)
- **定位**：开源的 AI 智能体团队编排控制平面，用开公司的方式管理多代理协作
- **简介**：**Paperclip** 是 Paperclip Labs, Inc 于 2026 年 3 月开源的 AI 智能体团队管理应用，MIT 协议，官网 paperclip.ing，主语言 TypeScript。官方定位一句话："如果 OpenClaw 是员工，Paperclip 就是公司"——它不是 Agent 框架、不是聊天机器人，而是多智能体的编排控制平面：Node.js 服务端 + React UI，本地自动内嵌 PostgreSQL 零配置，生产可外接自有 Postgres，要求 Node.js 24.11+、pnpm 9.15+，支持 install.sh（带 SHA-256 校验）安装或 npx paperclipai 免安装试用，另有 test-drive 隔离试跑模式。核心能力围绕"四大支柱"展开：**智能体任务管理器**（工单化任务、审批评审门、原子签出防重复劳动、从 diff/截图/测试验证产出）、**智能体组织架构图**（人+机混合的角色、汇报线、权限边界与 scoped secrets）、**智能体培训**（Skill Studio、evals 评测、绩效评估）、**Agentic OS**（跨提供商运行时、沙箱、MCP Tool Gateway、SSO/RBAC/GRC 与成本控制）。差异化亮点：心跳机制（数据库唤醒队列按计划驱动代理干活）、按公司/代理/项目/目标/模型多维度的 token 成本预算（达限自动暂停并取消排队任务）、单部署多组织完全数据隔离、整组织导出导入（含密钥脱敏）、插件系统、AgentMail 代理专属邮箱，以及 Slack/Discord/Telegram/Teams/iMessage 实验性聊天连接器（v2026.916.0 起）。规模数据：Stars 约 **87,221**、Forks 15,422、开放 issue 5,741、贡献者 **202**、commits 约 4,593、tags 1,643（日期版本号，迭代极快）。时间线：创建于 2026-03-02，最近推送 2026-09-26；最新版 v2026.916.1（2026-09-21），v2026.916.0（2026-09-16，含 503 commits，主打 Connections 凭证体系）。注意事项：匿名遥测**默认开启**，需 PAPERCLIP_TELEMETRY_DISABLED=1 或 DO_NOT_TRACK=1 关闭；官方明确面向同时管理多个代理的团队场景，单代理用户不需要它。社区：Discord、X @papercliping、awesome-paperclip 插件合集。
- **关联**：库内 [TencentCloud/Octop](https://github.com/TencentCloud/Octop)（同为自托管多 Agent 平台）、[obra/superpowers](https://github.com/obra/superpowers)
- **归档**：`开源项目介绍/2026.9.27/paperclip.md`
- **标签**：`#ai-agent` `#agent-orchestration` `#multi-agent` `#typescript` `#self-hosted`

### [PostHog/posthog](https://github.com/PostHog/posthog)
- **定位**：构建「自动驾驶产品」的一体化开发者平台：AI 可观测性、分析、会话回放、实验与日志，支持自托管。
- **简介**：构建「自动驾驶产品」的一体化开发者平台：AI 可观测性、分析、会话回放、实验与日志，支持自托管。（GitHub 每日趋势 2026-09-26：★39947，当日 +27）
- **归档**：`开源项目介绍/2026.9.27/posthog.md`
- **标签**：`#python`

### [Rizzo-AI-Academy/rizzo-pii](https://github.com/Rizzo-AI-Academy/rizzo-pii)
- **定位**：本地优先的隐私防护：文档交给 LLM 前先做 PII 匿名化脱敏。
- **简介**：本地优先的隐私防护：文档交给 LLM 前先做 PII 匿名化脱敏。（GitHub 每日趋势 2026-09-29：★1094，当日 +26）
- **归档**：`开源项目介绍/2026.9.29/rizzo-pii.md`
- **标签**：`#python`

### [s1t5/mail-archiver](https://github.com/s1t5/mail-archiver)
- **定位**：邮件归档 Web 应用：多账户归档、搜索与导出，支持文件夹同步。
- **简介**：邮件归档 Web 应用：多账户归档、搜索与导出，支持文件夹同步。（GitHub 每日趋势 2026-10-09：★2151，当日 +5）
- **归档**：`开源项目介绍/2026.10.9/mail-archiver.md`
- **标签**：`#csharp`

### [smartstore/Smartstore](https://github.com/smartstore/Smartstore)
- **定位**：基于 ASP.NET Core 10 的模块化、可扩展、超快开源全栈电商平台。
- **简介**：基于 ASP.NET Core 10 的模块化、可扩展、超快开源全栈电商平台。（GitHub 每日趋势 2026-09-29：★1689，当日 +65）
- **归档**：`开源项目介绍/2026.9.29/Smartstore.md`
- **标签**：`#csharp`

### [superdesigndev/treg](https://github.com/superdesigndev/treg)
- **定位**：「Agent 工具版的 OpenRouter」：统一路由调用各类 Agent 工具的网关。
- **简介**：「Agent 工具版的 OpenRouter」：统一路由调用各类 Agent 工具的网关。（GitHub 每日趋势 2026-09-26：★3327，当日 +359）
- **归档**：`开源项目介绍/2026.9.28/treg.md`
- **标签**：`#python`

### [Tencent/BrowserSkill](https://github.com/Tencent/BrowserSkill)
- **定位**：腾讯开源的 Agent 专用浏览器桥 · 复用你已登录的真实浏览器且不打断你的工作
- **简介**：架构为 **Agent → `bsk` CLI（shell）→ 本地 daemon（IPC）→ 浏览器扩展（127.0.0.1 WebSocket）→ 独立 Agent Window**，**Agent 从不直连浏览器**，形成天然安全边界。**三大差异化**：① **复用真实登录态**，免测试账号；② 任务在**可见的独立窗口**运行，**用户浏览器不受打扰**；③ **「借用-归还」标签页权限语义** + 内建 **human-in-the-loop**（`request-help` 处理验证码/登录），**0.3.0 起无人值守开关收归浏览器端设置——由被操作方而非 Agent 掌控权限**。**Agent 无关设计**：任何能调 shell 的 Agent（Cursor / Claude Code / Codex / OpenClaw / CodeBuddy）均可接入，`bsk install-skill` 一键装技能；另有 **DeepSeek Harness 原生插件**（`@wxg-prc-cpg/browser-skill-dsh-plugin`）与 `evals/browser` **确定性浏览器能力评测集**。支持 macOS/Linux/Windows x64、Chrome/Edge。**洞察**：走「扩展 + daemon」路线而非 CDP 直连，把**权限模型**和**可回归评测**做进 browser-use 赛道——与库里的 citrolabs/ego-lite（从内核定制 Chromium）形成两条鲜明技术路线：一个改浏览器，一个寄生在现有浏览器上。MIT，TypeScript + Rust（Cargo/pnpm monorepo），**6,020 stars** / 429 forks，2026-06-22 创建——**3 个月即破 6k star**。
- **归档**：`开源项目介绍/2026.9.23/BrowserSkill.md`
- **标签**：`#browser-use` `#agent基础设施` `#rust` `#浏览器扩展` `#human-in-the-loop` `#腾讯`

### [TencentCloud/Octop](https://github.com/TencentCloud/Octop)
- **定位**：腾讯云开源的自托管多用户多智能体 AI 助手平台 · 单进程集成 Web 控制台 + CLI + 五大 IM 渠道 + 定时任务
- **简介**：核心卖点是「**多用户 + 多 Agent + 数据全留本地**」：**JWT 多用户隔离**让一个管理员账号承载全家/全团队，内置**专家库与 16 种 MBTI 人格模板**，每个 Agent 拥有**独立工作区、模型配置与 cron**。**架构上基于自研 Harness 栈**（`harness-agent` 运行时、`harness-gateway` IM 桥、`harness-memory` 分层记忆、`harness-browser` CDP 自动化），Web / IM / 定时任务三路入口**统一收敛到进程内 HarnessProcessor**，状态全部持久化于 **SQLite（WAL，可选 PostgreSQL）** 控制面库，**重启即恢复，刻意不引入消息队列，运维极简**。接入面覆盖**飞书、钉钉、QQ、Discord、企微**及 HTTP/SSE/WebSocket；能力面含知识库 RAG、插件系统、**工具审批、shell 命令护栏、PII 脱敏**、终端 AI、浏览器 AI、跨平台远程桌面。**最具洞察的设计是 ACP 双向集成**：既把自己的 Agent 以 **stdio ACP 服务端**暴露给 Zed/OpenCode，又能把编码任务**委派给 Claude Code、Codex、CodeBuddy**——**占位「编排层」而非再造编码 Agent**。安装提供一行脚本、pip、Docker、桌面安装包乃至**飞牛 NAS `.fpk`** 五种方式，当前 v1.0.1 已上架 PyPI。与库里的 danny-avila/LibreChat、open-webui/open-webui 同属自托管 AI 平台赛道，Octop 的差异点在**中文 IM 渠道覆盖 + 多用户 JWT 隔离 + NAS 部署友好**。MIT，Python 3.12+，**4,141 stars** / 442 forks，2026-07-08 开源，2026-09-19 最近推送。
- **归档**：`开源项目介绍/2026.9.23/Octop.md`
- **标签**：`#self-hosted` `#multi-agent` `#腾讯云` `#im接入` `#本地优先` `#acp`

<a id="sec-15"></a>

## 🛰️ 十五、内容发现与情报（15）

### [666ghj/MiroFish](https://github.com/666ghj/MiroFish)
- **定位**：群体智能预测引擎 · 盛大出品
- **简介**：下一代多 Agent AI 预测引擎，从真实世界提取种子信息（新闻、政策、金融信号），自动构建高保真平行数字世界。数千个拥有独立人格、长期记忆和行为逻辑的智能体自由互动并社会演化，从「上帝视角」动态注入变量推演未来走向。五步工作流：图谱构建 → 环境搭建 → 模拟运行 → 报告生成 → 深度交互。已演示场景：武大舆情模拟、红楼梦失传结局推演。盛大出品，Docker 部署，在线 Demo 可用。 **🔄 2026-09-27 复核更新**：stars **74,132** / 11,406 forks / 145 open issues / 450 watchers，**AGPL-3.0**，官网 mirofish.ai，topics 含 swarm-intelligence、multi-agent-simulation、agent-memory、knowledge-graph、financial-forecasting、public-opinion-analysis、social-prediction、future-prediction；2025-11-26 建仓，最近推送 2026-09-16。
- **归档**：`开源项目介绍/2026.9.16/MiroFish.md`（2026-09-27 已复核更新）
- **标签**：`#agent` `#群体智能` `#预测` `#multi-agent` `#盛大`

### [achillean/shodan-python](https://github.com/achillean/shodan-python)
- **定位**：Shodan（互联网设备搜索引擎）的官方 Python 库。
- **简介**：Shodan（互联网设备搜索引擎）的官方 Python 库。（GitHub 每日趋势 2026-10-06：★3301，当日 +50）
- **归档**：`开源项目介绍/2026.10.8/shodan-python.md`
- **标签**：`#python`

### [D4Vinci/Scrapling](https://github.com/D4Vinci/Scrapling)
- **定位**：自适应网页抓取框架：从单次请求到全站爬取一站式搞定。
- **简介**：自适应网页抓取框架：从单次请求到全站爬取一站式搞定。（GitHub 每日趋势 2026-10-03：★85179，当日 +246）
- **归档**：`开源项目介绍/2026.10.3/Scrapling.md`
- **标签**：`#python`

### [Free-TV/IPTV](https://github.com/Free-TV/IPTV)
- **定位**：免费电视频道的 M3U 播放列表。
- **简介**：免费电视频道的 M3U 播放列表。（GitHub 每日趋势 2026-10-05：★20919，当日 +26）
- **归档**：`开源项目介绍/2026.10.5/IPTV.md`
- **标签**：`#python`

### [HunxByts/GhostTrack](https://github.com/HunxByts/GhostTrack)
- **定位**：位置与手机号码追踪工具。
- **简介**：位置与手机号码追踪工具。（GitHub 每日趋势 2026-10-01：★15913，当日 +579）
- **归档**：`开源项目介绍/2026.10.1/GhostTrack.md`
- **标签**：`#python`

### [IAmTomShaw/f1-race-replay](https://github.com/IAmTomShaw/f1-race-replay)
- **定位**：交互式 F1 比赛可视化与数据分析工具。
- **简介**：交互式 F1 比赛可视化与数据分析工具。（GitHub 每日趋势 2026-10-09：★6668，当日 +216）
- **归档**：`开源项目介绍/2026.10.9/f1-race-replay.md`
- **标签**：`#python`

### [jiji262/douyin-downloader](https://github.com/jiji262/douyin-downloader)
- **定位**：抖音去水印批量下载工具 · CLI + Douzy 桌面端双轨，桌面版覆盖 5 大平台
- **简介**：持续维护 3 年+ 的老牌项目。**CLI 支持博主主页批量下载**（post / like / mix / music 四种模式）、视频/图集/合集**去水印**、日期过滤、画质选择（highest/original 回退）、并发下载；**增量机制采用「SQLite 历史 + 磁盘非空文件」双重校验**，无需清库即可控制重下。附加能力包括**热榜抓取与关键词搜索（输出 JSONL）**、可选 **FastAPI REST 服务**、评论抓取、视频转写与下载通知。⚠️ **需诚实面对的现状**：抖音请求验证已**阻断 CLI 的单条视频/合集/音乐/点赞收藏下载**，主页帖子可尝试 **Playwright 浏览器兜底**但不保证成功；官方建议日常使用转向配套桌面应用 **Douzy（0.11.6，Windows/macOS）**——覆盖**抖音、TikTok、YouTube（含 Shorts/播放列表/字幕）、Telegram、X（书签/点赞，需 Cookie）**，部分批量与高级功能需激活。**洞察**：「**开源 CLI 打底线、闭源桌面端做体验**」的双轨策略，是开源下载工具应对平台风控与商业化的典型路径；这与库里 Panniantong/Agent-Reach 提到的「yt-dlp 被 B 站风控封死 → 切 bili-cli」是同一场猫鼠游戏的不同侧面。**JSONL 输出 + REST API 使其可直接作为内容情报采集管线的数据源组件**。MIT，Python 3.9+，**9,640 stars** / 1,510 forks，2023-05-25 创建，2026-09-06 最近推送。
- **归档**：`开源项目介绍/2026.9.23/douyin-downloader.md`
- **标签**：`#视频下载` `#抖音` `#python` `#批量抓取` `#内容归档`

### [koala73/worldmonitor](https://github.com/koala73/worldmonitor)
- **定位**：实时全球情报仪表盘
- **简介**：集成 500+ 精选新闻源（15 个类别），AI 合成简报；双地图引擎（3D 地球 globe.gl + WebGL 平面地图 deck.gl），56 种地图图层；国家不稳定指数（CII）覆盖 31 个重点国家；金融雷达追踪 29 个股票交易所及商品/加密资产。支持跨流事件关联分析（军事、经济、灾害、升级信号）。6,559 commits、228 issues，社区活跃，含 API/CLI/博客站点等多模块，内置 Agent Skills 与审计体系。
- **归档**：`开源项目介绍/2026.9.6/worldmonitor.md`
- **标签**：`#情报` `#可视化` `#全球监控` `#金融雷达`

### [QuantConnect/Lean](https://github.com/QuantConnect/Lean)
- **定位**：QuantConnect 的开源量化交易引擎（Python/C#），回测与实盘一体化。
- **简介**：QuantConnect 的开源量化交易引擎（Python/C#），回测与实盘一体化。（GitHub 每日趋势 2026-09-26：★21775，当日 +15）
- **归档**：`开源项目介绍/2026.9.28/Lean.md`
- **标签**：`#csharp`

### [RayWangQvQ/BiliBiliToolPro](https://github.com/RayWangQvQ/BiliBiliToolPro)
- **定位**：B 站（bilibili）自动任务工具：签到、直播打卡等，支持 Docker/青龙/k8s 部署。
- **简介**：B 站（bilibili）自动任务工具：签到、直播打卡等，支持 Docker/青龙/k8s 部署。（GitHub 每日趋势 2026-09-28：★8857，当日 +18）
- **归档**：`开源项目介绍/2026.9.28/BiliBiliToolPro.md`
- **标签**：`#csharp`

### [sherlock-project/sherlock](https://github.com/sherlock-project/sherlock)
- **定位**：按用户名跨社交网络搜寻账号的 OSINT 利器。
- **简介**：按用户名跨社交网络搜寻账号的 OSINT 利器。（GitHub 每日趋势 2026-09-26：★92806，当日 +104）
- **归档**：`开源项目介绍/2026.9.27/sherlock.md`
- **标签**：`#python`

### [shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos)
- **定位**：Kronos：金融市场语言基础模型（K 线原生 Transformer）。
- **简介**：Kronos：金融市场语言基础模型（K 线原生 Transformer）。（GitHub 每日趋势 2026-10-06：★40042，当日 +96）
- **归档**：`开源项目介绍/2026.10.8/Kronos.md`
- **标签**：`#python`

### [shy3130/tick-stock-panel](https://github.com/shy3130/tick-stock-panel)
- **定位**：自托管、零运维的 A 股选股＋监控＋回测量化工作台，LLM 驱动策略定制与个股复盘，可自由接入第三方数据源。
- **简介**：自托管、零运维的 A 股选股＋监控＋回测量化工作台，LLM 驱动策略定制与个股复盘，可自由接入第三方数据源。（GitHub 每日趋势 2026-09-26：★5234，当日 +191）
- **归档**：`开源项目介绍/2026.9.27/tick-stock-panel.md`
- **标签**：`#python`

### [TNT-Likely/PanWatch](https://github.com/TNT-Likely/PanWatch)
- **定位**：自托管 AI 盯盘助手，集成 TradingAgents 多 Agent 投资决策与全渠道推送
- **简介**：**盯盘侠 PanWatch** 是自托管的 AI 盯盘助手，覆盖 **A 股/港股/美股**实时行情，核心能力包括多券商持仓汇总、模拟盘（净值曲线+绩效）、技术指标共振分析（MACD/RSI/KDJ、K 线形态、量价、多级支撑压力位自动计算）、条件组合价格提醒（AND/OR、冷却时间、日触发上限）、机会页 AI 评分选股，以及 Telegram/企业微信/钉钉/飞书/Bark/自定义 Webhook 全渠道推送，前端支持 **PWA** 添加到手机主屏幕。**差异化**：集成 **TradingAgents（76k+ star）多 Agent 投资决策框架**，持仓页一键触发 9-Agent 投研接力——技术/情绪/新闻/基本面 4 类分析师→看多看空辩论→风控审查→PM 决策书，3–5 分钟输出完整推理链并直推 IM；默认 deepseek-chat 单次约 $0.05、月度预算可控；内建盘前分析、盘中监测、盘后日报、新闻速递 4 个定时 Agent；数据完全自托管、不经第三方。**技术栈**：后端 Python 3.10+/FastAPI/SQLAlchemy/APScheduler/OpenAI SDK，数据源含 AKShare，Playwright 提供截图能力（可跳过安装）；前端 React 18/TypeScript/Tailwind CSS/shadcn/ui；AI 层接 OpenAI 兼容 API（OpenAI/智谱/DeepSeek/Ollama），LangGraph 多 Agent，topics 含 MCP；可观测性内建 trace_id 结构化日志+agent_runs 运行表+节点级成本，可选 **OpenTelemetry OTLP 导出**（Jaeger/Tempo/Langfuse，遵循 GenAI 语义约定），默认关闭零副作用；Docker 单容器部署（端口 8000），打 tag 自动触发 GitHub Actions 构建推送镜像，JWT 认证、HTTP 代理、时区均可环境变量配置。**协议** MIT。**规模与时间线**：2026-01-23 创建，最近推送 2026-09-24，迭代极快——Commits 230、Tags 55，最新版 **0.14.0**（2026-09-21 发布，其前为 0.13.2、0.13.1）；Stars 1,761、Forks 320、Open Issues 65、Watchers 18、贡献者 3，以个人主导开发为主；社区有 Telegram 群（t.me/panwatch）与 Docker Hub 镜像 sunxiao0721/panwatch。**注意事项**：Release 更新说明正文因 GitHub API 限流未获取到；AI 分析结论仅供参考、不构成投资建议；需自备 LLM API Key，行情采集可能依赖代理网络环境；容器首次启动需下载 Chromium（可设 PLAYWRIGHT_SKIP_BROWSER_INSTALL=1 跳过）。
- **关联**：库内 [koala73/worldmonitor](https://github.com/koala73/worldmonitor)（同为自托管情报仪表盘）
- **归档**：`开源项目介绍/2026.9.25/PanWatch.md`
- **标签**：`#stock` `#ai-agent` `#self-hosted` `#fastapi` `#trading` `#fintech`

### [whiteguo233/OpenBiliClaw](https://github.com/whiteguo233/OpenBiliClaw)
- **定位**：本地优先 AI 内容发现 Agent
- **简介**：基于用户在 B站、小红书、抖音、YouTube、X、知乎、Reddit、微博等 11+ 平台的使用行为生成多维度心理画像，主动寻找用户可能喜欢的内容。数据和画像保存在本地 SQLite，支持点赞/点踩/聊天反馈持续优化推荐，是各平台推荐系统的私有替代。584 commits、67 tags，含浏览器扩展，2026-05 最新更新。
- **归档**：`开源项目介绍/2026.9.6/OpenBiliClaw.md`
- **标签**：`#推荐` `#本地优先` `#内容发现`

---

<a id="sec-16"></a>

## 🖼️ 十六、WPF / .NET UI 框架与控件库（23）

WPF/WinUI/.NET 桌面 UI 全家桶：框架、控件库、主题引擎与换肤方案。

### [aduskin/AduSkin](https://github.com/aduskin/AduSkin)
- **定位**：追求视觉完成度的国产 WPF 换肤控件库 · ⚠️ GPL-3.0 传染性协议
- **简介**：**AduSkin** 由国内个人开发者 Adu 维护，追求**开箱即用的视觉完成度**而非设计规范严谨性。**⚠️ 选型首要否决项：GPL-3.0——同类中唯一强传染性协议，闭源商业软件静态链接会触发整个衍生作品的开源义务。**控件分**两套命名体系并行**：`Adu*` 系列 50 个（AduWindow、AduButtonIcon、AduButtonSvg、AduSearchBox、AduPasswordBox、**AduSliderVerifyCode 滑块验证码**、AduNavigationPanel、AduTimeBarNew、AduUpload、AduNotifyIcon、AduRunningBlock、AduLoading、AduMessageBox、AduCheckComboBox、AduCornerClip、AduAnimationPath 等）与 `Metro*` 系列 32 个（MetroWindow、MetroButton、MetroTextBox、MetroComboBox、MetroTabControl、MetroSwitch、MetroColorPicker、**MetroWaterfallFlow 瀑布流**、MetroMenuTabControl、MetroRichTextBox、MetroWebBrowser 等），外加 Badge、Carousel、Cover、DatePickers、Notice、NumericUpDown、RatingBar、SegmentControls、StepBar、TimeLine 共 13 个子模块；另有 AduVideoPlayer 视频模块与基础图表能力。动效有 AduRipple 水波纹、AduAnimationPath 路径动画、AduTransitioningContentControl 内容过渡。**换肤只需一行 `AduSkinTheme` 的 ThemeType 声明，是同类中接入最简洁的。**一个反直觉亮点：**唯一同时提供 net9 与 net10 目标的库**——2.0.3 打包为 net472 / net6.0-windows / net9.0-windows / net10.0-windows，**跟进新 SDK 最激进**。⚠️ 但 `UseWPF` 与 `UseWindowsForms` **同时为 true**（MetroWebBrowser、托盘混用 WinForms），对纯 WPF 项目是隐性负担。**⚠️ 维护模式特殊**：**从不打 Tag、不发 GitHub Release**，但 NuGet 侧 2026 年 8—9 月连发 **2.0.1 → 2.0.2 → 2.0.3**——低强度但仍在更新，**节奏不可预期、无版本说明、无迁移指南、单一维护者巴士因子为 1**。**文档最弱**：README 全英文、无中文 README、无文档站、无 Wiki、无 CI 徽章，实际交流靠 QQ 群。**适合个人项目、内部工具与原型验证，商业产品线慎选。**C#，**2,213 stars** / 388 forks，NuGet 约 2.84 万次下载，2019-11-24 建仓，2026-08-11 最近推送。
- **归档**：`开源项目介绍/2026.9.26/AduSkin.md`
- **标签**：`#wpf` `#控件库` `#换肤` `#gpl` `#国产` `#ui库`

### [AvaloniaUI/Avalonia](https://github.com/AvaloniaUI/Avalonia)
- **定位**：跨平台 .NET UI 框架 · WPF 精神继承者
- **简介**：面向 dotnet 的跨平台 UI 框架，使用 XAML 描述界面、基于 Skia 自绘 UI 实现像素级一致渲染，一套代码支持 Windows、macOS、Linux、iOS、Android、WebAssembly。生产就绪，被 Schneider Electric、Unity、JetBrains（Rider）、GitHub 等公司采用，MIT 协议，27,948 commits。完整工具链：VS Code / Visual Studio 2022&2026 / Rider 插件（XAML 预览、补全、诊断）。另有商业产品 **Avalonia XPF**：让现有 WPF 应用几乎零改动运行于 macOS/Linux。版本双线并行：最新 **12.1.2**（2026-09 发布，新增 iOS VoiceOver 等）+ 长期维护线 11.3.x。文档：docs.avaloniaui.net。 **🔄 2026-09-25 复核更新**：stars **31,563** / 2,828 forks / 1,897 open issues / 474 watchers，最新 **12.1.3**（2026-09-22 发布，此前记录为 12.1.2），MIT，最近推送 2026-09-24。
- **归档**：`开源项目介绍/2026.8.29/Avalonia.md`（2026-09-25 已复核更新）
- **标签**：`#dotnet` `#跨平台` `#xaml` `#skia`

### [dotnet/aspnetcore](https://github.com/dotnet/aspnetcore)
- **定位**：跨平台 .NET Web 框架，构建现代云端应用的主力。
- **简介**：跨平台 .NET Web 框架，构建现代云端应用的主力。（GitHub 每日趋势 2026-09-26：★38464，当日 +1）
- **归档**：`开源项目介绍/2026.9.27/aspnetcore.md`
- **标签**：`#csharp`

### [dotnet/maui](https://github.com/dotnet/maui)
- **定位**：微软官方 .NET 跨平台应用 UI 框架 · 一套 C# + XAML 代码库构建 Android/iOS/iPadOS/macOS/Windows 原生应用
- **简介**：**Xamarin.Forms 的官方演进版**，把 Xamarin 时代仅覆盖移动端的方案扩展到桌面：**Windows 走 WinUI 3、macOS 走 Mac Catalyst**，形成「**单项目五平台**」的原生渲染架构——**handler 抽象比旧 Renderer 模型更薄，需要时可直通平台原生 API，不被框架锁死**。开发体验依托 dotnet CLI：`dotnet workload install maui` 装工具链、`dotnet new maui` 建项目，`-sc` 模板自带 **Syncfusion Toolkit（30+ 控件）+ MAUI Community Toolkit + MVVM Toolkit** 三件套。**版本节奏与 .NET 年度大版本绑定**（.NET 9 于 2024-11 发布，.NET 10 What's New 已上线），2024 年 10 月起正式接纳 Syncfusion 开源贡献。仓库体量约 443 MB，Issues/Projects/Wiki/Discussions 全开，属 Hacktoberfest 参与仓库。**洞察**：MAUI 是微软系企业从 Xamarin 迁移的**唯一官方路径**，其「移动 + Windows 桌面一套代码」是对 Flutter/RN 的差异化卖点；与库里的 AvaloniaUI/Avalonia 构成 .NET 跨平台 UI 的两条路线——**MAUI 用平台原生控件（渲染一致性靠各平台）、Avalonia 用 Skia 自绘（像素级一致）**；但 **4,213 个 open issues** 提示选型时应核查目标平台特定控件的已知问题。MIT，C#，**22,609 stars** / 1,818 forks / 636 subscribers，2020-05-08 创建。
- **归档**：`开源项目介绍/2026.9.23/maui.md`
- **标签**：`#dotnet` `#跨平台` `#xaml` `#移动端` `#ui框架` `#微软`

### [dotnet/runtime](https://github.com/dotnet/runtime)
- **定位**：.NET 官方跨平台运行时，云、桌面、移动全场景基座。
- **简介**：.NET 官方跨平台运行时，云、桌面、移动全场景基座。（GitHub 每日趋势 2026-09-26：★18300，当日 +3）
- **归档**：`开源项目介绍/2026.9.27/runtime.md`
- **标签**：`#csharp`

### [fluentribbon/Fluent.Ribbon](https://github.com/fluentribbon/Fluent.Ribbon)
- **定位**：Office 风格 Ribbon 功能区的 WPF 事实标准
- **简介**：把微软 Office Ribbon（功能区）交互范式完整搬进 WPF 的控件库，历史可追溯到 CodePlex 时代（现仓库建于 2014），是该细分领域几乎唯一的选择。提供 RibbonTabControl（功能区选项卡）、Backstage（Office 式后台视图）、Gallery（画廊选择器）、QuickAccessToolbar（快速访问工具栏）、ScreenTip（增强提示）等成套控件，可拼出 Word/Excel 观感的专业界面；属控件型库而非换肤型，常与 MahApps 等主题库搭配。batzendev 长期维护：AppVeyor 双分支 CI + 测试徽章、每个 release 附可运行 Showcase 演示、提供预览版 NuGet feed，已跟进 .NET 10 SDK。MIT 协议，stars 2,761 / forks 542，最新 v11.0.2（2026-01-19），最近推送 2026-09-13，活跃。注意组织名为小写 fluentribbon，旧链接 Fluent-Ribbon/Fluent.Ribbon 会 404。
- **归档**：`开源项目介绍/2026.9.26/Fluent.Ribbon.md`
- **标签**：`#wpf` `#ribbon` `#office风格` `#控件库` `#csharp`

### [flutter/flutter](https://github.com/flutter/flutter)
- **定位**：Flutter：跨平台应用开发框架，快速构建移动端及多端精美应用（Google 出品，★179K）。
- **简介**：Flutter：跨平台应用开发框架，快速构建移动端及多端精美应用（Google 出品，★179K）。（GitHub 每日趋势 2026-10-11：★179366，当日 +164）
- **归档**：`开源项目介绍/2026.10.11/flutter.md`
- **标签**：`#dart`

### [HandyOrg/HandyControl](https://github.com/handyOrg/HandyControl)
- **定位**：中文 WPF 圈事实标准的零依赖业务控件库 · 务实补齐原生缺口而非推销设计语言
- **简介**：**HandyControl** 是中文 WPF 圈的事实标准，由 NaBian 发起、已加入 **dotNET China** 组织，Gitee 与 GitCode 均有官方镜像。**设计取向与 MDIX 完全相反：不推销任何设计语言，只务实补齐 WPF 的控件缺口**。源码 `Controls` 分 **30 个分类**，涵盖 Growl 消息流、Dialog、Drawer 抽屉、**Screenshot 截屏**、**PropertyGrid 属性编辑器**（同类罕见）、SideMenu、StepBar、Pagination、CoverFlow、FlexPanel/HoneycombPanel/UniformSpacingPanel 布局面板、CheckComboBox、AutoCompleteTextBox、Watermark、PinBox、Magnifier、NotifyIcon、ChatBubble、Transfer 穿梭框、WaveProgressBar、FlipClock、GifImage、GooeyEffect 粘连动效——**多为国产业务软件的高频需求**。**两大工程亮点**：① **向下兼容最广**，目标框架从 **.NET Framework 4.0 一路到 4.8.1**，外加 netcoreapp3.0/3.1、net5.0—net8.0，老项目改造极友好（⚠️ **无 net9/net10**）；② **零第三方依赖**（所有 dependencyGroup 为空）。NuGet 主包 `HandyControl`（27 个版本、约 51.1 万次下载），另有 `HandyControl.Lang.en` 英文语言包——**反证库本身默认中文**。主题走 SkinDefault/SkinDark/SkinViolet 皮肤，支持运行时切换；接入只需合并两个资源字典并加 `hc` 命名空间，另有官方 VS2019 设计器扩展。**中文文档同类最完整**：中英双语 README + 独立文档站 + Slack 群。**⚠️ 维护状态需如实看待**：仓库最近推送 2026-08-11、master 最新提交 2026-06-27（新增 Dialog 样式），**但正式 Release 停在 v3.5.0（2024-02-07）、NuGet 稳定版停在 3.5.1（2024-03-05）**，3.6.0 自 2025-09-28 的 rc3 后无进展——**项目没死，但新代码进不了发行包**，实际使用者要么用两年前的稳定版，要么自行编译 master；叠加 **329 个未关闭 Issue**，长期依赖有风险。**💡 关键选型提示**：核心贡献者 ghost1372 另维护活跃分支 **HandyControls**（NuGet 已 3.7.0、约 22.9 万次下载），**发版比原库勤**，应把原库与分支当两个候选分别评估。MIT，C#，**7,194 stars** / 1,163 forks，2018-05-22 建仓。
- **归档**：`开源项目介绍/2026.9.26/HandyControl.md`
- **标签**：`#wpf` `#控件库` `#ui库` `#零依赖` `#中文文档` `#国产`

### [iNKORE-NET/UI.WPF.Modern](https://github.com/iNKORE-NET/UI.WPF.Modern)
- **定位**：ModernWpf 社区分叉 · Fluent 2 风格 · ⚠️ 自定义许可禁止未授权商用
- **简介**：**iNKORE.UI.WPF.Modern**（简称 iUWM）因上游 ModernWpf 停更而从其分叉，继承 WinUI 移植成果并推进到 **Fluent 2** 视觉。**⚠️⚠️ 选型时的一票否决项：使用自定义许可证（非 OSI 开源，GitHub 标记 Other/NOASSERTION），禁止未经 iNKORE Studios 书面许可的商用**——引用它的软件必须完全开源（协议可自选）并署名，同目的衍生库必须沿用同许可，商用需走捐赠定价的商业订阅。**商业闭源软件应避开或先谈授权。**另一大卖点是**兼容下限最低**：宣称可运行于 **Windows 7 及以上**（推荐 Win10+），是同类中唯一明确承诺「不抛弃 Win7 用户」的库。NuGet 单包 `iNKORE.UI.WPF.Modern`，目标框架 .NET Framework 与 .NET 6.0+。差异化能力：**原生 Mica 与 Acrylic 背景材质** + **Snap Layouts** 分屏；亮/暗主题可深度定制并附高对比度主题；**控件来源多元**——WinUI 移植（NavigationView、ContentDialog、NumberBox、AutoSuggestBox、Expander、FlipView）+ Community Toolkit + 自研（现代 MessageBox、可配置滚动动画的 `ScrollViewerEx`、带关闭按钮的 TabControl），Gallery 应用已上架 Microsoft Store 且大量页面对齐 WinUI 3 Gallery 重制。**三点需留意**：① v0.10.2 含破坏性变更（TabControl 关闭逻辑重构、`FullScreenHelper` 更名 `FullscreenHelper`），0.x 版本号也印证 API 尚未稳定；② 与「正统续作」ModernWPF 1.x 形成微妙竞争——iUWM 胜在已稳定迭代多年、兼容老框架，输在社区规模小一个量级且许可证劝退商业用户；③ README 公开记录了与被除名贡献者的纠纷，**治理带强个人色彩，存在单点维护风险**。适合开源/个人项目、Win7 兼容需求与 Fluent 2 审美偏好者。C#/XAML，**1,027 stars** / 85 forks，最新 **v0.10.2**（2025-11-18），2023-05-26 建仓，2026-07-26 最近推送，活跃开发中。
- **归档**：`开源项目介绍/2026.9.26/UI.WPF.Modern.md`
- **标签**：`#wpf` `#fluent` `#ui库` `#fork` `#自定义许可` `#win7兼容`

### [Kinnara/ModernWpf](https://github.com/Kinnara/ModernWpf)
- **定位**：WinUI 控件移植 WPF 的先驱 · 0.9.x 已冻结，社区重启的 1.x 处于 RC
- **简介**：**ModernWpf**（产品名 ModernWPF）是最早把 WinUI 控件系统性移植到 WPF 的库，在 WPF UI 崛起前几乎是事实标准，也因此积累了最多存量用户。**维护状态必须分两条线看**：**0.9.x 线已被官方明确标注为「冻结且不受支持」**（原作者 Kinnara 停更，无维护更新与安全修复），**1.x 线由社区重启、当前活跃**。**⚠️ 1.x 必须显式指定版本安装**，否则 NuGet 会解析到冻结的 0.9.x。最新 **1.0.0-rc.1**（2026-09-06，API 已冻结），1.x 目标框架 **net462 / net8.0-windows7.0 / net10.0-windows7.0**。**最独特的技术路线**：它是同类中唯一在 .NET 10 上**直接采用 WPF 官方 `PresentationFramework.Fluent` 主题**、旧框架用自家 backport 补齐的库——「官方为主、增量移植」最贴合微软 WPF 演进方向。控件面含 NavigationView、NumberBox、ContentDialog、InfoBar、CommandBarFlyout、ItemsRepeater、TabView、ItemsView、TwoPaneView，preview.4 起提供 TitleBar 与 **Mica / Desktop Acrylic** 背景材质，主题支持亮/暗/高对比度与紧凑资源模式，并提供**应用 / 窗口 / 元素三级主题 API**。**工程治理是它的独门优势**：公开 API 契约文档、WinUI 源码对齐审计（1,586+3,225 条 CLR 条目、5,501 条资源条目清单化）、14 天 RC 浸泡期，**open issues 仅 3 个**，严谨度在开源 UI 库中罕见。**风险同样明显**：1.0 正式版未落地，**与 0.9.x 不承诺兼容**（资源键变更、API 改名、MahApps 适配器移除，需按迁移指南升级），且维护主体已换成社区、长期人力存疑。**求稳的生产项目建议观望 1.0 正式版**；愿意跟进预览线、重视 WinUI API 语义对齐的团队则值得押注。MIT，C#/XAML，**4,958 stars** / 489 forks，2019-10-18 建仓，2026-09-21 最近推送。
- **归档**：`开源项目介绍/2026.9.26/ModernWpf.md`
- **标签**：`#wpf` `#fluent` `#ui库` `#winui` `#csharp`

### [Layui-WPF-Team/Layui-WPF](https://github.com/Layui-WPF-Team/Layui-WPF)
- **定位**：把 Web 版 Layui 设计语言移植到 WPF 的国产样式库 · Web 团队转桌面首选
- **简介**：**Layui-WPF** 由国内开发者 Coolkeke 主导，目标是把广受欢迎的 Web 前端框架 **Layui** 的视觉风格完整移植到 WPF 桌面端——**不是简单配色模仿，而是按 Layui 设计语言重做了按钮、表单、表格、弹窗、分页、导航等整套控件样式**，让熟悉 Layui 的 Web 团队以极低认知成本构建风格统一的 Windows 客户端。**⚠️ 仓库关系务必注意**：网上流传的 `awesomedotnetcore/Layui-WPF` 经 GitHub API 确认是 **fork**——stars/forks 均为 0、创建于 2025-03-25、最近推送停在 2025-03-20 的快照且**已关闭 Issues**，属停更镜像；**主仓库是 `Layui-WPF-Team/Layui-WPF`（530 stars / 105 forks / 6 open issues，创建于 2021-06-25，最近推送 2026-05-08，开启 Discussions，活跃维护中）**，引用时务必锁定主仓库。**💡 差异化洞察**：在 WPF 界几乎清一色模仿 Fluent / WinUI / Material 的大环境下，**它选择复刻中文 Web 生态的设计语言，精准切中「Web 团队转桌面、桌面端与 Web 端风格统一」这一真实痛点**——这是任何 Fluent 库都无法替代的定位。NuGet 包名 **`LayUI.Wpf`**，接入仅需在 App.xaml 合并 `Default.xaml` 资源字典并引入 `LayUI.Wpf.Controls` 命名空间。配套**中文在线文档站**（layui-wpf-team.github.io/Document）与 B 站教学视频，同门还有覆盖 Avalonia 平台的姊妹项目 **LayUI.Avalonia**（跨平台需求可一并评估）。⚠️ **GitHub Releases 为空，版本通过 NuGet 发布**；项目由个人团队驱动、**fork 生态混乱**（本次收录时拿到的地址即为静默快照），选型时要自行确认主仓库。MIT，C#（100%），**530 stars** / 105 forks，2021-06-25 建仓，2026-05-08 最近推送。
- **归档**：`开源项目介绍/2026.9.26/Layui-WPF.md`
- **标签**：`#wpf` `#layui` `#ui库` `#样式库` `#国产` `#中文文档`

### [lepoco/wpfui](https://github.com/lepoco/wpfui)
- **定位**：最活跃的 WPF Fluent Design 控件库 · 纯 WPF 实现 Windows 11 原生体验
- **简介**：**WPF UI** 是当前 WPF 生态里最活跃的 Fluent Design 库，也是同类中新手路径最顺的一个。**纯 WPF 实现、不依赖 WinUI 3 运行时**，NuGet 包名 `WPF-UI`（另有 Tray、DependencyInjection 等扩展包），目标框架覆盖 **.NET Framework 4.6.2+ 与 .NET 6/8/9 的 Windows 目标**。四大差异化亮点：① **原生 Mica / Acrylic 背景材质**（走 DWM API，Win11 效果最佳、Win10 有回退，⚠️ Win10 上只是降级模拟）；② `FluentWindow` + `TitleBar` 原生支持 Win11 **Snap Layouts** 分屏；③ 主题系统完备——亮/暗/高对比度三档，`ApplicationThemeManager` + `SystemThemeWatcher` 实时跟随系统主题与强调色；④ **控件面最广**，除移植 NavigationView、NumberBox、ContentDialog、InfoBar、AutoSuggestBox 等 WinUI 控件外，还提供 WinUI 里没有的 **Snackbar**、纯 WPF **NotifyIcon 系统托盘**、Card/CardExpander、ProgressRing 等约 40 余个控件，图标内置 Fluent System Icons。**生态是它最深的护城河**：VS2022 项目模板插件、Microsoft Store 上架的 Gallery、winget 安装、独立文档站一应俱全，由波兰 lepo.co 团队主导并提供付费商业支持，**可持续性在同类中最强**。值得注意的是 **4.x 迭代重心已从「加控件」转向「质量打磨」**（无障碍 AutomationPeer、RTL 布局、DataGrid 编辑行为、会话解锁后主题丢失修复），说明已被大量生产环境反哺。⚠️ 短板是 **453 个 open issues** 偏多。MIT，C#/XAML，**9,659 stars** / 1,003 forks，最新 **v4.3.0**（2026-05-04），2021-07-24 建仓，2026-06-27 最近推送，活跃维护中。
- **归档**：`开源项目介绍/2026.9.26/wpfui.md`
- **标签**：`#wpf` `#fluent` `#ui库` `#win11` `#mica` `#csharp`

### [LorisYounger/VPet](https://github.com/LorisYounger/VPet)
- **定位**：虚拟桌宠模拟器：开源桌宠软件，可内嵌到任何 WPF 应用。
- **简介**：虚拟桌宠模拟器：开源桌宠软件，可内嵌到任何 WPF 应用。（GitHub 每日趋势 2026-10-08：★6891，当日 +13）
- **归档**：`开源项目介绍/2026.10.8/VPet.md`
- **标签**：`#csharp`

### [MahApps/MahApps.Metro](https://github.com/MahApps/MahApps.Metro)
- **定位**：十五年历史的 WPF 老牌 UI 框架 · 就地重塑原生控件，改造与退出成本最低
- **简介**：**MahApps.Metro** 是 WPF 界资历最深的 UI 框架（始于 2011 年 1 月），2020 年起归属 **.NET Foundation**，160+ 贡献者。**最大差异化是「就地重塑」哲学**：合并两个资源字典即可让现有 Button、TextBox、DataGrid、TreeView **原地换装**，不换控件名、不绑定新 XAML 方言，**改造与退出成本同类最低**——这是它在存量大型项目翻新场景中不可替代的原因。`MetroWindow` 提供可控窗口铬（自定义标题栏命令、Glow 发光边框、四边滑入 Flyout），`ThemeManager` 支持基色+强调色运行时切换并跟随系统，**Message/Input/Login/Progress 对话框以窗口内覆盖层呈现、可 await 且能从 ViewModel 调用**；水印等能力通过 `TextBoxHelper.Watermark` 这类**附加属性挂到原生控件**而非强迫继承子类；另有 HamburgerMenu、ColorPicker、DateTimePicker、NumericUpDown、MultiSelectionComboBox、HotKeyBox、ToggleSwitch 等扩展控件，图标生态为 `MahApps.Metro.IconPacks`。⚠️ **它不是严格的 Fluent Design 实现**：设计语言以 Windows Metro/Modern 为本源，2.x 起持续向 Win10/11 与 WinUI 视觉靠拢，但 **2.x 无原生 Mica/Acrylic**，3.0 才引入新版背景材质并把标题栏按钮注册为非客户区控件以支持 Win11 Snap Layouts。框架支持：**2.4.x 支持 .NET Framework 4.5.2+ 与 .NET Core 3.x，3.0 RC 目标 .NET Framework 4.6.2 / .NET 6 / .NET 8**。**生产验证最充分**——Chocolatey GUI、Markdown Monster、NETworkManager、Hearthstone Deck Tracker 长期背书，**fork 数同类最高（2,421）**，open issues 仅 29 个。⚠️ **维护「保守但未停摆」**：最新 Release **2.4.11**（2025-09-14，仅修 .NET 10 下窗口无法拖动），**3.0 长期以 RC 挂在 NuGet**，发版间隔约两年，需评估时间线风险。MIT，C#/XAML，**9,826 stars**，2011-10-16 建仓，2026-09-25 最近推送。
- **归档**：`开源项目介绍/2026.9.26/MahApps.Metro.md`
- **标签**：`#wpf` `#metro` `#ui库` `#主题` `#dotnet-foundation` `#csharp`

### [MaterialDesignInXAML/MaterialDesignInXamlToolkit](https://github.com/MaterialDesignInXAML/MaterialDesignInXamlToolkit)
- **定位**：把 Google Material Design 完整移植到 XAML/WPF 的主题引擎与控件库
- **简介**：**MaterialDesignInXamlToolkit（MDIX）** 是 WPF 生态里维护最健康的 UI 库——**最近推送就在收录前一天（2026-09-25）**，一年内三个正式版、主干近乎每日提交。它的本质**不是「再造一套控件」，而是把 Google Material Design 的色板体系、Elevation 海拔、动效曲线与 Typography 系统翻译成 XAML 资源字典**，且是 WPF 里**唯一同时提供 Material Design 2 与 Material Design 3 双主题**的库。**NuGet 量级惊人**：主包 `MaterialDesignThemes`（113 个版本、约 **1,154 万次下载**），配套 `MaterialDesignColors`（约 999 万）与 `MaterialDesignThemes.MahApps`（约 145 万）；v5.3.2 目标框架 **net462 / net8.0-windows7.0 / net10.0-windows7.0**，已跟进 .NET 10，底层复用 ControlzEx，**官方声明兼容 Dragablz 与 MahApps.Metro**。控件除全部原生控件的 Material 样式外，补齐 Card、DialogHost、Clock/TimePicker、Snackbar、Drawer、NavigationBar/NavigationRail、Chip、RatingBar、MultiActionButton、ColorZone、Badge、NumericUpDown；动效含 **Ripple 水波纹、Elevation 阴影层级、Transitioner 页面过渡**。**主题切换最省心**：`BundledTheme` 的 BaseTheme/PrimaryColor/SecondaryColor 可在设计时与运行时经 `PaletteHelper` 直改；图标内置完整 Material Design Icons、按枚举名引用，省掉 WPF 最繁琐的图标资源管理。**代价**：视觉强绑 Google 设计语言，不适合中式企业软件或追求原生 Windows 观感的场景；模板层级偏深（官方 FAQ 有渲染性能文档）；**无官方中文文档**。⚠️ 域名 `materialdesigninxaml.net` 已失效并跳转无关站点、GitHub homepage 为空，**文档资产实际全在 GitHub Wiki 与三个 Demo 工程**。MIT，C#，**16,264 stars** / 3,497 forks，最新 **v5.3.2**（2026-05-01），2015-02-07 建仓。
- **归档**：`开源项目介绍/2026.9.26/MaterialDesignInXamlToolkit.md`
- **标签**：`#wpf` `#material-design` `#ui库` `#控件库` `#xaml` `#主题引擎`

### [microsoft/calculator](https://github.com/microsoft/calculator)
- **定位**：Windows 系统预装计算器的 MIT 开源实现 · 标准/科学/程序员/日期四模式 + 单位与货币换算的 UWP 应用
- **简介**：微软 2019 年开源的 **Windows 自带计算器**，持续活跃近 8 年。功能远超普通计算器：**标准模式输入即算、科学模式按运算优先级求值、程序员模式提供进制转换、日期计算支持差值与加减年月日**，另有计算历史、内存、多单位换算与**基于 Bing 汇率的货币换算**；**基础四则采用任意精度算法，永不丢失浮点精度**。**工程边界设计极具参考价值**：图形计算器 UI 已开源，但驱动 Microsoft Mathematics/OneNote 的**专有图形引擎不开源**，仓库以 `GraphingInterfaces` 公共 API + Mocks 实现划清界限；**开发构建默认关闭遥测**（需显式 `SEND_DIAGNOSTICS` 标志），**货币数据用行星名 mock 以规避授权问题**。构建需 Windows 11 build 22000+、VS UWP 工作负载、Windows 11 SDK 与 XAML Styler，入口为新格式解决方案 `src\Calculator.slnx`，UI 测试依赖 WinAppDriver，架构文档见 `docs/ApplicationArchitecture.md`（典型 MVVM 分层）。**作为「系统级应用开源化」样板（与 Windows Terminal、PowerToys 同策略）**，它既是社区直接影响 Windows 出货软件的通道，也是研究大型 XAML 应用工程化的优质范本——与库里的 lively、FluentFlyout、Files、QuickLook 一起构成 Windows 开源桌面生态的参照系。MIT，C++/C# 混合 + UWP/XAML，**31,054 stars** / 5,806 forks / 475 open issues，2019-01-28 开源，2026-09-16 最近推送。
- **归档**：`开源项目介绍/2026.9.23/calculator.md`
- **标签**：`#windows` `#uwp` `#xaml` `#计算器` `#微软` `#系统应用`

### [microsoft/fluentui-blazor](https://github.com/microsoft/fluentui-blazor)
- **定位**：微软 Fluent UI Blazor 组件库，用于 ASP.NET Core Blazor 应用。
- **简介**：微软 Fluent UI Blazor 组件库，用于 ASP.NET Core Blazor 应用。（GitHub 每日趋势 2026-10-01：★4840，当日 +4）
- **归档**：`开源项目介绍/2026.10.1/fluentui-blazor.md`
- **标签**：`#csharp`

### [MudBlazor/MudBlazor](https://github.com/MudBlazor/MudBlazor)
- **定位**：基于 Material Design 的 Blazor 组件库，CSS 优先、极简 JS。
- **简介**：基于 Material Design 的 Blazor 组件库，CSS 优先、极简 JS。（GitHub 每日趋势 2026-10-03：★10631，当日 +5）
- **归档**：`开源项目介绍/2026.10.3/MudBlazor.md`
- **标签**：`#csharp`

### [Panuon/Panuon.WPF.UI](https://github.com/Panuon/Panuon.WPF.UI)
- **定位**：附加属性 + 按需样式注入驱动的定制化 WPF UI 引擎 · 可无侵入改造老项目
- **简介**：**Panuon.WPF.UI** 定位「专业的定制化 UI 引擎」而非整套换皮，前身是 **Panuon.UI.Silver**（老包约 14.7 万次下载），自 Silver 2.2.20 起整体重命名。**协议是隐性优势：Apache-2.0**——比 GPL 宽松、比 MIT 多专利授权条款，**对企业商用最友好**。**真正的差异化落在两条机制上**：① **海量 Helper 附加属性**（`pu:ButtonHelper.CornerRadius` / `HoverBackground` / `ClickBackground`），把过去必须重写 ControlTemplate 才能改的视觉细节压成一行属性，**README 直接用行数背书**——报表页 261 行、VS2019 仿真界面 293 行、网易云音乐仿真 272 行、登录页 187 行，源码随 `Samples` 提供，**是同类中唯一敢量化承诺的**；② **样式注入粒度可控**——`StyleDictionary` 全量接管，或 `KeyOnlyStyleDictionary` 只注册资源 Key、按需取用。**因此它能无侵入嵌入既有大型 WPF 项目做局部美化，这是 MDIX 与 HandyControl 都不具备的能力，也是它最被低估的价值。**NuGet 包 `Panuon.WPF.UI`（89 个版本、约 8.9 万次下载），仅依赖自家 Panuon.WPF。目标框架 net452/462/472/48 + netcoreapp3.1 + net5—net8-windows，**无 net9/net10**——`SourceCode` 按框架拆成 **9 个独立工程**加共享层，改一处公共逻辑需同步多个工程，**维护成本随框架数线性增长，这正是它跟不上新 SDK 的结构性原因**。控件文档在 `docs/zh-cn` 下共 **57 篇 Markdown**，含 WindowX、MessageBoxX、NoticeBox、Toast、PendingBox、Drawer、Dropdown、Breadcrumb、Pagination、Timeline、CalendarX、DateTimePicker、ColorPicker、SearchBox、NumberInput、MultiComboBox、RateControl、RingProgressBar、Card、Carousel、Badge、FormGroup 等。**仅提供中文文档**，但 README 里的 Wiki 链接仍指向旧组织 PanuonGroup、有失效风险，应改用仓库内 `docs/zh-cn`。**⚠️ 维护明显放缓**：最近推送 2026-06-16 仅为文档，上一个功能提交 2026-04-15「新增 Converter」当天即被 Revert，**NuGet 稳定版停在 1.3.0.2（2025-03-20）已一年半未发版**；README 还明确警告不要从 Silver 1.x 直接升级到 WPF.UI 1.x（两代用法差异巨大），说明经历过断代式重构、**API 稳定性风险偏高**。4 位贡献者、Watch 仅 16，**社区体量同类最小**。**不建议作为无兜底方案的长期主线依赖。**C#，**1,286 stars** / 124 forks，2021-03-12 建仓。
- **归档**：`开源项目介绍/2026.9.26/Panuon.WPF.UI.md`
- **标签**：`#wpf` `#ui库` `#附加属性` `#样式引擎` `#中文文档` `#apache2`

### [Simnico99/MicaWPF](https://github.com/Simnico99/MicaWPF)
- **定位**：在 WPF 中实现 Windows 11 Mica 云母材质 · 把「优雅回退 Win10」当一等公民
- **简介**：**MicaWPF** 由开发者 Simnico99 维护，目标是在成熟但官方已不再重点投入的 WPF 里复刻 Windows 11 的 **Mica（云母）**半透明取色背景效果。**它最核心的差异化是「把回退当一等公民」的版本兼容策略**：在 **Windows 11** 上通过 `MicaWindow` 启用**系统级 Mica / Acrylic 真材质**，在 **Windows 10** 上**自动降级为贴近 Win11 深色/浅色风格的纯色主题**，避免同类库常见的透明黑块或崩溃——**因此能放心用于必须兼容 Win10 的企业环境**，这是它相较「只做 Win11 效果」的库最实际的价值。主题切换通过 `<mica:ThemeDictionary Theme="Auto|Light|Dark" />` 实现（Auto 跟随系统），并配 `ControlsDictionary` 提供成套 **WinUI 风格 Fluent 控件样式与动画**，`TitleBarType="WinUI"` 可修正标题栏按钮观感。**技术栈覆盖极广**：.NET Framework 4.6.1 / 4.7 / 4.8 / 4.8.1 与 **.NET 8 / 9 / 10**（`-windows` 目标框架），**持续跟进到 .NET 10 是它相对停更同类项目的最大优势**。NuGet 提供两个包：**`MicaWPF`（完整版）**与 **`MicaWPF.Lite`（精简版）**——Lite 仅含 MicaWindow + 精简强调色检测、体积更小，**代价是强调色精度下降**，轻量场景可选。⚠️ 完整版依赖 WinRT 互操作组件 **MicaWPFRuntimeComponent** 并需设 `TargetPlatformMinVersion 7.0`，**纯 .NET Framework 项目引入互操作组件的成本高于纯样式库**。**工程化程度同类最高**：配 Azure Pipelines CI、CodeFactor 代码评级与 dependabot 自动依赖更新，Topics 含 mica/acrylic/fluent/winui/net8/net9/net10。**版本节奏很勤**：最新 **7.1.0**（2026-08-06），此前 7.0.0（2026-07-16，**新增 .NET 10 支持并移除过时框架**）、6.3.2（2025-12-18）。⚠️ Mica 真效果**仅 Win11 生效**。MIT，C#（100%），**269 stars** / 13 forks / 仅 2 open issues，2021-10-29 建仓，2026-09-09 最近推送，活跃维护中。
- **归档**：`开源项目介绍/2026.9.26/MicaWPF.md`
- **标签**：`#wpf` `#mica` `#acrylic` `#fluent` `#主题` `#ui库`

### [stephenmthomas/TopazWPF](https://github.com/stephenmthomas/TopazWPF)
- **定位**：零 NuGet 依赖的暗色 WPF 控件库与自定义无边框窗口框架（极早期 WIP）
- **简介**：**TopazWPF** 由开发者 stephenmthomas 在编写自己第一批 WPF 项目时同步打造，定位**暗色主题控件库 + 自定义窗口 chrome 框架**。**⚠️⚠️ 必须如实标注它的成熟度：仓库经 API 验证真实存在，但创建于 2026-09-21（收录前仅 5 天）**，数据为 **3 stars / 0 forks / 0 open issues / 0 subscribers，无 Releases、无 tag、无 Topics**，属**活跃但极早期的 WIP 项目**，作者本人明确说明「当前状态可用于个人项目，但仍是半成品」。**现阶段适合学习借鉴暗色 WPF 实现思路，而非直接生产使用。****最大卖点是零 NuGet 依赖**——全部通过标准 WPF 项目引用接入，不引入任何外部包，**仅面向 .NET 8（Windows）**，平台要求 Windows 10 1809+、Mica 背景需 Windows 11，默认分支 master。功能面：`CustomChromeWindow` **无边框窗口基类**（集成 Mica/Acrylic 背景、DWM 深色模式与圆角、可配置标题栏与状态栏，**通过 `WM_NCHITTEST` 实现原生边缘缩放**）、**20+ 重绘暗色控件**（Button 含 8 种变体、ComboBox、Slider、TabControl、TreeView 等）、自定义 `RangeSlider` / `RangeSeeker` **双手柄控件**，内置 JetBrains Mono、Red Hat Display、Lucide/Material 图标字体。**最有想法的设计是语义 token 主题系统**：用 `Theme.Accent.Base`、`Theme.Brush.Surface.Dark` 等 **DynamicResource token 而非硬编码画刷**，换字典即全局换肤，**接近 Web design token 理念**；`ThemeManager` 支持运行时换肤、动态强调色并**通过色相旋转自动计算 hover/pressed/subtle 衍生色**。但作者标注该系统仍为 WIP 且自承架构存在原型阶段臃肿、未定型。**💡 差异化洞察**：它与 MicaWPF 思路重叠（都做 Mica 无边框窗口 + 暗色主题）**却走相反的工程哲学**——MicaWPF 靠 WinRT 互操作、覆盖到 .NET 10、发 NuGet 追求成熟开箱即用；**TopazWPF 坚持零依赖 + 纯项目引用 + 仅 .NET 8，更像「把作者自己的 UI 代码开源供参考」**。建议作为「新锐/观察中」条目跟踪后续迭代。MIT，C#（100%），**3 stars**，2026-09-21 建仓。
- **归档**：`开源项目介绍/2026.9.26/TopazWPF.md`
- **标签**：`#wpf` `#暗色主题` `#自定义窗口` `#mica` `#ui库` `#wip`

### [unoplatform/uno](https://github.com/unoplatform/uno)
- **定位**：Uno Platform：从单一 C#/XAML 代码库构建跨平台原生移动/Web/桌面/嵌入式应用。
- **简介**：Uno Platform：从单一 C#/XAML 代码库构建跨平台原生移动/Web/桌面/嵌入式应用。（GitHub 每日趋势 2026-10-11：★10069，当日 +3）
- **归档**：`开源项目介绍/2026.10.11/uno.md`
- **标签**：`#csharp`

### [wuyanxin1028/rubyer-wpf](https://gitee.com/wuyanxin1028/rubyer-wpf)
- **定位**：把主题能力做成可编程运行时 API 的通用 WPF 主题控件包（Gitee 主站）
- **简介**：**Rubyer-WPF** 由国内开发者 wuwuwu（wuyanxin1028）维护，**MIT 协议、免费商用**。**⚠️ Gitee 为唯一官方主站**——已用 API 验证 `github.com/wuyanxin1028/rubyer-wpf` **返回 404，不存在 GitHub 镜像**，意味着国际可见度与 CI 生态偏弱。**数据相当扎实**：**959 stars / 268 forks / 98 watchers / 20 open issues**，仓库 **6 年历史、累计 1,268 次提交**，**收录前 4 天仍推送新提交（最新 2.19.32）**，近期还及时受理了 DataGrid 卡顿等 Issue，属活跃维护。**它的价值不在控件多漂亮，而在把「设置面板里实时预览主题/深色模式」这类需求做成了开箱即用的运行时 API**：核心是 **`ThemeManager`**——`SwitchThemeMode(ThemeMode.Black|Light)` 实现亮/暗主题一键切换且**默认跟随系统**，`SwitchControlCornerRadius` / `SwitchContainerCornerRadius` 分别调控件与容器圆角，并可通过覆盖 Primary/Accent/Background/Border 等一批 Color/Brush 资源重塑全局配色。**这省去了自建 DynamicResource 主题框架的功夫**，是它相较其他国产库最务实的地方。技术栈上**多框架兼容 .NET Framework 4.6、.NET Core 3.1、.NET 6**，让它能同时服务老项目与新项目；NuGet 包名 **`Rubyer`**（`Install-Package Rubyer`），接入只需在 App.xaml 合并 `Generic.xaml`。内置**中英文国际化资源字典**（`I18N/en-US.xaml`），图标基于 **RemixIcon** 并自带 **RemixIconCodeGenerator** 生成工具，2.0 起优化控件样式并增加过渡动画。⚠️ 两点需评估：**268 fork 对 959 star 比例偏高**（被大量二次分发，注意版本来源）；**大数据量 DataGrid 场景需自行压测性能**。C#（100%），最新 **2.19.32**。
- **归档**：`开源项目介绍/2026.9.26/rubyer-wpf.md`
- **标签**：`#wpf` `#主题` `#ui库` `#暗色模式` `#国产` `#gitee`

<a id="sec-17"></a>

## 🛠️ 十七、系统工具与桌面效率（47）

### [andrewmd5/Borderless-Gaming](https://github.com/andrewmd5/Borderless-Gaming)
- **定位**：让游戏以无边框窗口运行，告别耗时的 Alt+Tab。
- **简介**：让游戏以无边框窗口运行，告别耗时的 Alt+Tab。（GitHub 每日趋势 2026-10-03：★6601，当日 +5）
- **归档**：`开源项目介绍/2026.10.3/Borderless-Gaming.md`
- **标签**：`#csharp`

### [babalae/better-genshin-impact](https://github.com/babalae/better-genshin-impact)
- **定位**：原神自动化辅助工具：自动拾取、自动剧情、全自动钓鱼等。
- **简介**：原神自动化辅助工具：自动拾取、自动剧情、全自动钓鱼等。（GitHub 每日趋势 2026-09-26：★15724，当日 +38）
- **归档**：`开源项目介绍/2026.9.27/better-genshin-impact.md`
- **标签**：`#csharp`

### [bbepis/XUnity.AutoTranslator](https://github.com/bbepis/XUnity.AutoTranslator)
- **定位**：Unity 游戏实时自动翻译插件（XUnity.AutoTranslator）：接入多家机器翻译引擎。
- **简介**：Unity 游戏实时自动翻译插件（XUnity.AutoTranslator）：接入多家机器翻译引擎。（GitHub 每日趋势 2026-09-29：★3433，当日 +3）
- **归档**：`开源项目介绍/2026.9.29/XUnity.AutoTranslator.md`
- **标签**：`#csharp`

### [beeradmoore/dlss-swapper](https://github.com/beeradmoore/dlss-swapper)
- **定位**：Steam 游戏的 DLSS/DLAA 帧生成替换工具，免改游戏文件切换 NVIDIA DLSS 版本。
- **简介**：Steam 游戏的 DLSS/DLAA 帧生成替换工具，免改游戏文件切换 NVIDIA DLSS 版本。（GitHub 每日趋势 2026-09-28：★7540，当日 +13）
- **归档**：`开源项目介绍/2026.9.28/dlss-swapper.md`
- **标签**：`#csharp`

### [BeyondDimension/SteamTools](https://github.com/BeyondDimension/SteamTools)
- **定位**：开源跨平台多功能 Steam 工具箱（瓦特工具箱）。
- **简介**：开源跨平台多功能 Steam 工具箱（瓦特工具箱）。（GitHub 每日趋势 2026-09-26：★26974，当日 +12）
- **归档**：`开源项目介绍/2026.9.27/SteamTools.md`
- **标签**：`#csharp`

### [builtbybel/FluentCleaner](https://github.com/builtbybel/FluentCleaner)
- **定位**：现代开源系统清理工具 · CCleaner 替代品（WinUI 3）
- **简介**：builtbybel 打造的 WinUI 3 清理工具（MIT），理念：现代、透明、无间谍软件、无恐吓营销、无暗黑模式、无追加销售。核心是自研 **winapp2.ini 解析器**——复用社区维护 15+ 年、数千条目的清理规则库（比原版 Piriform 实现更快），每条目精确指定清理路径，可检查可审计；支持自定义数据库（Settings > Database > Custom）。支持无界面静默清理（`/AUTO`，可配 `/SHUTDOWN`）+ Windows 任务计划程序自动化，日志记录到 `%AppData%\FluentCleaner\auto.log`。**刻意不做**安全擦除（SSD 上是安全剧场）和注册表清理器（风险收益倒挂）。要求 Win10 2004+/Win11 + Windows App SDK 2.0.1 运行时。当前版本 26.07.04，17 releases。⚠️ 唯一官方来源是 GitHub，注意假冒网站。
- **归档**：`开源项目介绍/2026.8.29/FluentCleaner.md`
- **标签**：`#清理工具` `#winui3` `#ccleaner替代` `#win10`

### [Devolutions/UniGetUI](https://github.com/Devolutions/UniGetUI)
- **定位**：包管理器的图形界面：一个界面管理所有包管理器（Winget/Scoop/Chocolatey 等）。
- **简介**：包管理器的图形界面：一个界面管理所有包管理器（Winget/Scoop/Chocolatey 等）。（GitHub 每日趋势 2026-10-03：★26365，当日 +16）
- **归档**：`开源项目介绍/2026.10.3/UniGetUI.md`
- **标签**：`#csharp`

### [DevToys-app/DevToys](https://github.com/DevToys-app/DevToys)
- **定位**：开发者的瑞士军刀：30+ 离线开发者小工具合集。
- **简介**：开发者的瑞士军刀：30+ 离线开发者小工具合集。（GitHub 每日趋势 2026-10-01：★32041，当日 +6）
- **归档**：`开源项目介绍/2026.10.1/DevToys.md`
- **标签**：`#csharp`

### [dortania/OpenCore-Legacy-Patcher](https://github.com/dortania/OpenCore-Legacy-Patcher)
- **定位**：在不受支持的旧 Mac 上体验最新 macOS（OpenCore 传统补丁器）。
- **简介**：在不受支持的旧 Mac 上体验最新 macOS（OpenCore 传统补丁器）。（GitHub 每日趋势 2026-10-06：★18450，当日 +32）
- **归档**：`开源项目介绍/2026.10.8/OpenCore-Legacy-Patcher.md`
- **标签**：`#python`

### [ed0ard/CS2-Bot-Improver](https://github.com/ed0ard/CS2-Bot-Improver)
- **定位**：CS2（Counter-Strike 2）机器人行为改进插件。
- **简介**：CS2（Counter-Strike 2）机器人行为改进插件。（GitHub 每日趋势 2026-09-26：★1174，当日 +10）
- **归档**：`开源项目介绍/2026.9.27/CS2-Bot-Improver.md`
- **标签**：`#csharp`

### [gibbed/SteamAchievementManager](https://github.com/gibbed/SteamAchievementManager)
- **定位**：Steam 游戏成就管理器：查看、解锁、重置成就。
- **简介**：Steam 游戏成就管理器：查看、解锁、重置成就。（GitHub 每日趋势 2026-09-29：★9133，当日 +8）
- **归档**：`开源项目介绍/2026.9.29/SteamAchievementManager.md`
- **标签**：`#csharp`

### [greenshot/greenshot](https://github.com/greenshot/greenshot)
- **定位**：老牌 Windows 开源截图工具：区域截图、标注、多格式导出。
- **简介**：老牌 Windows 开源截图工具：区域截图、标注、多格式导出。（GitHub 每日趋势 2026-09-26：★5135，当日 +2）
- **归档**：`开源项目介绍/2026.9.28/greenshot.md`
- **标签**：`#csharp`

### [home-assistant/core](https://github.com/home-assistant/core)
- **定位**：开源家庭自动化平台，本地控制与隐私优先（Home Assistant，★92K）。
- **简介**：开源家庭自动化平台，本地控制与隐私优先（Home Assistant，★92K）。（GitHub 每日趋势 2026-10-11：★91355，当日 +18）
- **归档**：`开源项目介绍/2026.10.11/core.md`
- **标签**：`#python`

### [HotCakeX/Harden-Windows-Security](https://github.com/HotCakeX/Harden-Windows-Security)
- **定位**：使用微软官方支持的方法安全地加固 Windows，附详细解释，始终最新。
- **简介**：使用微软官方支持的方法安全地加固 Windows，附详细解释，始终最新。（GitHub 每日趋势 2026-10-06：★4778，当日 +4）
- **归档**：`开源项目介绍/2026.10.8/Harden-Windows-Security.md`
- **标签**：`#csharp`

### [huiyadanli/RevokeMsgPatcher](https://github.com/huiyadanli/RevokeMsgPatcher)
- **定位**：Windows 微信/QQ/TIM 防撤回补丁（十六进制修改器）
- **简介**：**huiyadanli/RevokeMsgPatcher** 是 Windows 平台 PC 版**微信/QQ/TIM 防撤回补丁**工具（自述 "A hex editor for WeChat/QQ/TIM"，口号"我已经看到了，撤回也没用了"），**GPL-3.0** 协议，创建于 **2019-07-21**，约 **38,844 Stars、4,067 Forks**，主语言 **C#**（.NET Framework，需 Win7+ 与 .NET Framework 4.5.2+），默认分支 master。原理是**十六进制特征码匹配并原位改写聊天软件核心 DLL**——微信的 WeChatWin.dll、QQ/TIM 的 IM.dll——修改撤回消息处理逻辑，使对方撤回的消息本地仍可见；作者自述"不参与方法寻找，仅做特征搬运"，特征源自社区：早期源自 wechat_anti_revoke，微信 4.0 特征来自 BetterWX（@zetaloop），QQNT 2.1 特征来自 NTQQAntiRecall 与 @MliKiowa。微信可选装**多开**功能，另附独立通用微信多开工具（RevokeMsgPatcher.MultiInstance）。版本时间线：**1.9**（2024-09-28）新增 LiteLoaderQQNT 安装器与本体/插件更新，支持 QQNT 9.9.15.28060+；**2.0**（2024-11-06）支持微信 4.0 测试版防撤回（不带撤回提示）；**2.1**（2025-08-03，当前最新）因**封号/警告/下线问题（#864）移除 LiteLoaderQQNT 安装器**，改用全新 QQNT 防撤回方案（无撤回提示、仅支持群聊）。工具自动从注册表读取安装路径（绿色版手动选择），运行时联网获取最新补丁特征，需以管理员身份运行并先关闭聊天软件；软件更新后须重新打补丁。规模数据：**commits 312、贡献者 8、Tags/Releases 各 21 个（0.1–2.1）**；watchers 282、open issues 60；Wiki 与 Discussions 开启，AppVeyor CI；2.1 版 zip GitHub 下载 282,892 次、2.0 版 185,184 次、1.9 版 173,981 次，另提供蓝奏云/百度云备用下载；最近推送 2026-08-16。风险提示：①修改官方客户端二进制可能**违反微信/QQ/TIM 软件许可协议**；②补丁与客户端版本强绑定，存在**版本兼容**问题，支持范围见 Wiki"版本支持"；③存在**封号/警告/强制下线风险**，项目已因此移除一条 QQNT 补丁路径；④修改 DLL 会触发杀毒软件告警；⑤防撤回使对方撤回失效，涉及对方消息自主权，请在合规与知情场景谨慎使用。
- **归档**：`开源项目介绍/2026.9.25/RevokeMsgPatcher.md`
- **标签**：`#wechat` `#qq` `#tim` `#anti-recall` `#hex-editor` `#windows`

### [IgorMundstein/WinMemoryCleaner](https://github.com/IgorMundstein/WinMemoryCleaner)
- **定位**：免费便携的内存清理工具，用 Windows 原生特性优化内存区域。
- **简介**：免费便携的内存清理工具，用 Windows 原生特性优化内存区域。（GitHub 每日趋势 2026-09-29：★5097，当日 +11）
- **归档**：`开源项目介绍/2026.9.29/WinMemoryCleaner.md`
- **标签**：`#csharp`

### [indiff/qttabbar](https://github.com/indiff/qttabbar)
- **定位**：Windows 资源管理器多标签页增强（国内优化版）
- **简介**：给 Windows 资源管理器加上**标签页浏览**及一系列增强，本仓库是**针对 .NET 4.8 和现代 Windows 更新过的国内优化版**（基于 sf.net 的 2012-06-17 版本，原作者后来未再发布）。从此不用开一堆文件夹窗口，加上强大的文件夹预览，效率大幅提升——「就像 IE7、Firefox 和 Opera 那样」。还提供文件操作工具、树形目录、状态栏等插件。相比日本作者 quizo 的官方版，**本版本保留了被官方去掉的「捕获窗口」功能**，并加了些中文特性。**Win10 与 Win11 激活方式不同**：Win10 有经典工具栏，右键工具栏空白处勾选 QTTabBar + QT ButtonBar 即得完整体验（含自己的标签栏）；Win11 移除了经典工具栏，需在 QTTabBar Options 的 Window 页勾选「Enable QTTabBar on every Explorer window (experimental)」再重启 Explorer，此时**与 Win11 原生标签页共存**而不显示自己的标签栏，但能拿到「双击文件夹空白处向上返回一级」和「文本/图片/媒体文件悬停预览」。错误日志在 `%APPDATA%\QTTabBar\QTTabBarException.log`。构建用 VS2022 + WiX Toolset v3.14，`Build-Installer.ps1 -Version x.x.x.x` 是**唯一需要手输版本号的地方**（自动盖进 AssemblyInfo.cs / Installer.wxs / Bundle.wxs），About 页版本改为运行时从程序集读取。三处下载渠道：GitHub Releases / Gitee 中文镜像 / SourceForge。C#（含 C++ 组件）+ WPF + .NET Framework 4.8，GPL-3.0，4,901 stars / 324 forks，2026-09-21 仍在推送。配套 [Win11 深色模式皮肤](https://github.com/StickySli/qttabbar-dark-mode-skin)。
- **归档**：`开源项目介绍/2026.9.23/QTTabBar.md`
- **标签**：`#windows` `#资源管理器` `#标签页` `#效率工具` `#wpf`

### [itsfatduck/optimizerDuck](https://github.com/itsfatduck/optimizerDuck)
- **定位**：免费开源的 Windows 优化工具：性能、隐私、简洁（C#/.NET）。
- **简介**：免费开源的 Windows 优化工具：性能、隐私、简洁（C#/.NET）。（GitHub 每日趋势 2026-10-01：★9788，当日 +29）
- **归档**：`开源项目介绍/2026.10.1/optimizerDuck.md`
- **标签**：`#csharp`

### [JosefNemec/Playnite](https://github.com/JosefNemec/Playnite)
- **定位**：视频游戏库管理器：支持广泛的第三方库与游戏模拟，提供统一界面。
- **简介**：视频游戏库管理器：支持广泛的第三方库与游戏模拟，提供统一界面。（GitHub 每日趋势 2026-10-06：★14136，当日 +15）
- **归档**：`开源项目介绍/2026.10.8/Playnite.md`
- **标签**：`#csharp`

### [k1tbyte/Wand-Enhancer](https://github.com/k1tbyte/Wand-Enhancer)
- **定位**：提升体验与互操作性的扩展增强工具。
- **简介**：提升体验与互操作性的扩展增强工具。（GitHub 每日趋势 2026-09-26：★29304，当日 +179）
- **归档**：`开源项目介绍/2026.9.27/Wand-Enhancer.md`
- **标签**：`#csharp`

### [lostindark/DriverStoreExplorer](https://github.com/lostindark/DriverStoreExplorer)
- **定位**：驱动存储资源管理器：查看、删除、备份 Windows 驱动。
- **简介**：驱动存储资源管理器：查看、删除、备份 Windows 驱动。（GitHub 每日趋势 2026-10-02：★11757，当日 +3）
- **归档**：`开源项目介绍/2026.10.2/DriverStoreExplorer.md`
- **标签**：`#csharp`

### [luolangaga/tubatools](https://github.com/luolangaga/tubatools)
- **定位**：图吧工具箱 CE · WinUI 3 / .NET 10 现代化重构版（47 内置 + 89 收录工具）
- **简介**：经典「图吧工具箱」的 WinUI 3 现代化重构版，解决原版在 UTF-8 全球语言支持下的中文乱码问题。一站式硬件检测与工具集合启动器，覆盖处理器、显卡、内存、硬盘、屏幕、整机稳定性等检测方向。**🔄 2026-09-23 复核更新**：**4,221 stars** / 114 forks / 59 open issues，commits **391 → 498**，最新 **v1.6.4**（2026-09-19，共 25 个 release），2026-05-25 建仓、2026-09-22 仍在推送。**技术栈已从 WPF + .NET 8 升级为 WinUI 3 / .NET 10**，协议确认为 **GPL-3.0**，官方定名「**图吧工具箱 CE**」。**工具规模明确为 47 款内置 Fluent 工具 + 89 款收录第三方工具**，并新增三块重量级能力：**AI 助手**（28 个 Agent 工具、完全访问模式、**跨会话记忆**、可接任意 OpenAI 兼容端点）、**游戏工具箱**（监控覆盖层 / Tailscale 联机 / 运行库修复）、**双引擎格式转换**。⚠️ **架构支持修正**：发布二进制为 **x64 / ARM64（含 Lite 版）**，源码构建支持 x86/x64/ARM64，README 标注 **x86 完全支持**（此前记录的「移除 x86」不准确）。分发渠道扩至 **winget / Scoop / Microsoft Store / GitCode 镜像**，获 **AtomGit G-Star 毕业认证（No.0614）**，采用 **SignPath.io 代码签名**。
- **归档**：`开源项目介绍/2026.9.6/tubatools.md`（2026-09-23 已复核更新）
- **标签**：`#硬件检测` `#winui3` `#图吧` `#dotnet10` `#ai助手`

### [M-Abozaid/esp32-c3-adblock](https://github.com/M-Abozaid/esp32-c3-adblock)
- **定位**：在 2 美元 ESP32-C3 上实现 Pi-hole 级 DNS 广告拦截：53.7 万域名以 40 位 FNV-1a
- **简介**：在 2 美元 ESP32-C3 上实现 Pi-hole 级 DNS 广告拦截：53.7 万域名以 40 位 FNV-1a 哈希存入闪存、二分查找。（GitHub 每日趋势 2026-10-06：★1507，当日 +196）
- **归档**：`开源项目介绍/2026.10.8/esp32-c3-adblock.md`
- **标签**：`#cpp`

### [madoiscool/LuaTools](https://github.com/madoiscool/LuaTools)
- **定位**：Steam 相关的 AppID 管理小工具。
- **简介**：Steam 相关的 AppID 管理小工具。（GitHub 每日趋势 2026-09-26：★604，当日 +16）
- **归档**：`开源项目介绍/2026.9.27/LuaTools.md`
- **标签**：`#csharp`

### [marcussacana/DirectPackageInstaller](https://github.com/marcussacana/DirectPackageInstaller)
- **定位**：向 PS4 直接推送 PKG 安装包的工具。
- **简介**：向 PS4 直接推送 PKG 安装包的工具。（GitHub 每日趋势 2026-09-26：★484，当日 +6）
- **归档**：`开源项目介绍/2026.9.27/DirectPackageInstaller.md`
- **标签**：`#csharp`

### [memstechtips/Winhance](https://github.com/memstechtips/Winhance)
- **定位**：Windows 优化定制增强工具：设置、隐私、性能一站调教。
- **简介**：Windows 优化定制增强工具：设置、隐私、性能一站调教。（GitHub 每日趋势 2026-09-28：★13209，当日 +26）
- **归档**：`开源项目介绍/2026.9.28/Winhance.md`
- **标签**：`#csharp`

### [NickeManarin/ScreenToGif](https://github.com/NickeManarin/ScreenToGif)
- **定位**：录制屏幕选定区域、编辑并保存为 GIF 或视频。
- **简介**：录制屏幕选定区域、编辑并保存为 GIF 或视频。（GitHub 每日趋势 2026-10-01：★27723，当日 +8）
- **归档**：`开源项目介绍/2026.10.1/ScreenToGif.md`
- **标签**：`#csharp`

### [nomi-san/parsec-vdd](https://github.com/nomi-san/parsec-vdd)
- **定位**：完美的虚拟显示器方案，适合游戏串流。
- **简介**：完美的虚拟显示器方案，适合游戏串流。（GitHub 每日趋势 2026-10-02：★5596，当日 +16）
- **归档**：`开源项目介绍/2026.10.2/parsec-vdd.md`
- **标签**：`#csharp`

### [ok-oldking/ok-wuthering-waves](https://github.com/ok-oldking/ok-wuthering-waves)
- **定位**：鸣潮后台自动战斗、自动刷声骸、一键日常自动化。
- **简介**：鸣潮后台自动战斗、自动刷声骸、一键日常自动化。（GitHub 每日趋势 2026-10-05：★7543，当日 +69）
- **归档**：`开源项目介绍/2026.10.5/ok-wuthering-waves.md`
- **标签**：`#python`

### [omacom/omarchy](https://github.com/omacom/omarchy)
- **定位**：DHH 发起的 Arch 系 Linux 发行版 · 把操作系统做成 Agent 可编程的基座
- **简介**：**Rails 之父 DHH 主导**、Omacom Foundation 运营，口号 **We Can Fix Everything**，十条 Doctrine（Unite the nerds / **Welcome the agents** / Own the machine 等）。**数据非常炸**：42,137 stars / 4,845 forks / **4,779 open issues** / **521 位贡献者** / 6,002 个 PR；首年 ISO 下载 **1,165,980 次**，近一月 317,268 次；**募资曲线** 8/21 $8M → 8/24 $10M → 9/2 $13M → **9/17 $18.7M**，DigitalOcean 以每年 100 万连续三年成为创始企业赞助人，另有 1Password、37signals、OrcaRouter（15 万美元 token）。已招 3 名全职（内核 Krzysztof Wilczyński、Shell outfoxxed、基础设施 Emir Beganović），并成立 **Omarchy M（Apple 硬件）与 Omarchy Dragon（Snapdragon）** 平台团队。**产品侧**：最快 **35 秒**装完、只问 **5 个问题**、默认**全盘加密**，支持双启动、无人值守安装（当 VM/机群基础镜像）、以及按 Ctrl+C 切换的「**为他人代装**」模式；硬件从最新 Dell XPS 到老 Intel Mac 再到 **2011 年 ThinkPad X220 + 2GB 内存的「土豆机」**；**22 套内置主题按 T 切换，连官网都跟着换肤**；插件市场已有数千个社区插件（omapods、Time Machine restic 备份）；Neovim 默认，Foot/Alacritty/Ghostty/Kitty 四终端，Steam/RetroArch/Minecraft 游戏栈，以及跑 Office 的 **Windows 11 KVM 虚拟机**。**真正的差异化在 Agent 原生**：首启即引导设置默认 Agent，**App 崩溃时点通知就把 crash dump 交给 Agent 诊断**，仓库内置 `agents/skills` 帮 Agent 造 App、插件、主题；大量提交直接标注「Generated by Opus 4.8 in Claude Code」「Reviewed by Codex XHigh」。**最能说明「Agent 时代操作系统」思路的是 PR #8056**：默认不再把用户加入 `docker` 组（该组等价 root），改走 **polkit 弹窗**，免密 Docker 降级为带警告的显式开关，并在提权前由 root 复核挂载源是否为符号链接——**因为现在真的会有 Agent 在你机器上跑代码**。这是首批把「有 AI Agent 在本机执行代码」当作威胁模型前提来重新设计默认权限的操作系统级项目。当前 ISO 4.0.4（附 SHA-256 与签名），默认分支 quattro。MIT，Shell，2025-06-01 建仓，2026-09-22 仍在高频推送。
- **归档**：`开源项目介绍/2026.9.23/omarchy.md`
- **标签**：`#linux` `#arch` `#桌面os` `#agent原生` `#dhh` `#neovim`

### [pearlxcore/PS4PKGTool](https://github.com/pearlxcore/PS4PKGTool)
- **定位**：PS4 PKG 管理与操作工具。
- **简介**：PS4 PKG 管理与操作工具。（GitHub 每日趋势 2026-10-10：★506，当日 +7）
- **归档**：`开源项目介绍/2026.10.10/PS4PKGTool.md`
- **标签**：`#csharp`

### [QL-Win/QuickLook](https://github.com/QL-Win/QuickLook)
- **定位**：Windows 空格键快速预览工具（macOS 风格）
- **简介**：Windows 上最强大的 Quick Look 实现——选中文件按**空格键**即时预览，再按一次关闭，像 macOS 一样高效。支持图片、视频、音频、压缩包、PDF、Markdown、代码（语法高亮）等几乎所有常见格式，可通过插件扩展 Office 文档、字体、3D 模型等。触摸友好、高 DPI 支持、深浅主题、开机自启。Microsoft Store / winget / 便携版多种安装方式。
- **归档**：`开源项目介绍/2026.9.16/QuickLook.md`
- **标签**：`#效率工具` `#快速预览` `#windows` `#空格键`

### [RankFTW/RHI](https://github.com/RankFTW/RHI)
- **定位**：ReShade HDR 安装器。
- **简介**：ReShade HDR 安装器。（GitHub 每日趋势 2026-10-06：★1985，当日 +24）
- **归档**：`开源项目介绍/2026.10.8/RHI.md`
- **标签**：`#csharp`

### [redis-windows/redis-windows](https://github.com/redis-windows/redis-windows)
- **定位**：Redis 6.x~8.x 全系列 Windows 原生编译版。
- **简介**：Redis 6.x~8.x 全系列 Windows 原生编译版。（GitHub 每日趋势 2026-10-10：★4336，当日 +5）
- **归档**：`开源项目介绍/2026.10.10/redis-windows.md`
- **标签**：`#csharp`

### [rocksdanister/lively](https://github.com/rocksdanister/lively)
- **定位**：Windows 动态壁纸与屏保工具
- **简介**：Windows 免费开源动态壁纸与屏保工具（WinUI 3，GPL-3.0）。支持视频（MP4/WebM/AVI/MOV）、GIF、HTML5 网页、Shader 着色器、Unity/Godot 游戏、YouTube 等作为壁纸。核心特性：全屏应用/游戏时自动暂停（0% CPU/GPU）、屏保支持、命令行自动化、Lively API（硬件读数/音频频谱）、ML 推理动态壁纸、Shadertoy 支持、多显示器、电池模式智能暂停。19.5k stars、1,084 commits，Microsoft Store + GitHub 安装包双渠道。
- **归档**：`开源项目介绍/2026.9.6/lively.md`
- **标签**：`#winui3` `#壁纸` `#动态壁纸` `#屏保`

### [SafeExamBrowser/seb-win-refactoring](https://github.com/SafeExamBrowser/seb-win-refactoring)
- **定位**：Windows 版安全考试浏览器。
- **简介**：Windows 版安全考试浏览器。（GitHub 每日趋势 2026-10-03：★350，当日 +0）
- **归档**：`开源项目介绍/2026.10.3/seb-win-refactoring.md`
- **标签**：`#csharp`

### [scp222thj/MalumMenu](https://github.com/scp222thj/MalumMenu)
- **定位**：Among Us 的简易作弊菜单，带简洁 GUI 和多种实用模块。
- **简介**：Among Us 的简易作弊菜单，带简洁 GUI 和多种实用模块。（GitHub 每日趋势 2026-10-03：★409，当日 +0）
- **归档**：`开源项目介绍/2026.10.3/MalumMenu.md`
- **标签**：`#csharp`

### [seerge/g-helper](https://github.com/seerge/g-helper)
- **定位**：轻量级 Armoury Crate 替代品：华硕笔记本（ROG Zephyrus/Flow/TUF/Strix 等）风扇
- **简介**：轻量级 Armoury Crate 替代品：华硕笔记本（ROG Zephyrus/Flow/TUF/Strix 等）风扇/性能/灯光管理。（GitHub 每日趋势 2026-09-29：★15372，当日 +14）
- **归档**：`开源项目介绍/2026.9.29/g-helper.md`
- **标签**：`#csharp`

### [ShareX/ShareX](https://github.com/ShareX/ShareX)
- **定位**：老牌开源截图/录屏神器：一键捕获任意屏幕区域，集上传、编辑、OCR 于一体。
- **简介**：老牌开源截图/录屏神器：一键捕获任意屏幕区域，集上传、编辑、OCR 于一体。（GitHub 每日趋势 2026-09-29：★39794，当日 +18）
- **归档**：`开源项目介绍/2026.9.29/ShareX.md`
- **标签**：`#csharp`

### [snownico0722/PaperTodo](https://github.com/snownico0722/PaperTodo)
- **定位**：极简 Windows 桌面便签 · WPF 原生「一张纸」
- **简介**：「让桌面上有几张安静、可用、不打扰人的纸」——WPF 原生实现的桌面便签（.NET 10），无主窗口、无账号、无管理器，托盘是唯一全局入口。两种纸片：**待办纸**（勾选/拖动排序/拖拽删除/完成后自动清除）和**笔记纸**（Markdown 高亮三档渲染、本地图片存于 LMDB、外部编辑器打开）。特色：**胶囊模式**（折叠成小胶囊自动贴屏幕边缘，悬停滑出，多屏队列）；**脚本胶囊**（笔记首行写 `!p`/`!power` 把内容当 PowerShell 脚本快捷运行）；**待办关联纸片**（笔记纸拖到待办项建立关联）。数据全部本地：`data.json` + 滚动备份 + `note-assets.lmdb`。定制：四套配色（暖纸/墨/林/霞）、自定义字体字号、全局快捷键、启动参数（--show/--hide/--new-todo 等，单实例转发）、五语言、分屏贴靠、可从 Alt+Tab/任务栏隐藏。构建产物附 Sigstore 签名。1,013 commits。
- **归档**：`开源项目介绍/2026.8.29/PaperTodo.md`
- **标签**：`#便签` `#wpf` `#极简` `#桌面工具`

### [srwi/EverythingToolbar](https://github.com/srwi/EverythingToolbar)
- **定位**：把 Everything 搜索集成进 Windows 任务栏，即输即搜。
- **简介**：把 Everything 搜索集成进 Windows 任务栏，即输即搜。（GitHub 每日趋势 2026-09-29：★14819，当日 +10）
- **归档**：`开源项目介绍/2026.9.29/EverythingToolbar.md`
- **标签**：`#csharp`

### [studyzy/imewlconverter](https://github.com/studyzy/imewlconverter)
- **定位**：深蓝词库转换：开源免费的输入法词库转换程序（★10K）。
- **简介**：深蓝词库转换：开源免费的输入法词库转换程序（★10K）。（GitHub 每日趋势 2026-10-10：★10418，当日 +8）
- **归档**：`开源项目介绍/2026.10.10/imewlconverter.md`
- **标签**：`#csharp`

### [TGSAN/CMWTAT_Digital_Edition](https://github.com/TGSAN/CMWTAT_Digital_Edition)
- **定位**：Windows 10/11 数字权利（数字许可证）激活工具
- **简介**：CloudMoe Windows 10+ Activation Toolkit Digital Edition，用 **C#** 编写的 Win10/Win11 **数字权利激活**工具，作者自称「GitHub 上最棒的开源 Win10/Win11 数字权利激活工具」，曾登上 Trendshift 周榜（C# 分类）。⚠️ **安全公告（务必先读）**：官网 `cmwtat.cloudmoe.com` **曾遭入侵**，指向阿里云/亚马逊云的下载链接被替换为含**恶意 `.msi` 安装包**的 ZIP；正式入侵很可能始于 **2026 年 8 月 10 日傍晚**，服务器文件时间戳还被伪造为 2025 年。**GitHub Releases 不在已确认的受影响范围内**。辨别方法：正常下载应为**单独 `.exe`**，或 ZIP 内**仅含一个 `.exe`**；**ZIP 内若有 `.msi` 请勿运行**。若已运行可疑文件：立即全盘查杀、备份资料、条件允许时重装系统（删除 CMWTAT 不影响已完成的激活，重装后会自动激活）。事件由 @efojug 在 Issue #115 报告。**➡️ 只从 GitHub Releases 下载，别用官网网盘镜像。** GPL-2.0，**19,478 stars** / 2,183 forks，2018-05 创建，2026-09-20 仍在推送。
- **归档**：`开源项目介绍/2026.9.23/CMWTAT_Digital_Edition.md`
- **标签**：`#windows` `#激活工具` `#数字权利` `#安全警告`

### [thebookisclosed/ViVe](https://github.com/thebookisclosed/ViVe)
- **定位**：使用 Windows 10 2004+ 新特性控制 API 的 C# 库与命令行工具。
- **简介**：使用 Windows 10 2004+ 新特性控制 API 的 C# 库与命令行工具。（GitHub 每日趋势 2026-10-02：★7782，当日 +9）
- **归档**：`开源项目介绍/2026.10.2/ViVe.md`
- **标签**：`#csharp`

### [Tianyu199509/DeskBox](https://github.com/Tianyu199509/DeskBox)
- **定位**：免费开源的 Windows 桌面整理工具，原生质感的 WinUI 3 小组件。
- **简介**：免费开源的 Windows 桌面整理工具，原生质感的 WinUI 3 小组件。（GitHub 每日趋势 2026-09-28：★5595，当日 +179）
- **归档**：`开源项目介绍/2026.9.28/DeskBox.md`
- **标签**：`#csharp`

### [Tichau/FileConverter](https://github.com/Tichau/FileConverter)
- **定位**：Windows 右键菜单一键转换与压缩
- **简介**：非常简单但极其顺手——**通过 Windows 资源管理器的右键菜单**转换和压缩一个或多个文件。不用打开任何软件、不用拖进转换工具、不用记命令行：选中文件 → 右键 → 选目标格式 → 完事。它不自己实现编解码，而是把一批成熟开源中间件封装进右键菜单：**ffmpeg v8.0.1**（音视频转换）、**ImageMagick v14.10**（图片编辑与转换）、**Ghostscript 10.02.1**（PDF 编辑）、**SharpShell**（Dave Kerr 的 Windows 右键菜单扩展方案）、Ripper + yeti.mmedia（CD Audio 抓轨）、Markdown.XAML 与 WpfAnimatedGif（WPF 内渲染）。这是个 **2014 年开始的个人开源项目**，作者投入数百小时打磨，目标就是让所有人都能轻松完成转换与压缩。本地化覆盖面惊人——24 种语言，含简体中文（Snoopy1866）与繁体中文（Sedimentary-Rock / NeKoOuO / PeterDaveHello）。开发需 VS2022；安装器需 Wix 5 + Windows SDK Signing Tools。⚠️ 注意默认分支是 `integration` 而非 main/master。C# + WPF，GPL-3.0，**15,238 stars** / 925 forks / 354 open issues，官网 [file-converter.io](https://file-converter.io/)，最近推送 2026-02-27。
- **归档**：`开源项目介绍/2026.9.23/FileConverter.md`
- **标签**：`#windows` `#格式转换` `#右键菜单` `#ffmpeg` `#imagemagick`

### [unchihugo/FluentFlyout](https://github.com/unchihugo/FluentFlyout)
- **定位**：Windows 11 现代化浮出控件替代（官网 [fluentflyout.com](https://fluentflyout.com)）
- **简介**：采用 Fluent 2 设计语言，替换默认的音量/媒体控制弹窗，提供音乐封面+歌名+播放控制弹窗、「即将播放」弹窗、锁定键状态弹窗、**任务栏小组件**（直接在任务栏显示媒体信息）。支持 Mica 模糊、Fluent 2 组件、深浅色主题并自动匹配设备颜色主题、自定义弹窗位置、Repeat All/One/Shuffle、低调驻留托盘。WPF + C# 实现，6 种语言 README + Weblate 协作翻译。**永远免费开源**：GitHub 版功能完整无限制；微软商店版仅多了自动更新与一键安装，少量特性一次性付费 €2.99 资助开发。媒体评价很硬——Windows Central 称「Windows 11 可能又多了个必备应用」（报道标题直指微软忙着搞 AI 没空修 Win11 设计），Neowin 称「比微软官方给的做得好」。**4,522 stars、500k+ 下载、323 open issues、GPL-3.0**（早期记录为 MIT，已校正），2026-09-22 仍在推送。
- **归档**：`开源项目介绍/2026.9.6/FluentFlyout.md`
- **标签**：`#win11` `#fluent` `#系统工具` `#美化` `#任务栏`

<a id="sec-18"></a>

## 📁 十八、文件 · 下载 · 照片管理（20）

### [agalwood/Motrix](https://github.com/agalwood/Motrix)
- **定位**：现代化全功能开源下载管理器（Motrix Turbo v2）
- **简介**：支持 HTTP/FTP/BitTorrent/磁力链接的桌面下载管理器。v2（Motrix Turbo）用 Electron + React + TypeScript 从零重构，下载核心与 UI 独立。双形态运行：桌面应用（macOS/Windows/Linux）+ 无头服务器（Docker，带 Web UI，适合 NAS）。核心特性：BT 逐文件选择、tracker 自动更新与健康检查、UPnP/NAT-PMP 端口映射、SQLite 会话恢复、QuickJS 插件沙箱与插件市场、Chrome/Firefox 扩展一键接管下载、官方 CLI（@motrix/cli，适合 AI Agent 调用）、device-code 配对远程实例。生态协议 MDXP（基于 JSON-RPC 2.0）。技术栈：Electron 43 + React 19 + Tailwind + aria2 内核 + Fastify。
- **归档**：`开源项目介绍/2026.8.18/Motrix.md`
- **标签**：`#下载工具` `#electron` `#aria2` `#docker`

### [averygan/reclip](https://github.com/averygan/reclip)
- **定位**：几乎可从任何网站下载视频：轻量自托管媒体下载器，带清爽的 Web UI。
- **简介**：几乎可从任何网站下载视频：轻量自托管媒体下载器，带清爽的 Web UI。（GitHub 每日趋势 2026-09-30：★9935，当日 +114）
- **归档**：`开源项目介绍/2026.9.30/reclip.md`
- **标签**：`#html`

### [duplicati/duplicati](https://github.com/duplicati/duplicati)
- **定位**：加密云备份工具，支持多种存储后端与增量去重。
- **简介**：加密云备份工具，支持多种存储后端与增量去重。（GitHub 每日趋势 2026-09-26：★15031，当日 +10）
- **归档**：`开源项目介绍/2026.9.27/duplicati.md`
- **标签**：`#csharp`

### [files-community/Files](https://github.com/files-community/Files)
- **定位**：现代化 Windows 文件管理器（社区驱动 · WinUI 3）
- **简介**：社区驱动的 Windows 现代文件管理器（MIT + MPL-2.0 双协议，7,129 commits，141 releases），使命是打造 Windows 上最好的文件管理器。核心特性：多标签/多窗格、文件标签、Fluent Design 界面、**Git 集成**（支持 SSH + NativeAOT）、深度系统集成、高度可定制。技术栈：WinUI 3 / Windows App SDK / C# .NET，已启用 NativeAOT 原生编译（启动更快内存更低）。安装方式：Microsoft Store（付费支持社区）/ GitHub Releases 安装包 / 预览版。社区看板按规模和优先级排序任务，方便贡献者入门。
- **归档**：`开源项目介绍/2026.9.6/Files.md`
- **标签**：`#文件管理器` `#winui3` `#fluent` `#git集成` `#社区驱动`

### [immich-app/immich](https://github.com/immich-app/immich)
- **定位**：高性能自托管照片与视频管理方案（Google Photos 开源替代）
- **简介**：自托管照片/视频备份与管理平台，支持 iOS/Android（Flutter）与 Web 端。核心特性：打开应用自动备份、重复资产检测、相册/共享相册/协作分享、人脸识别聚类、CLIP 语义搜索、EXIF 与地图元数据、LivePhoto/MotionPhoto、Memories（N 年前的回忆）、多用户与 OAuth、公共分享、离线支持、用户自定义存储结构。技术栈：NestJS（TypeScript）+ Flutter（Dart）+ SvelteKit + Python 机器学习模块。AGPL-3.0 协议，10k+ commits、300+ releases（当前 v3.0.2），文档：docs.immich.app。
- **归档**：`开源项目介绍/2026.8.18/immich.md`
- **标签**：`#self-hosted` `#照片备份` `#google-photos替代`

### [Jackett/Jackett](https://github.com/Jackett/Jackett)
- **定位**：把各类种子站转换为标准 API 的代理工具，Sonarr 等自动化媒体方案的常用配件。
- **简介**：把各类种子站转换为标准 API 的代理工具，Sonarr 等自动化媒体方案的常用配件。（GitHub 每日趋势 2026-09-28：★16088，当日 +9）
- **归档**：`开源项目介绍/2026.9.28/Jackett.md`
- **标签**：`#csharp`

### [julyx10/lap](https://github.com/julyx10/lap)
- **定位**：离线优先的跨平台开源照片管理器，云相册的本地隐私替代方案
- **简介**：**Lap** 是 julyx10 开发的**本地优先（local-first）开源桌面照片管理器**，GPL-3.0-or-later 协议，官网 julyx10.github.io/lap，创建于 2024-08-11，支持 macOS（Apple 公证 DMG/Homebrew）、Windows（MSI x64/ARM64）与 Linux（DEB/AppImage，AppImage 支持 zsync 增量更新）。**核心能力**：面向 10 万+ 文件的大型图库优化，坚持"文件夹优先"工作流——直接在现有文件夹上工作、不导入封闭数据库、无强制云上传；浏览维度覆盖日期、文件夹、位置、相机、镜头、标签、评分、人脸与日历层级；v0.3.2（2026-09-12）新增**交互式地图视图**、Google Motion Photos 播放、按日期结构导入与全库去重。**本地 AI** 是最大差异化：文本搜图、视觉相似搜索、主体识别、人脸聚类、智能标签全部经 ONNX Runtime 本地推理（CLIP 图文相似 + InsightFace 人脸），可选 50+ 语言多语言搜索模型，隐私不出机器。还支持 Apple Live Photos（HEIC/MOV 配对与联动文件操作）、RAW+JPEG/HEIC 配对显示、可配置 RAW 预览、Smart Albums 规则相册、Collections/Tags 非破坏性组织、四窗格对比选片、重复清理（含可回收空间汇总）、内置裁剪旋转编辑与 60+ 图片/RAW/视频格式。**技术栈**：Tauri + Rust 核心，Vue + Vite + Tailwind CSS + daisyUI 前端，SQLite 本地库；关键依赖 LibRaw、libheif、libjpeg-turbo、FFmpeg、Video.js、Leaflet；源码构建需 Node.js 20+、pnpm、Rust stable 与 tauri-cli。**规模数据**：约 2,814 Stars、171 Forks、41 开放 Issues、约 1,170 commits、9 位贡献者、24 个 tags，最近推送 2026-09-24，README 提供 9 种语言，版本节奏约每月一更（v0.3.0 智能相册/Live Photos → v0.3.1 文件夹搜索 → v0.3.2 地图视图）。**注意事项**：Collections、标签、评分、智能相册规则与 AI 索引只存于 Lap 本地数据库，不写入 EXIF/XMP sidecar，文件被复制或在 Lap 外移动时不跟随，官方建议数据库与照片一并备份；Windows 安装包未签名，SmartScreen 可能拦截；Linux 视频播放依赖系统 GStreamer 插件；卸载或删除数据库不会删除原始照片。
- **关联**：库内 [immich-app/immich](https://github.com/immich-app/immich)（自托管服务端方案，Lap 是纯本地桌面方案）
- **归档**：`开源项目介绍/2026.9.25/lap.md`
- **标签**：`#photo-manager` `#tauri` `#本地优先` `#privacy` `#桌面应用` `#vue`

### [mealie-recipes/mealie](https://github.com/mealie-recipes/mealie)
- **定位**：自托管菜谱管理与膳食规划器：RestAPI 后端 + Vue 响应式前端，体验极佳。
- **简介**：自托管菜谱管理与膳食规划器：RestAPI 后端 + Vue 响应式前端，体验极佳。（GitHub 每日趋势 2026-09-29：★13361，当日 +18）
- **归档**：`开源项目介绍/2026.9.29/mealie.md`
- **标签**：`#python`

### [NickvisionApps/Parabolic](https://github.com/NickvisionApps/Parabolic)
- **定位**：下载网页视频与音频。
- **简介**：下载网页视频与音频。（GitHub 每日趋势 2026-10-03：★7213，当日 +19）
- **归档**：`开源项目介绍/2026.10.4/Parabolic.md`
- **标签**：`#csharp`

### [pablostanley/yoinks](https://github.com/pablostanley/yoinks)
- **定位**：从终端抓取任意视频，无广告、无套路。
- **简介**：从终端抓取任意视频，无广告、无套路。（GitHub 每日趋势 2026-10-02：★2783，当日 +356）
- **归档**：`开源项目介绍/2026.10.2/yoinks.md`
- **标签**：`#typescript`

### [qbittorrent/search-plugins](https://github.com/qbittorrent/search-plugins)
- **定位**：qBittorrent 搜索功能的搜索插件合集。
- **简介**：qBittorrent 搜索功能的搜索插件合集。（GitHub 每日趋势 2026-10-01：★7044，当日 +174）
- **归档**：`开源项目介绍/2026.10.1/search-plugins.md`
- **标签**：`#python`

### [Radarr/Radarr](https://github.com/Radarr/Radarr)
- **定位**：电影管理器：面向 usenet/torrent 用户的自动化追片方案。
- **简介**：电影管理器：面向 usenet/torrent 用户的自动化追片方案。（GitHub 每日趋势 2026-10-07：★14509，当日 +8）
- **归档**：`开源项目介绍/2026.10.8/Radarr.md`
- **标签**：`#csharp`

### [rmcrackan/Libation](https://github.com/rmcrackan/Libation)
- **定位**：Libation：解放你的 Audible 有声书库。
- **简介**：Libation：解放你的 Audible 有声书库。（GitHub 每日趋势 2026-10-08：★6269，当日 +17）
- **归档**：`开源项目介绍/2026.10.8/Libation.md`
- **标签**：`#csharp`

### [shaked6540/YoutubePlaylistDownloader](https://github.com/shaked6540/YoutubePlaylistDownloader)
- **定位**：下载整个播放列表、频道或单个 YouTube 视频，并可转换为几乎任何格式。
- **简介**：下载整个播放列表、频道或单个 YouTube 视频，并可转换为几乎任何格式。（GitHub 每日趋势 2026-10-09：★3146，当日 +3）
- **归档**：`开源项目介绍/2026.10.9/YoutubePlaylistDownloader.md`
- **标签**：`#csharp`

### [SirDiabo/GithubLauncher](https://github.com/SirDiabo/GithubLauncher)
- **定位**：从 GitHub Releases 下载并自动更新应用的启动器。
- **简介**：从 GitHub Releases 下载并自动更新应用的启动器。（GitHub 每日趋势 2026-09-30：★1650，当日 +9）
- **归档**：`开源项目介绍/2026.9.30/GithubLauncher.md`
- **标签**：`#csharp`

### [slskd/slskd](https://github.com/slskd/slskd)
- **定位**：Soulseek 文件共享网络的现代客户端-服务器应用。
- **简介**：Soulseek 文件共享网络的现代客户端-服务器应用。（GitHub 每日趋势 2026-10-09：★4027，当日 +8）
- **归档**：`开源项目介绍/2026.10.9/slskd.md`
- **标签**：`#csharp`

### [Sonarr/Sonarr](https://github.com/Sonarr/Sonarr)
- **定位**：智能追剧管理器（PVR）：自动跟踪、搜索、下载新剧集。
- **简介**：智能追剧管理器（PVR）：自动跟踪、搜索、下载新剧集。（GitHub 每日趋势 2026-09-28：★16597，当日 +32）
- **归档**：`开源项目介绍/2026.9.28/Sonarr.md`
- **标签**：`#csharp`

### [SteamRE/DepotDownloader](https://github.com/SteamRE/DepotDownloader)
- **定位**：基于 SteamKit2 的 Steam 仓库（Depot）下载器。
- **简介**：基于 SteamKit2 的 Steam 仓库（Depot）下载器。（GitHub 每日趋势 2026-10-02：★3423，当日 +5）
- **归档**：`开源项目介绍/2026.10.2/DepotDownloader.md`
- **标签**：`#csharp`

### [tgeorgiadis/quiver-launcher](https://github.com/tgeorgiadis/quiver-launcher)
- **定位**：现代化启动器：从 GitHub/GitLab Releases 下载、安装、运行应用，带个人库与社区目录订阅。
- **简介**：现代化启动器：从 GitHub/GitLab Releases 下载、安装、运行应用，带个人库与社区目录订阅。（GitHub 每日趋势 2026-09-30：★967，当日 +450）
- **归档**：`开源项目介绍/2026.9.30/quiver-launcher.md`
- **标签**：`#csharp`

### [Tyrrrz/YoutubeDownloader](https://github.com/Tyrrrz/YoutubeDownloader)
- **定位**：下载 YouTube 视频与播放列表。
- **简介**：下载 YouTube 视频与播放列表。（GitHub 每日趋势 2026-10-06：★16354，当日 +6）
- **归档**：`开源项目介绍/2026.10.8/YoutubeDownloader.md`
- **标签**：`#csharp`

<a id="sec-19"></a>

## ▶️ 十九、图片查看与媒体播放（9）

### [0x90d/videoduplicatefinder](https://github.com/0x90d/videoduplicatefinder)
- **定位**：跨平台重复视频/图片查找器（可选本地 AI 匹配）
- **简介**：基于**相似度**在硬盘上查找重复视频与图片。与其他查重工具的关键差异：**能找到分辨率不同、帧率不同、甚至带水印的重复视频**。4.1 版带来全新界面 + 可选本地 AI 匹配。两大独门能力：① **部分片段检测**——找出「短视频是长视频的一段」（从电影里扒的一场戏、长录像里存下的一段），用音频指纹管线（Chromaprint 风格 chroma 提取 + 滑窗 Hamming 相似度）作为视觉查重后的可选第二阶段，默认还会用视觉二次确认，结果带 **Clip Offset** 列标明片段在源视频中的起点；② **AI Matching**——用 DINOv2 视觉模型经 ONNX Runtime 做神经图像嵌入，专治像素级方法漏掉的场景：裁剪/镜像/缩放/加黑边/调色等**变形副本**（结果带 AI 标记），以及**视觉部分检测**（对静音、消音、重新配音的视频同样有效）。设计上很克制：**经典比对始终权威，AI 只追加有把握的结果对，开启它绝不会让你少看到东西**。隐私与开销也交代得清楚：首次下载约 100MB 组件（ONNX Runtime 官方发布 + 嵌入模型，固定 SHA256 校验），**全部本地 CPU 运行，无云服务、无账号、不上传任何东西**；哈希阶段每文件约 50ms，嵌入缓存每文件约 2KB，密集关键帧缓存约 25KB/视频且自清理。四种形态：桌面 GUI / 无头 CLI / Web UI（远程/NAS）/ Docker。需 FFmpeg + FFprobe（8.x shared，非 master），首次启动尝试自动下载；4.x 已把图像处理从 ImageSharp 迁到 FFmpeg。平台覆盖 Windows、Linux x64/ARM64、macOS Intel + Apple Silicon。⚠️ **仓库未声明 License**（GitHub API license 字段为空），商用前需自行确认。C#，3,707 stars / 313 forks，2019-01 创建，2026-09-21 仍在推送。
- **归档**：`开源项目介绍/2026.9.23/VideoDuplicateFinder.md`
- **标签**：`#查重` `#视频` `#本地ai` `#dinov2` `#跨平台` `#docker`

### [d2phap/ImageGlass](https://github.com/d2phap/ImageGlass)
- **定位**：跨平台现代图片查看器（90+ 格式）
- **简介**：快速、现代、开源的图片查看器，支持 Windows/macOS/Linux 三平台。**90+ 图片格式**（WEBP、JXL、SVG、HEIC、AVIF、HDR、各种 RAW），硬件感知智能缓存 + Turbo 模式超快速浏览。内置工具：旋转/翻转/裁剪/缩放/取色器/帧导航/无损压缩/EXIF 查看。支持插件和外部工具扩展（ImageGlass.SDK）。v10 版本全面重构提速。免费基础版 + Pro 付费版。**🔄 2026-09-23 复核更新**：**14,443 stars** / 753 forks / 222 open issues，最新稳定版 **v10.0.6.906**（2026-09-05），2012-12-30 建仓（**十三年老项目**）、2026-09-22 仍在推送。v10.0.6.906 版本主题正是「**Linux .AppImage Support**」——新增 **AppImage 与 Flatpak** 分发，全平台覆盖 **win-x64 / win-arm64 / mac-arm64 / linux-x64**，补齐了此前 Linux 支持偏弱的短板；单是 `win-x64.msi` 一个包的下载量已超 **3.4 万次**，README 新增下载量徽章并导流 `imageglass.org/pricing` 的免费/Pro 对比页。⚠️ **两点务必注意**：① **协议并非标准 OSI 开源许可**，GitHub 标记为 Other/NOASSERTION（自定义许可 + 免费基础版/Pro 付费版双轨），商用或二次分发前需读清条款；② 官方发布安全警示——**有 AI 冒充仓库与 Gist 分发恶意包**，**仅 `d2phap/ImageGlass` 仓库与 ImageGlass 组织为官方渠道**。
- **归档**：`开源项目介绍/2026.9.16/ImageGlass.md`（2026-09-23 已复核更新）
- **标签**：`#图片查看器` `#跨平台` `#高性能` `#多格式` `#appimage`

### [huynhsontung/Screenbox](https://github.com/huynhsontung/Screenbox)
- **定位**：Windows 现代媒体播放器（Fluent + VLC 引擎）
- **简介**：基于 LibVLCSharp（VLC 引擎）和 UWP 构建的现代视频播放器，关注**在广泛设备类型上的性能与易用性**，界面美观友好且轻快。Fluent Design 界面，手势支持（滑动快进/调音量），**窗口尺寸快捷键（数字行 `1`-`4`）**，YouTube 风格快捷键布局，画中画模式，Chromecast 投屏，网络媒体浏览与播放，保存视频帧为图片。支持 Windows 10 1903+ / Windows 11 / **Xbox 主机**。推荐从 Microsoft Store 安装（自动更新，**下载不需要微软账号**），也可 `winget install screenbox -s winget`。本地化走 [Crowdin](https://crowdin.com/project/screenbox)（自动同步到 GitHub 并在下个次要版本发布），也可离线翻译——源语言是 en-US，可本地化文件为 `Screenbox\Strings\` 下的 `.resw` 与 `.md`，文件夹按 IETF 语言标记命名。开发者上手：VS2026 + UWP 工作负载，打开 `Screenbox.slnx` 构建，平台设 x64 后 F5；仓库另有 Contributing Guide 与 Project Structure 文档。GPL-3.0，**4,423 stars** / 208 forks / 245 open issues，2026-09-22 仍在推送。
- **归档**：`开源项目介绍/2026.9.16/Screenbox.md`
- **标签**：`#媒体播放器` `#uwp` `#fluent` `#vlc` `#xbox`

### [jellyfin/jellyfin](https://github.com/jellyfin/jellyfin)
- **定位**：自由开源的媒体服务器系统，影视、音乐、照片一站式管理。
- **简介**：自由开源的媒体服务器系统，影视、音乐、照片一站式管理。（GitHub 每日趋势 2026-09-26：★57528，当日 +43）
- **归档**：`开源项目介绍/2026.9.27/jellyfin.md`
- **标签**：`#csharp`

### [Kareadita/Kavita](https://github.com/Kareadita/Kavita)
- **定位**：快速、功能丰富的跨平台电子书与漫画阅读服务器。
- **简介**：快速、功能丰富的跨平台电子书与漫画阅读服务器。（GitHub 每日趋势 2026-09-26：★11749，当日 +10）
- **归档**：`开源项目介绍/2026.9.27/Kavita.md`
- **标签**：`#csharp`

### [PintaProject/Pinta](https://github.com/PintaProject/Pinta)
- **定位**：简洁的 GTK 画图程序（Linux 版 Paint）。
- **简介**：简洁的 GTK 画图程序（Linux 版 Paint）。（GitHub 每日趋势 2026-10-03：★4066，当日 +4）
- **归档**：`开源项目介绍/2026.10.3/Pinta.md`
- **标签**：`#csharp`

### [Stremio/stremio-web](https://github.com/Stremio/stremio-web)
- **定位**：Stremio——流媒体自由（多平台视频聚合播放器 Web 端）。
- **简介**：Stremio——流媒体自由（多平台视频聚合播放器 Web 端）。（GitHub 每日趋势 2026-10-06：★14353，当日 +111）
- **归档**：`开源项目介绍/2026.10.8/stremio-web.md`
- **标签**：`#javascript`

### [SubtitleEdit/subtitleedit](https://github.com/SubtitleEdit/subtitleedit)
- **定位**：好用的字幕编辑器。
- **简介**：好用的字幕编辑器。（GitHub 每日趋势 2026-10-03：★14414，当日 +12）
- **归档**：`开源项目介绍/2026.10.4/subtitleedit.md`
- **标签**：`#csharp`

### [umlx5h/LLPlayer](https://github.com/umlx5h/LLPlayer)
- **定位**：为语言学习而生的媒体播放器（双字幕 + AI 字幕 + 实时翻译）
- **简介**：一款**专注字幕能力**的视频播放器，核心场景是「看外语视频学外语」。功能密度很高：**双字幕**同时显示（文本与位图字幕都支持）、**AI 生成字幕（ASR）**基于 OpenAI Whisper 实时生成（双引擎可选 whisper.cpp / faster-whisper）、**实时翻译**（Google / DeepL / **Ollama / LM Studio / OpenAI**）、**上下文感知翻译**（用 LLM 识别字幕上下文，准确度大幅提升）、**实时 OCR 字幕**（Tesseract + Microsoft OCR 把位图字幕转文本）、字幕侧栏（可跳转可查词，支持增量搜索）、即时查词与**完全可定制的浏览器搜索站点**、集成 **yt-dlp** 播放任意在线视频且同样支持 AI 字幕与查词、内置 opensubtitles.org 字幕下载、可与 **Yomitan / 10ten** 等浏览器扩展联动、任意格式字幕跳转、双字幕尺寸位置灵活可调、全可定制快捷键（**同一动作可绑多个键**）、按 `F1` 打开内置 Cheat Sheet。用法上有个关键细节：进度条上有**两个 CC 按钮**，左边主字幕设成你在学的语言、右边副字幕设成母语。技术选择很务实——**用 C#/WPF 而不是 C，二次定制极其容易**。⚠️ 依赖 .NET Desktop Runtime 10 + **VC++ Redistributable >= 2022**（不装的话能启动，但一开 ASR 或 OCR 就崩）；NVIDIA 用户装 CUDA Toolkit 可显著加快字幕生成。仅 Windows 10 1903+ / Windows 11 x64。播放内核 Flyleaf。GPL-3.0，4,232 stars，2025-01 创建，Beta 阶段，官网 [llplayer.com](https://llplayer.com)。
- **归档**：`开源项目介绍/2026.9.23/LLPlayer.md`
- **标签**：`#语言学习` `#播放器` `#双字幕` `#whisper` `#实时翻译` `#wpf`

<a id="sec-20"></a>

## ✨ 二十、AI 桌面应用（8）

### [aayushch/laya](https://github.com/aayushch/laya)
- **定位**：本地优先的 AI 通知指挥中心桌面应用，事件先由本地 LLM 研究再给出待批准行动卡片
- **简介**：Laya 是 aayushch 于 **2026-05-10** 开源的**本地优先 AI 通知指挥中心**，Apache-2.0 协议，主张"在你打开那条通知之前，答案就已经准备好了"。它从 Gmail、Slack、GitHub、Bitbucket、Jira、Linear、Notion、Outlook（邮件+日历）与 Google Calendar 拦截事件，经 LLM Agent 分类、自主研究与行动预编排后，在桌面端呈现为可一键批准或忽略的 **Action Card**；批准后由 n8n 真正执行（建 PR、回邮件、评论等）。差异化亮点有四：一是**推理可完全本地**，Ollama / LM Studio 之外也支持 Claude、GPT、Gemini 与任意 OpenAI 兼容端点（LiteLLM 封装），甚至能把流水线跑在已安装 CLI Agent 自己的额度上（`agent/<id>/<model>`，覆盖 Claude Code、Codex、Gemini、Pi CLI）；二是**跨平台实体记忆**，把 Jira 的 BUG-1234、Bitbucket 的 PR-891 与 Slack 里"那个支付 bug"解析为同一实体，检索用 ChromaDB 向量 + SQLite FTS5 BM25 经 Reciprocal Rank Fusion 融合；三是**自学习规则**，从你对优先级/persona 的纠正中抽取分类规则、从 link/unlink 纠正中抽取上下文规则，规则可查看编辑、过大时由 LLM 自动合并；四是**成本可控**，Analytics 按功能与流水线步骤拆分 LLM 花费，Budget Tracking 支持月度上限自动暂停。此外还有六人格路由（Engineer/Comms/Ops/Sales/HR/Finance）、Card Workspaces（与编码 Agent 多步审批协作）、Card Research、Coherence 跨平台叙事、Omni 四层时间摘要、Egress 发送前预览、Daily Briefing、三级数据分类、dead event 审计重试与自建 Bitbucket Server/GitHub Enterprise 支持。技术栈：**Tauri v2（Rust）外壳 + SvelteKit/Svelte 5（runes）+ Skeleton UI + Tailwind v4 前端 + Python 3.10+/FastAPI/asyncio 引擎（uvicorn :8420，27 个路由、70 个迁移）+ 本地 n8n（Node，:45678）网关**，存储为 SQLite(WAL)+FTS5 与嵌入式 ChromaDB，嵌入用 ChromaDB 内置 ONNX 或可选 sentence-transformers；流水线为 ingest→route→stage→emit→trace→learn→context_learn→omni，配置与密钥落在 `~/.laya/`（Key 存 OS keychain），22 个提示词可在 `~/.laya/prompts/` 覆盖并热加载。规模：**275 stars / 43 forks / 4 watchers / 7 open issues / 381 commits / 1 位贡献者 / 92 个 tag**，仓库约 162 MB、9 种语言。时间线：最新 Release **v1.6.0** 于 **2026-09-19** 由 GitHub Actions 自动打包（macOS dmg、Windows msi/exe、Linux deb/AppImage/rpm，附 .sig 与 latest.json），Git 侧 **v1.7.0 已打 tag 但尚未发布 Release**，最近推送 2026-09-24。注意事项：单人维护的早期项目，PR 策略 `collaborators_only`、Discussions 未开启，生产采用前需评估可持续性；Linux 源码开发需 `libwebkit2gtk-4.1-dev` 等依赖并把 `fs.inotify.max_user_watches` 提到 524288，否则 Tailwind 类名会静默失效；macOS 源码构建默认未签名。
- **归档**：`开源项目介绍/2026.9.25/laya.md`
- **标签**：`#notifications` `#tauri` `#本地优先` `#ollama` `#productivity` `#n8n`

### [abi/screenshot-to-code](https://github.com/abi/screenshot-to-code)
- **定位**：AI 设计稿转前端代码（Design-to-Code）
- **简介**：用 AI 将截图、mockups、Figma 设计、屏幕录制转换为干净可用的前端代码，还能将网站录屏转为功能原型。支持技术栈：HTML+Tailwind / HTML+CSS / React / Vue / Bootstrap / Ionic。默认模型：Gemini 3 Flash & 3.1 Pro（最佳）、GPT-5.5 / 5.4 Mini、Claude Opus 4.6 / 4.8，图像生成用 Replicate z-image-turbo。Gemini 负责素材提取（复用截图中的真实 logo/图片），Replicate 负责图像生成/背景移除/编辑。可选截图预览功能：Agent 用 Playwright 无头浏览器渲染生成的页面并自我视觉校验。架构：React/Vite 前端 + FastAPI 后端（Poetry），支持 Docker 一键部署。1,455 commits，官方托管体验：screenshottocode.com。
- **归档**：`开源项目介绍/2026.8.29/screenshot-to-code.md`
- **标签**：`#代码生成` `#设计转代码` `#ui` `#vision`

### [androoAGI/starnet](https://github.com/androoAGI/starnet)
- **定位**：像素风「活的车站」桌面：真实 AI Agent 在其中工作的本地优先可视化。
- **简介**：像素风「活的车站」桌面：真实 AI Agent 在其中工作的本地优先可视化。（GitHub 每日趋势 2026-09-26：★361，当日 +118）
- **归档**：`开源项目介绍/2026.9.28/starnet.md`
- **标签**：`#javascript`

### [argustang/zcode-assistant](https://gitee.com/argustang/zcode-assistant)
- **定位**：ZCode 编码 Agent 使用增强工具（Tauri 桌面应用）
- **简介**：围绕智谱 **ZCode** 编码 Agent 的桌面增强工具，解决配额看不见、模型切换靠手改配置、会话积压占磁盘、界面无法定制等痛点。核心模块：**总览**（每 5 小时 / 每周配额监控，托盘双环图标实时反映用量）、**模型管理**（拉取可用模型、配置上下文与输出上限写回 zcode、自定义供应商 + 预设一键填充、与 Oh My Pi 的 `~/.pi/agent/models.json` 手动双向同步、Token Plan 6 家供应商自动额度查询）、**自动切换**（定时切换 + 配额耗尽自动切到下一个供应商，直写会话模型选择记录与 `setting.json`）、**项目/会话**（读 zcode 会话库按项目统计会话数/对话次数/token 消耗，行内改名、归档恢复、批量删除、按 3 天~1 个月清理久未活跃会话并 VACUUM 压缩）、**用量查询**（解析 rollout 日志按供应商/模型/日期统计 token 与速度）、**美化**（asar 秒级原地补丁注入 `file://` 外链，主题资产外置 + 每秒热重载，参数改动约 1 秒生效，支持视频壁纸与三区域独立透明度）、悬浮球、命令面板（Ctrl/Cmd+K 跳转 10 个功能页）、HTTP/SOCKS5 代理、多账号一键切换。技术栈 **Tauri 2 + Vue 3 + myui + TypeScript + Vite 6**，Rust 后端，SQLite + 系统 keyring 存凭证，AES-256-GCM 解密 zcode `credentials.json`，reqwest（rustls 免 OpenSSL）。统一界面方案（myui 设计令牌 · OKLCH 液态玻璃 · 深浅双主题），v0.12.0 从 React 18 整体迁移到 Vue 3。数据全部本地读写 `~/.zcode/v2` **不外传**；匿名统计 opt-in 且仅上报设备 ID + 版本 + 系统。自定义轻量自动更新（拉 Gitee 发行版按 semver 比较，流式下载 + 安装重启）。v0.13.0 已适配 ZCode 3.14 配置迁移（`provider_config.json` 双向投影 + 模型信息只补缺不覆盖回填）。Apache-2.0，37 commits、16 tags，最新版 v0.13.0，迭代极快。
- **归档**：`开源项目介绍/2026.9.22/zcode-assistant.md`
- **标签**：`#tauri` `#桌面应用` `#编码agent` `#配额管理` `#vue3` `#gitee`

### [ATH-MaaS/Pixelle-Video](https://github.com/ATH-MaaS/Pixelle-Video)
- **定位**：AI 全自动短视频引擎 · 输入一个主题，文案/配图/配音/配乐/合成一条龙出片
- **简介**：**AIDC-AI / HITsz-TMG 团队**（阿里国际数字商业 + 哈工大深圳）出品的开源短视频引擎，只需输入一个**主题**，自动完成「撰写文案 → 生成 AI 配图/视频 → 合成语音解说 → 添加 BGM → 一键合成视频」，**零剪辑经验**可上手。与同类工具（MoneyPrinterTurbo / NarratoAI / MoneyPrinterPlus，均在 README 致谢）最大的差异是**模块化 + 原子能力可替换**：文案、图像、视频、TTS、VLM 每个环节都能单独换供应商。图像/视频走**双路线**——**工作流路线**（本地 ComfyUI 或云端 RunningHub，支持 48G 显存机型与并发数配置，默认 `image_flux.json`）与**直连 API 路线**（OpenAI GPT Image、DashScope Wan/HappyHorse、Volcengine ARK Seedream/Seedance、Kling 可灵、Nano Banana），2026-06-01 起可在 WebUI 直接配置供应商 / Base URL / 代理开关。语音支持 Edge-TTS（已锁 7.2.7 保稳定）、Index-TTS 等 **20+ TTS 工作流**，可上传参考音频做**声音克隆**并在生成前「预览语音」先听效果，2026-01 起扩展韩/法/葡/德/俄/土/西多语言音色。模板按 **`static_*.html`（纯文字静态）/ `image_*.html`（AI 图背景）/ `video_*.html`（AI 视频背景）** 命名规范，按竖屏 9:16 / 横屏 16:9 / 方形 1:1 分组，可自写 HTML 并自定义参数预览。**四个扩展模块**：**数字人口播**（一张照片开口说话）、**图生视频**（Audio-Visual 音画同步）、**动作迁移**（参考视频 + 图片让人物跳舞）、**自定义素材**（上传自己的照片视频，AI 智能分析生成脚本）；另有历史记录页 + 批量创建任务，API 支持 `template_params`。工程细节很实在：API 视频下载重试、**内容审核失败后提示词中性化重试**、按旁白音频时长生成片段并参考相邻片段信息提升连贯性、选择本地 SelfHost 工作流时自动弹窗提醒先去 ComfyUI 验证以免 400 错误。**成本可压到 0 元**：Ollama 本地 LLM + 本地 ComfyUI 完全免费；推荐组合是通义千问 + 本地 ComfyUI（性价比最高）；纯云端则 OpenAI + RunningHub（无需本地环境但费用较高）。技术栈 Python + **Streamlit 三栏 WebUI**（默认 `localhost:8501`），依赖 `uv` + `ffmpeg`，部署有 **Windows 一键整合包**（解压双击 `start.bat`，内置全部依赖）、源码 `uv run streamlit run web/app.py`、Docker（`docker-compose`）三种。**学术血统是隐形加分项**——同系列工作包括 FilmAgent（SIGGRAPH Asia 2024）、Anim-Director（SIGGRAPH Asia 2024）、ComfyUI-Copilot（ACL 2025）、AniMaker（SIGGRAPH Asia 2025），工程与论文双线并行。选型可与库内 [MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo) 对照：后者强在 4 种入口 + 免费图库素材，Pixelle-Video 强在 ComfyUI 工作流可插拔与数字人/动作迁移等扩展流水线。⚠️ 仓库已从 `AIDC-AI/Pixelle-Video` 转移到 `ATH-MaaS` 组织（README 内链接仍写 AIDC-AI，GitHub 会自动重定向，不影响使用）。Apache-2.0，Python（+ 234KB HTML 模板），**28,222 stars** / 4,101 forks / 168 open issues / 18 位贡献者，377 commits、14 tags、12 releases，最新 **v0.1.15**（2026-01-27）整合包已下载 **72,182 次**，2025-11-07 建仓、最近推送 2026-06-14。文档站 [aidc-ai.github.io/Pixelle-Video/zh](https://aidc-ai.github.io/Pixelle-Video/zh)，社区有微信群 + Discord。
- **归档**：`开源项目介绍/2026.9.23/Pixelle-Video.md`（另有早前撰写的推文全文：`开源项目介绍/2026.7.12/Pixelle-Video——输入一个主题，AI全自动从零到一帮你做好一个视频.md`）
- **标签**：`#ai视频` `#短视频` `#comfyui` `#tts` `#数字人` `#streamlit`

### [harry0703/MoneyPrinterTurbo](https://github.com/harry0703/MoneyPrinterTurbo)
- **定位**：一站式 AI 短视频生成工具
- **简介**：只需提供视频主题或关键词，自动完成脚本→配音→素材→字幕→配乐→剪辑全流程，合成高清短视频。**4 种使用方式**：AI Agent / WebUI / API / CLI，支持批量生成和任务历史。集成 10+ 大模型（Kimi、GPT、Claude、Gemini、DeepSeek、通义千问、MiniMax 等）和 15+ 网关/聚合平台。素材来源：Pexels/Pixabay 免费图库 + 本地素材 + AI 文生视频（MiniMax H3、Seedance、WaveSpeed 等多模型）。Python 3.11+，Windows/macOS/Linux 三平台。 **🔄 2026-09-25 复核更新**：stars **125,517** / 19,518 forks / 33 open issues / 773 watchers，最新 **v1.3.7**（2026-09-13 发布），MIT，最近推送 2026-09-24，仍在高频迭代。
- **归档**：`开源项目介绍/2026.9.16/MoneyPrinterTurbo.md`（2026-09-25 已复核更新）
- **标签**：`#ai视频` `#短视频` `#自动化` `#python` `#多模型`

### [lightningpixel/modly](https://github.com/lightningpixel/modly)
- **定位**：本地开源 AI 图像转 3D 网格生成桌面应用
- **简介**：把任意照片变成 3D 模型，使用开源 AI 模型完全在本地 GPU 上运行，数据无需上传云端。Windows/Linux 桌面应用（macOS 即将支持），技术栈 TypeScript + Electron + Python 后端（含 C++/CUDA 组件）。支持外部 AI 模型扩展系统（每个扩展是一个含 manifest.json + generator.py 的 GitHub 仓库），官方扩展包括 Hunyuan3D 2 Mini（含 Turbo/Fast）、TripoSG、Trellis2 GGUF。MIT 协议，当前版本 Beta v0.3.6。
- **归档**：`开源项目介绍/2026.8.18/Modly.md`
- **标签**：`#3d` `#图像转3d` `#本地ai` `#electron`

### [microsoft/data-formulator](https://github.com/microsoft/data-formulator)
- **定位**：微软出品的交互式 AI 数据分析系统：对话式生成图表与数据变换，可视化零门槛。
- **简介**：微软出品的交互式 AI 数据分析系统：对话式生成图表与数据变换，可视化零门槛。（GitHub 每日趋势 2026-09-28：★17410，当日 +111）
- **归档**：`开源项目介绍/2026.9.28/data-formulator.md`
- **标签**：`#python`

<a id="sec-21"></a>

## 🔗 二十一、跨设备工具（10）

### [boykopovar/AnyPS5](https://github.com/boykopovar/AnyPS5)
- **定位**：PS5 可执行文件自动移植到 Linux 与 Windows 的工具。
- **简介**：PS5 可执行文件自动移植到 Linux 与 Windows 的工具。（GitHub 每日趋势 2026-10-06：★5141，当日 +997）
- **归档**：`开源项目介绍/2026.10.8/AnyPS5.md`
- **标签**：`#cpp`

### [firebase/firebase-ios-sdk](https://github.com/firebase/firebase-ios-sdk)
- **定位**：苹果应用开发官方 Firebase SDK。
- **简介**：苹果应用开发官方 Firebase SDK。（GitHub 每日趋势 2026-10-01：★6732，当日 +4）
- **归档**：`开源项目介绍/2026.10.1/firebase-ios-sdk.md`
- **标签**：`#cpp`

### [InfinityLoop1308/PipePipe](https://github.com/InfinityLoop1308/PipePipe)
- **定位**：开源 Android 应用，自由浏览 YouTube 等服务的第三方客户端（NewPipe 的活跃维护分支）。
- **简介**：开源 Android 应用，自由浏览 YouTube 等服务的第三方客户端（NewPipe 的活跃维护分支）。（GitHub 每日趋势 2026-09-28：★6460，当日 +139）
- **归档**：`开源项目介绍/2026.9.28/PipePipe.md`
- **标签**：`#shell`

### [kunkundi/crossdesk](https://github.com/kunkundi/crossdesk)
- **定位**：轻量跨平台远程桌面 · 电脑、浏览器、iPhone/iPad 连到同一张桌面
- **简介**：**最大差异点是控制端可以是浏览器**——被控电脑装好 CrossDesk 并保持「已连接服务器」，控制端直接打开 [web.crossdesk.cn](https://web.crossdesk.cn/) 输入设备 ID 和密码就能连，**无需安装任何客户端，手机平板也能用**。被控端支持 Windows 10+ x64（`.exe` 安装包，**便携构建也支持**）/ macOS 14.0+（Intel 与 Apple Silicon 各自的 `.pkg`）/ Linux Ubuntu 20.04+（amd64 与 arm64，**glibc 2.31 基线**）的 `.deb`；控制端另有 Win/macOS/Linux 桌面互控与**原生 iOS 客户端**（iOS 16+ 真机，需 Xcode 构建签名，CI 产物未签名）。基于作者自研的 **[MiniRTC](https://github.com/kunkundi/minirtc)**，iOS 端与桌面端共用同一套协议。能力面：H.264 / AV1 编码、30/60 fps、硬件编解码选项、远端声音播放、多设备与远端显示器切换、键鼠输入与光标同步、组合键、文本剪贴板同步、文件传输（带进度）、会话内实时查看流量/丢包率/帧率/分辨率及**直连或中继状态**。网络层支持 **P2P 直连 + TURN 中继 + SRTP 加密**，且**信令与中继都可自托管**（Compose 部署，配套 [crossdesk-server](https://github.com/kunkundi/crossdesk-server) 与 [crossdesk-web-client](https://github.com/kunkundi/crossdesk-web-client) 两个仓库，两端需启用同一套配置）。**Windows 锁屏控制是个硬功夫**：`CrossDesk Service`（服务名 `CrossDeskService`）支持锁屏、登录界面、凭据输入及**安全桌面**的状态上报、`Ctrl+Alt+Del` 发送与键鼠转发；安装版注册按需启动的服务且**本机无客户端进程后自动退出**，便携版需管理员权限手动装，命令行提供 `--service-install/start/status/ping/stop/uninstall`。另内置 Amyuni **USB Mobile Monitor 虚拟显示器驱动**（`usbmmidd_v2`，未作修改）解决**无显示器主机**的问题。iOS 端只能作控制端、不能作被控端；鼠标有相对位置（触控板式）与绝对位置（触摸直接映射）两种模式，手势支持单指点击/双指右键/长按拖动/捏合缩放。技术栈 **C++ + Slint 桌面 UI + xmake 构建**，音视频走 WebRTC / libdatachannel / RTP / KCP，另有 SDL3 与 imgui。**官方 Windows 发布包由 SignPath.io 提供代码签名**（证书来自 SignPath Foundation）。⚠️ 两个坑：**默认分支是 `p2p-enhancement` 而非 main**；macOS 首次运行必须在「隐私与安全性」授予**屏幕录制**（新系统叫「屏幕与系统音频录制」）与**辅助功能**两项权限。GPL-3.0，**4,305 stars** / 407 forks / 仅 15 open issues，2023-11 创建，2026-09-22 仍在推送，官网 [crossdesk.cn](https://www.crossdesk.cn/)，曾获 HelloGitHub、阮一峰科技爱好者周刊与 LinuxDo 推荐。
- **归档**：`开源项目介绍/2026.9.23/crossdesk.md`
- **标签**：`#远程桌面` `#跨平台` `#webrtc` `#self-hosted` `#c++` `#web客户端`

### [mRemoteNG/mRemoteNG](https://github.com/mRemoteNG/mRemoteNG)
- **定位**：mRemote 的下一代：开源多标签、多协议远程连接管理器。
- **简介**：mRemote 的下一代：开源多标签、多协议远程连接管理器。（GitHub 每日趋势 2026-09-30：★11134，当日 +4）
- **归档**：`开源项目介绍/2026.9.30/mRemoteNG.md`
- **标签**：`#csharp`

### [nefarius/DsHidMini](https://github.com/nefarius/DsHidMini)
- **定位**：索尼手柄的虚拟 HID 用户态驱动。
- **简介**：索尼手柄的虚拟 HID 用户态驱动。（GitHub 每日趋势 2026-09-26：★1816，当日 +5）
- **归档**：`开源项目介绍/2026.9.27/DsHidMini.md`
- **标签**：`#csharp`

### [PhilippC/keepass2android](https://github.com/PhilippC/keepass2android)
- **定位**：Android 密码管理器（KeePass 2.x / KeePassXC 兼容）
- **简介**：把密码和敏感信息存在一个用强密钥保护的「数据库」文件里，**该文件可跨设备同步**——用内置的云存储选项效果最好，也可以用第三方应用同步。**兼容性是它的核心价值**：与 PC 上的 **KeePass 2.x** 和 **KeePassXC** 兼容，也兼容众多其他平台的 KeePass 移植版，意味着**你不被锁进任何专有生态**——同一个 `.kdbx` 数据库可在 Windows/macOS/Linux 的 KeePass、KeePassXC 与 Android 的 Keepass2Android 之间自由流转。Google Play 提供两个版本：**标准版**（含网络同步能力）与 **Offline 版**（包名带 `_nonet`，**无网络权限**，适合高安全需求）；两者都有 Beta 测试通道。支持**插件系统**扩展（仓库内有插件开发指南），翻译走 Crowdin。贡献方式：翻译、写插件、提 PR（**动手前最好先联系作者协调**）、GitHub Sponsor 或直接捐赠。免责声明写得很直白：GPLv3、按「原样」提供、**作者对使用导致的任何损害不承担责任**（除适用法律另有要求），**使用完全由你自行承担风险**；捐赠是**自愿贡献，不构成购买、合同或对特定功能/服务/支持的权利**。C#（Xamarin / .NET for Android），GPL-3.0，6,244 stars / 480 forks / **1,179 open issues**，2017 年建仓（项目本身历史更久），2026-09-17 仍在推送。
- **归档**：`开源项目介绍/2026.9.23/keepass2android.md`
- **标签**：`#密码管理` `#android` `#keepass` `#离线优先` `#插件`

### [RayrenSX/iPhoneMirror](https://github.com/RayrenSX/iPhoneMirror)
- **定位**：Windows 上的低延迟 iPhone/iPad 投屏（USB + AirPlay 双通道）
- **简介**：面向 **Windows 10/11 x64** 的本地 iPhone/iPad 投屏与**蓝牙反向控制**工具，当前正式版 **v1.8.3**。目标很明确：**在不依赖云端中转的前提下**，把 USB 有线采集和局域网 AirPlay 接收统一到同一套预览、音频、截图、独立窗口、OBS 和多设备会话能力中。**架构分四层且边界清晰**：C++ 核心负责 Apple 私有 USB 协议、QuickTime/CoreMedia 解析、**H.264 解码**、**D3D11 渲染**和 **WASAPI 音频**；WPF 主程序负责设备列表/会话控制/UI；独立无线宿主负责 AirPlay 协议与解码，通过**有界命名管道**传递媒体帧；驱动的安装/修复/卸载由**独立的 `iPhoneMirror.Driver.exe`** 负责，**主程序只读检查有线设备状态、绝不在投屏进程中改系统驱动**。**两个亮点值得记**：① **按真实机型适配外形**——不给所有设备套同一个通用圆角，而是按 Apple `ProductType` 识别 iPhone X/刘海屏/mini/标准/Max/**Dynamic Island** 以及 iPad Pro/Air/mini/全面屏基础款，为每台设备匹配独立的屏幕圆角、曲线和裁切配置；带 Home 键或已知直角屏保持直角，**未知新设备按画面比例保守回退，避免把 iPad 误裁成手机**；这套适配同时作用于原生渲染和独立窗口轮廓，拖动/等比缩放/横竖屏切换/全屏时窗口仍保持设备视觉形状，也可右键手动去除或恢复圆角（⚠️ 圆角参数是**基于公开外观和画面比例的视觉拟合**，非 Apple 公布的工业尺寸）。② **多设备真并行**——每台设备有独立会话和独立窗口可同时运行，切换时不必停止上一台；设备卡片支持长按拖动排序，无线设备刚连接时只自动切换一次。其他：H.264/CoreMedia 与 AirPlay 帧**在本机解码**经 **D3D11/DirectComposition 原生显示**；**媒体不经云端中转**，USB 场景不依赖网络；干净的独立窗口可直接喂 **OBS**，截图**直接读解码帧、不含软件 UI**；可选 **BLE HID 鼠标/键盘控制**，配合 iOS 辅助触控**无需在手机装 App 或越狱**。⚠️ **使用须知**：当前是公开预览版、**尚未商业 Authenticode 签名**（Windows 会弹 SmartScreen/「未知发布者」）；Apple Screen Capture 用**私有协议**，未来 iOS 更新可能需要适配；**仅支持 Windows x64，ARM64 不支持**（USB 内核驱动与无线运行库缺 ARM64 版本）。社区 [@furruka](https://github.com/furruka) 正在做 **Linux 原生移植**（针对 GUI/渲染/音频/视频解码/USB 通信/设备发现等 Windows 专有部分适配，尽量保持上游协议层与策略层一致），**但尚未提供可用的 Linux 发布包**。QQ 群 1050045279。C# + C++，GPL-3.0-only，708 stars / 47 forks，2026-07 创建（较新）。
- **归档**：`开源项目介绍/2026.9.23/iPhoneMirror.md`
- **标签**：`#投屏` `#windows` `#airplay` `#usb` `#d3d11` `#obs`

### [wilbowes/EchoMuse](https://github.com/wilbowes/EchoMuse)
- **定位**：Echo Dot 二代的 Alexa 替代与控制器。
- **简介**：Echo Dot 二代的 Alexa 替代与控制器。（GitHub 每日趋势 2026-10-05：★1030，当日 +50）
- **归档**：`开源项目介绍/2026.10.5/EchoMuse.md`
- **标签**：`#python`

### [willfaust/Madeira](https://github.com/willfaust/Madeira)
- **定位**：在未越狱 iOS 上运行 x86-64 Windows PC 游戏的方案（FEX-Emu + Wine + DXMT）。
- **简介**：在未越狱 iOS 上运行 x86-64 Windows PC 游戏的方案（FEX-Emu + Wine + DXMT）。（GitHub 每日趋势 2026-09-28：★735，当日 +171）
- **归档**：`开源项目介绍/2026.9.28/Madeira.md`
- **标签**：`#c`

<a id="sec-22"></a>

## 🗺️ 二十二、地理信息 / GIS（1）

### [opengeos/GeoLibre](https://github.com/opengeos/GeoLibre)
- **定位**：云原生 GIS 平台
- **简介**：免费开源、轻量级云原生 GIS 平台：一套代码运行于浏览器、桌面（Tauri v2）、移动端和 Jupyter Notebook。内置 1000+ 地理处理工具（地形、水文等），全部基于 WebAssembly 在浏览器本地运行，数据不上传保障隐私。支持行星制图（火星/月球）、OGC SLD/QGIS QML 符号系统互操作、GeoPackage/PostGIS 可编辑图层。MIT 协议，897 commits，2026-07 最新更新（时间滑块 1.8.3）。
- **归档**：`开源项目介绍/2026.9.6/GeoLibre.md`
- **标签**：`#gis` `#webassembly` `#云原生` `#tauri`

---

<a id="sec-23"></a>

## 📰 二十三、文章收藏 / AI 动态（8）

### [4 个高频 Obsidian 插件推荐](https://mp.weixin.qq.com/s/WWEhZmheiqH00UepUxF-MQ)
- **来源**：公众号「陌晨」｜ **主题**：Obsidian 插件 / 工具推荐
- **归档**：`开源项目介绍/2026.8.16/4个高频Obsidian插件推荐.md`（含全文）
- **要点**：Obsidian 存本地、轻量化、可扩展，支持与 codex / claude code 无缝衔接。4 个高频插件：**claudian**（侧边栏无缝使用 Claude code / codex，最多 10 个聊天窗口，双端互通无链路摩擦）；**MP Publisher 公众号编辑器**（markdown 实时公众号预览，多模板、自定义 CSS、图片带入并发布到公众号草稿箱，无需模型烧 token 渲染）；**editing Toolbar**（markdown 常用菜单固定页眉，忘语法随时可查）；**Web Clipper**（剪藏文档/页面/公众号文章到 Obsidian 知识库，盘活收藏功能）。
- **标签**：`#obsidian` `#插件` `#工具`

### [AI 辅助 CAD 绘图：用豆包等大模型画 CAD 及图片转图纸](https://mp.weixin.qq.com/s/LtfnWK9bcjcshaFYXncH3A)
- **来源**：微信公众号 ｜ **主题**：AI 绘图 / CAD 自动化
- **归档**：`其它文章/2026.9.18/AI辅助CAD绘图.md`（含全文）
- **要点**：通过「本地电脑模式」让大模型（豆包、Codex、Claude 等）直接操控已打开的 CAD 软件绘图，支持图片转 CAD 图纸。操作仅需两句话：创建 CAD 制图 skill → 转换图片为 CAD。不同模型精细度不同，可要求细化补充。GitHub/Gitee 上已有开源 skill，最火的是 **Autocad DWG Redraw**（操控电脑画图），也可自训 skill 或开发插件。
- **标签**：`#ai绘图` `#cad` `#skill` `#图片转cad`

### [办公小浣熊桌面端：本地 Agent 接入飞书 / Obsidian](https://mp.weixin.qq.com/s/FT39-5mEAkAdWZVs18N5uQ)
- **来源**：公众号「逛逛 GitHub」｜ **主题**：AI 办公产品
- **归档**：`其它文章/2026.8.18/办公小浣熊桌面端发布.md`（含全文）
- **要点**：办公小浣熊桌面端正式发布（macOS/Windows），可直接调用本地文件、历史对话、Obsidian 笔记、飞书文档发起任务，内置 5+ 款模型并接入 DeepSeek-V4-Pro。五个亮点：①**@ 引入上下文**（本地文件/历史会话/Obsidian 笔记）+ **Quick Bar**（选中内容按 ⌘K/Ctrl+K 唤起 AI）；②**Skills 技能系统**（artifacts-builder、可交互的深度研究 skill 等一键安装）+ 多智能体专家团；③**连接第三方应用**（飞书、钉钉、Obsidian，结果可导出飞书文档）；④**本地记忆**（记住职业背景、文档偏好，越用越懂你）；⑤**定时任务**（可绑定本地文件/飞书文档等数据源），形成「到点触发 → 获取资料 → 技能分析 → 生成报告 → 沉淀协作平台」的自动化链路。
- **标签**：`#办公ai` `#本地agent` `#定时任务`

### [DeepSeek Harness：一切皆插件](https://mp.weixin.qq.com/s/jcJh2z2OJ8Sc892syfa8ng)
- **来源**：公众号「逛逛 GitHub」｜ **主题**：AI Agent 框架
- **要点**：DeepSeek 首款 Agent 产品，核心理念「一切皆插件」（Everything is a Plugin）。Agent = Model + Harness，底层 Cordis 只负责插件的加载、卸载与依赖，模型、工具、技能、会话、沙箱、存储、循环、调度乃至界面全部可插拔。开源约两天即冲过 10 万+ Star。安装：`npx @deepseek-ai/dsh web`，默认地址 http://127.0.0.1:3080，内置标准/PTC/极简/创造四套模式，轨迹视图可查看每轮工具调用与耗时。
- **标签**：`#deepseek` `#agent` `#插件化`

### [DSH Desktop：Harness 桌面客户端](https://mp.weixin.qq.com/s/qneGR9yZjNmtwKHJFuPPZw)
- **来源**：公众号「逛逛 GitHub」｜ **主题**：桌面应用 / 社区开源（MIT）
- **GitHub**：https://github.com/dataelement/dsh-desktop ｜ **官网**：https://www.dshdesktop.com/
- **要点**：社区开发的 DeepSeek Harness 桌面客户端（MIT 协议，非官方），支持 macOS/Windows 一键安装，免去命令行操作。特色：Preset 广场（通用 Agent + Preset = 专业 Agent，比 Skill 更底层的可配置组合）、多模型支持（DeepSeek/OpenAI/Anthropic/Gemini，可接 OpenRouter）、Agent 配置可导出 .dshpreset 文件跨机分享。对话与设置保存在本地，API Key 存放于系统密钥库。
- **标签**：`#桌面应用` `#preset` `#多模型`

### [商汤 SenseNova U1.5 Lite：轻量级原生统一多模态模型开源](https://mp.weixin.qq.com/s/k4GIcf7Trw8W4kcngACsNw)
- **来源**：商汤科技（公众号）｜ **主题**：多模态大模型 / 开源
- **归档**：`开源项目介绍/2026.8.24/SenseNova-U1.5-Lite.md`（含全文）
- **要点**：商汤正式开源轻量级原生统一多模态大模型 **SenseNova U1.5 Lite**（8B 参数），聚焦真实视觉创作交付。核心能力：3-4k 字符超长复杂指令遵循（多数开源模型 1k 字符即崩溃）、原生 4K 高清输出、原生图像编辑（局部修改/元素替换/文字精修/多参考图融合）、中英文文字与复杂布局、Bounding Box/Visual Marker 精细控制。架构基于 NEO-unify 统一架构 + MOPD 多专家在线策略蒸馏（训练期多专家、交付期无损融合进单体 8B），单卡可跑、无需 Router，极致性价比；RL 后训练聚焦指令遵循/视觉偏好/编辑保持。GitHub：OpenSenseNova/SenseNova-U1。
- **标签**：`#商汤` `#多模态` `#图像生成` `#开源模型`

### [WPF 开源 UI 框架选型指南](其它文章/2026.9.26/WPF开源UI框架选型指南.md)
- **来源**：AI 会话整理 · 用户收藏｜ **主题**：WPF UI 框架选型
- **要点**：8 个 WPF 开源 UI 框架的推荐清单与快速选型表：WPF UI（Win11 Fluent / Mica / SnapLayout）、HandyControl（企业级、80+ 控件、中文文档）、MaterialDesignInXamlToolkit（Google MD3、主题热重载）、MahApps.Metro（老牌 Metro、MetroWindow）、Panuon.WPF.UI（附加属性改样式、零模板门槛）、Rubyer（亮暗一键切换、Gitee 主站）、Layui-WPF（Layui 风格移植、快速搭后台）、Fluent.Ribbon（Office 风格工具栏）；附「需求场景 → 推荐框架」六行选型对照表。收录时已逐库核对 stars/协议/最新版本（2026-09-26 实测），并连同 MicaWPF、ModernWPF、UI.WPF.Modern、TopazWPF 4 个补充库共 12 个 WPF 库全部登记入「六、桌面应用 / UI 框架」分区。
- **归档**：`其它文章/2026.9.26/WPF开源UI框架选型指南.md`
- **标签**：`#wpf` `#ui框架` `#选型指南`

### [智谱 GLM-5.3：后训练之王](https://mp.weixin.qq.com/s/1gXdfR6KU0Q4iyU8XR19RQ)
- **来源**：公众号「逛逛 GitHub」｜ **主题**：大模型 / 网络安全
- **体验入口**：https://zcode.z.ai/cn
- **要点**：智谱最新基座模型：沿用 GLM-5.2 同一基座、参数不增，仅靠继续加码后训练，在 Z.ai Code Bench 上提升 50%。最大亮点是网络安全能力——发布前两周联合国内安全团队发现 2404 个潜在漏洞（1088 个中高危，覆盖 220 个项目），包括潜伏 40 多年的 DNS 协议级风险（1983 年形成，特定请求可将计算压力放大近 8 万倍）与三枚微软重大漏洞。
- **标签**：`#glm` `#网络安全` `#开源模型`

<a id="sec-24"></a>

## 📚 二十四、开发者资源 / 精选合集（39）

### [Alban1911/Rose](https://github.com/Alban1911/Rose)
- **定位**：英雄联盟（League of Legends）相关解锁工具。
- **简介**：英雄联盟（League of Legends）相关解锁工具。（GitHub 每日趋势 2026-09-26：★582，当日 +21）
- **归档**：`开源项目介绍/2026.9.28/Rose.md`
- **标签**：`#python`

### [ardalis/CleanArchitecture](https://github.com/ardalis/CleanArchitecture)
- **定位**：Clean Architecture 解决方案模板：经过验证的 ASP.NET Core 10 架构范本。
- **简介**：Clean Architecture 解决方案模板：经过验证的 ASP.NET Core 10 架构范本。（GitHub 每日趋势 2026-10-01：★18498，当日 +3）
- **归档**：`开源项目介绍/2026.10.1/CleanArchitecture.md`
- **标签**：`#csharp`

### [Arindam200/awesome-ai-apps](https://github.com/Arindam200/awesome-ai-apps)
- **定位**：132 个 LLM 应用实战示例合集（RAG · Agents · Workflows）
- **简介**：不是纯链接列表，而是**可跑代码**的综合合集——**132 个项目**、教程和配方，覆盖文本 Agent、语音助手、RAG 应用和 MCP 支持的工具，给使用各种 AI 框架与技术栈的开发者当实操指南。分类构成一条清晰的进阶路径：**Starter Agents**（最小可跑通）→ **Simple Agents**（单一职责）→ **Voice Agents**（语音助手）→ **MCP Agents**（基于 Model Context Protocol）→ **Memory Agents**（带记忆）→ **RAG Applications** → **Advanced Agents**（多步推理与工具编排）→ **Fine-Tuning**（微调），另配 **Tutorials & Videos**。用法建议很直接：学 RAG 怎么落地就看 RAG 分类的可跑代码；学 Agent 架构分层就顺着 Starter→Simple→Memory→MCP→Advanced 走；找语音 Agent 参考实现看 Voice Agents；学微调流程看 Fine-Tuning。项目带 `hacktoberfest` topic，适合找入门贡献机会。赞助商含 Bright Data、Nebius Token Factory、ScrapeGraphAI、Memori（SQL 原生 AI 记忆层）。Python，MIT，**15,883 stars** / 1,832 forks，2025-02 创建，Trendshift 上榜并带 [Awesome](https://awesome.re) 认证徽章，2026-09-18 仍在更新。
- **归档**：`开源项目介绍/2026.9.23/awesome-ai-apps.md`
- **标签**：`#合集` `#rag` `#agent` `#mcp` `#教程` `#可跑代码`

### [BepInEx/BepInEx](https://github.com/BepInEx/BepInEx)
- **定位**：Unity/XNA 游戏补丁与插件框架（Mod 生态基石）。
- **简介**：Unity/XNA 游戏补丁与插件框架（Mod 生态基石）。（GitHub 每日趋势 2026-10-06：★8778，当日 +5）
- **归档**：`开源项目介绍/2026.10.8/BepInEx.md`
- **标签**：`#csharp`

### [bobeff/open-source-games](https://github.com/bobeff/open-source-games)
- **定位**：开源游戏与商业游戏开源重制的精选清单
- **简介**：一份**开源电子游戏**及**商业游戏开源重制版**的清单，按 17 个游戏类型组织（动作 / 冒险 / 商业大亨 / 城市建设 / 第一人称 / 平台跳跃 / 解谜 / 竞速 / 即时战略 / Roguelike / RPG / 沙盒 / 射击 STG / 体育 / 第三人称 / 塔防 / 回合制战略）+ Other lists 外链区。双重价值：**可以直接玩**（大量条目是完整可玩的成品游戏，不是引擎或 demo），**也可以直接读源码学**——尤其那些经典商业游戏的开源重制项目（OpenTTD、OpenRCT2、OpenLoco、CorsixTH 等），是学习「一个完整商业级游戏如何组织代码」的极佳材料。条目格式统一为「**[项目名](官网)** - 一句话简介。[[source]](源码仓库)」，官网与源码双链接齐全。特别值得一提的是**逆向工程重制**类（学习价值最高）：《塞尔达传说：黄昏公主》被反编译成人类可读可修改的源码（zeldaret/tp）、《众神的三角力量》的逆向克隆（snesrev/zelda3）；以及经典模拟经营重制四件套 OpenTTD / OpenRCT2 / OpenLoco / CorsixTH。托管平台以 GitHub 为主，也有 Codeberg（如 Hurry Curry!）。**协议是 CC0-1.0**（放弃版权、公有领域贡献），可自由引用转载。⚠️ 更新频率不高（最近推送 2026-02），但作为「找开源游戏玩 / 找游戏源码学」的索引依然好用。**15,323 stars** / 1,272 forks，2021-09 创建。
- **归档**：`开源项目介绍/2026.9.23/open-source-games.md`
- **标签**：`#游戏` `#合集` `#开源重制` `#cc0` `#学习资源`

### [bojieli/ai-agent-book](https://github.com/bojieli/ai-agent-book)
- **定位**：《深入理解 AI Agent：设计原理与工程实践》开源教材（李博杰 著 · 10 章 + 109 个实验）
- **简介**：围绕核心公式 **Agent = LLM + 上下文 + 工具**，10 章从原理讲到生产实战，全书正文、配图、**109 个配套实验**全部开源（含本地项目与外部复现轨道）。**已升级到 2.0 版**（相较 1.4 版）：把原第四章「异步交互」与原第九章「多模态 Agent」合并重组为新的**第六章「交互：观察与动作空间的扩展」**（异步与事件驱动、语音交互、Computer Use、机器人操作），原第六/七/八章依次后移为第七/八/九章——若手上是旧版 PDF 建议重新下载。十章结构与实验数：①AI Agent 入门（4）②上下文工程：KV Cache/提示工程/Agent Skills/上下文压缩（10）③用户记忆和知识库：RAG/结构化索引/知识图谱（12）④工具：MCP 协议 + 感知/执行/协作三类工具与主动工具发现（5）⑤Coding Agent 与通用 Agent：「代码是能创造新工具的工具」（16）⑥交互：观察与动作空间的扩展（14）⑦Agent 的评估：评估环境/指标/统计显著性/评估驱动选型（14）⑧模型后训练：预训练/SFT/RL 三阶段，何时选 SFT 何时选 RL、工具调用内化、样本效率（19）⑨Agent 的持续进化：从运行轨迹获得学习信号，更新知识/指令/程序/参数（9）⑩多 Agent 协作：协作框架、上下文共享与隔离、涌现的「Agent 社会」（6）。**15 种语言**社区翻译（中/英/西/印尼/阿/繁中/俄/泰米尔/越/日/土耳其/韩/匈牙利/希伯来/葡(巴西)），提供 PDF + EPUB 下载（链接始终指向 main 分支最新构建）和[在线阅读](https://bojieli.github.io/ai-agent-book/astro/)（多语言切换、章节折叠、高亮笔记、实验直达，每次推送自动重建）。自行编译需 pandoc + xelatex + ElegantBook，`cd book && bash build_pdf.sh`。**姊妹篇《深入理解 AI Infra：量化分析与系统设计》已开源**（[bojieli/ai-infra-book](https://github.com/bojieli/ai-infra-book)）。实验统一支持 Python 3.11–3.13，`uv sync --locked --extra ch1` 按章安装（未装 uv 用 `pip install -e ".[ch1]"`），凭据走 `.env`，仅当实验 README/CLI 明确列出 `ollama` 时才可 `--provider ollama` 用本地模型。Apache-2.0，**50,071 stars** / 5,612 forks，GitHub Trending Project of the Day。
- **归档**：`开源项目介绍/2026.9.16/ai-agent-book.md`
- **标签**：`#教材` `#开源书籍` `#agent` `#实验` `#多语言` `#上下文工程`

### [bregman-arie/devops-exercises](https://github.com/bregman-arie/devops-exercises)
- **定位**：DevOps/Linux/云计算面试题大全，覆盖 Linux、AWS、Docker、K8s、网络等主题。
- **简介**：DevOps/Linux/云计算面试题大全，覆盖 Linux、AWS、Docker、K8s、网络等主题。（GitHub 每日趋势 2026-09-26：★84660，当日 +64）
- **归档**：`开源项目介绍/2026.9.27/devops-exercises.md`
- **标签**：`#python`

### [byoungd/up](https://github.com/byoungd/up)
- **定位**：「人生进阶指南」：涵盖 AI 学习、英语学习等方向的长线个人成长知识库（韩先凯维护）。
- **简介**：「人生进阶指南」：涵盖 AI 学习、英语学习等方向的长线个人成长知识库（韩先凯维护）。（GitHub 每日趋势 2026-09-29：★64578，当日 +310）
- **归档**：`开源项目介绍/2026.9.29/up.md`
- **标签**：`#javascript`

### [cs341-illinois/coursebook](https://github.com/cs341-illinois/coursebook)
- **定位**：伊利诺伊大学开源的《系统编程导论》教材（CS 341 课程用书）。
- **简介**：伊利诺伊大学开源的《系统编程导论》教材（CS 341 课程用书）。（GitHub 每日趋势 2026-09-29：★2416，当日 +316）
- **归档**：`开源项目介绍/2026.9.29/coursebook.md`
- **标签**：`#tex`

### [Cysharp/UniTask](https://github.com/Cysharp/UniTask)
- **定位**：Unity 高性能零分配的 async/await 集成库。
- **简介**：Unity 高性能零分配的 async/await 集成库。（GitHub 每日趋势 2026-09-26：★11217，当日 +1）
- **归档**：`开源项目介绍/2026.9.27/UniTask.md`
- **标签**：`#csharp`

### [datawhalechina/hello-agents](https://github.com/datawhalechina/hello-agents)
- **定位**：《从零开始构建智能体》——Datawhale 出品的智能体原理与实践教程（★82K）。
- **简介**：《从零开始构建智能体》——Datawhale 出品的智能体原理与实践教程（★82K）。（GitHub 每日趋势 2026-10-10：★82247，当日 +193）
- **归档**：`开源项目介绍/2026.10.10/hello-agents.md`
- **标签**：`#python`

### [django/django](https://github.com/django/django)
- **定位**：老牌 Python Web 框架——给有截止日期的完美主义者。
- **简介**：老牌 Python Web 框架——给有截止日期的完美主义者。（GitHub 每日趋势 2026-09-28：★91210，当日 +27）
- **归档**：`开源项目介绍/2026.9.28/django.md`
- **标签**：`#python`

### [EbookFoundation/free-programming-books](https://github.com/EbookFoundation/free-programming-books)
- **定位**：免费编程书籍大合集，覆盖各语言与主题的经典清单。
- **简介**：免费编程书籍大合集，覆盖各语言与主题的经典清单。（GitHub 每日趋势 2026-09-28：★397950，当日 +169）
- **归档**：`开源项目介绍/2026.9.28/free-programming-books.md`
- **标签**：`#python`

### [Effect-TS/effect](https://github.com/Effect-TS/effect)
- **定位**：用 TypeScript 构建生产级应用的工具库（Effect 生态核心）。
- **简介**：用 TypeScript 构建生产级应用的工具库（Effect 生态核心）。（GitHub 每日趋势 2026-10-03：★16467，当日 +76）
- **归档**：`开源项目介绍/2026.10.3/effect.md`
- **标签**：`#typescript`

### [freestylefly/awesome-gpt-image-2](https://github.com/freestylefly/awesome-gpt-image-2)
- **定位**：GPT-Image2/2.5 工业级提示词引擎与模板库 · 544 个逆向案例 + 20+ 套模板 + Agent Skill
- **简介**：「苍何」维护的 **Prompt as Code** 资产库。它抓的痛点很准：GPT-Image2 普及后，出图瓶颈从「**能不能生成**」变成「**能不能稳定、可控、可复用地生成**」，而社区爆款案例多是**散文式提示词**——抄一次能用一次，无法批量、无法交给脚本和 Agent。仓库把 **544 个案例全部逆向拆解，压缩成结构化协议**：主体、光照、材质、布局、视觉细节拆为**可组合的原子 schema**，再按 **13 类场景**沉淀模板——UI 界面 73、海报排版 90、摄影写实 78、插画艺术 59、信息图表 53、电商产品 42、角色 31、品牌 Logo 27、场景叙事 21、历史国风 16、建筑空间 12、文档出版 11。配套 **gpt-image2.canghe.ai** 可视化站点，新增 **GPT-Image 2.5 专区**覆盖 Sunburst（生成+精准编辑）与 Flare（快速日常生成）双模型，提供同提示词可拖拽对比。**最有工程价值的设计**是 Agent Skill `gpt-image-2-style-library`（已发 npm 与 GitHub Packages）**与网站共用同一份 `data/style-library.json`**，避免了「文档一套、代码一套」的割裂；支持 `npx skills add` 与 Claude Code 插件市场两种安装路径。站点技术栈是完整的 SaaS 形态：**Vite + Vercel + Supabase（Google OAuth、8 份 migration）+ Stripe 与支付宝双支付（$5/300 credits）+ APIMart 异步生成 API + GA4**。版权立场写得克制：源自 YouMind、OpenNana 启发，保留原始出处，第三方遵循 **CC BY 4.0**，**明确不保证可商用**。MIT，JavaScript，仓库约 215MB（主要是案例图），**32,718 stars** / 3,160 forks / 132 watchers，2026-04-25 建仓，2026-09-11 最近推送，Trendshift 收录。**star/fork 比约 10:1，是典型实用型资源库曲线**。
- **归档**：`开源项目介绍/2026.9.23/awesome-gpt-image-2.md`
- **标签**：`#提示词工程` `#gpt-image` `#合集` `#agent-skill` `#ai设计`

### [Goob-Station/Goob-Station](https://github.com/Goob-Station/Goob-Station)
- **定位**：SS14（太空站 14）的开源社区分支服务器，主打随机玩法。
- **简介**：SS14（太空站 14）的开源社区分支服务器，主打随机玩法。（GitHub 每日趋势 2026-09-28：★236，当日 +0）
- **归档**：`开源项目介绍/2026.9.28/Goob-Station.md`
- **标签**：`#csharp`

### [harvard-edge/cs249r_book](https://github.com/harvard-edge/cs249r_book)
- **定位**：哈佛 CS249r 教材《机器学习系统》四卷本：基础、规模化、Agentic AI 与物理 AI。
- **简介**：哈佛 CS249r 教材《机器学习系统》四卷本：基础、规模化、Agentic AI 与物理 AI。（GitHub 每日趋势 2026-09-30：★28715，当日 +62）
- **归档**：`开源项目介绍/2026.9.30/cs249r_book.md`
- **标签**：`#python`

### [jamwithai/production-agentic-rag-course](https://github.com/jamwithai/production-agentic-rag-course)
- **定位**：生产级 Agentic RAG 课程（Jam with AI 出品）。
- **简介**：生产级 Agentic RAG 课程（Jam with AI 出品）。（GitHub 每日趋势 2026-10-03：★9325，当日 +192）
- **归档**：`开源项目介绍/2026.10.4/production-agentic-rag-course.md`
- **标签**：`#python`

### [jasontaylordev/CleanArchitecture](https://github.com/jasontaylordev/CleanArchitecture)
- **定位**：ASP.NET Core 的 Clean Architecture 解决方案模板（经典版）。
- **简介**：ASP.NET Core 的 Clean Architecture 解决方案模板（经典版）。（GitHub 每日趋势 2026-10-02：★20619，当日 +10）
- **归档**：`开源项目介绍/2026.10.2/CleanArchitecture.md`
- **标签**：`#csharp`

### [kelseyhightower/kubernetes-the-hard-way](https://github.com/kelseyhightower/kubernetes-the-hard-way)
- **定位**：Kelsey Hightower 的经典教程：纯手工从零引导 Kubernetes，不用脚本、理解每一步。
- **简介**：Kelsey Hightower 的经典教程：纯手工从零引导 Kubernetes，不用脚本、理解每一步。（GitHub 每日趋势 2026-09-26：★50056，当日 +105）
- **归档**：`开源项目介绍/2026.9.28/kubernetes-the-hard-way.md`
- **标签**：`#开源`

### [liquidslr/system-design-notes](https://github.com/liquidslr/system-design-notes)
- **定位**：《系统设计面试——内行指南》一书的学习笔记。
- **简介**：《系统设计面试——内行指南》一书的学习笔记。（GitHub 每日趋势 2026-10-09：★24422，当日 +398）
- **归档**：`开源项目介绍/2026.10.9/system-design-notes.md`
- **标签**：`#开源`

### [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search)
- **定位**：本地运行的 AI 求职框架（基于 Claude Code）：评估职位、定制简历、写求职信、准备面试。
- **简介**：本地运行的 AI 求职框架（基于 Claude Code）：评估职位、定制简历、写求职信、准备面试。（GitHub 每日趋势 2026-09-30：★44450，当日 +138）
- **归档**：`开源项目介绍/2026.9.30/ai-job-search.md`
- **标签**：`#python`

### [MikuLeaks/MikuSB](https://github.com/MikuLeaks/MikuSB)
- **定位**：开源 C#/.NET 研究服务器模拟器，用于本地协议与网络实验。
- **简介**：开源 C#/.NET 研究服务器模拟器，用于本地协议与网络实验。（GitHub 每日趋势 2026-09-30：★729，当日 +7）
- **归档**：`开源项目介绍/2026.9.30/MikuSB.md`
- **标签**：`#csharp`

### [MUnique/OpenMU](https://github.com/MUnique/OpenMU)
- **定位**：MU Online MMORPG 的易用、可扩展、可定制服务端。
- **简介**：MU Online MMORPG 的易用、可扩展、可定制服务端。（GitHub 每日趋势 2026-10-09：★1201，当日 +2）
- **归档**：`开源项目介绍/2026.10.9/OpenMU.md`
- **标签**：`#csharp`

### [NawfalMotii79/PLFM_RADAR](https://github.com/NawfalMotii79/PLFM_RADAR)
- **定位**：开源低成本 10.5 GHz PLFM 相控阵雷达系统，硬件方案全部开放。
- **简介**：开源低成本 10.5 GHz PLFM 相控阵雷达系统，硬件方案全部开放。（GitHub 每日趋势 2026-09-29：★25690，当日 +145）
- **归档**：`开源项目介绍/2026.9.29/PLFM_RADAR.md`
- **标签**：`#plsql`

### [OpenRA/OpenRA](https://github.com/OpenRA/OpenRA)
- **定位**：开源即时战略游戏引擎，复刻红警等早期 Westwood 经典。
- **简介**：开源即时战略游戏引擎，复刻红警等早期 Westwood 经典。（GitHub 每日趋势 2026-09-28：★17444，当日 +5）
- **归档**：`开源项目介绍/2026.9.28/OpenRA.md`
- **标签**：`#csharp`

### [PowerShell/PowerShell](https://github.com/PowerShell/PowerShell)
- **定位**：跨平台 PowerShell——每个系统都能用。
- **简介**：跨平台 PowerShell——每个系统都能用。（GitHub 每日趋势 2026-10-03：★55568，当日 +14）
- **归档**：`开源项目介绍/2026.10.3/PowerShell.md`
- **标签**：`#csharp`

### [ppy/osu](https://github.com/ppy/osu)
- **定位**：开源节奏音乐游戏 osu!——rhythm is just a click away。
- **简介**：开源节奏音乐游戏 osu!——rhythm is just a click away。（GitHub 每日趋势 2026-09-26：★19168，当日 +17）
- **归档**：`开源项目介绍/2026.9.28/osu.md`
- **标签**：`#csharp`

### [practical-tutorials/project-based-learning](https://github.com/practical-tutorials/project-based-learning)
- **定位**：项目驱动学习教程合集：按语言分类、跟着做完整项目学编程（28 万星经典清单）。
- **简介**：项目驱动学习教程合集：按语言分类、跟着做完整项目学编程（28 万星经典清单）。（GitHub 每日趋势 2026-09-29：★285102，当日 +215）
- **归档**：`开源项目介绍/2026.9.29/project-based-learning.md`
- **标签**：`#python`

### [ProwlEngine/Prowl](https://github.com/ProwlEngine/Prowl)
- **定位**：MIT 协议开源 C# 3D 游戏引擎，Unity 风格、上手友好。
- **简介**：MIT 协议开源 C# 3D 游戏引擎，Unity 风格、上手友好。（GitHub 每日趋势 2026-09-28：★1218，当日 +1）
- **归档**：`开源项目介绍/2026.9.28/Prowl.md`
- **标签**：`#csharp`

### [public-apis/public-apis](https://github.com/public-apis/public-apis)
- **定位**：免费公共 API 合集大全
- **简介**：GitHub 最知名的免费 API 合集项目（MIT 协议，5,244 commits），由开源社区集体维护，覆盖各领域的免费公共 API。用途包括：开发者寻找可用 API 服务、项目原型开发快速找数据接口、了解各领域开放数据与服务、API 设计参考。按主题分类整理，自动化脚本验证维护。
- **归档**：`开源项目介绍/2026.9.6/public-apis.md`
- **标签**：`#api` `#开发者资源` `#免费` `#合集`

### [roflmuffin/CounterStrikeSharp](https://github.com/roflmuffin/CounterStrikeSharp)
- **定位**：用 C# 编写 CS2（Counter-Strike 2）服务器插件的框架。
- **简介**：用 C# 编写 CS2（Counter-Strike 2）服务器插件的框架。（GitHub 每日趋势 2026-09-26：★1361，当日 +3）
- **归档**：`开源项目介绍/2026.9.28/CounterStrikeSharp.md`
- **标签**：`#csharp`

### [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch)
- **定位**：从零动手构建 AI 工程核心组件的教学项目：自己实现、自己上线、边造边学。
- **简介**：从零动手构建 AI 工程核心组件的教学项目：自己实现、自己上线、边造边学。（GitHub 每日趋势 2026-09-26：★58074，当日 +828）
- **归档**：`开源项目介绍/2026.9.27/ai-engineering-from-scratch.md`
- **标签**：`#python`

### [Shubhamsaboo/awesome-llm-apps](https://github.com/Shubhamsaboo/awesome-llm-apps)
- **定位**：100+ AI Agent、Agent Skills 与 RAG 应用合集——免费开源。
- **简介**：100+ AI Agent、Agent Skills 与 RAG 应用合集——免费开源。（GitHub 每日趋势 2026-10-02：★140496，当日 +139）
- **归档**：`开源项目介绍/2026.10.2/awesome-llm-apps.md`
- **标签**：`#python`

### [SmartlyDressedGames/U3-SDK](https://github.com/SmartlyDressedGames/U3-SDK)
- **定位**：Unturned 游戏源代码：免费开源的僵尸生存沙盒游戏。
- **简介**：Unturned 游戏源代码：免费开源的僵尸生存沙盒游戏。（GitHub 每日趋势 2026-10-11：★3935，当日 +8）
- **归档**：`开源项目介绍/2026.10.11/U3-SDK.md`
- **标签**：`#csharp`

### [space-wizards/space-station-14](https://github.com/space-wizards/space-station-14)
- **定位**：太空站 14：关于太空站上猜疑与混乱的多人游戏（经典 SS13 重制）。
- **简介**：太空站 14：关于太空站上猜疑与混乱的多人游戏（经典 SS13 重制）。（GitHub 每日趋势 2026-10-07：★3850，当日 +2）
- **归档**：`开源项目介绍/2026.10.8/space-station-14.md`
- **标签**：`#csharp`

### [stride3d/stride](https://github.com/stride3d/stride)
- **定位**：Stride（原 Xenko）：免费开源的跨平台 C# 游戏引擎。
- **简介**：Stride（原 Xenko）：免费开源的跨平台 C# 游戏引擎。（GitHub 每日趋势 2026-10-06：★7844，当日 +3）
- **归档**：`开源项目介绍/2026.10.8/stride.md`
- **标签**：`#csharp`

### [tModLoader/tModLoader](https://github.com/tModLoader/tModLoader)
- **定位**：制作与游玩 Terraria Mod 的加载器（支持 1.4 及更早版本）。
- **简介**：制作与游玩 Terraria Mod 的加载器（支持 1.4 及更早版本）。（GitHub 每日趋势 2026-10-03：★5690，当日 +3）
- **归档**：`开源项目介绍/2026.10.3/tModLoader.md`
- **标签**：`#csharp`

### [vercel/next.js](https://github.com/vercel/next.js)
- **定位**：Vercel 出品的 React 全栈框架，服务端渲染、静态生成与路由的一体化方案。
- **简介**：Vercel 出品的 React 全栈框架，服务端渲染、静态生成与路由的一体化方案。（GitHub 每日趋势 2026-09-26：★142507，当日 +31）
- **归档**：`开源项目介绍/2026.9.27/next.js.md`
- **标签**：`#javascript`

<a id="sec-25"></a>

## 🚀 二十五、DevOps / 开发者工具（27）

### [actions/runner](https://github.com/actions/runner)
- **定位**：GitHub Actions 作业执行器（自托管 Runner）
- **简介**：GitHub 官方出品，**运行 GitHub Actions 工作流中一个作业（job）的应用程序**。GitHub 在托管虚拟环境里用它跑你的 Actions，你也可以**在自己环境里自托管**。自托管的价值在于：需要访问内网资源、需要特殊硬件（GPU/特定设备）、需要更快更便宜的构建、或出于合规不能让代码出内网——这些 GitHub 托管 runner 都做不到。Windows / macOS / Linux 三平台均有发布包，每个平台有独立的前置条件文档（`docs/start/envwin.md` / `envosx.md` / `envlinux.md`）。⚠️ **重要状态：本仓库当前不接受贡献**。官方表示资源正被分配到 Actions 的其他方向，因此暂不接受 PR；想了解功能进展要看 [GitHub 公开路线图](https://github.com/orgs/projects)。请求分流：问题与支持 → Community Discussions 的 Actions 分类；高优先级 bug → Discussions 或[支持团队](https://support.github.com/contact/bug-report)；安全问题 → 按 SECURITY.md 处理。**期间仍提供安全更新并修复重大破坏性变更**，也仍可在本仓库提 bug。C# / .NET，MIT，6,280 stars / 1,438 forks / 538 open issues，2019-04 创建，2026-09-22 仍在推送。 **🔄 2026-09-27 复核更新**：stars **6,277** / 1,436 forks / 541 open issues / 144 watchers，MIT，C#，最近推送 2026-09-21；仍维持「本仓库当前不接受贡献」的官方状态。
- **归档**：`开源项目介绍/2026.9.23/GitHubActionsRunner.md`（2026-09-27 已复核更新）
- **标签**：`#cicd` `#github-actions` `#self-hosted` `#devops` `#官方`

### [actions/runner-images](https://github.com/actions/runner-images)
- **定位**：GitHub 托管 Runner 的 VM 镜像定义与构建脚本仓库
- **简介**：actions/runner-images 是 **GitHub 托管 Runner（GitHub-hosted runners）所用 VM 镜像**的源代码与构建脚本仓库，由 GitHub 官方维护，**MIT** 协议，主语言 **PowerShell**，配合 **Packer** 生成三大平台标准化镜像。它定义了你写 `runs-on: ubuntu-latest/windows-latest/macos-latest` 时机器里预装的操作系统与工具链，同时为 Azure Pipelines 的 Microsoft 托管代理供镜像。镜像矩阵覆盖 Ubuntu 22.04/24.04/26.04（x64+Arm64）、Ubuntu Slim、macOS 14/15/26、Xcode 27（preview）、Windows Server 2022/2025、Windows 11 Arm64（含 VS2026），按周滚动更新，走 Beta→GA 生命周期，`-latest` 标签分 1–2 个月迁移到最新 GA，同刻最多维护 2 GA+1 Beta。**与 actions/runner（库内 [actions/runner](https://github.com/actions/runner)）的分工是关键**：runner 是 C#/.NET 写的执行器应用程序（领取并运行 job，托管/自托管都用它），runner-images 是托管 Runner 的镜像定义（OS+预装软件）——前者是「房子里干活的管家」，后者是「房子的图纸与精装清单」；本仓库由旧名 actions/virtual-environments 改名而来。规模数据（2026-09-27）：Stars ~13,296、Forks ~3,866、Open Issues 136、Subscribers 373、Commits ~7.3K，创建 2019-06-05，最近推送 2026-09-25，最新镜像发布 ubuntu22-arm64/20260920.137、win25/20260922.270。注意事项：无官网、无 topics；贡献者精确总数与 tags 总数因 GitHub API 限流未获取到（ungh/badgen 贡献者封顶显示 30），数据经 api.github.com、ungh.cc、badgen.net 交叉校验。
- **关联**：库内 [actions/runner](https://github.com/actions/runner)（执行器本体，本仓库是其托管镜像定义）
- **归档**：`开源项目介绍/2026.9.27/runner-images.md`
- **标签**：`#github-actions` `#cicd` `#runner-images` `#devops` `#packer`

### [caddyserver/caddy](https://github.com/caddyserver/caddy)
- **定位**：快速可扩展的多平台 HTTP/1-2-3 Web 服务器，自动 HTTPS。
- **简介**：快速可扩展的多平台 HTTP/1-2-3 Web 服务器，自动 HTTPS。（GitHub 每日趋势 2026-10-05：★76387，当日 +31）
- **归档**：`开源项目介绍/2026.10.5/caddy.md`
- **标签**：`#go`

### [dotnet/efcore](https://github.com/dotnet/efcore)
- **定位**：EF Core：.NET 的现代对象-数据库映射器，支持 LINQ 查询、变更追踪与架构迁移。
- **简介**：EF Core：.NET 的现代对象-数据库映射器，支持 LINQ 查询、变更追踪与架构迁移。（GitHub 每日趋势 2026-10-03：★14797，当日 +2）
- **归档**：`开源项目介绍/2026.10.3/efcore.md`
- **标签**：`#csharp`

### [dotnet/eShop](https://github.com/dotnet/eShop)
- **定位**：微软官方 .NET 参考应用：完整电商站点实现。
- **简介**：微软官方 .NET 参考应用：完整电商站点实现。（GitHub 每日趋势 2026-09-30：★10914，当日 +1）
- **归档**：`开源项目介绍/2026.9.30/eShop.md`
- **标签**：`#csharp`

### [dotnet/roslyn](https://github.com/dotnet/roslyn)
- **定位**：Roslyn .NET 编译器：为 C# 与 Visual Basic 提供丰富的代码分析 API。
- **简介**：Roslyn .NET 编译器：为 C# 与 Visual Basic 提供丰富的代码分析 API。（GitHub 每日趋势 2026-10-03：★20700，当日 +3）
- **归档**：`开源项目介绍/2026.10.3/roslyn.md`
- **标签**：`#csharp`

### [dotnet/sdk](https://github.com/dotnet/sdk)
- **定位**：.NET Core 项目创建的核心功能（Visual Studio 与 CLI 共用）。
- **简介**：.NET Core 项目创建的核心功能（Visual Studio 与 CLI 共用）。（GitHub 每日趋势 2026-10-05：★3217，当日 +1）
- **归档**：`开源项目介绍/2026.10.5/sdk.md`
- **标签**：`#csharp`

### [EpicGames/raddebugger](https://github.com/EpicGames/raddebugger)
- **定位**：Epic Games 出品：原生用户态多进程图形调试器。
- **简介**：Epic Games 出品：原生用户态多进程图形调试器。（GitHub 每日趋势 2026-10-08：★7789，当日 +82）
- **归档**：`开源项目介绍/2026.10.8/raddebugger.md`
- **标签**：`#c`

### [fastapi/fastapi](https://github.com/fastapi/fastapi)
- **定位**：FastAPI：高性能 Python Web 框架，易学、快写、生产就绪（★103K）。
- **简介**：FastAPI：高性能 Python Web 框架，易学、快写、生产就绪（★103K）。（GitHub 每日趋势 2026-10-11：★102968，当日 +56）
- **归档**：`开源项目介绍/2026.10.11/fastapi.md`
- **标签**：`#python`

### [git-ecosystem/git-credential-manager](https://github.com/git-ecosystem/git-credential-manager)
- **定位**：微软维护的跨平台 Git 凭据管理器，支持 GitHub/Azure/Bitbucket 等认证。
- **简介**：微软维护的跨平台 Git 凭据管理器，支持 GitHub/Azure/Bitbucket 等认证。（GitHub 每日趋势 2026-09-26：★9318，当日 +5）
- **归档**：`开源项目介绍/2026.9.28/git-credential-manager.md`
- **标签**：`#csharp`

### [JasperFx/wolverine](https://github.com/JasperFx/wolverine)
- **定位**：Wolverine：超级增强的 .NET 服务端开发框架。
- **简介**：Wolverine：超级增强的 .NET 服务端开发框架。（GitHub 每日趋势 2026-10-09：★2376，当日 +2）
- **归档**：`开源项目介绍/2026.10.9/wolverine.md`
- **标签**：`#csharp`

### [llvm/llvm-project](https://github.com/llvm/llvm-project)
- **定位**：LLVM 编译器基础设施：模块化可复用的编译器与工具链技术集合，Clang/Swift/Rust 等的底层。
- **简介**：LLVM 编译器基础设施：模块化可复用的编译器与工具链技术集合，Clang/Swift/Rust 等的底层。（GitHub 每日趋势 2026-09-26：★40703，当日 +29）
- **归档**：`开源项目介绍/2026.9.27/llvm-project.md`
- **标签**：`#cpp`

### [max-sixty/worktrunk](https://github.com/max-sixty/worktrunk)
- **定位**：为并行 AI Agent 工作流设计的 Git worktree CLI
- **简介**：**三个核心命令让 worktree 像 branch 一样好用**。问题背景很实在：Claude Code、Codex 这类 Agent 已能在无人监督下处理较长任务，**同时管理 5-10+ 个是可行的**；Git 原生 worktree 给每个 Agent 独立工作目录避免互踩，但**UX 很笨拙**——开个新 worktree 就要把分支名打三遍（`git worktree add -b feat ../repo.feat` 再 `cd ../repo.feat`）。Worktrunk 的做法是：**worktree 用分支名寻址，路径由可配置模板计算**，接受分支名的命令也接受该分支 checkout 的 worktree 路径。核心命令对比：切换 `wt switch feat`（原生要 `cd ../repo.feat`）· 创建并启动 Claude `wt switch -c -x claude feat`（原生要三条命令串起来）· 清理 `wt remove`（原生要 `cd` 回去 + `git worktree remove` + `git branch -d`）· 带状态列出 `wt list`（原生 `git worktree list` **只有路径**）。工作流自动化特性密度很高：**Hooks**（在 create / pre-merge / post-merge 等时机跑命令）· **LLM commit messages**（从 diff 生成）· **Merge workflow**（squash / rebase / merge / 清理**一条命令搞定**）· **Interactive picker**（浏览 worktree，带**流式 CI 状态**和 diff、log、PR、评论预览）· **共享构建缓存**（十个 worktree 都能拿到 `target/`、`node_modules/` 等，**既不用构建也不用拷贝**——靠 APFS / btrfs / XFS 的写时复制）· **`wt list --full`**（每分支的 CI 状态 + **AI 生成摘要**）· **PR checkout**（`wt switch pr:123` 直接跳到某 PR 的分支）· **每 worktree 一个 dev server**（`hash_port` 模板过滤器分配唯一端口）· **别名与 per-branch 变量**（自定义 `wt <name>` 命令 + 给 hook 模板用的分支作用域状态）。作者 max-sixty 在 2026-09 的说明里称它**已迅速成为最流行的 git worktree 管理器**，并强调「**there's no slop!**」（没有糊弄事），欢迎把感知到的任何摩擦反馈给他。Rust，**MIT OR Apache-2.0 双许可**（GitHub API 报 NOASSERTION），8,341 stars / 292 forks，2025-10 创建，文档站 [worktrunk.dev](https://worktrunk.dev)，2026-09-22 仍在推送。⚠️ 写时复制构建缓存依赖 APFS（macOS）/ btrfs / XFS（Linux）文件系统。
- **归档**：`开源项目介绍/2026.9.23/worktrunk.md`
- **标签**：`#git` `#worktree` `#并行agent` `#rust` `#cli` `#ci`

### [microsoft/aspire](https://github.com/microsoft/aspire)
- **定位**：微软的 .NET 云原生应用编排工具，代码优先、可扩展。
- **简介**：微软的 .NET 云原生应用编排工具，代码优先、可扩展。（GitHub 每日趋势 2026-09-26：★6324，当日 +3）
- **归档**：`开源项目介绍/2026.9.27/aspire.md`
- **标签**：`#csharp`

### [microsoft/vscode](https://github.com/microsoft/vscode)
- **定位**：微软开源的轻量级代码编辑器，扩展生态极其庞大，事实上的编辑器标准。
- **简介**：微软开源的轻量级代码编辑器，扩展生态极其庞大，事实上的编辑器标准。（GitHub 每日趋势 2026-09-26：★192997，当日 +78）
- **归档**：`开源项目介绍/2026.9.27/vscode.md`
- **标签**：`#typescript`

### [NethermindEth/nethermind](https://github.com/NethermindEth/nethermind)
- **定位**：以太坊节点的高性能执行客户端。
- **简介**：以太坊节点的高性能执行客户端。（GitHub 每日趋势 2026-10-03：★1608，当日 +0）
- **归档**：`开源项目介绍/2026.10.4/nethermind.md`
- **标签**：`#csharp`

### [nopSolutions/nopCommerce](https://github.com/nopSolutions/nopCommerce)
- **定位**：ASP.NET Core 开源电商软件：免费开源购物车平台。
- **简介**：ASP.NET Core 开源电商软件：免费开源购物车平台。（GitHub 每日趋势 2026-10-01：★10161，当日 +2）
- **归档**：`开源项目介绍/2026.10.1/nopCommerce.md`
- **标签**：`#csharp`

### [open-telemetry/opentelemetry-dotnet](https://github.com/open-telemetry/opentelemetry-dotnet)
- **定位**：OpenTelemetry .NET 官方客户端。
- **简介**：OpenTelemetry .NET 官方客户端。（GitHub 每日趋势 2026-10-03：★3761，当日 +0）
- **归档**：`开源项目介绍/2026.10.3/opentelemetry-dotnet.md`
- **标签**：`#csharp`

### [open-telemetry/opentelemetry-dotnet-contrib](https://github.com/open-telemetry/opentelemetry-dotnet-contrib)
- **定位**：OpenTelemetry .NET 的社区扩展组件集。
- **简介**：OpenTelemetry .NET 的社区扩展组件集。（GitHub 每日趋势 2026-09-26：★676，当日 +0）
- **归档**：`开源项目介绍/2026.9.28/opentelemetry-dotnet-contrib.md`
- **标签**：`#csharp`

### [openbao/openbao](https://github.com/openbao/openbao)
- **定位**：HashiCorp Vault 的开源分叉，OpenSSF 社区治理的密钥与敏感数据管理平台
- **简介**：**OpenBao** 是 HashiCorp Vault 的开源分叉，MPL-2.0 协议，官网 openbao.org，主语言 Go。**分叉背景**：2023 年 8 月 HashiCorp 将 Vault 从 MPL-2.0 转为 BUSL-1.1 非开源许可，社区随即于 2023-11-09 基于 Vault 的 MPL 版本代码建立分叉；**治理方**为 Linux 基金会旗下开源安全基金会（OpenSSF），由技术指导委员会（TSC）及 namespaces、PKCS#11、scalability、supply、UI 等专项工作组按开放治理原则运作，承诺以 OSI 认可的开源许可持续演进，漏洞走 openbao-security@lists.openssf.org 负责任披露。核心能力：安全密钥存储（key/value 加密后落盘，支持磁盘与 PostgreSQL 后端）、动态密钥（为 AWS/SQL 按需签发临时凭证，租约到期自动吊销）、数据加密即服务（Transit 只加解密不存储）、租约续期、单密钥或整棵密钥树吊销、cert/kubernetes/userpass 等多种认证与插件化引擎生态。**v2.7.0 新亮点 External Keys**：PKI 与 Transit 引擎可经 /sys/external-keys 映射 HSM/KMS 托管密钥（含 PKCS#11 的 kms-pkcs11 插件）完成签名与加解密，密钥材料不落入 OpenBao 本体。技术栈：Go Modules 构建单一 bao 二进制，与 Vault API 高度兼容（请求头仍为 X-Vault-Request）；主仓含 Web UI 与官网文档子树，另发布 api/v2、sdk/v2 两个可导入库，但官方明确不支持将主仓整体作为 Go 库导入。规模数据：Stars 约 **7,998**、Forks 590、开放 issue 327、贡献者 **374**、commits 约 21,150（含继承自 Vault 的历史）、tags 215。时间线：创建 2023-11-09，最近推送 2026-09-24；**v2.7.0 与维护版 v2.6.3 于 2026-09-23 同日发布，均含多项安全修复**（agent/proxy quit 端点 X-Vault-Request 头校验 GHSA-8gmq-wv9h-fcwp、路径规范化 GHSA-fg5x-7whg-6c28、插件目录逃逸 GHSA-j6wc-jpvg-xfxq），旧版本用户应尽快升级。注意事项：提 PR 前必须阅读 CONTRIBUTING.md，否则大概率被拒；项目持 OpenSSF Scorecard 与 Best Practices 认证。
- **归档**：`开源项目介绍/2026.9.27/openbao.md`
- **标签**：`#secret-management` `#security` `#go` `#devops` `#vault-fork`

### [pardeike/Harmony](https://github.com/pardeike/Harmony)
- **定位**：运行时修补、替换和装饰 .NET 与 Mono 方法的库（Unity Mod 生态基石）。
- **简介**：运行时修补、替换和装饰 .NET 与 Mono 方法的库（Unity Mod 生态基石）。（GitHub 每日趋势 2026-10-01：★6677，当日 +3）
- **归档**：`开源项目介绍/2026.10.1/Harmony.md`
- **标签**：`#csharp`

### [psf/black](https://github.com/psf/black)
- **定位**：绝不妥协的 Python 代码格式化器。
- **简介**：绝不妥协的 Python 代码格式化器。（GitHub 每日趋势 2026-10-09：★41879，当日 +7）
- **归档**：`开源项目介绍/2026.10.9/black.md`
- **标签**：`#python`

### [quartznet/quartznet](https://github.com/quartznet/quartznet)
- **定位**：Quartz 企业级 .NET 任务调度库。
- **简介**：Quartz 企业级 .NET 任务调度库。（GitHub 每日趋势 2026-10-01：★7090，当日 +1）
- **归档**：`开源项目介绍/2026.10.1/quartznet.md`
- **标签**：`#csharp`

### [rakyll/hey](https://github.com/rakyll/hey)
- **定位**：HTTP 压测工具，ApacheBench (ab) 的现代替代品。
- **简介**：HTTP 压测工具，ApacheBench (ab) 的现代替代品。（GitHub 每日趋势 2026-09-30：★20425，当日 +31）
- **归档**：`开源项目介绍/2026.9.30/hey.md`
- **标签**：`#go`

### [sourcegit-scm/sourcegit](https://github.com/sourcegit-scm/sourcegit)
- **定位**：开源跨平台 Git GUI 客户端（Win / macOS / Linux）
- **简介**：开源、免费、**快**的三平台 Git 图形客户端，带可视化提交图、内置明暗双主题 + 自定义主题（社区主题在 [sourcegit-theme](https://github.com/sourcegit-scm/sourcegit-theme.git) 仓库）、**14 种语言**（含简繁中文、日语、韩语、泰米尔语等）、每个 remote 独立配置 SSH。Git 操作 GUI 化覆盖面很全：Clone/Fetch/Pull/Push、Merge/Rebase/Reset/Revert/Cherry-pick、Amend/Reword/Squash、**交互式 rebase**、Branches/Remotes/Tags/Stashes/Submodules/**Worktrees**/Archive、Diff、存为 patch/应用 patch、文件历史、Blame、Revision Diff、Branch Diff、**图片 Diff 三模式（Side-By-Side / Swipe / Blend）**。进阶能力：Git 命令日志（能看到实际执行的命令）、搜索提交、GitFlow、Git LFS、**Bisect**、Issue Link、Workspace、Custom Action、在 GitHub/GitLab/Gitea/Gitee/Bitbucket **创建 PR**、**用 AI 生成 commit message**、内置 conventional commit 助手。⚠️ Linux 仅在 Debian 12（X11 + Wayland）测过；**Windows 不支持 MSYS Git**，须用官方 Git for Windows；`git-flow` 自 Git for Windows 2.51.1 起不再随包发布，需手动装 git-flow-next 并改名。需 **Git >= 2.25.1**。安装渠道齐全：Windows `scoop install sourcegit`、macOS `brew install --cask sourcegit`（⚠️ Release 页的 macOS 包**全部未签名**，手动装需 `sudo xattr -cr`，担心安全可从 @ybeapps 的分发仓库取已签名包）、Linux 有 Codeberg 上的 deb/rpm 仓库。**便携模式**：在可执行文件旁建 `data` 文件夹即把设置/头像/日志存进去（仅 Windows 包与 Linux AppImage）。数据目录：Win `%APPDATA%\SourceGit`、Linux `${XDG_CONFIG_HOME}` + `${XDG_CACHE_HOME}`、macOS `~/Library/Application Support/SourceGit`。C# + Avalonia，MIT，6,012 stars / 510 forks / 185 open issues，2021-11 创建，2026-09-22 仍在推送。
- **归档**：`开源项目介绍/2026.9.23/SourceGit.md`
- **标签**：`#git` `#gui` `#跨平台` `#avalonia` `#devops` `#开发工具`

### [Tracer-Cloud/opensre](https://github.com/Tracer-Cloud/opensre)
- **定位**：构建你自己的 AI SRE Agent——AI 时代的开源运维工具箱。
- **简介**：构建你自己的 AI SRE Agent——AI 时代的开源运维工具箱。（GitHub 每日趋势 2026-10-03：★11337，当日 +23）
- **归档**：`开源项目介绍/2026.10.3/opensre.md`
- **标签**：`#python`

### [vercel-labs/scriptc](https://github.com/vercel-labs/scriptc)
- **定位**：Vercel 实验室的 TypeScript 编译为原生可执行文件的编译器。
- **简介**：Vercel 实验室的 TypeScript 编译为原生可执行文件的编译器。（GitHub 每日趋势 2026-09-28：★5279，当日 +76）
- **归档**：`开源项目介绍/2026.9.28/scriptc.md`
- **标签**：`#typescript`

---

## 🗂️ 待整理区

> 💡 新收藏的内容先放在这里，定期整理归类到对应分区。直接告诉 AI 助手「帮我把 XXX 加入知识库」即可追加。

*（暂无待整理内容）*

---

## 总结与趋势观察

1. **Agent Skills 生态爆发**：收录项目中 20+ 个直接围绕 AI 编程助手与 Agent 的能力扩展，「Skill 化」已成为 AI 工具链的核心范式——从文本润色、视频理解、知识蒸馏到图表生成、CAD 建模、手机操控，技能包覆盖越来越多的专业领域。**新趋势是「Skill 的输出形态本身也在被 Skill 化」**：i-have-adhd（约束 Agent 别把答案埋在客套话里）与 no-ai-slop（清除 20+ 种 AI 味写作套路）都不增加能力，而是**改造表达**——前者 5 万 star / 后者两个月破万 star，说明「AI 太啰嗦」是被严重低估的痛点。
2. **代码智能向图谱化演进**：code-review-graph 和 code-graph-rag 都采用 Tree-sitter + 知识图谱方案，目标是解决 AI 编码工具「全量读代码浪费 token」的痛点，精准上下文是下一代 AI 编程的关键。
3. **AI 操纵手机成为新热点**：MobiAgent、Mobile-Agent、Droidrun、AppAgent、mobile-use 等 5 个项目均通过「视觉理解屏幕 + ADB 执行 + 每步截图自检」的方式实现 AI 操控手机，多模态视觉模型是核心驱动力。
4. **本地优先与隐私保护**：OpenBiliClaw、ego-lite、GeoLibre、code-review-graph 等项目都强调数据本地存储、不上传云端，反映出用户对 AI 时代数据主权的重视。
5. **知识蒸馏成热门方向**：cangjie-skill、book-to-skill、colleague-skill 都在做「将非结构化知识转化为 AI 可调用的结构化 Skill」——书籍、视频、同事经验都在被「Skill 化」。
6. **AI 基础设施层完善**：OmniRoute（多模型路由）和 ego-lite（Agent 浏览器）代表了 AI 应用基础设施的成熟——统一接入、高效执行、资源隔离。
7. **本地推理的竞争焦点从「跑得快」转向「跑什么、怎么被 Agent 用」**：FreeToken 用**语义锚点缓存**为 Agent 的上下文编辑优化（工具调用/思考块插入不必重算前缀）、magnitude 用**硬件画像**替你选模型（先 profile 再预估 tok/s）、OmniVoice 把**零样本语音克隆**做到 600+ 语言 + RTF 0.0115。三者共同指向一个判断：**本地化的下一个战场不是吞吐量，而是「与 Agent 工作流的贴合度」**。
8. **Agent 正在成为操作系统与应用的一等公民**：omarchy 是最激进的样本——首启即引导设置默认 Agent、App 崩溃点通知就把 crash dump 交给 Agent 诊断、大量提交直接标注「Generated by Opus 4.8 in Claude Code」；**PR #8056 默认收回 docker 组权限改走 polkit 弹窗，是首批把「有 Agent 在本机执行代码」写进威胁模型的操作系统级决策**。同一思路也体现在 BrowserSkill（无人值守开关收归浏览器端、由被操作方而非 Agent 掌控）与 tech-leads-club/agent-skills（引用「开放市场 13.4% 技能含严重漏洞」做安全策展）——**权限与安全正从「附加功能」变成 Agent 时代的默认设计约束**。
9. **腾讯系在本批次集中出现**：BrowserSkill（Agent 浏览器桥）、Octop（自托管多用户多 Agent 平台）分别落子「Agent 工具链」与「Agent 编排层」，且 Octop 刻意**通过 ACP 把编码任务委派给 Claude Code / Codex 而非自造编码 Agent**——大厂开源的边界感比想象中清晰。
10. **经典项目依然是最好的工程教材**：microsoft/calculator（任意精度算法 + `GraphingInterfaces` 公共 API 划清专有引擎边界 + 货币数据用行星名 mock 规避授权）与 dotnet/maui（handler 抽象可直通原生 API）证明，**读系统级应用的源码，学到的是「工程边界怎么划」而不是「功能怎么实现」**。
