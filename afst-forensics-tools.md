---
name: afst-forensics-tools
description: Ale Forensic Suite Toolkit (AFST) 阿乐取证工具集完整工具使用指南。涵盖 90+ 取证工具的详细使用说明，包括内存取证、磁盘取证、Android 分析、恶意代码分析、内网渗透等。支持场景化查找和 AI 辅助分析（IDA MCP / JADX MCP）。
---

# Ale Forensic Suite Toolkit (AFST) 阿乐取证工具集 - 工具使用指南

**AI 赋能的取证工具集 · 90+ 专业工具 · 开箱即用**

---

## 📋 快速索引

### 按场景查找工具

#### 🚨 应急响应场景
1. **信息收集**: fscan, Ladon
2. **内存采集**: Magnet RAM Capture, WinPmem
3. **磁盘采集**: FTK Imager, KAPE
4. **日志分析**: Hayabusa, Chainsaw
5. **内存分析**: Volatility, MemProcFS
6. **时间线**: Plaso, Timeline Explorer

#### 🔐 恶意代码分析场景
1. **初步检测**: Detect It Easy, PEStudio
2. **静态分析**: IDA Pro (AI), Ghidra
3. **动态调试**: x64dbg, OllyDbg
4. **行为分析**: Capa, YARA
5. **流量分析**: Wireshark, NetworkMiner

#### 📱 Android 取证场景
1. **数据提取**: ADB
2. **APK 分析**: JADX (AI), APKTool
3. **动态分析**: Frida
4. **日志分析**: ALEAPP
5. **安全评估**: MobSF, Drozer

#### 🎯 CTF 取证场景
- 内存取证: Volatility, MemProcFS
- 磁盘取证: Autopsy, X-Ways
- 流量分析: Wireshark, NetworkMiner
- 密码破解: Hashcat, John
- 数据处理: CyberChef

---

## 🔍 核心取证工具

### 1. Volatility - 内存取证框架

**路径**: `C:\Penetration\ForensicsTools\Volatility\`

**快速启动**:
```bash
volatility3.bat
# 或
C:\Penetration\ForensicsTools\Volatility\venv\Scripts\activate
vol3 -h
```

**常用命令**:
```bash
# 查看镜像信息
vol3 -f memory.dmp windows.info

# 列出进程
vol3 -f memory.dmp windows.pslist

# 扫描网络连接
vol3 -f memory.dmp windows.netscan

# 提取进程内存
vol3 -f memory.dmp windows.memmap --pid 1234 --dump

# 扫描恶意代码
vol3 -f memory.dmp windows.malfind
```

**应用场景**: 应急响应内存分析、恶意代码提取、CTF 内存取证

---

### 2. MemProcFS - 内存进程文件系统

**路径**: `C:\Penetration\ForensicsTools\MemProcFS\`

**快速启动**:
```bash
# 挂载内存镜像
memprocfs.exe -device memory.dmp -mount M:

