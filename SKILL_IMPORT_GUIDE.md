# AFST 工具 Skill 导入指南

## 📦 文件说明

**文件**: `afst-forensics-tools.md`  
**类型**: Claude Code / Cursor AI Skill  
**大小**: 约 20 KB  
**工具数量**: 90+  
**更新日期**: 2026-06-29

---

## 🚀 导入方法

### 方法 1: Claude Code（推荐）

#### Windows
```powershell
# 1. 复制 skill 文件到 Claude 目录
Copy-Item "afst-forensics-tools.md" "$env:USERPROFILE\.claude\skills\"

# 2. 重启 Claude Code（如果已运行）
# 按 Win+R，输入：claude
```

#### macOS / Linux
```bash
# 1. 复制 skill 文件
cp afst-forensics-tools.md ~/.claude/skills/

# 2. 重启 Claude Code
claude
```

#### 验证导入
```bash
# 在 Claude Code 中输入
/skills

# 应该能看到 "afst-forensics-tools" 技能
```

---

### 方法 2: Cursor

#### 方法 2.1: 项目级使用（推荐）
1. 将 `afst-forensics-tools.md` 放到项目目录
2. 在 Cursor 中使用 `@` 引用：
   ```
   @afst-forensics-tools.md 应急响应推荐哪些工具
   ```

#### 方法 2.2: 全局配置
1. 打开 Cursor 设置
2. 找到 "Rules for AI"
3. 添加规则：
   ```
   Use @afst-forensics-tools.md for forensics tool guidance
   ```

---

### 方法 3: 其他 AI 工具

#### ChatGPT / Claude.ai
1. 打开 `afst-forensics-tools.md`
2. 复制全部内容
3. 发送给 AI：
   ```
   这是我的工具指南，请记住并在后续对话中使用：
   [粘贴内容]
   ```

#### VS Code Copilot
1. 将文件放到工作区
2. 在 `.vscode/settings.json` 中添加：
   ```json
   {
     "github.copilot.advanced": {
       "contextFiles": ["afst-forensics-tools.md"]
     }
   }
   ```

---

## 💡 使用示例

### 场景 1: 应急响应

**Claude Code**:
```bash
# 直接调用 skill
/afst-forensics-tools

# 然后提问
应急响应场景推荐哪些工具？给我完整流程
```

**Cursor**:
```
@afst-forensics-tools.md 我需要做应急响应，推荐工具和流程
```

---

### 场景 2: Android 取证

**Claude Code**:
```bash
@afst-forensics-tools.md 如何使用 JADX 分析 APK
```

**Cursor**:
```
@afst-forensics-tools.md Android 取证完整流程
```

---

### 场景 3: 恶意代码分析

**Claude Code**:
```bash
@afst-forensics-tools.md 分析恶意代码的工具链是什么
```

**Cursor**:
```
@afst-forensics-tools.md 使用 IDA 和 x64dbg 调试恶意样本
```

---

## 🔍 Skill 功能

### 支持的查询类型

1. **工具查找**
   ```
   Volatility 怎么用？
   有哪些内存取证工具？
   ```

2. **场景推荐**
   ```
   应急响应推荐哪些工具？
   Android 取证流程是什么？
   ```

3. **命令帮助**
   ```
   Hashcat 破解 NTLM 的命令是什么？
   如何用 Frida Hook 函数？
   ```

4. **AI 集成**
   ```
   如何用 Claude 分析 APK？
   IDA MCP 怎么用？
   ```

---

## 📊 包含的工具分类

- ✅ 内存取证（6 个工具）
- ✅ 磁盘取证（6 个工具）
- ✅ 日志分析（5 个工具）
- ✅ Android 分析（7 个工具）
- ✅ 逆向工程（6 个工具）
- ✅ 内网渗透（6 个工具）
- ✅ 流量分析（3 个工具）
- ✅ 密码破解（2 个工具）
- ✅ 辅助工具（10+ 个）
- ✅ AI 集成（IDA MCP + JADX MCP + 26 Skills）

**总计**: 90+ 工具

---

## ⚡ 快速测试

导入后，在 Claude Code 中测试：

```bash
# 测试 1: 列出技能
/skills

# 测试 2: 调用技能
/afst-forensics-tools

# 测试 3: 提问
应急响应推荐哪些工具？
```

如果显示工具列表和使用说明，说明导入成功！

---

## 🔄 更新 Skill

当工具集更新时：

```powershell
# Windows
Copy-Item "afst-forensics-tools.md" "$env:USERPROFILE\.claude\skills\" -Force

# macOS / Linux
cp afst-forensics-tools.md ~/.claude/skills/ -f
```

重启 Claude Code 即可。

---

## 🆘 故障排除

### 问题 1: Skill 不显示

**解决方案**:
1. 检查文件是否在 `~/.claude/skills/` 目录
2. 检查文件名是否为 `afst-forensics-tools.md`
3. 检查文件开头是否有正确的 frontmatter
4. 重启 Claude Code

### 问题 2: 无法调用 Skill

**解决方案**:
1. 使用完整命令: `/afst-forensics-tools`
2. 或直接 @ 引用: `@afst-forensics-tools.md`
3. 检查 skill 名称是否正确

### 问题 3: Cursor 无法识别

**解决方案**:
1. 确保文件在工作区内
2. 使用 `@afst-forensics-tools.md` 引用
3. 如果还不行，直接复制内容到对话

---

## 📚 相关文档

- **完整工具指南**: `TOOLS_GUIDE_INDEX.md`（分 6 个文档）
- **项目主文档**: `README.md`
- **快速介绍**: `INTRO.md`
- **更新日志**: `CHANGELOG_20260629.md`

---

## 🎯 推荐工作流

1. **导入 Skill**: 按上述方法导入
2. **场景化查询**: 根据实际场景提问
3. **工具组合**: 让 AI 推荐工具链
4. **AI 辅助**: 使用 IDA/JADX MCP 加速分析

---

**💡 提示**: 
- Skill 文件可以分享给团队成员
- 支持离线使用（Claude Code 本地模式）
- 定期更新以获取最新工具信息

**📧 问题反馈**: burpsuite@qq.com

---

**生成日期**: 2026-06-29  
**适用于**: Claude Code, Cursor, VS Code Copilot, ChatGPT, Claude.ai
