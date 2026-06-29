<h1 align="center">Ale Forensic Suite Toolkit 阿乐取证工具集</h1>
<p align="center">
  <strong>AI 赋能的取证工具集 · 开箱即用 · 数字取证 · 应急响应 · CTF 取证 · 安全分析</strong>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Digital%20Forensics-blue.svg">
  <img src="https://img.shields.io/badge/Platform-Windows%20VM-red.svg">
  <img src="https://img.shields.io/badge/AI-Powered-brightgreen.svg">
  <img src="https://img.shields.io/badge/Version-v20260629-orange.svg">
</p>

## 💡 项目愿景

**Ale Forensic Suite Toolkit（阿乐取证工具集，简称 AFST）**是一个专为取证人员打造的 **AI 赋能的开箱即用工具集成环境**。

### 🎯 核心价值

- **AI 赋能**：集成 Claude Code + IDA MCP + JADX MCP + 26+ CTF/安全 Skills，AI 辅助逆向分析与取证
- **开箱即用**：无需繁琐配置，一键启动所有取证工具
- **环境隔离**：虚拟机环境 + Python venv，避免工具污染主机系统
- **场景全覆盖**：支持电子数据取证、应急响应、CTF 取证、恶意代码分析
- **持续更新**：基于真实 WP 调研，优先更新高频实战工具

### 🔥 解决的痛点

1. **找工具难**：取证现场需要临时找工具，浪费宝贵时间
2. **环境污染**：工具安装卸载繁琐，重装系统后需要重新配置
3. **比武应急**：取证比武、竞赛、演练时需要快速部署标准化环境
4. **版本混乱**：工具版本不一致，依赖冲突难以解决
5. **分析瓶颈**：复杂样本分析耗时，缺少 AI 辅助效率低下
6. **技能缺口**：CTF 涉及多个方向，工具和技巧需要不断学习积累

## 🆕 20260629 更新说明

### ✨ AI 分析能力大幅增强

#### 🤖 Claude Code 深度集成
- **安装 Claude Code**：官方 AI 编程助手，支持代码分析、自动化脚本编写
- **Cursor AI 编辑器**：AI 驱动的代码编辑器，支持自然语言编程

#### 🔍 逆向分析 AI 加持
- **IDA Pro MCP 集成**：Claude 可直接调用 IDA 分析二进制文件
  - 支持函数分析、交叉引用查询、结构体解析
  - AI 辅助识别加密算法、恶意代码模式
- **JADX MCP 集成**：Claude 可直接分析 APK 文件
  - 自动反编译、代码搜索、组件分析
  - AI 辅助识别恶意行为、隐私泄漏

#### 📚 CTF 与安全技能库（26+ Skills）
集成四大技能仓库，Claude 自动调用相关技能：
1. **ctf-skills**（19 个技能）
   - 密码学、Web、Pwn、逆向、取证、Misc、OSINT、AI/ML 安全
2. **awesome-skills-security**（7 个工具技能）
   - 模糊测试、密码字典、Payload、WebShell、用户名字典
3. **secknowledge-skill**（中文安全知识库）
   - WooYun 88,636 真实漏洞案例
   - OWASP Top 10 + GAARM AI 风险框架
4. **SecSkills**（道一安全团队知识库）

### 🛠️ 新增核心取证工具

#### 📱 移动端取证
- **iLEAPP v0.15.0**：iOS 取证神器，支持 300+ 工件分析（GUI + CLI）
- **ALEAPP v4.1.0**：Android 取证工具，完整分析 Android 数据
- **Frida 16.7.19 + fridaUiTools**：动态分析框架，已配置雷电模拟器
- **JADX v1.5.5 + MCP**：APK 反编译，支持 AI 辅助分析

#### 💾 磁盘与内存取证
- **Arsenal Image Mounter**：镜像挂载工具，支持只读挂载
- **VeraCrypt v1.26.7**：加密卷管理与破解
- **AVML**：Linux 内存采集工具
- **DumpIt**：Windows 内存转储工具
- **Velociraptor v0.73**：端点取证与响应平台

