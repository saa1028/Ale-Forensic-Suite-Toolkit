import argparse
import csv
import json
import re
import time
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup


ROOT = Path("forensics-wp-corpus")
USER_AGENT = "Mozilla/5.0 (compatible; ForensicsWPCorpus/1.0; +https://github.com/saa1028/forensic-suite-toolkit)"
DIDCTF_BASE = "https://forensics.didctf.com"


TOOL_ALIASES = {
    "Autopsy": [r"\bAutopsy\b"],
    "FTK Imager": [r"\bFTK\s+Imager\b", r"\bFTK\b"],
    "EnCase": [r"\bEnCase\b"],
    "X-Ways Forensics": [r"\bX-?Ways\b", r"\bWinHex\b"],
    "Magnet AXIOM": [r"\bMagnet\s+AXIOM\b", r"\bAXIOM\b"],
    "Volatility": [r"\bVolatility(?:\s*2|\s*3)?\b", r"\bvol\.py\b"],
    "MemProcFS": [r"\bMemProcFS\b"],
    "Wireshark": [r"\bWireshark\b"],
    "tshark": [r"\btshark\b"],
    "NetworkMiner": [r"\bNetworkMiner\b"],
    "Zeek": [r"\bZeek\b", r"\bBro\b"],
    "binwalk": [r"\bbinwalk\b"],
    "foremost": [r"\bforemost\b"],
    "scalpel": [r"\bscalpel\b"],
    "strings": [r"\bstrings\b"],
    "grep": [r"\bgrep\b", r"\bripgrep\b", r"\brg\b"],
    "find": [r"\bfind\b"],
    "file": [r"\bfile\b"],
    "xxd": [r"\bxxd\b"],
    "010 Editor": [r"\b010\s*Editor\b"],
    "HxD": [r"\bHxD\b"],
    "CyberChef": [r"\bCyberChef\b"],
    "StegSolve": [r"\bStegSolve\b"],
    "zsteg": [r"\bzsteg\b"],
    "exiftool": [r"\bexiftool\b"],
    "ExifTool": [r"\bExifTool\b"],
    "pngcheck": [r"\bpngcheck\b"],
    "Audacity": [r"\bAudacity\b"],
    "Sonic Visualiser": [r"\bSonic\s+Visualiser\b"],
    "R-Studio": [r"\bR-?Studio\b"],
    "DiskGenius": [r"\bDiskGenius\b"],
    "取证大师": [r"取证大师"],
    "火眼证据分析": [r"火眼证据分析", r"火眼"],
    "火眼仿真取证": [r"火眼仿真取证"],
    "美亚取证": [r"美亚", r"DC-?4501", r"取证航母"],
    "弘连": [r"弘连"],
    "盘古石": [r"盘古石"],
    "雷电 APP 智能分析": [r"雷电\s*APP\s*智能分析"],
    "SQLite Browser": [r"DB\s+Browser\s+for\s+SQLite", r"SQLite\s+Browser"],
    "sqlite3": [r"\bsqlite3\b"],
    "MySQL": [r"\bMySQL\b", r"\bmysql\b"],
    "Redis": [r"\bRedis\b", r"\bredis-cli\b"],
    "Docker": [r"\bDocker\b", r"\bdocker\b"],
    "Kubernetes": [r"\bKubernetes\b", r"\bk8s\b", r"\bkubectl\b"],
    "VMware": [r"\bVMware\b"],
    "VirtualBox": [r"\bVirtualBox\b"],
    "qemu": [r"\bqemu\b", r"\bqemu-img\b"],
    "7-Zip": [r"\b7-?Zip\b", r"\b7z\b"],
    "John the Ripper": [r"\bJohn(?:\s+the\s+Ripper)?\b", r"\bjohn\b"],
    "hashcat": [r"\bhashcat\b"],
    "HashMyFiles": [r"\bHashMyFiles\b"],
    "YARA": [r"\bYARA\b", r"\byara\b"],
    "IDA": [r"\bIDA(?:\s+Pro)?\b"],
    "Ghidra": [r"\bGhidra\b"],
    "JADX": [r"\bjadx\b", r"\bJADX\b"],
    "apktool": [r"\bapktool\b"],
    "ADB": [r"\badb\b", r"\bADB\b"],
}

