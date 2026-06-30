# Ale Forensic Suite Toolkit 阿乐取证工具集 v20260629 更新日志

## 🎯 本次更新主题：AI 赋能取证分析

本次更新的核心是将 AI 能力深度整合到取证工作流中，让 Claude Code 成为取证分析师的得力助手。

---

## ✨ 重大更新

### 1. AI 分析能力革命性提升

#### 🤖 Claude Code 生态集成
- ✅ 安装 **Claude Code** 官方 CLI 工具
- ✅ 安装 **Cursor AI** 编辑器（v0.50.5）
- ✅ 配置全局快捷方式，随时唤起 AI 助手

#### 🔌 MCP 协议深度集成

**IDA Pro MCP Server v6.4.0**
- ✅ 安装并配置 IDA Pro MCP 插件
- ✅ Claude 可直接调用 IDA API 分析二进制文件
- ✅ 支持功能：
  - 函数列表枚举与分析
  - 反编译代码查看
  - 交叉引用（xref）查询
  - 结构体与数据类型解析
  - 内存数据读取
  - 函数重命名与注释

**JADX MCP Server v6.4.0**
- ✅ 安装并配置 JADX MCP 插件
- ✅ Claude 可直接分析 APK 文件
- ✅ 支持功能：
  - APK 反编译与源码查看
  - 类、方法、字段搜索
  - AndroidManifest.xml 解析
  - 组件（Activity/Service/Receiver/Provider）分析
  - 交叉引用查询
  - 类与方法重命名
  - Smali 代码查看

**实战效果**：
```
用户："分析这个 APK 的主要功能"
Claude：[自动调用 JADX MCP]
       - 解析 MainActivity
       - 提取网络请求代码
       - 识别数据加密方式
       - 生成功能分析报告
```

#### 📚 安全技能库（26+ Skills）

集成四大技能仓库到 Claude Code：

**1. ctf-skills（19 个技能）**
- `ctf-crypto` - 密码学攻击（RSA、AES、DES、古典密码）
- `ctf-web` - Web 漏洞利用（SQL 注入、XSS、SSRF、反序列化）
- `ctf-pwn` - 二进制漏洞利用（栈溢出、堆利用、ROP）
- `ctf-reverse` - 逆向工程（静态分析、动态调试、混淆还原）
- `ctf-forensics` - 数字取证（内存取证、流量分析、文件恢复）
- `ctf-misc` - 综合技能（编码、套娃、沙箱逃逸）
- `ctf-osint` - 开源情报（社交媒体、地理定位、人肉搜索）
- `ctf-ai-ml` - AI 安全（模型攻击、提示注入、对抗样本）
- `ctf-malware` - 恶意软件分析（C2 通信、内存马、混淆）

**2. awesome-skills-security（7 个工具技能）**
- `security-fuzzing` - 模糊测试 Payload
- `security-passwords` - 密码字典（Top 10K）
- `security-payloads` - 漏洞利用 Payload
- `security-webshells` - WebShell 样本库
- `security-usernames` - 用户名字典
- `security-patterns` - 敏感数据模式匹配

**3. secknowledge-skill（中文安全知识库）**
- 整合 **WooYun 88,636** 真实漏洞案例
- 集成 OWASP Top 10（Web + LLM + API）
- 包含 GAARM AI 风险框架（173 个风险点）
- 支持实战安全测试场景

**4. SecSkills（道一安全团队）**
- 中文安全技术文档
- 实战渗透测试技巧

**技能自动调用机制**：
当你向 Claude 提出取证、逆向、CTF 相关问题时，Claude 会自动识别场景并调用对应技能库，无需手动指定。

---

## 🛠️ 新增核心取证工具（40+）