#### 🔐 密码与加密分析
- **Passware Kit 2022**：商业级密码恢复工具
- **HashMyFiles**：文件哈希计算与校验
- **Navicat 密码查看器**：数据库密码解密
- **FinalShell 密码解密**：SSH 工具密码提取

#### 📊 数据分析与恢复
- **R-Studio v9.3**：专业数据恢复工具
- **万兴易修**：损坏文件修复工具
- **DBever CE**：通用数据库管理工具
- **SpaceSniffer**：磁盘空间可视化分析

#### 🌐 网络与流量分析
- **Zui (Brim)**：Zeek 日志分析工具，可视化流量分析
- **NetworkMiner**：网络取证分析工具
- **CTF-NetA**：CTF 流量分析工具包
- **ApacheLogsViewer**：Apache/IIS/Nginx 日志可视化分析工具

#### 🔬 恶意代码分析
- **Capa v7.5**：恶意软件能力检测工具
- **ImHex v1.35**：现代化十六进制编辑器
- **PEStudio v9.66**：PE 文件静态分析
- **YARA**：恶意软件模式匹配
- **Python 逆向工具**：pycdc、pyinstxtractor

#### 📁 文件取证工具
- **ExifTool + GUI**：元数据提取与分析
- **EFDD v2024**：邮件取证与分析
- **FileLocator Pro**：文件内容搜索
- **Document Tools**：Office 文档分析套件

#### 🔍 系统取证工具
- **Eric Zimmerman Tools**：Windows 取证工具全家桶
  - RECmd、PECmd、EvtxECmd、RegistryExplorer 等
- **Plaso (log2timeline)**：时间线分析工具
- **Hayabusa**：Windows 事件日志威胁狩猎
- **The Sleuth Kit**：文件系统取证工具包
- **Scalpel**：文件雕刻恢复工具

#### 🧰 应急响应工具
- **火绒剑**：行为监控与分析
- **PCHunter (系统工具)**：Rootkit 检测
- **Process Monitor**：进程监控工具
- **WebShellKiller**：Webshell 查杀
- **wywz**：恶意软件检测

#### 🎨 辅助工具
- **uTools**：效率工具集合（集成多个插件）
- **Recaf v4.0**：Java 字节码编辑器
- **离线经纬度查询**：GPS 坐标分析
- **星号密码查看器**：密码显示工具
- **RecentFile 查看器**：最近文件记录

### 🔧 系统优化与更新

#### 💻 基础软件更新
- **Windows 11 系统补丁**：更新至 2026 年 6 月最新版
- **Chrome 浏览器**：升级至 136.0.7103.114
- **KMS 激活工具**：更新至最新版本
- **Cherry Studio v1.3.12**：AI 聚合工具

#### 🔨 环境配置优化
- **ADB 全局命令**：永久添加到系统 PATH，无需手动配置
- **Python 虚拟环境**：所有工具独立 venv，避免依赖冲突
- **快捷启动脚本**：所有工具配备一键启动脚本
- **桌面快捷方式**：常用工具添加桌面图标

#### 📖 知识库建设
- **取证实录视频**：实战案例录像
- **取证知识库**：离线文档资料
- **在线书签库**：参考奶牛快传、CTF OS、PD 等平台资源

### 🚀 特色功能

#### 🤖 AI 取证分析工作流
```
1. 启动 JADX-GUI / IDA Pro
2. 打开待分析的 APK / EXE 文件
3. 在 Claude Code 中直接询问：
   - "分析这个 APK 的主要功能"
   - "查找可疑的加密函数"
   - "列出所有网络请求"
   - "识别这个函数的作用"
4. Claude 自动调用 MCP 工具，返回分析结果
```

