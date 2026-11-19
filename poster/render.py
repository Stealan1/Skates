"""Render the Skates P8 poster to one PNG per realm.

    python poster/render.py [--out .] [--realm SCL]

Reads poster/poster.html + poster/poster.json (this file's folder), writes skates-p8-poster-<realm>.png into --out.
Headless Chrome only, no pip packages: pass 1 dumps the DOM to read the poster's measured height (body data-h),
pass 2 screenshots exactly that size. Any failure exits non-zero with the reason.

Searched: find_fn (render/page/chrome), jsp/chrome_launcher.py, dclone/render.py -- nothing fits because this file
runs alone on a Linux GitHub runner in Stealan1/Skates (no CSM/service imports there); chrome_launcher is a Windows
window launcher, not a headless screenshotter.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
WIDTH = 1400
CHROME_CANDIDATES = [
    os.environ.get("CHROME", ""),
    "google-chrome", "google-chrome-stable", "chromium", "chromium-browser",
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
]


def chrome() -> str:
    for c in CHROME_CANDIDATES:
        if c and (shutil.which(c) or Path(c).is_file()):
            return shutil.which(c) or c
    sys.exit("render: no Chrome found (set CHROME=<path>)")


def page_for(realm: str, data: dict, template: str) -> Path:
    inject = "<script>window.POSTER=%s;window.POSTER_REALM=%s;window.POSTER_BASE=\"\";</script>\n" % (
        json.dumps(data).replace("</", "<\\/"), json.dumps(realm))
    if "</head>" not in template:
        sys.exit("render: poster.html has no </head>")
    path = HERE / ("_render_%s.html" % realm.lower())
    path.write_text(template.replace("</head>", inject + "</head>", 1), encoding="utf-8")
    return path


def run(args: list[str]) -> str:
    p = subprocess.run(args, capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=120)
    if p.returncode != 0:
        sys.exit("render: chrome failed (%d): %s" % (p.returncode, p.stderr[-800:]))
    return p.stdout


def render(realm: str, data: dict, template: str, out: Path, exe: str) -> Path:
    page = page_for(realm, data, template)
    url = page.as_uri()
    base = [exe, "--headless=new", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
            "--force-device-scale-factor=1", "--virtual-time-budget=15000", "--run-all-compositor-stages-before-draw"]
    try:
        dom = run(base + ["--window-size=%d,1000" % WIDTH, "--dump-dom", url])
        m = re.search(r'data-h="(\d+)"', dom)
        if not m:
            sys.exit("render: %s never set data-h (fonts or logo did not load?)" % realm)
        height = int(m.group(1))
        target = out.resolve() / ("skates-p8-poster-%s.png" % realm.lower())
        run(base + ["--window-size=%d,%d" % (WIDTH, height), "--screenshot=%s" % target, url])
        if not target.is_file() or target.stat().st_size < 10000:
            sys.exit("render: %s screenshot missing or tiny" % target)
        print("render: %s %dx%d %d bytes" % (target.name, WIDTH, height, target.stat().st_size))
        return target
    finally:
        page.unlink(missing_ok=True)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=str(HERE.parent))
    ap.add_argument("--realm", action="append", help="one realm (repeatable); default every realm in poster.json")
    a = ap.parse_args()
    data = json.loads((HERE / "poster.json").read_text(encoding="utf-8"))
    template = (HERE / "poster.html").read_text(encoding="utf-8")
    realms = [r.upper() for r in (a.realm or list((data.get("realms") or {}).keys()))]
    if not realms:
        sys.exit("render: poster.json has no realms")
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    exe = chrome()
    for r in realms:
        render(r, data, template, out, exe)


if __name__ == "__main__":
    main()