NON_TOOL_TERMS = {
    "MySQL",
    "Docker",
    "Kubernetes",
    "Redis",
    "file",
    "grep",
    "find",
    "strings",
    "qemu",
    "sqlite3",
    "xxd",
    "Linux",
}


@dataclass
class Page:
    site: str
    title: str
    url: str
    path: Path
    text_path: Path
    status: int


def session() -> requests.Session:
    s = requests.Session()
    s.headers.update({"User-Agent": USER_AGENT})
    return s


def safe_name(value: str, max_len: int = 120) -> str:
    value = re.sub(r"https?://", "", value)
    value = re.sub(r"[\\/:*?\"<>|\s]+", "_", value).strip("_")
    return value[:max_len] or "index"


def normalize_url(base: str, href: str) -> str | None:
    if not href or href.startswith(("mailto:", "tel:", "javascript:")):
        return None
    url = urljoin(base, href)
    url, _ = urldefrag(url)
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None
    return url


def get_html(s: requests.Session, url: str) -> tuple[int, str]:
    r = s.get(url, timeout=30)
    r.encoding = r.apparent_encoding or r.encoding
    return r.status_code, r.text


def page_text(html: str) -> tuple[str, str]:
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "noscript", "svg"]):
        tag.decompose()
    title = soup.title.get_text(" ", strip=True) if soup.title else ""
    main = soup.select_one("article") or soup.select_one("main") or soup.body or soup
    text = main.get_text("\n", strip=True)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return title, text


def save_page(site: str, url: str, status: int, html: str) -> Page:
    site_dir = ROOT / "raw" / site
    text_dir = ROOT / "text" / site
    site_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)
    title, text = page_text(html)
    name = safe_name(urlparse(url).path.strip("/") or title or url)
    html_path = site_dir / f"{name}.html"
    txt_path = text_dir / f"{name}.txt"
    html_path.write_text(html, encoding="utf-8", errors="replace")
    txt_path.write_text(f"{title}\n{url}\n\n{text}\n", encoding="utf-8", errors="replace")
    return Page(site, title, url, html_path, txt_path, status)


def save_local_page(html_path: Path) -> Page:
    site = html_path.parent.name
    text_dir = ROOT / "text" / site
    text_dir.mkdir(parents=True, exist_ok=True)
    html = html_path.read_text(encoding="utf-8", errors="replace")
    title, text = page_text(html)
    txt_path = text_dir / f"{html_path.stem}.txt"
    txt_path.write_text(f"{title}\n{html_path}\n\n{text}\n", encoding="utf-8", errors="replace")
    return Page(site, title, str(html_path), html_path, txt_path, 200)


def crawl_yagami(s: requests.Session, limit_pages: int | None = None) -> list[Page]:
    site = "yagami"
    start = "https://www.yagami.vip/"
    queue = [start]
    seen = set()
    article_urls = []
    pages: list[Page] = []

    while queue:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        status, html = get_html(s, url)
        if status != 200:
            continue
        soup = BeautifulSoup(html, "lxml")
        for a in soup.select("a[href]"):
            next_url = normalize_url(url, a.get("href"))
            if not next_url:
                continue
            parsed = urlparse(next_url)
            if parsed.netloc != "www.yagami.vip":
                continue
            if parsed.path.startswith("/archives/") and next_url not in article_urls:
                article_urls.append(next_url)
            if re.fullmatch(r"/page/\d+", parsed.path) and next_url not in seen and next_url not in queue:
                queue.append(next_url)
        time.sleep(0.3)

    if limit_pages:
        article_urls = article_urls[:limit_pages]
    for url in article_urls:
        status, html = get_html(s, url)
        if status == 200:
            pages.append(save_page(site, url, status, html))
        time.sleep(0.3)
    return pages


