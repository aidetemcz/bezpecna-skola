"""Obecny prevod PDF do Markdownu pro dokumenty bez vlastniho barevneho kodovani.

Na rozdil od pdf_struktura.py, ktery tezi barevne pruhy metodiky MSMT, tenhle
modul si strukturu odvodi jen z typografie: velikost pisma, rez, odsazeni
a opakujici se zahlavi/zapati.
"""
import re
from collections import Counter, defaultdict

BULLET_CHARS = "•◦▪‣∙·–-—"
NUMBERED = re.compile(r"^(\d{1,2}[.)]|[a-z][.)])\s+")


def _lines(page):
    """Znaky -> radky shlukovanim podle uctove linky."""
    chars = sorted(page.chars, key=lambda c: c["bottom"])
    out = []
    for ch in chars:
        if out and abs(ch["bottom"] - out[-1]["ref"]) <= 3.5:
            cl = out[-1]
            cl["chars"].append(ch)
            cl["ref"] = sum(c["bottom"] for c in cl["chars"]) / len(cl["chars"])
        else:
            out.append({"ref": ch["bottom"], "chars": [ch]})
    res = []
    for cl in out:
        allc = sorted(cl["chars"], key=lambda c: c["x0"])
        vis = [c for c in allc if c["text"].strip()]
        if not vis:
            continue
        res.append({
            "text": re.sub(r"\s+", " ", "".join(c["text"] for c in allc)).strip(),
            "x0": vis[0]["x0"],
            "top": min(c["top"] for c in vis),
            "size": round(max(c["size"] for c in vis), 1),
            "bold": all("Bold" in c["fontname"] or not c["text"].strip() for c in allc),
            "first": vis[0],
            "nvis": len(vis),
        })
    return res


def _repeated(pages_lines, npages):
    """Text zahlavi a zapati, ktery se opakuje na vetsine stran."""
    seen = Counter()
    for lines in pages_lines:
        if not lines:
            continue
        edge = [ln["text"] for ln in lines[:3]] + [ln["text"] for ln in lines[-2:]]
        for t in set(edge):
            seen[t] += 1
    return {t for t, n in seen.items() if n >= max(2, npages * 0.5) and len(t) < 120}


def _bullet(ln):
    """Uroven odrazky, nebo None."""
    ch = ln["first"]
    t = ch["text"]
    font = ch["fontname"].split("+")[-1]
    sym = t in BULLET_CHARS or "" <= t <= ""
    sym = sym or (t == "o" and ("Courier" in font or "Symbol" in font or "Wingding" in font))
    if not (sym or NUMBERED.match(ln["text"])):
        return None
    return 1 if ln["x0"] < 120 else 2


def parse(pdf, min_heading_len=3, skip_extra=()):
    pages_lines = [_lines(p) for p in pdf.pages]
    skip = _repeated(pages_lines, len(pdf.pages)) | {t.strip() for t in skip_extra}

    weight = Counter()
    for lines in pages_lines:
        for ln in lines:
            if ln["text"] not in skip:
                weight[ln["size"]] += ln["nvis"]
    body = weight.most_common(1)[0][0] if weight else 11.0

    blocks, prev_bottom = [], None
    for pno, lines in enumerate(pages_lines):
        for ln in lines:
            if ln["text"] in skip or not ln["text"]:
                continue
            if re.fullmatch(r"[-–—\s]*\d{1,3}[-–—\s]*", ln["text"]):   # cislo strany
                continue
            lvl = _bullet(ln)
            big = ln["size"] > body + 0.4
            short_bold = (ln["bold"] and len(ln["text"]) < 90
                          and not ln["text"].rstrip().endswith((".", ",", ";")))
            heading = (big or short_bold) and len(ln["text"]) >= min_heading_len
            if heading and lvl and not (big or ln["bold"]):
                heading = False
            if lvl and heading:      # cislovany nadpis neni odrazka
                lvl = None
            gap = prev_bottom is not None and (ln["top"] - prev_bottom) > ln["size"] * 1.6
            prev_bottom = ln["top"] + ln["size"]
            blocks.append({"text": ln["text"], "size": ln["size"], "bullet": lvl,
                           "heading": heading,
                           "gap": gap, "x0": ln["x0"]})
    return blocks, body


def _norm(t):
    return re.sub(r"[^0-9a-zA-Zá-žÁ-Ž]+", " ", t).strip().lower()


def to_markdown(blocks, body_size, meta, title):
    sizes = sorted({round(b["size"]) for b in blocks
                    if b["heading"] and b["size"] > body_size}, reverse=True)
    level = {s: min(2 + i, 4) for i, s in enumerate(sizes)}

    # tucny radek, na ktery navazuje pokracovani vety, je odstavec, ne nadpis
    blocks = [dict(b) for b in blocks]
    for i in range(len(blocks) - 2, -1, -1):
        b, nxt = blocks[i], blocks[i + 1]
        if (b["heading"] and b["size"] <= body_size + 0.4 and not nxt["heading"]
                and not nxt["bullet"] and nxt["text"][:1].islower()
                and not b["text"].rstrip().endswith(":")):
            b["heading"] = False

    merged = []
    for b in blocks:
        p = merged[-1] if merged else None
        same = p and p["heading"] == b["heading"] and p["bullet"] == b["bullet"]
        too_long = p and p["heading"] and len(p["text"]) + len(b["text"]) > 110
        if p and same and not b["gap"] and not b["bullet"] \
                and p["size"] == b["size"] and not too_long:
            p["text"] += " " + b["text"]
            continue
        if p and p["bullet"] and not b["bullet"] and not b["heading"] and not b["gap"] \
                and b["x0"] > 100:
            p["text"] += " " + b["text"]
            continue
        merged.append(dict(b))

    out, seen_title = [], False
    for b in merged:
        if not seen_title and b["heading"] and _norm(b["text"]) == _norm(title):
            seen_title = True       # nadpis shodny s nazvem dokumentu se neopakuje
            continue
        if b["heading"]:
            depth = level.get(round(b["size"]), 2 if b["size"] > body_size else 3)
            out.append("#" * depth + " " + b["text"])
        elif b["bullet"]:
            m = NUMBERED.match(b["text"])
            if m:                       # cislovany seznam si cislo ponecha
                num = m.group(1).rstrip(".)")
                text = b["text"][m.end():].strip()
                marker = f"{num}. "
            else:
                text = b["text"].lstrip(BULLET_CHARS + " ").strip()
                marker = "- "
            out.append("  " * (b["bullet"] - 1) + marker + text)
        else:
            out.append(b["text"])

    lines = []
    for i, chunk in enumerate(out):
        lines.append(chunk)
        nxt = out[i + 1] if i + 1 < len(out) else ""
        item = re.compile(r"(- |\d+\. |[a-z]\. )")
        if not (item.match(chunk.lstrip()) and item.match(nxt.lstrip())):
            lines.append("")
    text = "\n".join(["---"] + meta + ["---", "", "# " + title, ""] + lines)
    return re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
