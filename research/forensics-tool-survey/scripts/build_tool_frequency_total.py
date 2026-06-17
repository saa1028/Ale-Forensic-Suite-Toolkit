import csv
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PROJECT_ROOT = ROOT.parents[1]
TEXT_ROOT = ROOT / "data" / "text"
TOOL_DB = ROOT / "didctf_tool_database.csv"
OUT = ROOT / "tool_frequency_total.csv"
PROJECT_README = PROJECT_ROOT / "README.md"


LEGACY_ALIASES = {
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
    "010 Editor": [r"\b010\s*Editor\b"],
    "HxD": [r"\bHxD\b"],
    "CyberChef": [r"\bCyberChef\b"],
    "StegSolve": [r"\bStegSolve\b"],
    "zsteg": [r"\bzsteg\b"],
    "ExifTool": [r"\bexiftool\b", r"\bExifTool\b"],
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
    "VMware": [r"\bVMware\b"],
    "VirtualBox": [r"\bVirtualBox\b"],
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


# Extra candidates from forensic writeup review and common forensic workflows. These are
# intentionally tool/product names, not generic commands like `file` or `grep`.
CURATED_ALIASES = {
    "The Sleuth Kit": [r"\bThe\s+Sleuth\s+Kit\b", r"\bSleuth\s+Kit\b", r"\btsk_[a-z_]+\b"],
    "KAPE": [r"\bKAPE\b", r"\bKroll\s+Artifact\s+Parser\b"],
    "Eric Zimmerman Tools": [r"\bEric\s+Zimmerman\b", r"\bZimmerman\s+Tools\b"],
    "MFTECmd": [r"\bMFTECmd\b"],
    "EvtxECmd": [r"\bEvtxECmd\b"],
    "AmcacheParser": [r"\bAmcacheParser\b"],
    "PECmd": [r"\bPECmd\b"],
    "RECmd": [r"\bRECmd\b"],
    "SQLECmd": [r"\bSQLECmd\b"],
    "Timeline Explorer": [r"\bTimeline\s+Explorer\b"],
    "Registry Explorer": [r"\bRegistry\s+Explorer\b"],
    "ShellBags Explorer": [r"\bShellBags?\s+Explorer\b"],
    "BrowsingHistoryView": [r"\bBrowsingHistoryView\b"],
    "USBDeview": [r"\bUSBDeview\b"],
    "LastActivityView": [r"\bLastActivityView\b"],
    "Everything": [r"\bEverything\b"],
    "DMDE": [r"\bDMDE\b"],
    "TestDisk": [r"\bTestDisk\b"],
    "PhotoRec": [r"\bPhotoRec\b"],
    "Steghide": [r"\bsteghide\b", r"\bSteghide\b"],
    "Outguess": [r"\boutguess\b", r"\bOutguess\b"],
    "F5-steganography": [r"\bF5-steganography\b", r"\bf5-steganography\b"],
    "zbarimg": [r"\bzbarimg\b"],
    "QR Research": [r"\bQR\s+Research\b"],
    "CapAnalysis": [r"\bCapAnalysis\b"],
    "tcpdump": [r"\btcpdump\b"],
    "Brim": [r"\bBrim\b"],
    "Zui": [r"\bZui\b"],
    "RITA": [r"\bRITA\b"],
    "SQLiteStudio": [r"\bSQLiteStudio\b"],
    "DB Browser for SQLite": [r"\bDB\s+Browser\s+for\s+SQLite\b"],
    "Frida": [r"\bFrida\b", r"\bfrida\b"],
    "MobSF": [r"\bMobSF\b", r"\bMobile\s+Security\s+Framework\b"],
    "iLEAPP": [r"\biLEAPP\b"],
    "ALEAPP": [r"\bALEAPP\b"],
    "Belkasoft Evidence Center": [r"\bBelkasoft\b"],
    "OSForensics": [r"\bOSForensics\b"],
    "Passware Kit": [r"\bPassware(?:\s+Kit)?\b"],
    "Magnet RAM Capture": [r"\bMAGNET\s+RAM\s+Capture\b", r"\bMagnet\s+RAM\s+Capture\b"],
    "DumpIt": [r"\bDumpIt\b"],
    "AVML": [r"\bAVML\b", r"\bavml\b"],
    "LiME": [r"\bLiME\b"],
    "Volatility2": [r"\bVolatility\s*2\b", r"\bVolatility2\b"],
    "Volatility3": [r"\bVolatility\s*3\b", r"\bVolatility3\b"],
    "capa": [r"\bcapa\b"],
    "FLOSS": [r"\bFLOSS\b"],
    "Detect It Easy": [r"\bDetect\s+It\s+Easy\b", r"\bDIE\b"],
    "PEStudio": [r"\bPEStudio\b", r"\bpefile\b"],
    "PEiD": [r"\bPEiD\b"],
    "RsaCtfTool": [r"\bRsaCtfTool\b"],
    "Yafu": [r"\bYAFU\b", r"\byafu\b"],
    "SageMath": [r"\bSageMath\b", r"\bSage\b"],
    "OpenPuff": [r"\bOpenPuff\b"],
    "SilentEye": [r"\bSilentEye\b"],
    "Forensically": [r"\bForensically\b"],
    "InVID": [r"\bInVID\b"],
    "HxD Hex Editor": [r"\bHxD\s+Hex\s+Editor\b"],
    "WinRAR": [r"\bWinRAR\b"],
    "Bandizip": [r"\bBandizip\b"],
    "ExifToolGUI": [r"\bExifToolGUI\b"],
    "Wazuh": [r"\bWazuh\b"],
    "Hayabusa": [r"\bHayabusa\b"],
    "Chainsaw": [r"\bChainsaw\b"],
    "Velociraptor": [r"\bVelociraptor\b"],
    "GRR Rapid Response": [r"\bGRR\s+Rapid\s+Response\b", r"\bGRR\b"],
    "Plaso": [r"\bPlaso\b", r"\blog2timeline\b", r"\bpsort\b"],
    "Timesketch": [r"\bTimesketch\b"],
    "Mimikatz": [r"\bMimikatz\b"],
    "LaZagne": [r"\bLaZagne\b"],
    "HackBrowserData": [r"\bHackBrowserData\b"],
    "BrowserGhost": [r"\bBrowserGhost\b"],
    "Navicat password decrypt": [r"\bnavicat_password_decrypt\b", r"Navicat密码解密", r"Navicat\s+password"],
    "FinalShell Decoder": [r"\bFinalShell-Decoder\b", r"FinalShell\s*密码"],
    "CTF-NetA": [r"\bCTF-NetA\b"],
    "科来网络分析系统": [r"科来网络分析系统", r"科来"],
    "蓝灯": [r"蓝灯"],
    "麒麟取证": [r"麒麟取证"],
}


NON_TOOL_TERMS = {
    "Linux",
    "Python",
    "Windows",
    "Android",
    "Java",
    "PHP",
    "SQL",
    "SSH",
    "Web",
    "APK",
}


CANONICAL_NAMES = {
    "Binwalk": "binwalk",
    "Foremost": "foremost",
    "Stegsolve": "StegSolve",
    "volatility": "Volatility",
    "Volatility2": "Volatility",
    "Volatility3": "Volatility",
    "DB Browser for SQLite": "SQLite Browser",
    "Magnet RAM Capture": "MAGNET RAM Capture",
    "FinalShell Decoder": "FinallShell 密码解密GUI工具",
    "HxD Hex Editor": "HxD",
    "Navicat password decrypt": "navicat_password_decrypt",
    "Detect It Easy": "DIE",
    "pestudio": "PEStudio",
    "Scalpel": "scalpel",
}


ONLINE_TOOLS = {
    "CyberChef",
    "Forensically",
    "InVID",
    "IP138",
    "微步在线云沙箱",
    "奇安信威胁情报中心",
    "微步在线X情报社区",
    "腾讯安全 威胁情报中心",
    "360威胁情报中心",
    "绿盟威胁情报中心",
    "安恒威胁情报中心",
    "天际友盟情报查询",
    "FOFA",
    "Hunter鹰图平台",
    "Quake",
    "ZoomEye钟馗之眼",
    "Seebug漏洞平台",
    "安全星图平台",
    "站长工具",
}

COMMERCIAL_TOOLS = {
    "FTK Imager",
    "X-Ways Forensics",
    "Magnet AXIOM",
    "Belkasoft Evidence Center",
    "Passware Kit",
    "IDA",
    "010 Editor",
    "R-Studio",
    "VMware",
    "EnCase",
    "火眼证据分析",
    "火眼仿真取证",
    "雷电 APP 智能分析",
    "美亚取证",
    "取证大师",
    "弘连",
    "盘古石",
    "X-Ways Forensics",
}

OPEN_SOURCE_TOOLS = {
    "hashcat",
    "Frida",
    "Volatility",
    "John the Ripper",
    "CyberChef",
    "Wireshark",
    "DIE",
    "iLEAPP",
    "ADB",
    "JADX",
    "binwalk",
    "SQLite Browser",
    "LiME",
    "Autopsy",
    "SageMath",
    "Mimikatz",
    "foremost",
    "YARA",
    "MemProcFS",
    "Steghide",
    "StegSolve",
    "Wazuh",
    "Zeek",
    "ALEAPP",
    "Ghidra",
    "VirtualBox",
    "Hayabusa",
    "SQLiteStudio",
    "AVML",
    "Eric Zimmerman Tools",
    "ExifTool",
    "GRR Rapid Response",
    "MAGNET RAM Capture",
    "navicat_password_decrypt",
    "Registry Explorer",
    "The Sleuth Kit",
    "tshark",
    "apk_analyzer",
    "BrowserGhost",
    "CAINE",
    "capa",
    "Chainsaw",
    "DumpIt",
    "HackBrowserData",
    "MobaXterm密码解密",
    "PanelForensics",
    "ForensicsTool",
    "FinallShell 密码解密GUI工具",
    "RevokeMsgPatcher",
    "FatSmallTools",
}

FREEWARE_TOOLS = {
    "7-Zip",
    "HashMyFiles",
    "WinRAR",
    "Everything",
    "HxD",
    "DiskGenius",
}

DOMESTIC_VENDOR_TOOLS = {
    "盘古石": "盘古石",
    "美亚取证": "美亚柏科",
    "取证大师": "美亚柏科",
    "弘连": "弘连",
    "火眼证据分析": "弘连",
    "火眼仿真取证": "弘连",
    "雷电 APP 智能分析": "弘连",
}


PROJECT_TOOL_ALIASES = {
    "hashcat": ["Hashcat"],
    "John the Ripper": ["John", "Johnny"],
    "Volatility": ["Volatility2", "Volatility3"],
    "Wireshark": ["WireShark", "Wireshark"],
    "DIE": ["DetectItEasy"],
    "JADX": ["Jadx-GUI", "SuperJadx"],
    "ADB": ["AdbDriver"],
    "binwalk": ["Binwalk"],
    "SQLite Browser": ["sqLite"],
    "foremost": ["Foremost"],
    "StegSolve": ["Stegsolve"],
    "Steghide": ["Steghide"],
    "CyberChef": ["CyberChef"],
    "IDA": ["IDAPro"],
    "VMware": ["VMware"],
    "7-Zip": ["7-Zip"],
    "Autopsy": ["Autopsy", "AutoSpy"],
    "Ghidra": ["Ghidra"],
    "YARA": ["Yara"],
    "ExifTool": ["ExifTool"],
    "HxD": ["HxD"],
    "R-Studio": ["R-Studio"],
    "Navicat": ["Navicat"],
    "Mimikatz": ["Mimikatz"],
    "Frida": ["Frida"],
    "apktool": ["Apktool", "ApkToolPlus"],
}


def literal_pattern(name: str) -> str:
    escaped = re.escape(name)
    if re.fullmatch(r"[A-Za-z0-9_.+ -]+", name):
        return rf"(?<![A-Za-z0-9_]){escaped}(?![A-Za-z0-9_])"
    return escaped


def add_alias(alias_map: dict[str, set[str]], tool: str, pattern: str) -> None:
    tool = tool.strip()
    if not tool or tool in NON_TOOL_TERMS:
        return
    tool = CANONICAL_NAMES.get(tool, tool)
    alias_map.setdefault(tool, set()).add(pattern)


def load_candidates() -> dict[str, list[re.Pattern[str]]]:
    alias_map: dict[str, set[str]] = {}
    for source in (LEGACY_ALIASES, CURATED_ALIASES):
        for tool, patterns in source.items():
            for pattern in patterns:
                add_alias(alias_map, tool, pattern)

    with TOOL_DB.open("r", encoding="utf-8-sig", newline="") as f:
        for row in csv.DictReader(f):
            title = (row.get("title") or "").strip()
            if title:
                add_alias(alias_map, title, literal_pattern(title))
    return {
        tool: [re.compile(pattern, re.IGNORECASE) for pattern in sorted(patterns)]
        for tool, patterns in sorted(alias_map.items())
    }


def deployment_type(tool: str) -> str:
    if tool in ONLINE_TOOLS:
        return "online"
    if tool in DOMESTIC_VENDOR_TOOLS:
        return "vendor_platform"
    return "local"


def license_type(tool: str) -> str:
    if tool in OPEN_SOURCE_TOOLS:
        return "open_source"
    if tool in FREEWARE_TOOLS:
        return "freeware"
    if tool in COMMERCIAL_TOOLS:
        return "commercial"
    return "unknown"


def domestic_vendor(tool: str) -> str:
    return DOMESTIC_VENDOR_TOOLS.get(tool, "")


def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "", value.lower())