def crawl_xidian(s: requests.Session, limit_pages: int | None = None) -> list[Page]:
    site = "xidian"
    start = "https://forensics.xidian.edu.cn/writeups/"
    queue = [start]
    seen = set()
    pages: list[Page] = []

    while queue:
        url = queue.pop(0)
        if url in seen:
            continue
        seen.add(url)
        status, html = get_html(s, url)
        if status != 200:
            continue
        parsed = urlparse(url)
        if "/writeups/" in parsed.path:
            pages.append(save_page(site, url, status, html))
            if limit_pages and len(pages) >= limit_pages:
                break
        soup = BeautifulSoup(html, "lxml")
        for a in soup.select("a[href]"):
            next_url = normalize_url(url, a.get("href"))
            if not next_url:
                continue
            p = urlparse(next_url)
            if p.netloc != "forensics.xidian.edu.cn":
                continue
            if "/writeups/" not in p.path:
                continue
            if any(part.startswith(("assets", "javascripts", "stylesheets")) for part in p.path.split("/")):
                continue
            if next_url not in seen and next_url not in queue:
                queue.append(next_url)
        time.sleep(0.25)
    return pages


def rebuild_from_raw() -> list[Page]:
    pages = []
    for html_path in sorted((ROOT / "raw").glob("*/*.html")):
        pages.append(save_local_page(html_path))
    return pages


def first_text(node) -> str:
    if node is None:
        return ""
    return " ".join(node.get_text(" ", strip=True).split())


def parse_didctf_writeups() -> list[dict[str, str]]:
    api_path = ROOT / "raw" / "didctf" / "writeups_api.json"
    if api_path.exists():
        data = json.loads(api_path.read_text(encoding="utf-8"))
        rows = []
        for idx, item in enumerate(data, 1):
            writeup_id = item.get("id", "")
            content_type = item.get("content_type", "")
            link = item.get("link", "") or ""
            detail_url = f"{DIDCTF_BASE}/practice/writeups/{writeup_id}" if writeup_id else ""
            row = {
                "index": f"#{idx:03d}",
                "id": writeup_id,
                "title": item.get("title", "") or "",
                "event": item.get("category1_name", "") or "",
                "source_type": "站内" if content_type == "markdown" else "外链",
                "author": item.get("author_name", "") or "",
                "origin": item.get("source", "") or "",
                "meta": f"{item.get('view_count', 0)} 次浏览",
                "content_type": content_type,
                "writeup_type": item.get("writeup_type", "") or "",
                "category1_id": str(item.get("category1_id", "") or ""),
                "view_count": str(item.get("view_count", "") or ""),
                "link": link,
                "detail_url": detail_url,
            }
            rows.append(row)
        return rows

    files = sorted((ROOT / "raw" / "didctf").glob("*.html"))
    if not files:
        return []

    html = ""
    for path in files:
        content = path.read_text(encoding="utf-8", errors="ignore")
        if "writeup-item-card" in content:
            html = content
            break
    if not html:
        return []

    soup = BeautifulSoup(html, "lxml")
    rows = []
    for card in soup.select(".writeup-item-card"):
        index = first_text(card.select_one(".writeups-item-index"))
        title = first_text(card.select_one(".writeups-item-title"))
        tags = [first_text(tag) for tag in card.select(".ant-tag")]
        meta = first_text(card.select_one(".writeups-item-meta"))
        row = {
            "index": index,
            "id": "",
            "title": title,
            "event": tags[0] if len(tags) > 0 else "",
            "source_type": tags[1] if len(tags) > 1 else "",
            "author": tags[2] if len(tags) > 2 else "",
            "origin": tags[3] if len(tags) > 3 else "",
            "meta": meta,
            "content_type": "",
            "writeup_type": "",
            "category1_id": "",
            "view_count": "",
            "link": "",
            "detail_url": "",
        }
        if row["index"] and row["title"]:
            rows.append(row)
    return rows