# 启动 GUI
MemProcFS.exe
```

**使用方法**:
挂载后访问 M:\ 盘符，文件夹结构：
- `name\` - 按进程名浏览
- `pid\` - 按 PID 浏览
- `sys\` - 系统信息
- `forensic\` - 取证时间线

**应用场景**: 快速浏览内存、提取进程文件、生成时间线

---

### 3. IDA Pro - 反汇编神器

**路径**: `C:\Penetration\ReverseTools\IDA\`

**AI 加持**:
```bash
# 在 Claude Code 中使用
@ida 分析这个函数的功能
@ida 查找字符串 "password"
@ida 这个算法是什么加密
```

**常用操作**:
- `F5` - 反编译
- `X` - 交叉引用
- `N` - 重命名
- `Y` - 修改类型
- `G` - 跳转到地址

**应用场景**: 恶意代码分析、算法逆向、漏洞分析

---

### 4. JADX - APK 反编译

**路径**: `C:\Penetration\AndroidTools\jadx\`

**快速启动**:
```bash
jadx-gui.bat  # GUI 版本
jadx-cli.bat  # 命令行版本
```

**AI 加持**:
```bash
# 在 Claude Code 中使用
@jadx 分析这个 APK 的网络请求
@jadx 查找敏感权限
@jadx 分析加密算法
```

**应用场景**: APK 逆向、恶意代码检测、漏洞挖掘

---

### 5. X-Ways Forensics - 商业取证套件

**路径**: `C:\Penetration\ForensicsTools\X-Ways\`

**主要功能**:
- 磁盘镜像创建（E01/AFF）
- 文件恢复
- 数据雕刻
- $MFT 解析
- 注册表分析

**应用场景**: 磁盘取证、数据恢复、反取证检测

---

### 6. FTK Imager - 镜像采集工具

**路径**: `C:\Penetration\ForensicsTools\FTK Imager\`

**常用操作**:
1. 创建镜像: File → Create Disk Image
2. 挂载镜像: File → Add Evidence Item
3. 导出文件: 右键 → Export Files
4. 内存采集: File → Capture Memory

**应用场景**: 现场镜像采集、文件提取、内存 dump

---

### 7. Autopsy - 开源取证平台

**路径**: `C:\Penetration\ForensicsTools\AutoSpy\`

**主要模块**:
- Recent Activity: 浏览器历史、最近文件
- Hash Lookup: 已知恶意文件检测
- Keyword Search: 关键词搜索
- Timeline Analysis: 时间线分析

**应用场景**: 电子数据取证、案件调查、CTF 取证

---

### 8. Hayabusa - Windows 事件日志分析

**路径**: `C:\Penetration\ForensicsTools\Hayabusa\`

**常用命令**:
```bash
# 分析单个 evtx
hayabusa.exe csv-timeline -f Security.evtx -o result.csv

# 分析整个日志目录
hayabusa.exe csv-timeline -d C:\Windows\System32\winevt\Logs -o timeline.csv

# 实时监控
hayabusa.exe live-analysis
```

**应用场景**: 应急响应、威胁狩猎、时间线分析

---

### 9. Wireshark - 网络流量分析

**路径**: `C:\Penetration\TrafficTools\Wireshark\`

**常用过滤器**:
```
http                          # HTTP 流量
tcp.stream eq 0               # TCP 流
ip.addr == 192.168.1.1        # 特定 IP
frame contains "password"     # 包含关键字
```

**提取文件**: File → Export Objects → HTTP

**应用场景**: 网络取证、恶意流量分析、协议逆向

---

### 10. NetworkMiner - 网络取证

**路径**: `C:\Penetration\ForensicsTools\NetworkMiner\`

**主要功能**:
- Hosts: 识别所有主机
- Files: 自动提取所有文件
- Credentials: 提取明文密码
- Images: 提取所有图片
- Messages: 提取聊天记录

**应用场景**: 快速 PCAP 分析、自动化取证、CTF 流量题

---

### 11. ApacheLogsViewer (httpLogsView) - Web 服务器日志分析

**路径**: `C:\Penetration\ForensicsTools\ApacheLogsViewer\`

**支持格式**:
- Apache/Apache2 访问日志
- IIS (Microsoft Internet Information Services) 日志
- Nginx 访问日志
- Amazon CloudFront Web 分发日志

**主要功能**:
- 可视化日志查看，支持排序和筛选
- 按 IP、URL、状态码、User-Agent 等字段过滤
- 导出为 HTML/XML/CSV/TXT 格式
- 统计分析（访问量、状态码分布、热门 URL）
- 支持多种日志格式自动识别

**常用场景**:
```
1. Web 入侵分析
   - 查找异常 URL 请求（SQL 注入、命令注入）
   - 识别 WebShell 访问痕迹
   - 分析攻击者 IP 和行为模式

2. 应急响应
   - 快速定位攻击时间线
   - 提取恶意请求特征
   - 溯源攻击者身份

3. CTF Web 取证
   - 分析 flag 泄漏路径
   - 还原攻击利用链
   - 识别隐藏的后门访问
```

**应用场景**: Web 入侵分析、日志取证、应急响应、CTF Web 题

---

## 📱 Android 工具

### 12. ADB - Android 调试桥

**路径**: `C:\Penetration\AndroidTools\AdbDriver\`

**常用命令**:
```bash
adb devices                                    # 连接设备
adb install app.apk                            # 安装 APK
adb pull /data/app/com.example.app/base.apk   # 提取 APK
adb pull /data/data/com.example.app/           # 提取数据
adb shell screencap -p /sdcard/screen.png      # 截图
adb logcat | grep "关键字"                     # 日志
adb forward tcp:8080 tcp:8080                  # 端口转发
```

**应用场景**: 应用调试、数据提取、设备取证

---

### 13. Frida - 动态插桩

**路径**: `C:\Penetration\AndroidTools\Frida\`

**快速启动**:
```bash
# 启动 Frida Server（手机上）
adb push frida-server /data/local/tmp/
adb shell "chmod 755 /data/local/tmp/frida-server"
adb shell "/data/local/tmp/frida-server &"