def extract_project_tools() -> dict[str, str]:
    if not PROJECT_README.exists():
        return {}
    text = PROJECT_README.read_text(encoding="utf-8", errors="ignore")
    marker = '<h1 align="center">Windows11 Penetration Suite Toolkit v6.0</h1>'
    upstream = text.split(marker, 1)[1] if marker in text else text
    matches = re.findall(r"\*\*\[([^\]]+)\]\([^)]+\)", upstream)
    tools: dict[str, str] = {}
    for name in matches:
        clean = re.sub(r"\s+v?\d+(?:\.\d+)*.*$", "", name.strip(), flags=re.I)
        if clean:
            tools[normalize_name(clean)] = clean
    # Include plain bold names that are not linked in the upstream README.
    for name in re.findall(r"\*\*([A-Za-z][A-Za-z0-9 ._+-]{2,})[:：]", upstream):
        clean = name.strip()
        tools.setdefault(normalize_name(clean), clean)
    known_patterns = {
        "7-Zip": r"\b7-?Zip\b",
        "VMware": r"\bVMware\b",
        "AutoSpy": r"\bAutoSpy\b",
        "WinHex": r"\bWinHex\b",
    }
    for name, pattern in known_patterns.items():
        if re.search(pattern, upstream, flags=re.IGNORECASE):
            tools.setdefault(normalize_name(name), name)
    return tools