### 📱 移动端取证

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **iLEAPP** | v0.15.0 | ✅ 新增 - iOS 取证神器，支持 300+ 工件分析 |
| | | • GUI + CLI 双模式 |
| | | • 独立 Python 虚拟环境 |
| | | • 桌面快捷方式已配置 |
| | | • 支持文件系统、iTunes 备份、TAR/ZIP 分析 |
| **ALEAPP** | v4.1.0 | ✅ 新增 - Android 取证工具 |
| | | • 完整分析 Android 数据结构 |
| | | • 生成 HTML 报告与时间线 |
| **Frida** | v16.7.19 | ✅ 新增 - 动态插桩框架 |
| | | • 已配置雷电模拟器环境 |
| | | • Root 权限已启用 |
| | | • 端口转发自动设置（tcp:27042） |
| **fridaUiTools** | 最新版 | ✅ 新增 - Frida 图形化工具 |
| | | • 进程列表与 Hook 管理 |
| | | • 脚本编辑器与 RPC 调用 |
| | | • 内存 Dump 与调用栈追踪 |
| **雷电模拟器** | LDPlayer9 | ✅ 新增 - Android 模拟器环境 |
| | | • 已配置 Root + Frida Server |
| | | • 一键启动脚本：`start_frida_ldplayer.ps1` |
| **JADX MCP** | v6.4.0 | ✅ 升级 - 集成 MCP 插件 |
| | | • Claude 可直接分析 APK |
| | | • AI 辅助逆向分析 |

**一键启动脚本**：
```powershell
# 启动 Frida 完整环境
C:\Penetration\AndroidTools\start_frida_ldplayer.ps1

# 自动完成：
# 1. 连接模拟器
# 2. 启动 Frida Server
# 3. 设置端口转发
# 4. 启动 fridaUiTools
```

### 💾 磁盘与镜像取证

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **Arsenal Image Mounter** | 最新版 | ✅ 新增 - 专业镜像挂载工具 |
| | | • 只读挂载保护证据完整性 |
| | | • 支持 E01、DD、VHD、VMDK 等格式 |
| **VeraCrypt** | v1.26.7 | ✅ 新增 - 加密卷管理 |
| | | • 挂载与破解加密卷 |
| | | • 支持 TrueCrypt 兼容模式 |
| **R-Studio** | v9.3 | ✅ 新增 - 专业数据恢复 |
| | | • 支持 RAID 重建 |
| | | • 原始磁盘扫描 |

### 🧠 内存取证

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **MemProcFS** | v5.14 | ✅ 更新 - 内存进程文件系统 |
| | | • 挂载内存为文件系统，直接浏览 |
| | | • 实时内存分析 |
| **AVML** | 最新版 | ✅ 新增 - Linux 内存采集 |
| | | • 微软开源工具 |
| | | • 支持大内存系统 |
| **DumpIt** | 最新版 | ✅ 新增 - Windows 内存转储 |
| | | • 一键内存采集 |
| **LiME** | 最新版 | ✅ 新增 - Linux 内存提取器（Kali） |
| | | • 内核模块方式采集 |
| **Volatility 2** | v2.6.1 | ⬆️ 保留 - 经典版本 |
| **Volatility 3** | v2.26.0 | ⬆️ 更新 - 新一代框架 |

### 🖥️ Windows 取证

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **Eric Zimmerman Tools** | 最新版 | ✅ 新增 - Windows 取证全家桶 |
| | | • RECmd、PECmd、EvtxECmd |
| | | • RegistryExplorer、Timeline Explorer |
| | | • JumpList Explorer、ShellBags Explorer |
| **Hayabusa** | 最新版 | ✅ 新增 - 事件日志威胁狩猎 |
| | | • 基于 Sigma 规则检测威胁 |
| | | • 生成时间线与 CSV 报告 |
| **Plaso** | 最新版 | ✅ 新增 - 时间线分析（log2timeline） |
| | | • 独立 Python 虚拟环境 |
| | | • 支持 130+ 解析器 |

### 🌐 网络与流量取证

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **Zui (Brim)** | 最新版 | ✅ 新增 - Zeek 日志可视化分析 |
| | | • 替代 Zeek 命令行的现代化界面 |
| | | • 支持大规模流量分析 |
| **NetworkMiner** | 最新版 | ✅ 新增 - 网络取证分析工具 |
| | | • 提取文件、图片、证书 |
| | | • 识别主机与操作系统 |
| **CTF-NetA** | 最新版 | ✅ 新增 - CTF 流量分析工具包 |
| | | • 专为 CTF 流量题设计 |

