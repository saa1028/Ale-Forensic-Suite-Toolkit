<h1 align="center">Ale Forensic Suite Toolkit 阿乐取证工具集</h1>
<p align="center">
  <strong>AI 赋能的取证工具集 · 开箱即用 · 数字取证 · 应急响应 · CTF 取证 · 安全分析</strong>
</p>

<p align="center">
  <a href="https://github.com/saa1028/Ale-Forensic-Suite-Toolkit/stargazers"><img src="https://img.shields.io/github/stars/saa1028/Ale-Forensic-Suite-Toolkit?style=flat-square&logo=github&label=Stars" alt="GitHub Stars"></a>
  <a href="https://github.com/saa1028/Ale-Forensic-Suite-Toolkit/network/members"><img src="https://img.shields.io/github/forks/saa1028/Ale-Forensic-Suite-Toolkit?style=flat-square&logo=github&label=Forks" alt="GitHub Forks"></a>
  <a href="https://github.com/saa1028/Ale-Forensic-Suite-Toolkit/issues"><img src="https://img.shields.io/github/issues/saa1028/Ale-Forensic-Suite-Toolkit?style=flat-square&logo=github&label=Issues" alt="GitHub Issues"></a>
  <img src="https://img.shields.io/badge/License-Apache%202.0-blue.svg?style=flat-square">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Focus-Digital%20Forensics-blue.svg?style=flat-square">
  <img src="https://img.shields.io/badge/Platform-Windows%2011%20VM-red.svg?style=flat-square">
  <img src="https://img.shields.io/badge/AI-Claude%20MCP%20Powered-brightgreen.svg?style=flat-square">
  <img src="https://img.shields.io/badge/Version-v20260629-orange.svg?style=flat-square">
  <img src="https://img.shields.io/badge/Tools-150%2B-blueviolet.svg?style=flat-square">
</p>

<p align="center">
  <a href="#-快速开始">快速开始</a> •
  <a href="#-演示视频">演示视频</a> •
  <a href="#️-界面预览">界面预览</a> •
  <a href="#-核心价值">核心价值</a> •
  <a href="#-工具清单">工具清单</a> •
  <a href="#-学习资源">学习资源</a> •
  <a href="docs/CONTRIBUTING.md">贡献指南</a>
</p>

---

## 📑 目录