def project_match(tool: str, project_tools: dict[str, str]) -> str:
    names = [tool, *PROJECT_TOOL_ALIASES.get(tool, [])]
    for name in names:
        key = normalize_name(name)
        if key in project_tools:
            return project_tools[key]
    return ""


def count_tools() -> list[dict[str, int | str]]:
    candidates = load_candidates()
    project_tools = extract_project_tools()
    totals = Counter()
    by_site: dict[str, Counter] = defaultdict(Counter)

    for site in ("didctf", "xidian", "yagami"):
        site_dir = TEXT_ROOT / site
        for path in site_dir.glob("*.txt"):
            text = path.read_text(encoding="utf-8", errors="ignore")
            for tool, patterns in candidates.items():
                count = sum(len(pattern.findall(text)) for pattern in patterns)
                if count:
                    totals[tool] += count
                    by_site[site][tool] += count

    rows = []
    for tool, total in totals.items():
        if tool in NON_TOOL_TERMS:
            continue
        rows.append(
            {
                "tool": tool,
                "mentions_total": total,
                "didctf": by_site["didctf"][tool],
                "xidian": by_site["xidian"][tool],
                "yagami": by_site["yagami"][tool],
                "deployment": deployment_type(tool),
                "license_type": license_type(tool),
                "domestic_vendor": domestic_vendor(tool),
                "already_in_project": "yes" if project_match(tool, project_tools) else "no",
                "project_match": project_match(tool, project_tools),
            }
        )
    rows.sort(key=lambda row: (-int(row["mentions_total"]), str(row["tool"]).lower()))
    return rows


def main() -> None:
    rows = count_tools()
    with OUT.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "tool",
                "mentions_total",
                "didctf",
                "xidian",
                "yagami",
                "deployment",
                "license_type",
                "domestic_vendor",
                "already_in_project",
                "project_match",
            ],
        )
        writer.writeheader()
        writer.writerows(rows)
    print(f"wrote {len(rows)} rows to {OUT}")


if __name__ == "__main__":
    main()