#### 📱 移动端动态分析流程
```
1. 启动雷电模拟器
2. 运行 start_frida_ldplayer.ps1
3. 使用 Claude 辅助编写 Frida 脚本
```

#### 🔍 综合取证分析流程
```
1. 使用 iLEAPP/ALEAPP 快速提取工件
2. 用 Arsenal Image Mounter 挂载镜像
3. Eric Zimmerman Tools 分析 Windows 痕迹
4. Plaso 生成时间线
5. 使用 Claude 辅助编写分析报告
```

## 📂 项目说明

本仓库基于 [makoto56/penetration-suite-toolkit](https://github.com/makoto56/penetration-suite-toolkit) 二次开发，在原 Windows 安全工具虚拟机基础上，针对**数字取证、电子数据取证、应急响应、CTF Forensics、恶意代码分析**场景进行深度定制。

### 🎯 适用场景

- **电子数据取证**：手机取证、计算机取证、网络取证
- **应急响应**：入侵排查、日志分析、恶意代码分析
- **CTF 取证竞赛**：Misc、Forensics 方向题目环境
- **取证比武**：公安、司法、企业安全取证演练
- **安全培训**：取证技能培训、实验室环境搭建
- **恶意代码分析**：APK、EXE、内存 dump 分析

## 📊 调研依据

为避免"凭感觉加工具"，本仓库整理了取证 WP 与工具出现频率调研，作为工具更新依据：

- [取证 WP 与工具频率调研说明](research/forensics-tool-survey/README.md)
- [WP 原始链接表](research/forensics-tool-survey/wp_links.csv)
- [工具频率总表](research/forensics-tool-survey/tool_frequency_total.csv)
- [DIDCTF 工具数据库](research/forensics-tool-survey/didctf_tool_database.csv)

调研数据来自以下站点：
- [Yagami](https://www.yagami.vip)
- [西电取证平台](https://forensics.xidian.edu.cn)
- [DIDCTF 取证平台](https://forensics.didctf.com)

## 🔧 核心取证工具清单

### 🤖 AI 工具 (C:\Penetration\AiTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Claude Code** | 最新版 | Anthropic AI 编程助手，支持 MCP 协议 | [claude.ai](https://claude.ai/code) |
| **Cursor** | v0.50.5 | AI 代码编辑器 | [cursor.com](https://www.cursor.com/) |
| **CherryStudio** | v1.3.12 | AI 资源聚合工具 | [cherry-ai.com](https://www.cherry-ai.com/) |
| **CTF Skills** | 2026.06 | 26+ 安全技能库（CTF/取证/渗透） | 集成 |
| **IDA MCP Server** | v6.4.0 | IDA Pro MCP 集成，支持 AI 分析二进制 | 集成 |
| **JADX MCP Server** | v6.4.0 | JADX MCP 集成，支持 AI 分析 APK | 集成 |

### 📱 移动端取证 (C:\Penetration\AndroidTools & ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **iLEAPP** | v0.15.0 | iOS 取证神器，300+ 工件分析 | [GitHub](https://github.com/abrignoni/iLEAPP) |
| **ALEAPP** | v4.1.0 | Android 取证工具 | [GitHub](https://github.com/abrignoni/ALEAPP) |
| **JADX-GUI** | v1.5.5 | APK 反编译工具（含 MCP 插件） | [GitHub](https://github.com/skylot/jadx) |
| **Frida** | v16.7.19 | 动态插桩框架 | [frida.re](https://frida.re/) |
| **fridaUiTools** | 最新版 | Frida 图形化工具 | [GitHub](https://github.com/dqzg12300/fridaUiTools) |
| **雷电模拟器** | LDPlayer9 | 已配置 Root + Frida Server | [ldplayer.net](https://www.ldplayer.net/) |
| **AndroidKiller** | v1.3.1.0 | APK 综合分析工具 | - |
| **ApkToolPlus** | 最新版 | APK 反编译分析工具 | [GitHub](https://github.com/linchaolong/ApkToolPlus) |

### 💾 磁盘与镜像取证 (C:\Penetration\ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Arsenal Image Mounter** | 最新版 | 专业镜像挂载工具 | [Arsenal](https://arsenalrecon.com/) |
| **Autopsy** | v4.22.1 | 开源数字取证平台 | [autopsy.com](https://www.autopsy.com/) |
| **FTK Imager** | 最新版 | 镜像采集与查看 | [Exterro](https://www.exterro.com/ftk-imager) |
| **DiskGenius** | v5.6.1 | 磁盘管理与数据恢复 | [diskgenius.cn](https://www.diskgenius.cn/) |
| **R-Studio** | v9.3 | 专业数据恢复 | [r-studio.com](https://www.r-studio.com/) |
| **VeraCrypt** | v1.26.7 | 加密卷管理 | [veracrypt.fr](https://www.veracrypt.fr/) |
| **QEMU** | 2025.04.22 | 虚拟机镜像分析 | [qemu.org](https://www.qemu.org/) |

### 🧠 内存取证 (C:\Penetration\ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Volatility 2** | v2.6.1 | 经典内存取证框架 | [volatilityfoundation.org](https://volatilityfoundation.org/) |
| **Volatility 3** | v2.26.0 | 新一代内存取证框架 | [GitHub](https://github.com/volatilityfoundation/volatility3) |
| **MemProcFS** | v5.14 | 内存进程文件系统 | [GitHub](https://github.com/ufrisk/MemProcFS) |
| **WinPmem** | v4.0 | Windows 内存采集 | [GitHub](https://github.com/Velocidex/WinPmem) |
| **AVML** | 最新版 | Linux 内存采集 | [GitHub](https://github.com/microsoft/avml) |
| **DumpIt** | 最新版 | Windows 内存转储 | - |
| **LiME** | 最新版 | Linux 内存提取器（Kali） | [GitHub](https://github.com/504ensicsLabs/LiME) |
| **GhostWolf** | v1.1 | 内存敏感信息提取 | [GitHub](https://github.com/SickleSec/GhostWolf) |

### 🖥️ Windows 取证 (C:\Penetration\ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Eric Zimmerman Tools** | 最新版 | Windows 取证工具全家桶 | [ericzimmerman.github.io](https://ericzimmerman.github.io/) |
| **RegistryExplorer** | v2.1.0 | 注册表分析 | 包含在 EZ Tools |
| **EvtxECmd** | v1.5.2.0 | Windows 事件日志分析 | 包含在 EZ Tools |
| **Hayabusa** | 最新版 | 事件日志威胁狩猎 | [GitHub](https://github.com/Yamato-Security/hayabusa) |
| **Log Parser Studio** | v3.0 | 日志解析工具 | [Microsoft](https://techcommunity.microsoft.com/) |
| **NTFSStreamsEditor** | v2.0.2 | NTFS 数据流编辑 | [GitHub](https://github.com/studycpp/NtfsStreamsEditor) |
| **NTPWEdit** | v0.5 | SAM 文件编辑 | [GitHub](https://github.com/patrickgill/ntpwedit) |
| **Plaso (log2timeline)** | 最新版 | 时间线分析 | [GitHub](https://github.com/log2timeline/plaso) |

### 🌐 网络与流量取证 (C:\Penetration\TrafficTools & ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Wireshark** | v4.4.6 | 流量抓包分析 | [wireshark.org](https://www.wireshark.org/) |
| **NetworkMiner** | 最新版 | 网络取证分析 | [netresec.com](https://www.netresec.com/) |
| **Zui (Brim)** | 最新版 | Zeek 日志可视化 | [zui.brimdata.io](https://zui.brimdata.io/) |
| **CTF-NetA** | 最新版 | CTF 流量分析工具包 | - |
| **ApacheLogsViewer** | 最新版 | Apache/IIS/Nginx 日志可视化分析 | [NirSoft](https://www.nirsoft.net/utils/apache_logs_viewer.html) |

### 🔐 密码恢复与破解 (C:\Penetration\CrackTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Hashcat** | v6.2.6 | GPU 加速密码破解 | [hashcat.net](https://hashcat.net/) |
| **John the Ripper** | v1.9.0 | 密码破解工具 | [openwall.com](https://www.openwall.com/john/) |
| **Passware Kit** | 2022 | 商业级密码恢复（注册版） | [passware.com](https://www.passware.com/) |
| **HashMyFiles** | 最新版 | 文件哈希计算 | - |
| **HackBrowserData** | v0.4.6 | 浏览器数据解密 | [GitHub](https://github.com/moonD4rk/HackBrowserData) |
| **Navicat 密码查看器** | 最新版 | 数据库密码解密 | - |
| **FinalShell 密码解密** | 最新版 | SSH 工具密码提取 | - |

### 🔬 恶意代码分析 (C:\Penetration\ReverseTools & ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **IDA Pro** | v9.1 | 顶级逆向工具（注册版 + MCP） | [hex-rays.com](https://hex-rays.com/) |
| **Ghidra** | v11.3.2 | NSA 开源逆向工具 | [ghidra-sre.org](https://ghidra-sre.org/) |
| **x64dbg** | 2025 | 动态调试器 | [x64dbg.com](https://x64dbg.com/) |
| **Capa** | v7.5 | 恶意软件能力检测 | [GitHub](https://github.com/mandiant/capa) |
| **PEStudio** | v9.66 | PE 文件静态分析 | [winitor.com](https://www.winitor.com/) |
| **DetectItEasy** | v3.10 | 查壳工具 | [GitHub](https://github.com/horsicq/Detect-It-Easy) |
| **ImHex** | v1.35 | 现代十六进制编辑器 | [GitHub](https://github.com/WerWolv/ImHex) |
| **dnSpy** | v6.1.8 | .NET 逆向工具 | [GitHub](https://github.com/dnSpy/dnSpy) |
| **pycdc + pyinstxtractor** | 最新版 | Python 逆向工具 | - |

### 📁 文件分析与恢复 (C:\Penetration\ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **The Sleuth Kit** | 最新版 | 文件系统取证 | [sleuthkit.org](https://www.sleuthkit.org/) |
| **Scalpel** | 最新版 | 文件雕刻工具（Kali） | - |
| **Binwalk** | v3.1.0 | 固件与嵌入式文件分析 | [GitHub](https://github.com/ReFirmLabs/binwalk) |
| **ExifTool + GUI** | 最新版 | 元数据提取分析 | [exiftool.org](https://exiftool.org/) |
| **oletools** | v0.60.2 | OLE 文件分析 | [GitHub](https://github.com/decalage2/oletools) |
| **EFDD** | v2024 | 邮件取证与分析 | - |
| **FileLocator Pro** | 最新版 | 文件内容搜索 | - |
| **Document Tools** | 最新版 | Office 文档分析 | - |
| **万兴易修** | 最新版 | 损坏文件修复 | [wondershare.cn](https://wondershare.cn/) |
| **ImageStrike** | 最新版 | 图片分析工具 | - |

### 🗄️ 数据库取证 (C:\Penetration\DatabaseTools & ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **DBever Community Edition** | 最新版 | 通用数据库管理 | [dbeaver.io](https://dbeaver.io/) |
| **Navicat Premium** | v17.1.12 | 数据库管理（注册版） | [navicat.com](https://www.navicat.com/) |
| **SQLite Browser** | 最新版 | SQLite 查看编辑 | [sqlitebrowser.org](https://sqlitebrowser.org/) |
| **HeidiSQL** | v12.10 | 轻量数据库工具 | [heidisql.com](https://www.heidisql.com/) |

### 🛡️ 应急响应工具 (C:\Penetration\ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Velociraptor** | v0.73 | 端点取证与响应 | [docs.velociraptor.app](https://docs.velociraptor.app/) |
| **FireKylin** | v1.4.0 | 系统痕迹采集 | [GitHub](https://github.com/MountCloud/FireKylin) |
| **GetInfo** | v1.2.1 | 应急响应信息采集 | [GitHub](https://github.com/ra66itmachine/GetInfo) |
| **Hawkeye** | v3.0 | 应急响应工具 | [GitHub](https://github.com/mir1ce/Hawkeye) |
| **火绒剑** | 最新版 | 行为监控分析 | [huorong.cn](https://www.huorong.cn/) |
| **PCHunter** | 最新版 | Rootkit 检测 | - |
| **Process Monitor** | 最新版 | 进程监控（Sysinternals） | [Microsoft](https://learn.microsoft.com/sysinternals/) |
| **WebShellKiller** | 最新版 | WebShell 查杀 | - |

### 🎭 隐写与 CTF (C:\Penetration\CTFTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **Stegsolve** | 最新版 | 图片隐写分析 | [GitHub](https://github.com/Giotino/stegsolve) |
| **Steghide** | 最新版 | 隐写工具 | [GitHub](https://github.com/StefanoDeVuono/steghide) |
| **zsteg** | 最新版 | PNG/BMP 隐写检测 | [GitHub](https://github.com/zed-0xff/zsteg) |
| **Binwalk** | v3.1.0 | 固件分析 | [GitHub](https://github.com/ReFirmLabs/binwalk) |
| **CyberChef** | v10.19.4 | 编码解码瑞士军刀 | [gchq.github.io](https://gchq.github.io/CyberChef/) |
| **CTFCrackTools** | v4.0.7 | CTF 工具框架 | [GitHub](https://github.com/0Chencc/CTFCrackTools) |
| **QRResearch** | 最新版 | 二维码解析工具 | - |

### 💬 聊天与社交取证 (C:\Penetration\ForensicsTools)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **WxDump** | v1.4.1 | 微信取证工具 | [GitHub](https://github.com/cmluZw/WxDump) |
| **BrowserGhost** | 最新版 | 浏览器历史提取 | - |

### 🧰 辅助工具 (C:\Penetration\各目录)

| 工具 | 版本 | 说明 | 官网 |
| --- | --- | --- | --- |
| **uTools** | 最新版 | 效率工具集（含多插件） | [u.tools](https://u.tools/) |
| **SpaceSniffer** | 最新版 | 磁盘空间可视化 | [uderzo.it](http://www.uderzo.it/main_products/space_sniffer/) |
| **Everything** | v1.4.1 | 文件快速搜索 | [voidtools.com](https://www.voidtools.com/) |
| **Recaf** | v4.0 | Java 字节码编辑 | [GitHub](https://github.com/Col-E/Recaf) |
| **星号密码查看器** | 最新版 | 显示隐藏密码 | - |
| **RecentFile 查看器** | 最新版 | 最近文件记录 | - |
| **GPS 经纬度查询** | 离线版 | 坐标解析工具 | - |

## 💻 系统环境说明

### 基础信息
- **操作系统**：Windows 11 Workstation 24H2 x64
- **WSL 子系统**：Kali Linux 2025.1（完整安装）
- **推荐配置**：
  - VMware 17.x 或更高版本
  - 内存：8 GB 以上
  - 硬盘：300 GB SSD
  - 处理器：支持 CPU 虚拟化（Intel VT-x / AMD-V）

### 已安装运行环境
- **Python**：2.7 / 3.8 / 3.13（多版本共存，虚拟环境隔离）
- **Java**：JDK 8 + JDK 21
- **Node.js**：v22.16.0
- **Go**：v1.24.3
- **Rust**：v1.87.0
- **.NET Framework**：完整安装
- **Microsoft Visual C++**：2008-2022 运行库
- **数据库**：MariaDB、SQL Server 2022、PostgreSQL、Oracle 23ai、Redis、Neo4j

### 虚拟环境说明
所有 Python 工具采用独立虚拟环境（venv），避免依赖冲突：
- Windows 工具：`项目目录\win\` 文件夹
- Kali 工具：`项目目录\kali\` 文件夹
- 所有工具配备 `start.bat` 一键启动脚本，自动激活虚拟环境

## 🚀 快速开始

### 1. AI 辅助逆向分析

#### 步骤 1：启动 JADX 或 IDA
```powershell
# 启动 JADX-GUI（APK 分析）
C:\Penetration\AndroidTools\Jadx\jadx-gui-1.5.5.exe

# 或启动 IDA Pro（二进制分析）
C:\Penetration\ReverseTools\IDAPro\ida64.exe
```

#### 步骤 2：打开待分析文件
在 JADX/IDA 中打开 APK/EXE 文件

#### 步骤 3：在 Claude Code 中提问
```
"分析 com.example.MainActivity 的主要功能"
"查找所有网络请求相关的代码"
"这个加密函数使用了什么算法？"
"列出所有调用 System.loadLibrary 的位置"
```

Claude 会自动通过 MCP 协议调用 JADX/IDA，返回分析结果。

### 2. 移动端动态分析

#### 启动 Frida 环境
```powershell
cd C:\Penetration\AndroidTools
.\start_frida_ldplayer.ps1
```

脚本会自动：
- 连接雷电模拟器
- 启动 Frida Server
- 设置端口转发
- 启动 fridaUiTools

#### 使用 fridaUiTools
1. 在界面中选择目标进程
2. 加载 Hook 脚本
3. 实时查看函数调用和返回值

### 3. iOS 取证分析

#### 使用 iLEAPP（图形界面）
```powershell
# 双击桌面快捷方式 "iLEAPP GUI"
# 或运行
C:\Penetration\ForensicsTools\iLEAPP\iLEAPP-GUI.bat
```

#### 使用 iLEAPP（命令行）
```powershell
cd C:\Penetration\ForensicsTools\iLEAPP
.\iLEAPP-CLI.bat

# 分析文件系统数据
ileapp -i "D:\iOS_Data" -o "D:\Results" -t fs

# 分析 iTunes 备份
ileapp -i "D:\Backup" -o "D:\Results" -t itunes
```

### 4. Windows 取证分析

#### 快速时间线生成
```powershell
# 使用 Plaso 生成时间线
cd C:\Penetration\ForensicsTools\Plaso
.\start.bat
log2timeline.exe timeline.plaso D:\evidence\

# 导出为 CSV
psort.exe -o l2tcsv -w timeline.csv timeline.plaso
```

#### 注册表分析
```powershell
# 使用 Registry Explorer
C:\Penetration\ForensicsTools\EricZimmermanTools\RegistryExplorer\RegistryExplorer.exe
```

#### 事件日志分析
```powershell
# 使用 Hayabusa 威胁狩猎
cd C:\Penetration\ForensicsTools\Hayabusa
.\hayabusa.exe csv-timeline -d D:\logs\ -o results.csv
```

### 5. 内存取证分析

#### Volatility 3 分析
```powershell
cd C:\Penetration\ForensicsTools\Volatility3
.\start.bat

# 查看进程列表
python vol.py -f memory.dmp windows.pslist

# 提取进程
python vol.py -f memory.dmp windows.dumpfiles --pid 1234
```

#### MemProcFS 挂载内存
```powershell
cd C:\Penetration\ForensicsTools\MemProcFS
.\MemProcFS.exe -device memory.dmp -mount M:
```

内存文件系统会挂载到 M: 盘，可直接浏览进程、文件、注册表。

### 6. 网络流量分析

#### 使用 Zui 分析 Zeek 日志
```powershell
# 启动 Zui
C:\Penetration\ForensicsTools\Zui\Zui.exe

# 导入 .pcap 文件或 Zeek 日志目录
```

#### Wireshark 深度分析
```powershell
C:\Penetration\TrafficTools\Wireshark\Wireshark.exe
```

## 📚 学习资源

### 🛠️ 工具使用指南（必读）

📖 **[afst-forensics-tools.md](afst-forensics-tools.md)** - 取证工具详细使用手册

包含完整的工具使用说明，支持在 Claude Code / Cursor 中直接引用，涵盖：
- 核心取证工具使用方法
- 移动端取证与 CTF 工具
- 内网渗透与逆向分析
- AI 辅助分析工作流

**在 AI 中使用**：
```bash
@afst-forensics-tools.md 应急响应推荐哪些工具
@afst-forensics-tools.md Volatility 怎么用
@afst-forensics-tools.md JADX 如何配合 AI 分析
```

### 🎬 演示视频

📹 **AI 辅助逆向分析演示**

- **AI 分析 APK 演示**：展示如何使用 Claude Code + JADX MCP 自动分析 Android 应用
- **AI 分析 EXE 演示**：展示如何使用 Claude Code + IDA MCP 自动分析二进制文件

**视频位置**：
- 虚拟机内：`C:\Penetration\ForensicsTools\Forensic_Knowledge_Base\演示视频\`
- 桌面快捷方式：双击 `视频取证工具` 可快速访问
- GitHub 仓库：[演示视频目录](演示视频/)

### 取证实录
- 位置：`C:\Penetration\ForensicsTools\ForensicRecorder\`
- 包含取证实录电子期刊

### 离线知识库
- 位置：`C:\Penetration\ForensicsTools\Forensic_Knowledge_Base\`
- 包含取证技术文档、工具手册、案例库

### 在线资源书签
- 浏览器书签已导入，包含：
  - 取证平台：DIDCTF、西电取证、Yagami
  - 工具文档：官方手册、GitHub 仓库
  - 学习资源：博客、论坛、视频教程

## 🔄 工具更新日志

### 2026.06.29 更新
详见本文档 [20260629 更新说明](#-20260629-更新说明) 章节

### 2025.06.06 更新（原作者）
1. 由于微软即将对 Windows 10 结束技术支持，使用 Windows 11 母盘镜像制作
2. 所有运行库、系统组件、安装软件、脚本类工具均升级至最新版本
3. 去除部分长期未更新、使用效果不佳的工具
4. 优化扫描器、数据库等工具自启动后台服务占用系统资源过大的问题
5. 重构工具的快捷方式，运行时显示详细使用参数及方法

## 🤝 参与贡献

欢迎通过 Issue 或 Pull Request 参与维护。推荐提交内容包括：

- **新工具推荐**：说明用途、官网或仓库地址、许可证、适用场景
- **工具分类优化**：让取证、应急、CTF、逆向、流量等分类更清晰
- **安装和配置脚本**：优先选择官方来源、可复现、可校验的安装方式
- **文档修正**：补充工具说明、版本信息、使用注意事项和截图
- **镜像构建建议**：例如系统优化、快捷启动、环境变量和依赖隔离

详细贡献说明见 [CONTRIBUTING.md](CONTRIBUTING.md)。

## ⚠️ 免责声明

1. 本镜像仅面向合法授权的企业安全建设行为，如您需要测试本镜像，请自行搭建环境
2. 在使用本镜像时，您应确保相关行为符合当地的法律法规，且已经取得了足够的授权
3. 如果您在使用本镜像中产生任何非法行为，需自行承担相应后果，作者不承担任何法律连带责任
4. 本镜像所使用的工具资源均来自于互联网整理，如果侵犯了您的知识产权，作者将第一时间删除

## 📧 联系方式

- **作者**：Alenm (alenm1208@gmail.com)

---

<p align="center">
  <strong>🎉 开箱即用，取证必备，AI 加持 🎉</strong>
</p>

<p align="center">
  Made with ❤️ by Alenm | Based on <a href="https://github.com/makoto56/penetration-suite-toolkit">Penetration Suite Toolkit</a>
</p>