- [💡 项目愿景](#-项目愿景)
- [💎 核心价值](#-核心价值)
- [🚀 快速开始](#-快速开始)
- [🎬 演示视频](#-演示视频)
- [🆕 更新说明](#-更新说明)
- [🖼️ 界面预览](#️-界面预览)
- [🔧 工具清单](#-工具清单)
- [💻 系统环境](#-系统环境)
- [📊 调研依据](#-调研依据)
- [📚 学习资源](#-学习资源)
- [🔄 历史更新](#-历史更新)
- [🤝 参与贡献](#-参与贡献)
- [⚠️ 免责声明](#️-免责声明)

---

## 💡 项目愿景

**Ale Forensic Suite Toolkit（阿乐取证工具集，简称 AFST）** 是一个专为取证人员打造的 AI 赋能的开箱即用工具集成环境。

本项目基于 [makoto56/penetration-suite-toolkit](https://github.com/makoto56/penetration-suite-toolkit) 二次开发，在原 Windows 安全工具虚拟机基础上，针对数字取证、电子数据取证、应急响应、CTF Forensics、恶意代码分析场景进行深度定制。

### 🎯 适用场景

- **电子数据取证**：手机取证、计算机取证、网络取证
- **应急响应**：入侵排查、日志分析、恶意代码分析
- **CTF 取证竞赛**：Misc、Forensics 方向题目环境
- **取证比武**：公安、司法、企业安全取证演练
- **安全培训**：取证技能培训、实验室环境搭建
- **恶意代码分析**：APK、EXE、内存 dump 分析

### 💎 核心价值

- **AI 赋能**：集成 Claude Code + IDA MCP + JADX MCP + CTF/安全 Skills，AI 辅助逆向分析与取证
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

## 📥 获取最新版本

### 下载方式

**关注公众号「阿乐取证工具集」获取最新版本下载链接**

<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/微信公众号.jpg" alt="阿乐取证工具集公众号" width="300">
</p>

- 🔄 **持续更新**：每次更新会在公众号首发最新版本下载链接
- 📢 **更新通知**：及时获取工具更新、使用技巧、取证案例分享
- 💬 **技术交流**：获取取证技术文章、CTF WriteUp、工具教程
- 🎯 **问题反馈**：遇到问题可在公众号留言反馈

> **提示**：镜像文件较大，使用百度网盘会员下载，更多下载方式等待补充

---

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

#### 步骤 3：配置 CC Switch（重要）
在使用 Claude Code 前，需要配置 CC Switch 连接 AI 中转站或 API 接口
#### 步骤 4：在 Claude Code 中提问
```
"分析 test.apk 的主要功能"
"分析 test.apk 的回连地址"
"这个test.exe使用了什么加密算法？"
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

### 3. iOS 取证分析

```powershell
# 双击桌面快捷方式 "iLEAPP GUI"
# 或运行
C:\Penetration\ForensicsTools\iLEAPP\iLEAPP-GUI.bat

# 命令行方式
cd C:\Penetration\ForensicsTools\iLEAPP
.\iLEAPP-CLI.bat
ileapp -i "D:\iOS_Data" -o "D:\Results" -t fs
```

### 4. Windows 取证分析

```powershell
# 使用 Plaso 生成时间线
cd C:\Penetration\ForensicsTools\Plaso
.\start.bat
log2timeline.exe timeline.plaso D:\evidence\

# 导出为 CSV
psort.exe -o l2tcsv -w timeline.csv timeline.plaso
```

## 🎬 演示视频

### 📱 AI 分析 APK 演示

![AI分析APK演示](https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/demo-apk.gif)

> **完整视频**：[点击查看高清版](演示视频/AI分析apk演示.mkv)  
> 展示如何使用 Claude Code + JADX MCP 自动分析 Android 应用，包括：
> - 自动反编译 APK 并定位关键代码
> - AI 识别恶意行为和隐私泄漏模式
> - 智能生成分析报告

### 💻 AI 分析 EXE 演示

![AI分析EXE演示](https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/demo-exe.gif)

> **完整视频**：[点击查看高清版](演示视频/AI分析exe演示.mkv)  
> 展示如何使用 Claude Code + IDA MCP 自动分析二进制文件，包括：
> - 函数识别与交叉引用分析
> - 加密算法自动识别
> - 恶意代码模式检测

**视频位置**：
- 虚拟机内：`C:\Penetration\ForensicsTools\Forensic_Knowledge_Base\演示视频\`
- 桌面快捷方式：双击 `视频取证工具` 可快速访问

## 🆕 更新说明

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

#### 📚 CTF 与安全技能库（100+ Skills）
集成四大技能仓库，Claude 自动调用相关技能：
1. **ctf-skills**（19 个技能）
   - 密码学、Web、Pwn、逆向、取证、Misc、OSINT、AI/ML 安全
2. **awesome-skills-security**（7 个工具技能）
   - 模糊测试、密码字典、Payload、WebShell、用户名字典
3. **secknowledge-skill**（中文安全知识库）
   - WooYun 88,636 真实漏洞案例
   - OWASP Top 10 + GAARM AI 风险框架
4. **SecSkills**（道一安全团队知识库）

<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/skills.png" alt="Skills 技能库" width="800">
</p>

> **Skills 技能库概览**：涵盖 100+ 个技能，持续更新中。包括：
> - **安全渗透测试**（约 30+ 个）：CTF 相关、Pwn、逆向、Web、密码学、取证、OSINT、恶意代码分析等
> - **开发与调试**（约 25 个）：代码审查、系统调试、测试驱动开发、前端开发、Canvas 设计、Git 工作流等
> - **文档协作**（约 15 个）：docx、pptx、xlsx、PDF、Excel 分析、协同创作等
> - **逆向工程**（约 15 个）：Android APK、JADX、IDA、DEX dumper、Unity IL2CPP、二进制分析、Frida、Unicorn 模拟等
> - **AI 与创意**（约 18 个）：LLM 应用、Claude API、算法艺术、小说创作、GIF 制作等
> - **其他专业领域**：数据库系统、深度研究、人格世观建模、天气查询等
> 
> 你可以使用 `/find-skills` 搜索特定领域的技能，或直接调用相关技能，AI 会自动匹配合适的技能。
> 
> **🔜 即将推出**：独立的**取证 Skills 库**，可直接导入到 Claude Code，专注于数字取证、应急响应、CTF 取证等场景。

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

### 🚀 特色功能

#### 🤖 AI 取证分析工作流
```
1. 启动 JADX-GUI / IDA Pro
2. 打开待分析的 APK / EXE 文件
3. 配置 CC Switch 连接 AI 中转站/API 接口
4. 在 Claude Code 中直接询问：
   - "分析这个 APK 的主要功能"
   - "查找可疑的加密函数"
   - "列出所有网络请求"
   - "识别这个函数的作用"
5. Claude 自动调用 MCP 工具，返回分析结果
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

## 🖼️ 界面预览

### 主界面展示

#### AFST 主界面与壁纸
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/V1.0.png" alt="AFST 主界面" width="800">
</p>

> 精心设计的 AFST 主题壁纸，展现专业取证工具集的视觉风格

#### Kali Linux 集成环境
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/kali.png" alt="Kali Linux" width="800">
</p>

> **WSL Kali Linux 2025.1 完整集成**
> - 用户账号：`kali` / 密码：`kali`
> - Root 账号：`root` / 密码：`root`
> - 启动桌面：运行 `kex --win -s` 命令开启 Kali 桌面环境
> - 集成常用取证和渗透测试工具

### 工具组织与管理

#### 全部工具目录结构
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/程序列表.png" alt="程序列表" width="800">
</p>

> 25 个工具分类文件夹，涵盖 AI 工具、安卓工具、免杀工具、审计工具、连接工具、破解工具、CTF 工具等

#### 取证工具详细列表
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/取证工具列表.png" alt="取证工具列表" width="800">
</p>

> ForensicsTools 目录包含 80+ 取证工具，包括 iLEAPP、ALEAPP、Autopsy、Volatility、MemProcFS 等核心取证工具

#### uTools + 开始菜单 + Maye 分类
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/utools插件+开始菜单+maya分类.png" alt="工具快速启动" width="800">
</p>

> uTools 效率工具集成多插件，开始菜单完整展示 AFST 工具树，Maye 快捷启动工具按字母索引分类

### 在线资源与书签

#### Markoob 书签管理 - 电子取证分类
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/Markoob书签1.png" alt="书签管理1" width="800">
</p>

> 精心整理的电子取证在线资源，包括数据存储分析、APK 分析、密码破解、内网取证、Windows 取证等 30+ 分类

#### Markoob 书签管理 - 渗透与工具分类
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/Markoob书签2.png" alt="书签管理2" width="800">
</p>

> 涵盖目录探测、子域名探测、WebShell、密码破解、CTF 入门、信息收集等安全测试在线资源和工具仓库

### 系统性能

#### 资源占用情况
<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/screenshots/资源占用.png" alt="资源占用" width="800">
</p>

> 系统经过深度优化，CPU 和内存占用率低，确保取证工具流畅运行

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

### 工具使用频率 Top 50

基于真实取证 WP 统计，以下是出现频次最高的 50 个工具（✅ 表示已集成到 AFST）：

| 排名 | 工具名称 | 出现次数 | 类型 | 已集成 | AFST 对应工具 |
|------|---------|---------|------|--------|--------------|
| 1 | 火眼证据分析 | 552 | 商业 | ❌ | 参考工具 |
| 2 | hashcat | 239 | 开源 | ✅ | Hashcat |
| 3 | Frida | 178 | 开源 | ✅ | Frida |
| 4 | FTK Imager | 132 | 商业 | ✅ | FTK Imager |
| 5 | Volatility | 104 | 开源 | ✅ | Volatility 2/3 |
| 6 | 盘古石 | 96 | 商业 | ❌ | 参考工具 |
| 7 | John the Ripper | 94 | 开源 | ✅ | John the Ripper |
| 8 | 美亚取证 | 85 | 商业 | ❌ | 参考工具 |
| 9 | CyberChef | 80 | 开源 | ✅ | CyberChef |
| 10 | Wireshark | 78 | 开源 | ✅ | Wireshark |
| 11 | VMware | 65 | 商业 | ✅ | VMware |
| 12 | IDA | 57 | 商业 | ✅ | IDA Pro + MCP |
| 13 | DIE | 49 | 开源 | ✅ | Detect It Easy |
| 14 | X-Ways Forensics | 46 | 商业 | ✅ | X-Ways |
| 15 | iLEAPP | 42 | 开源 | ✅ | iLEAPP |
| 16 | 010 Editor | 40 | 商业 | ✅ | 010 Editor |
| 17 | ADB | 40 | 开源 | ✅ | ADB |
| 18 | JADX | 40 | 开源 | ✅ | JADX + MCP |
| 19 | 取证大师 | 32 | 商业 | ❌ | 参考工具 |
| 20 | Passware Kit | 29 | 商业 | ✅ | Passware Kit 2022 |
| 21 | binwalk | 28 | 开源 | ✅ | Binwalk |
| 22 | SQLite Browser | 27 | 开源 | ✅ | SQLite Browser |
| 23 | LiME | 26 | 开源 | ✅ | LiME (Kali) |
| 24 | 弘连 | 26 | 商业 | ❌ | 参考工具 |
| 25 | 7-Zip | 19 | 免费 | ✅ | 7-Zip |
| 26 | Autopsy | 18 | 开源 | ✅ | Autopsy |
| 27 | SageMath | 14 | 开源 | ❌ | 环境依赖复杂 |
| 28 | 科来网络分析系统 | 14 | 免费 | ✅ | 科来网络分析系统 |
| 29 | 雷电 APP 智能分析 | 14 | 商业 | ❌ | 参考工具 |
| 30 | Mimikatz | 13 | 开源 | ✅ | Mimikatz |
| 31 | foremost | 12 | 开源 | ✅ | Foremost |
| 32 | HashMyFiles | 12 | 免费 | ✅ | HashMyFiles |
| 33 | YARA | 11 | 开源 | ✅ | YARA |
| 34 | 火眼仿真取证 | 11 | 商业 | ❌ | 参考工具 |
| 35 | MemProcFS | 10 | 开源 | ✅ | MemProcFS |
| 36 | Steghide | 9 | 开源 | ✅ | Steghide |
| 37 | R-Studio | 8 | 商业 | ✅ | R-Studio |
| 38 | StegSolve | 8 | 开源 | ✅ | StegSolve |
| 39 | Wazuh | 8 | 开源 | ❌ | 需容器部署 |
| 40 | Zeek | 8 | 开源 | ❌ | 需容器部署 |
| 41 | ALEAPP | 6 | 开源 | ✅ | ALEAPP |
| 42 | Ghidra | 6 | 开源 | ✅ | Ghidra |
| 43 | VirtualBox | 6 | 开源 | ❌ | 虚拟机嵌套 |
| 44 | Zui | 6 | 开源 | ✅ | Zui (Brim) |
| 45 | Hayabusa | 5 | 开源 | ✅ | Hayabusa |
| 46 | WinRAR | 5 | 免费 | ❌ | 已有 7-Zip |
| 47 | CTF-NetA | 4 | 开源 | ✅ | CTF-NetA |
| 48 | FinalShell 密码解密 | 4 | 开源 | ✅ | FinalShell 密码解密 |
| 49 | SQLiteStudio | 4 | 开源 | ❌ | 已有 SQLite Browser |
| 50 | AVML | 3 | 开源 | ✅ | AVML |

**统计说明**：
- **出现次数**：该工具在所有调研 WP 中被提及的总次数
- **已集成**：✅ 表示已内置在 AFST 中，❌ 表示未集成
- **商业工具**：火眼、盘古石、美亚、取证大师等商业平台/工具作为参考
- **未集成原因**：环境依赖复杂、需容器部署、虚拟机嵌套、功能重复等

**覆盖率**：Top 50 工具中，适合集成的开源/商业工具覆盖率达到 **90%+**

## 🔧 工具清单

> **📖 完整工具列表**：
> - **在线查看**：[原项目工具清单](https://github.com/makoto56/penetration-suite-toolkit#%EF%B8%8F-%E8%BD%AF%E4%BB%B6%E5%8F%8A%E5%B7%A5%E5%85%B7%E4%BB%8B%E7%BB%8D)（包含所有渗透测试工具的详细介绍）
> - **本地查看**：[docs/original-pst-README.md](docs/original-pst-README.md)（原项目 README 本地副本）
> 
> 本项目基于原渗透工具集，**额外增强了取证、应急响应、AI 辅助分析**能力。下方列出的是 **AFST 特色工具**和核心取证工具。

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

## 💻 系统环境

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

## 📚 学习资源

### 🛠️ 工具使用指南（必读）

📖 **[docs/afst-forensics-tools.md](docs/afst-forensics-tools.md)** - 取证工具详细使用手册

包含完整的工具使用说明，支持在 Claude Code / CodeX 中直接引用，涵盖：
- 核心取证工具使用方法
- 移动端取证与 CTF 工具
- 内网渗透与逆向分析
- AI 辅助分析工作流

**在 AI 中使用**：
```bash
@docs/afst-forensics-tools.md 应急响应推荐哪些工具
@docs/afst-forensics-tools.md Volatility 怎么用
@docs/afst-forensics-tools.md JADX 如何配合 AI 分析
```

### 📚 离线资源

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

## 🔄 历史更新

### 2026.06.29 更新
详见本文档 [更新说明](#-更新说明) 章节

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

详细贡献说明见 [docs/CONTRIBUTING.md](docs/CONTRIBUTING.md)。

## ⚠️ 免责声明

1. 本镜像仅面向合法授权的企业安全建设行为，如您需要测试本镜像，请自行搭建环境
2. 在使用本镜像时，您应确保相关行为符合当地的法律法规，且已经取得了足够的授权
3. 如果您在使用本镜像中产生任何非法行为，需自行承担相应后果，作者不承担任何法律连带责任
4. 本镜像所使用的工具资源均来自于互联网整理，如果侵犯了您的知识产权，作者将第一时间删除

## 📧 联系方式

- **邮箱**：alenm1208@gmail.com
- **微信**：jgotea 
- **公众号**：阿乐取证工具集

## ☕ 打赏与捐赠

如果这个项目对您有帮助，欢迎请阿乐喝杯咖啡 ☕

<p align="center">
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/支付宝收款码.jpg" alt="支付宝收款码" width="300">
  &nbsp;&nbsp;&nbsp;&nbsp;
  <img src="https://raw.githubusercontent.com/saa1028/Ale-Forensic-Suite-Toolkit/main/assets/微信收款码.jpg" alt="微信收款码" width="300">
</p>

> 您的支持是我持续更新的动力！感谢每一位支持者 🙏

---

## ⭐ Star History

<p align="center">
  <a href="https://www.star-history.com/?type=date&repos=saa1028%2FAle-Forensic-Suite-Toolkit">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=saa1028/Ale-Forensic-Suite-Toolkit&type=date&theme=dark&legend=top-left" />
      <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=saa1028/Ale-Forensic-Suite-Toolkit&type=date&legend=top-left" />
      <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=saa1028/Ale-Forensic-Suite-Toolkit&type=date&legend=top-left" />
    </picture>
  </a>
</p>

---

<p align="center">
  <strong>🎉 开箱即用，取证必备，AI 加持 🎉</strong>
</p>

<p align="center">
  Made with ❤️ by Alenm | Based on <a href="https://github.com/makoto56/penetration-suite-toolkit">Penetration Suite Toolkit</a>
</p>