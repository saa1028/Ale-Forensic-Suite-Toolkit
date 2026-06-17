# Survey Summary

## Websites Used

- `https://www.yagami.vip`
- `https://forensics.xidian.edu.cn`
- `https://forensics.didctf.com`

## What Was Collected

1. Public writeup pages from Yagami
2. Public writeup pages from XD Forensics Wiki
3. DIDCTF writeup listing metadata
4. DIDCTF writeup external links
5. DIDCTF tool-page metadata
6. Text extracted from saved HTML and downloaded external pages

## DIDCTF Snapshot

From the saved DIDCTF writeup API snapshot:

- total writeups: `48`
- external-link writeups: `46`
- internal markdown writeups: `2`

This matters because DIDCTF was not fully recoverable from the saved listing HTML alone. The `writeups_api.json` snapshot became the authoritative source for real writeup IDs and external target links.

## Main Frequency Signal

Top items from the cleaned forensics-oriented frequency output:

1. `火眼证据分析` - `552`
2. `hashcat` - `116`
3. `盘古石` - `96`
4. `John the Ripper` - `92`
5. `FTK Imager` - `88`
6. `美亚取证` - `85`
7. `VMware` - `65`
8. `IDA` - `57`
9. `Volatility` - `56`
10. `X-Ways Forensics` - `46`
11. `ADB` - `40`
12. `010 Editor` - `40`
13. `JADX` - `40`
14. `CyberChef` - `38`
15. `Wireshark` - `35`

Reference file:

- [forensics_tool_frequency.csv](data/processed/forensics_tool_frequency.csv)

## Important Caveat

The broad frequency table also contains non-tool infrastructure terms such as:

- `Docker`
- `MySQL`
- `Redis`
- `grep`
- `find`
- `strings`

Those are useful for environment awareness, but they should not be treated as direct candidates for the curated forensics tool VM unless there is a separate packaging reason.

## Recommended Use In The Next VM Phase

### High-priority candidates to verify and improve

- `FTK Imager`
- `Volatility`
- `X-Ways Forensics`
- `Wireshark`
- `CyberChef`
- `010 Editor`
- `ADB`
- `JADX`
- `Autopsy`
- `MemProcFS`

### China-specific or competition-driven tools worth explicit tracking

- `火眼证据分析`
- `美亚取证`
- `取证大师`
- `弘连`
- `雷电 APP 智能分析`

### Password / artifact recovery set worth keeping together

- `hashcat`
- `John the Ripper`
- `HashMyFiles`
- `7-Zip`

## Suggested Next Actions

1. compare current VM inventory against the top-ranked tools
2. mark missing tools, outdated tools, and weak-category coverage
3. reorganize launcher categories around real usage:
   - disk and filesystem
   - memory
   - mobile
   - traffic and logs
   - password recovery
   - reverse and binary analysis
   - CTF forensics helpers
4. keep this survey directory updated as a rolling evidence base for future releases