# 列出进程
frida-ps -U

# 注入脚本
frida -U -f com.example.app -l hook.js
```

**应用场景**: 绕过 Root 检测、SSL Pinning、协议逆向

---

### 13. ALEAPP - Android 日志分析

**路径**: `C:\Penetration\ForensicsTools\ALEAPP\`

**分析内容**:
- 应用使用记录
- 通话/短信记录
- 浏览器历史
- 位置信息

**应用场景**: Android 设备取证、用户行为分析

---

## 🌐 内网渗透工具

### 14. Mimikatz - 凭据提取

**路径**: `C:\Penetration\IntranetTools\Mimikatz\`

**常用命令**:
```bash
privilege::debug                # 提升权限
sekurlsa::logonpasswords        # 导出密码
sekurlsa::tickets /export       # 导出票据
sekurlsa::pth /user:Admin /domain:DOMAIN /ntlm:HASH  # PTH
```

**应用场景**: 凭据窃取、横向移动、域渗透

⚠️ 仅限授权测试

---

### 15. BloodHound - AD 关系分析

**路径**: `C:\Penetration\IntranetTools\BloodHound\`

**使用流程**:
1. 使用 SharpHound 采集域信息
2. 导入 BloodHound
3. 分析攻击路径
4. 查找到 Domain Admin 的路径

**应用场景**: 域渗透、权限提升路径分析

---

### 16. fscan - 内网扫描

**路径**: `C:\Penetration\ScanTools\fscan\`

**快速启动**:
```bash
fscan.exe -h 192.168.1.0/24              # 扫描网段
fscan.exe -h 192.168.1.0/24 -p 1-65535   # 详细扫描
fscan.exe -h 192.168.1.0/24 -o result.txt # 保存结果
```

**应用场景**: 内网资产发现、快速信息收集

---

## 🔬 逆向工程工具

### 17. Ghidra - NSA 开源逆向工具

**路径**: `C:\Penetration\ReverseTools\Ghidra\`

**主要功能**:
- 多架构支持
- 反编译器
- 脚本自动化
- 协作分析

**应用场景**: 免费替代 IDA、大型项目逆向

---

### 18. x64dbg - 动态调试器

**路径**: `C:\Penetration\ReverseTools\x64dbg\`

**常用快捷键**:
- `F2` - 设置断点
- `F7` - 单步进入
- `F8` - 单步跳过
- `F9` - 运行
- `Ctrl+G` - 跳转

**应用场景**: 程序调试、反混淆、算法提取

---

### 19. dnSpy - .NET 反编译

**路径**: `C:\Penetration\ReverseTools\dnSpy\`

**主要功能**:
- C# 反编译
- 动态调试
- 代码修改
- 重新编译

**应用场景**: .NET 逆向、Unity 游戏破解

---

### 20. Detect It Easy - 壳检测

**路径**: `C:\Penetration\ReverseTools\DetectItEasy\`

**检测内容**:
- 文件格式
- 编译器
- 加壳/混淆
- 签名信息

**应用场景**: 样本分类、脱壳前检测

---

## 🔐 密码破解工具

### 21. Hashcat - GPU 加速密码破解

**路径**: `C:\Penetration\CrackTools\hashcat\`

**常用命令**:
```bash
# 字典攻击
hashcat -m 0 -a 0 hash.txt wordlist.txt

