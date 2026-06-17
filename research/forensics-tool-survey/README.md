# Forensics Tool Survey

This directory records the first round of evidence collection and tool-frequency analysis used to guide future updates to the `forensic-suite-toolkit` virtual machine.

## Scope

The survey focused on three websites that continuously accumulate digital forensics writeups, competition writeups, and tool references:

1. `https://www.yagami.vip`
2. `https://forensics.xidian.edu.cn`
3. `https://forensics.didctf.com`

The goal of this stage was:

- collect available writeups and tool pages
- preserve a reproducible raw-data snapshot
- extract text for analysis
- count tool mentions across the corpus
- produce an update reference for the next VM tool-refresh stage

## Directory Layout

- [data/raw](data/raw)
  - saved source snapshots used in this round
- [data/processed](data/processed)
  - cleaned tables and analysis outputs
- [scripts](scripts)
  - collection and analysis script used for this round
- [SUMMARY.md](SUMMARY.md)
  - concise findings for VM update planning

## Raw Data Included

Current repository snapshot keeps the key DIDCTF raw inputs that were needed to recover real writeup links and metadata:

- [writeups_api.json](data/raw/didctf/writeups_api.json)
- [wp.html](data/raw/didctf/wp.html)
- [工具合集.html](data/raw/didctf/工具合集.html)

These files were enough to reconstruct:

- DIDCTF writeup listing metadata
- DIDCTF external-link targets
- DIDCTF tool-page metadata

Large downstream mirrors and full downloaded external pages remain in the local working corpus used during analysis, while the repository keeps the lighter-weight source artifacts and processed outputs needed for reproducibility.

## Processed Outputs

Main outputs copied into this repository:

- [didctf_writeups.csv](data/processed/didctf_writeups.csv)
- [didctf_tools.csv](data/processed/didctf_tools.csv)
- [didctf_tool_tags.csv](data/processed/didctf_tool_tags.csv)
- [index.csv](data/processed/index.csv)
- [tool_frequency.csv](data/processed/tool_frequency.csv)
- [forensics_tool_frequency.csv](data/processed/forensics_tool_frequency.csv)
- [tool_frequency_by_site.csv](data/processed/tool_frequency_by_site.csv)
- [tool_hits_by_doc.json](data/processed/tool_hits_by_doc.json)

## Notes On Cleaning

The raw frequency results contain both:

- true tool names, such as `FTK Imager`, `Volatility`, `X-Ways Forensics`, `Wireshark`
- environment or generic technical terms, such as `Docker`, `MySQL`, `grep`, `find`, `strings`

For VM refresh decisions, priority should be given to the cleaned forensics-oriented list in:

- [forensics_tool_frequency.csv](data/processed/forensics_tool_frequency.csv)

## Reproduction

The script used in this round is:

- [collect_forensics_wp.py](scripts/collect_forensics_wp.py)

Typical usage during this stage:

```powershell
python collect_forensics_wp.py --rebuild-from-raw
python collect_forensics_wp.py --crawl-didctf-external
python collect_forensics_wp.py --analyze-only
```

## Why This Matters For The VM

This survey is the evidence base for the next phase:

- decide which tools are worth adding
- decide which tools deserve category promotion or better launcher placement
- identify tools that appear frequently in recent public writeups
- identify Chinese-language ecosystem tools that are heavily used in actual practice

The next VM update can now proceed with a traceable rationale instead of ad hoc tool accumulation.