### 🔐 密码恢复与加密分析

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **Passware Kit** | 2022 | ✅ 新增 - 商业级密码恢复（注册版） |
| | | • 支持 300+ 文件类型 |
| | | • GPU 加速破解 |
| **HashMyFiles** | 最新版 | ✅ 新增 - 文件哈希计算 |
| | | • 批量哈希校验 |
| **Navicat 密码查看器** | 最新版 | ✅ 新增 - 数据库密码解密 |
| **FinalShell 密码解密** | 最新版 | ✅ 新增 - SSH 工具密码提取 |

### 🔬 恶意代码分析

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **Capa** | v7.5 | ✅ 新增 - Mandiant 恶意软件能力检测 |
| | | • 自动识别恶意行为模式 |
| | | • 基于 MITRE ATT&CK |
| **PEStudio** | v9.66 | ✅ 新增 - PE 文件静态分析 |
| | | • 可疑 API 调用标记 |
| | | • 熵值分析与加壳检测 |
| **ImHex** | v1.35 | ✅ 新增 - 现代化十六进制编辑器 |
| | | • 模式匹配与数据可视化 |
| | | • 脚本化分析 |
| **pycdc** | 最新版 | ✅ 新增 - Python 反编译 |
| **pyinstxtractor** | 2026.04 | ✅ 新增 - PyInstaller 解包 |
| **IDA Pro MCP** | v6.4.0 | ✅ 升级 - 集成 MCP 插件 |
| | | • Claude 可直接分析二进制文件 |

### 📁 文件分析与恢复

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **The Sleuth Kit** | 最新版 | ✅ 新增 - 文件系统取证工具包 |
| | | • 支持 NTFS、FAT、EXT、HFS+ 等 |
| **Scalpel** | 最新版 | ✅ 新增 - 文件雕刻工具（Kali） |
| | | • 基于文件头尾特征恢复 |
| **ExifTool + GUI** | 最新版 | ✅ 新增 - 元数据提取与分析 |
| | | • 支持图片、视频、PDF、Office 等 |
| **EFDD** | v2024 | ✅ 新增 - 邮件取证与分析 |
| | | • PST、OST、EML、MSG 解析 |
| **FileLocator Pro** | 最新版 | ✅ 新增 - 文件内容搜索 |
| | | • 正则表达式搜索 |
| **Document Tools** | 最新版 | ✅ 新增 - Office 文档分析套件 |
| **万兴易修** | 最新版 | ✅ 新增 - 损坏文件修复工具 |
| | | • 修复损坏的图片、视频、文档 |
| **ImageStrike** | 最新版 | ✅ 新增 - 图片分析工具 |

### 🗄️ 数据库取证

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **DBever CE** | 最新版 | ✅ 新增 - 通用数据库管理工具 |
| | | • 支持 40+ 数据库类型 |
| | | • ER 图生成与 SQL 编辑器 |

### 🛡️ 应急响应工具

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **Velociraptor** | v0.73 | ✅ 新增 - 端点取证与响应平台 |
| | | • Agent-based 架构 |
| | | • VQL 查询语言 |
| **火绒剑** | 最新版 | ✅ 新增 - 行为监控与分析 |
| | | • 进程、网络、文件监控 |
| | | • 威胁行为检测 |
| **WebShellKiller** | 最新版 | ✅ 新增 - WebShell 查杀 |
| **PCHunter** | 最新版 | ✅ 新增 - Rootkit 检测 |
| **Process Monitor** | 最新版 | ✅ 新增 - Sysinternals 进程监控 |

### 🎭 隐写与 CTF

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **zsteg** | 最新版 | ✅ 新增 - PNG/BMP 隐写检测（Ruby） |
| | | • LSB 隐写检测 |
| **QRResearch** | 最新版 | ✅ 新增 - 二维码解析工具 |