def parse_didctf_tools() -> list[dict[str, str]]:
    files = sorted((ROOT / "raw" / "didctf").glob("*.html"))
    if not files:
        return []

    html = ""
    for path in files:
        content = path.read_text(encoding="utf-8", errors="ignore")
        if "tools-card-actions" in content and "Lovelymem" in content:
            html = content
            break
    if not html:
        return []

    # Remove svg blocks so icon markup does not pollute text extraction.
    cleaned = re.sub(r"<svg\b.*?</svg>", "", html, flags=re.IGNORECASE | re.DOTALL)
    soup = BeautifulSoup(cleaned, "lxml")
    rows = []
    for action in soup.select(".tools-card-actions"):
        card = action
        while card and "ant-card-body" not in (card.get("class") or []):
            card = card.parent
        if card is None:
            continue

        title = first_text(card.select_one("h5"))
        desc = first_text(card.select_one(".ant-typography-ellipsis-multiple-line"))
        tags = [first_text(tag) for tag in card.select(".ant-tag")]
        links = {}
        for anchor in action.select("a[href]"):
            label = first_text(anchor)
            href = anchor.get("href", "")
            if label and href:
                links[label] = href
        row = {
            "title": title,
            "description": desc,
            "tags": " | ".join(tags),
            "download": links.get("下载", ""),
            "github": links.get("GitHub", ""),
            "website": links.get("官网", ""),
        }
        if row["title"]:
            rows.append(row)
    return rows


def fetch_binary(s: requests.Session, url: str) -> tuple[int, bytes, str]:
    r = s.get(url, timeout=45, allow_redirects=True)
    content_type = r.headers.get("Content-Type", "")
    return r.status_code, r.content, content_type


def extract_text_from_bytes(content: bytes, content_type: str) -> str:
    if "text/html" in content_type or "xml" in content_type:
        html = content.decode("utf-8", errors="replace")
        _, text = page_text(html)
        return text
    if "text/plain" in content_type or "json" in content_type:
        return content.decode("utf-8", errors="replace")
    return ""


def crawl_didctf_external_writeups(s: requests.Session) -> list[Page]:
    api_path = ROOT / "raw" / "didctf" / "writeups_api.json"
    if not api_path.exists():
        return []

    data = json.loads(api_path.read_text(encoding="utf-8"))
    raw_dir = ROOT / "raw" / "didctf_external"
    text_dir = ROOT / "text" / "didctf_external"
    raw_dir.mkdir(parents=True, exist_ok=True)
    text_dir.mkdir(parents=True, exist_ok=True)

    pages: list[Page] = []
    for idx, item in enumerate(data, 1):
        if item.get("content_type") != "link":
            continue
        url = (item.get("link") or "").strip()
        if not url:
            continue

        status = 0
        content = b""
        content_type = ""
        try:
            status, content, content_type = fetch_binary(s, url)
        except requests.RequestException:
            continue

        title = item.get("title", "") or f"writeup_{idx:03d}"
        writeup_id = item.get("id", "") or f"writeup_{idx:03d}"
        ext = ".html"
        if "pdf" in content_type:
            ext = ".pdf"
        elif "zip" in content_type or url.lower().endswith(".zip"):
            ext = ".zip"
        elif "word" in content_type or url.lower().endswith((".doc", ".docx")):
            ext = ".docx" if url.lower().endswith(".docx") else ".doc"
        elif "markdown" in content_type or url.lower().endswith(".md"):
            ext = ".md"
        elif "text/plain" in content_type or url.lower().endswith(".txt"):
            ext = ".txt"

        stem = safe_name(f"{idx:03d}_{title}_{writeup_id}")
        raw_path = raw_dir / f"{stem}{ext}"
        raw_path.write_bytes(content)

        extracted = extract_text_from_bytes(content, content_type)
        txt_path = text_dir / f"{stem}.txt"
        header = "\n".join(
            [
                title,
                url,
                f"id={writeup_id}",
                f"source={item.get('source', '')}",
                f"author={item.get('author_name', '')}",
                "",
            ]
        )
        txt_path.write_text(header + extracted + "\n", encoding="utf-8", errors="replace")
        pages.append(Page("didctf_external", title, url, raw_path, txt_path, status))
        time.sleep(0.35)

    return pages


