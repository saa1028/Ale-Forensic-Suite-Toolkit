# Survey Summary

## What This Corpus Contains

This survey corpus contains raw HTML, extracted text, WP source links, DIDCTF tool database entries, and a tool-frequency summary collected from:

- `https://www.yagami.vip`
- `https://forensics.xidian.edu.cn`
- `https://forensics.didctf.com`

## Main Tables

Use these three files for the next VM update phase:

- `wp_links.csv`
  - source link table for collected writeups
- `tool_frequency_total.csv`
  - main tool ranking table with per-source counts; DIDCTF site pages and DIDCTF external writeups are merged into one `didctf` column
- `didctf_tool_database.csv`
  - DIDCTF tool collection table with project links

## Top Tool Frequency Signal

Top rows from `tool_frequency_total.csv`:

| tool | mentions_total | didctf | xidian | yagami |
| --- | ---: | ---: | ---: | ---: |
| 火眼证据分析 | 552 | 236 | 316 | 0 |
| hashcat | 116 | 42 | 58 | 16 |
| 盘古石 | 96 | 54 | 32 | 10 |
| John the Ripper | 92 | 10 | 76 | 6 |
| FTK Imager | 88 | 28 | 54 | 6 |
| 美亚取证 | 85 | 27 | 58 | 0 |
| VMware | 65 | 11 | 48 | 6 |
| IDA | 57 | 18 | 39 | 0 |

## How To Use This For The VM

Start from `tool_frequency_total.csv` when deciding which tools should be added, upgraded, or promoted in the launcher.

Use `didctf_tool_database.csv` to find project links, download links, GitHub links, and official websites.

Use `wp_links.csv` to trace why a tool appeared in the corpus and which source material supported the ranking.