### 💬 聊天与社交取证

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **BrowserGhost** | 最新版 | ✅ 新增 - 浏览器历史提取 |
| | | • 支持 Chrome、Edge、Firefox 等 |

### 🧰 辅助工具

| 工具 | 版本 | 更新说明 |
|------|------|----------|
| **uTools** | 最新版 | ✅ 新增 - 效率工具集合 |
| | | • 集成多个实用插件 |
| | | • 快捷启动与文件搜索 |
| **SpaceSniffer** | 最新版 | ✅ 新增 - 磁盘空间可视化 |
| | | • Treemap 可视化展示 |
| **Recaf** | v4.0 | ✅ 新增 - Java 字节码编辑器 |
| **星号密码查看器** | 最新版 | ✅ 新增 - 显示隐藏密码 |
| **RecentFile 查看器** | 最新版 | ✅ 新增 - 最近文件记录 |
| **GPS 经纬度查询** | 离线版 | ✅ 新增 - 坐标解析工具 |

---

## 🔧 系统优化与配置

### 💻 系统更新
- ✅ **Windows 11 系统补丁**：更新至 2026 年 6 月最新版
- ✅ **Chrome 浏览器**：升级至 136.0.7103.114（绿色修改版）
- ✅ **KMS 激活工具**：更新至最新版本

### ⚙️ 环境配置
- ✅ **ADB 全局命令**：永久添加到系统 PATH
  - 位置：`C:\Penetration\AndroidTools\AdbDriver\`
  - 无需 cd 切换，直接运行 `adb devices`
- ✅ **Python 虚拟环境优化**：
  - 所有 Python 工具独立 venv，避免依赖冲突
  - 统一目录结构：`工具目录\venv\`
  - 一键启动脚本自动激活虚拟环境
- ✅ **快捷方式优化**：
  - 所有工具配备桌面/开始菜单快捷方式
  - 快捷方式显示工具版本与用途
- ✅ **Claude Code 快捷方式**：
  - 添加到桌面和开始菜单
  - 一键唤起 AI 助手

### 📚 知识库建设
- ✅ **取证实录视频**：
  - 位置：`C:\Penetration\ForensicsTools\ForensicRecorder\`
  - 包含实战案例录像
- ✅ **取证知识库**：
  - 位置：`C:\Penetration\ForensicsTools\Forensic_Knowledge_Base\`
  - 离线文档资料、工具手册、案例库
- ✅ **在线书签库**：
  - 已导入浏览器书签
  - 参考奶牛快传、CTFOS、PD 等平台资源

---

## 📊 工具统计

### 按类别统计

| 类别 | 工具数量 | 主要工具 |
|------|---------|---------|
| AI 工具 | 6 | Claude Code, Cursor, IDA MCP, JADX MCP |
| 移动端取证 | 12 | iLEAPP, ALEAPP, Frida, JADX |
| 磁盘镜像取证 | 7 | Arsenal, Autopsy, FTK Imager, VeraCrypt |
| 内存取证 | 8 | Volatility 2/3, MemProcFS, WinPmem, AVML |
| Windows 取证 | 8 | EZ Tools, Hayabusa, Plaso, Registry Explorer |
| 网络流量取证 | 4 | Wireshark, Zui, NetworkMiner, CTF-NetA |
| 密码破解 | 7 | Hashcat, John, Passware Kit, HashMyFiles |
| 恶意代码分析 | 10 | IDA Pro, Ghidra, Capa, PEStudio, x64dbg |
| 文件分析恢复 | 10 | TSK, Scalpel, ExifTool, EFDD, R-Studio |
| 应急响应 | 8 | Velociraptor, 火绒剑, WebShellKiller |
| CTF 隐写 | 7 | Stegsolve, Steghide, zsteg, CyberChef |
| 辅助工具 | 10+ | uTools, Everything, SpaceSniffer |

### 总计
- **核心取证工具**：90+
- **AI Skills**：26+
- **Python 虚拟环境**：30+
- **一键启动脚本**：50+

---

## 🚀 新增工作流

### AI 辅助逆向分析流程
```
1. 启动 JADX-GUI / IDA Pro
2. 打开待分析的 APK / EXE 文件
3. 启动 Claude Code
4. 直接提问：
   - "分析这个 APK 的核心功能"
   - "查找可疑的网络请求代码"
   - "这个函数是做什么的？"
   - "列出所有加密算法"