def write_csv(path: Path, rows: list[dict[str, str]], fieldnames: list[str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def export_didctf_tables() -> None:
    writeups = parse_didctf_writeups()
    tools = parse_didctf_tools()
    if writeups:
        write_csv(
            ROOT / "didctf_writeups.csv",
            writeups,
            [
                "index",
                "id",
                "title",
                "event",
                "source_type",
                "author",
                "origin",
                "meta",
                "content_type",
                "writeup_type",
                "category1_id",
                "view_count",
                "detail_url",
                "link",
            ],
        )
    if tools:
        write_csv(
            ROOT / "didctf_tools.csv",
            tools,
            ["title", "description", "tags", "download", "github", "website"],
        )


def export_didctf_tag_stats() -> None:
    path = ROOT / "didctf_tools.csv"
    if not path.exists():
        return

    tags = Counter()
    with path.open(encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            for tag in row["tags"].split(" | "):
                tag = tag.strip()
                if not tag or re.fullmatch(r"\+\d+", tag):
                    continue
                tags[tag] += 1

    with (ROOT / "didctf_tool_tags.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["tag", "count"])
        for tag, count in tags.most_common():
            writer.writerow([tag, count])


def write_index(pages: Iterable[Page]) -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    rows = list(pages)
    with (ROOT / "index.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["site", "title", "url", "html_path", "text_path", "status"])
        w.writeheader()
        for p in rows:
            w.writerow({
                "site": p.site,
                "title": p.title,
                "url": p.url,
                "html_path": str(p.path),
                "text_path": str(p.text_path),
                "status": p.status,
            })


def analyze_tools() -> None:
    compiled = {
        tool: [re.compile(pattern, re.IGNORECASE) for pattern in patterns]
        for tool, patterns in TOOL_ALIASES.items()
    }
    tool_counts = Counter()
    site_counts = defaultdict(Counter)
    doc_hits = []

    for txt in sorted((ROOT / "text").glob("*/*.txt")):
        text = txt.read_text(encoding="utf-8", errors="ignore")
        site = txt.parent.name
        per_doc = Counter()
        for tool, patterns in compiled.items():
            count = sum(len(p.findall(text)) for p in patterns)
            if count:
                canonical = "ExifTool" if tool == "exiftool" else tool
                per_doc[canonical] += count
        if per_doc:
            for tool, count in per_doc.items():
                tool_counts[tool] += count
                site_counts[site][tool] += count
            doc_hits.append({
                "site": site,
                "file": str(txt),
                "tools": dict(per_doc.most_common()),
            })

    ROOT.mkdir(parents=True, exist_ok=True)
    with (ROOT / "tool_frequency.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["tool", "count"])
        for tool, count in tool_counts.most_common():
            w.writerow([tool, count])

    with (ROOT / "tool_frequency_by_site.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["site", "tool", "count"])
        for site, counter in sorted(site_counts.items()):
            for tool, count in counter.most_common():
                w.writerow([site, tool, count])

    with (ROOT / "forensics_tool_frequency.csv").open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f)
        w.writerow(["tool", "count"])
        for tool, count in tool_counts.most_common():
            if tool in NON_TOOL_TERMS:
                continue
            w.writerow([tool, count])

    (ROOT / "tool_hits_by_doc.json").write_text(
        json.dumps(doc_hits, ensure_ascii=False, indent=2),
        encoding="utf-8",
    )

    lines = ["# Forensics Tool Frequency", ""]
    for tool, count in tool_counts.most_common(50):
        lines.append(f"- {tool}: {count}")
    (ROOT / "tool_frequency.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site", choices=["all", "yagami", "xidian"], default="all")
    parser.add_argument("--limit-pages", type=int)
    parser.add_argument("--analyze-only", action="store_true")
    parser.add_argument("--rebuild-from-raw", action="store_true")
    parser.add_argument("--crawl-didctf-external", action="store_true")
    args = parser.parse_args()

    ROOT.mkdir(parents=True, exist_ok=True)
    pages: list[Page] = []
    if args.rebuild_from_raw:
        pages = rebuild_from_raw()
        write_index(pages)
    elif not args.analyze_only:
        s = session()
        if args.site in {"all", "yagami"}:
            pages.extend(crawl_yagami(s, args.limit_pages))
        if args.site in {"all", "xidian"}:
            pages.extend(crawl_xidian(s, args.limit_pages))
        if args.crawl_didctf_external:
            pages.extend(crawl_didctf_external_writeups(s))
        write_index(pages)
    export_didctf_tables()
    export_didctf_tag_stats()
    analyze_tools()


if __name__ == "__main__":
    main()