# 掩码攻击
hashcat -m 0 -a 3 hash.txt ?a?a?a?a?a?a
```

**常见哈希类型**:
- `-m 0`: MD5
- `-m 1000`: NTLM
- `-m 1800`: sha512crypt
- `-m 13100`: Kerberos TGS

**应用场景**: 密码恢复、哈希碰撞、CTF

---

### 22. John the Ripper - 密码破解

**路径**: `C:\Penetration\CrackTools\john\`

**常用命令**:
```bash
john --wordlist=wordlist.txt hash.txt  # 破解
john --show hash.txt                   # 查看结果
ssh2john id_rsa > hash.txt             # 格式转换
```

**应用场景**: 多格式密码破解、弱口令检测

---

## 🛠️ 辅助工具

### 23. CyberChef - 数据处理瑞士军刀

**路径**: `C:\Penetration\CTFTools\CyberChef\`

**常用操作**:
- Base64 编解码
- URL 编解码
- AES 加解密
- 图片隐写提取
- 数据格式转换

**应用场景**: CTF 解题、快速数据处理

---

### 24. Capa - 恶意代码能力识别

**路径**: `C:\Penetration\ForensicsTools\capa\`

**快速启动**:
```bash
capa malware.exe           # 分析
capa -v malware.exe        # 详细输出
capa -j malware.exe        # JSON 格式
```

**应用场景**: 快速恶意代码分类、功能能力识别

---

### 25. PEStudio - PE 文件分析

**路径**: `C:\Penetration\ForensicsTools\PEStudio\`

**主要功能**:
- 导入表分析
- 字符串提取
- 熵值计算
- VirusTotal 查询
- 数字签名验证

**应用场景**: 快速样本分类、恶意代码初筛

---

## 🤖 AI 辅助功能

### Claude + IDA MCP

**在 Claude Code 中直接分析二进制文件**:
```bash
@ida 列出所有导入函数
@ida 分析函数 sub_401000 的功能
@ida 查找字符串 "http"
@ida 这个函数是什么加密算法
@ida 识别反调试技术
```

### Claude + JADX MCP

**在 Claude Code 中直接分析 APK**:
```bash
@jadx 获取应用的网络请求
@jadx 查找敏感权限
@jadx 分析加密方法
@jadx 查找存储路径
@jadx 这个应用有什么可疑行为
```

### 26+ CTF & 安全技能

```bash
/ctf-forensics         # 数字取证技能
/ctf-reverse           # 逆向工程技能
/ctf-web               # Web 安全技能
/ctf-crypto            # 密码学技能
/ctf-pwn               # 二进制利用技能
/ssh-penetration-testing  # SSH 渗透测试
/wireshark-analysis    # 流量分析
/memory-forensics      # 内存取证技能
```

---

## 📊 工具分类索引

### 内存取证
- Volatility
- MemProcFS
- Magnet RAM Capture
- WinPmem
- AVML
- LiME

### 磁盘取证
- X-Ways Forensics
- FTK Imager
- Autopsy
- Arsenal Image Mounter
- DiskGenius
- R-Studio

### 日志分析
- Hayabusa
- Chainsaw
- Eric Zimmerman Tools
- LogParser
- Plaso

### Android 分析
- JADX (AI 集成)
- APKTool
- ADB
- Frida
- Android Killer
- MobSF
- ALEAPP

### 逆向工程
- IDA Pro (AI 集成)
- Ghidra
- x64dbg
- dnSpy
- Detect It Easy
- Recaf

### 内网渗透
- Cobalt Strike
- Metasploit
- Mimikatz
- BloodHound
- Impacket

### 流量分析
- Wireshark
- NetworkMiner
- Burp Suite

---

## 🚀 快速启动方式

### 1. 使用 Maye Lite（推荐）
- 按全局快捷键启动
- 使用字母索引（Q-取证, A-AI, N-内网）
- 单击图标启动

### 2. 命令行启动
所有工具都有 `.bat` 启动脚本：
```batch
C:\Penetration\[分类]\[工具名]\[工具名].bat
```

### 3. AI 辅助启动
在 Claude Code 中：
```bash
启动 Volatility 分析内存
打开 JADX 分析这个 APK
使用 IDA 逆向这个二进制文件
```

---

## 📝 使用说明

此 Skill 提供 AFST 中 90+ 工具的快速使用指南，包括：
- 工具路径和快速启动命令
- 常用命令和操作
- 应用场景说明
- AI 辅助使用方法

**工具基础路径**: `C:\Penetration\`

**虚拟环境**: 每个 Python 工具都有独立的 venv

**Maye Lite**: 所有工具都可通过 Maye Lite 快速启动

---

**版本**: 20260629  
**工具数量**: 90+  
**支持场景**: 应急响应、恶意代码分析、Android 取证、内网渗透、CTF 取证

**⚠️ 注意**: 内网渗透工具仅限授权测试环境使用