5. Claude 自动通过 MCP 调用工具，返回结果
6. 继续追问，深入分析
```

### 移动端动态分析流程
```
1. 启动雷电模拟器
2. 运行 start_frida_ldplayer.ps1
   • 自动连接模拟器
   • 启动 Frida Server
   • 设置端口转发
   • 启动 fridaUiTools
3. 在 fridaUiTools 中选择目标进程
4. 加载 Hook 脚本（可请 Claude 帮忙编写）
5. 实时观察函数调用与返回值
```

### iOS 取证分析流程
```
1. 提取 iOS 数据
   • iTunes 备份
   • 或文件系统镜像
2. 运行 iLEAPP
   • GUI 模式：双击桌面快捷方式
   • CLI 模式：ileapp -i 输入 -o 输出 -t fs
3. 查看 HTML 报告
   • 300+ 工件自动解析
   • 时间线视图
   • CSV 数据导出
4. 使用 Claude 辅助分析报告中的异常点
```

### 综合取证分析流程
```
1. 镜像挂载
   Arsenal Image Mounter → 只读挂载证据镜像
2. 快速工件提取
   Eric Zimmerman Tools → 注册表、事件日志、MFT
3. 内存分析
   Volatility 3 → 进程列表、网络连接、DLL 注入
4. 时间线生成
   Plaso → 统一时间线
5. 威胁狩猎
   Hayabusa → 检测可疑事件
6. 报告生成
   Claude Code → AI 辅助编写取证报告
```

---

## 🎓 使用建议

### 给新手
1. **先看取证实录**：`ForensicRecorder` 目录下的案例录像
2. **熟悉快捷启动**：Maye Lite 快速启动工具
3. **学会用 AI**：遇到问题直接问 Claude
4. **从简单工具开始**：Autopsy → Volatility → IDA

### 给老手
1. **AI 是加速器**：复杂分析交给 Claude + MCP
2. **虚拟环境隔离**：每个工具独立 venv，互不干扰
3. **自动化脚本**：Python + Claude 编写自动化分析脚本
4. **知识库沉淀**：整理自己的案例到 `Forensic_Knowledge_Base`

### 给比武选手
1. **环境预热**：比赛前启动常用工具
2. **快捷键熟悉**：Maye Lite 分类索引
3. **AI 快速答疑**：不确定的技术点问 Claude
4. **脚本准备**：常用脚本放在 `Scripts` 目录

---

## ⚠️ 已知问题

1. **Plaso 安装较慢**：首次启动会编译依赖，耐心等待
2. **Frida Server 启动延迟**：雷电模拟器中 Frida Server 首次启动约 30 秒
3. **MCP 需要 JADX/IDA 运行中**：MCP 工具调用前必须先启动 JADX-GUI 或 IDA Pro

---

## 📝 下一步计划

- [ ] 添加更多操作教学录像
- [ ] 编写工具使用手册（中文）
- [ ] 集成更多 AI 辅助分析脚本
- [ ] 优化虚拟机性能（减少后台服务）
- [ ] 增加 macOS 取证工具支持

---

## 🙏 致谢

- **原项目作者**：makoto56 - 提供了优秀的渗透测试工具集基础
- **MCP 社区**：zinja-coder - 开发了 IDA 和 JADX 的 MCP Server
- **取证社区**：Alexis Brignoni (iLEAPP/ALEAPP 作者)
- **开源社区**：所有工具的开发者和维护者

---

<p align="center">
  <strong>🎉 v20260629 - AI 赋能取证分析 🎉</strong>
</p>

<p align="center">
  更新日期：2026 年 6 月 29 日
</p>
