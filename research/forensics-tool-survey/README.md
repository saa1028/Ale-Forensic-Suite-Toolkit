# 取证 WP 与工具频率调研

本目录保存本轮取证工具更新前的调研数据，用来作为 `forensic-suite-toolkit` 后续虚拟机工具增补、替换和分类调整的依据。

## 数据来源

本轮共整理 3 个站点的数据：

- [Yagami](https://www.yagami.vip)
- [西电取证平台](https://forensics.xidian.edu.cn)
- [DIDCTF 取证平台](https://forensics.didctf.com)

DIDCTF 中保存的站内 WP 页面和外链 WP 页面已经合并到同一个 `didctf` 来源桶中，便于按域名维度管理。

## 目录结构

- [data/raw_html](data/raw_html)：原始 HTML 快照，按来源分为 `yagami`、`xidian`、`didctf`
- [data/text](data/text)：从 HTML 中清洗提取出的纯文本，目录结构与 `raw_html` 一致
- [wp_links.csv](wp_links.csv)：WP 原始链接与来源信息表
- [tool_frequency_total.csv](tool_frequency_total.csv)：工具出现频率总表，也是下一阶段工具更新的主要依据
- [didctf_tool_database.csv](didctf_tool_database.csv)：DIDCTF 工具合集整理表，包含分类、工具名、描述、标签、下载链接、GitHub、官网、图标和更新时间等信息
- [scripts](scripts)：采集、清洗与分析脚本，其中 [build_tool_frequency_total.py](scripts/build_tool_frequency_total.py) 用于重建工具频率总表

## 主要表格

### WP 链接表

[wp_links.csv](wp_links.csv) 记录每篇 WP 的来源站点、标题、原始链接、DIDCTF 详情页链接和外部原文链接。后续如果需要复查某个工具为何被统计，可以从这里追溯到原始文章。

### 工具频率总表

[tool_frequency_total.csv](tool_frequency_total.csv) 是整理后的核心结果，字段如下：

- `tool`：工具或平台名称
- `mentions_total`：总出现次数
- `didctf`：DIDCTF 站内 WP 与外链 WP 合并后的出现次数
- `xidian`：西电取证平台出现次数
- `yagami`：Yagami 出现次数
- `deployment`：使用形态，当前包括 `local`、`online`、`vendor_platform`
- `license_type`：授权/来源类型，当前包括 `open_source`、`commercial`、`freeware`、`unknown`
- `domestic_vendor`：国内取证厂商归属；例如盘古石、美亚柏科、弘连等
- `already_in_project`：该工具是否已出现在当前项目原有工具清单中，取值为 `yes` 或 `no`
- `project_match`：匹配到的原有项目工具名称，用于复核 `already_in_project`

该表目前用于确定虚拟机优先更新的工具。候选工具来自三部分：旧版手工别名词典、[didctf_tool_database.csv](didctf_tool_database.csv) 的工具名，以及根据 WP 内容补充的高可信取证工具名。当前总表 168 行，例如 `hashcat`、`Frida`、`FTK Imager`、`Volatility`、`Wireshark`、`CyberChef`、`binwalk`、`Autopsy` 等。表中同时标记了工具使用形态、授权/来源类型、国内厂商归属，以及是否已在当前项目原有工具清单中，便于后续筛选虚拟机优先集成项。

### DIDCTF 工具数据库

[didctf_tool_database.csv](didctf_tool_database.csv) 来自 DIDCTF 工具合集板块，主要用于补充新工具的分类、项目地址、下载地址、标签、简介、图标和更新时间。后续更新虚拟机时，可以优先检查该表中是否存在官方仓库、官网链接或可下载版本。

## 清洗原则

- 原始 HTML 只放入 `data/raw_html`
- 文本提取结果只放入 `data/text`
- 根目录只保留 3 个主表，减少中间文件干扰
- DIDCTF 站内 WP 与外链 WP 合并为一个来源维度
- 已对采集文本中出现的疑似 API Key 做脱敏处理，统一替换为 `[REDACTED_API_KEY]`

## English Summary

This directory contains the simplified forensics writeup corpus used as evidence for the next `forensic-suite-toolkit` VM update. It includes raw HTML snapshots, extracted text, a writeup link index, a tool-frequency table, and the DIDCTF tool database. The main prioritization table is [tool_frequency_total.csv](tool_frequency_total.csv).
