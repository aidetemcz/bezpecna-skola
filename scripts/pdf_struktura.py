"""Prevod metodiky MSMT "Minimalni standard bezpecnosti" z PDF do strukturovaneho Markdownu.

Vyuziva tri signaly z PDF:
  * barevne pruhy v levem okraji -> kategorie obsahu (zavazne / doporuceni / informace),
  * barvu nadpisu (cerna vs. petrolejova) -> uroven nadpisu,
  * typografii (velikost, rez, odsazeni) -> odrazky, poznamky pod carou.
"""
import pdfplumber, re
from collections import defaultdict

BAR_CAT = {
    (1.0, 0.949, 0.8):     "zavazne",
    (0.886, 0.941, 0.851): "doporuceni",
    (0.851, 0.949, 0.816): "doporuceni",
    (0.871, 0.922, 0.969): "informace",
}
CAT_LABEL = {
    "zavazne":    "**[§ ZÁVAZNÉ]**",
    "doporuceni": "**[D DOPORUČENÍ]**",
    "informace":  "**[I INFORMACE]**",
}
ACCENT = {(0.259, 0.553, 0.588), (0.0, 0.502, 0.502), (0.58, 0.788, 0.816)}
BULLET_FONTS = {"Wingdings2", "Wingdings", "SymbolMT"}


def _color(ch):
    return tuple(round(c, 3) for c in (ch.get("non_stroking_color") or ()))


def bars(page):
    out = []
    for r in page.rects:
        w, h = r["x1"] - r["x0"], r["bottom"] - r["top"]
        if r["x0"] < 60 and 10 < w < 20 and h > 5:
            key = tuple(round(c, 3) for c in (r.get("non_stroking_color") or ()))
            if key in BAR_CAT:
                out.append((r["top"], r["bottom"], BAR_CAT[key]))
    return out


def footnote_rule(page):
    ys = [r["top"] for r in page.rects
          if (r["x1"] - r["x0"]) > 80 and (r["bottom"] - r["top"]) < 2
          and r["x0"] < 100 and r["top"] > page.height * 0.6]
    return min(ys) if ys else None


def is_sup(ch):
    return ch["size"] <= 8.5 and ch["text"].strip().isdigit()


def lines_of(page, rule=None):
    """Znaky -> radky. Radky se shlukuji podle uctove linky s toleranci;
    horni indexy se pak priradi k nejblizsimu radku na stejne strane cary poznamek."""
    chars = list(page.chars)
    main = sorted((c for c in chars if not is_sup(c)), key=lambda c: c["bottom"])
    rest = [c for c in chars if is_sup(c)]

    clusters = []
    for ch in main:
        if clusters and abs(ch["bottom"] - clusters[-1]["ref"]) <= 3.5:
            cl = clusters[-1]
            cl["chars"].append(ch)
            cl["ref"] = sum(c["bottom"] for c in cl["chars"]) / len(cl["chars"])
        else:
            clusters.append({"ref": ch["bottom"], "chars": [ch]})
    if not clusters:
        return []

    def side(y):
        return rule is None or y > rule

    for ch in rest:
        same = [cl for cl in clusters if side(cl["ref"]) == side(ch["bottom"])]
        if not same:
            continue
        min(same, key=lambda cl: abs(cl["ref"] - ch["bottom"]))["chars"].append(ch)

    out = []
    for cl in sorted(clusters, key=lambda c: c["ref"]):
        allc = sorted(cl["chars"], key=lambda c: c["x0"])
        vis = [c for c in allc if c["text"].strip()]
        if not vis:
            continue
        body = [c for c in vis if not is_sup(c)] or vis
        out.append({
            "chars": allc, "vis": vis, "main": body,
            "top": min(c["top"] for c in body),
            "bottom": max(c["bottom"] for c in body),
            "x0": vis[0]["x0"],
            "size": max(c["size"] for c in body),
            "fonts": {c["fontname"].split("+")[-1] for c in body},
        })

    res = []                       # iniciala nadpisu patri k nasledujicimu radku
    for ln in out:
        if (res and ln["size"] >= 15 and res[-1]["size"] >= 15
                and ln["top"] < res[-1]["bottom"] - 3):
            p = res[-1]
            p["chars"] = sorted(p["chars"] + ln["chars"], key=lambda c: c["x0"])
            p["bottom"] = max(p["bottom"], ln["bottom"])
        else:
            res.append(ln)
    return res


def render(ln, mark_bold=False):
    """Text radku. Horni indexy -> [^n]; volitelne zvyrazneni tucnych useku."""
    runs = []                      # [(text, tucne)]
    for c in ln["chars"]:
        t = c["text"]
        font = c["fontname"].split("+")[-1]
        if font in BULLET_FONTS:
            t = " "
        if is_sup(c):
            t, bold = f"@@{t}@@", False
        else:
            bold = mark_bold and "Bold" in font
        if not t.strip():
            t, bold = " ", runs[-1][1] if runs else False
        if runs and runs[-1][1] == bold:
            runs[-1][0] += t
        else:
            runs.append([t, bold])

    # tucny usek bez pismen (jen mezery/interpunkce) tucny nezustava
    for r in runs:
        if r[1] and not any(ch.isalnum() for ch in r[0]):
            r[1] = False
    out = []
    for text, bold in runs:
        if not bold:
            out.append(text); continue
        lead = text[:len(text) - len(text.lstrip())]
        trail = text[len(text.rstrip()):]
        core = text.strip()
        out.append(f"{lead}**{core}**{trail}" if core else text)
    s = "".join(out).replace("\xa0", " ")
    s = re.sub(r"\*\*(\s*)\*\*", r"\1", s)          # sousedni useky spojit
    s = re.sub(r"(@@\d@@)+", lambda m: "[^" + "".join(re.findall(r"\d", m.group())) + "]", s)
    s = re.sub(r"[\ue000-\uf8ff]", "", s)          # glyfy odrazek z Private Use Area
    return re.sub(r"\s+", " ", s).strip()


def bullet_level(ln):
    f = ln["vis"][0]["fontname"].split("+")[-1]
    if f not in BULLET_FONTS:
        return None
    return 1 if ln["vis"][0]["x0"] < 110 else 2


def category_at(bar_list, ln):
    mid = (ln["top"] + ln["bottom"]) / 2
    for top, bottom, cat in bar_list:
        if top - 2 <= mid <= bottom + 2:
            return cat
    return None


def parse(path):
    blocks, notes = [], []
    with pdfplumber.open(path) as pdf:
        for pno, page in enumerate(pdf.pages):
            bar_list, rule = bars(page), footnote_rule(page)
            prev_bottom = None
            for ln in lines_of(page, rule):
                if ln["top"] < 60:
                    continue
                plain = render(ln)
                if not plain:
                    continue
                if re.fullmatch(r"\[\^\d+\]|\d{1,3}", plain) and ln["x0"] > 480:
                    continue
                if rule and ln["top"] > rule:
                    notes.append(plain)
                    continue
                lvl = bullet_level(ln)
                names = ln["fonts"] - BULLET_FONTS - {"ArialMT"}
                bold = bool(names) and all("Bold" in f for f in names)
                gap = prev_bottom is not None and (ln["top"] - prev_bottom) > 18
                prev_bottom = ln["bottom"]
                accent = all(_color(c) in ACCENT for c in ln["main"])
                big = ln["size"] >= 15
                if big and pno == 0:
                    kind, text = "title", plain
                elif big:
                    kind, text = "heading", plain
                elif lvl:
                    kind, text = "bullet", render(ln, mark_bold=True)
                elif bold:
                    kind, text = "heading", plain
                else:
                    kind, text = "para", render(ln, mark_bold=True)
                starts_bold = bool(ln["main"]) and "Bold" in ln["main"][0]["fontname"]
                blocks.append({"kind": kind, "level": lvl or 0, "text": text,
                               "starts_bold": starts_bold, "big": big,
                               "cat": category_at(bar_list, ln), "x0": ln["x0"],
                               "gap": gap, "accent": accent})
    return blocks, notes


def to_markdown(blocks, notes, meta, title=None):
    has_plain_heading = any(b["kind"] == "heading" and not b["accent"] for b in blocks)
    title = title or " ".join(b["text"] for b in blocks if b["kind"] == "title")
    blocks = [b for b in blocks if b["kind"] != "title"]

    # slouceni navazujicich radku do bloku
    merged = []
    for b in blocks:
        p = merged[-1] if merged else None
        if p and not b["gap"]:
            if p["kind"] == "heading" and b["kind"] == "heading" and p["accent"] == b["accent"]:
                p["text"] += " " + b["text"]; continue
            if p["kind"] == "bullet" and b["kind"] == "para" and b["x0"] > 100:
                p["text"] += " " + b["text"]; continue
            konec_vety = p["text"].rstrip().endswith((".", ":", "!", "?"))
            # zmena barevneho pruhu na hranici vety je novy odstavec; uprostred
            # vety je to jen zlom v sazbe a odstavec pokracuje
            zmena_kategorie = b["cat"] != p["cats"][-1] and konec_vety
            if (p["kind"] == "para" and b["kind"] == "para" and not zmena_kategorie
                    and not (b.get("starts_bold") and konec_vety)):
                p["text"] += " " + b["text"]
                p["cats"].append(b["cat"]); continue
        b = dict(b); b["cats"] = [b["cat"]]
        merged.append(b)

    for b in merged:  # useky spojene pres konec radku sjednotit
        b["text"] = re.sub(r"\*\*(\s+)\*\*", r"\1", b["text"])

    for b in merged:  # kategorie odstavce = prevazujici pruh
        cats = [c for c in b["cats"] if c]
        # dict.fromkeys drzi poradi prvniho vyskytu, takze shodu poctu
        # rozhodne kategorie, ktera na strance zacina driv - ne poradi
        # iterace mnoziny, ktere Python mezi procesy randomizuje
        b["cat"] = max(dict.fromkeys(cats), key=cats.count) if cats else None

    out, prev_cat, stack = [], None, []
    for b in merged:
        if b["cat"] and b["cat"] != prev_cat:
            out.append(CAT_LABEL[b["cat"]])
            prev_cat = b["cat"]
        if b["kind"] == "heading":
            rank = 2 if (b["accent"] and has_plain_heading and not b.get("big")) else 1
            while stack and stack[-1] > rank:
                stack.pop()
            if not stack or stack[-1] != rank:
                stack.append(rank)
            out.append("#" * (1 + len(stack)) + " " + b["text"])
        elif b["kind"] == "bullet":
            out.append(("  " * (b["level"] - 1)) + "- " + b["text"])
        else:
            out.append(b["text"])

    body = []
    for i, chunk in enumerate(out):
        body.append(chunk)
        nxt = out[i + 1] if i + 1 < len(out) else ""
        if not (chunk.lstrip().startswith("- ") and nxt.lstrip().startswith("- ")):
            body.append("")

    md = ["---"] + meta + ["---", "", "# " + title, ""] + body
    if notes:
        md += ["## Poznámky pod čarou", ""]
        for n in notes:
            m = re.match(r"\[\^(\d+)\]\s*(.*)", n)
            md += [f"[^{m.group(1)}]: {m.group(2)}" if m else n, ""]
    text = "\n".join(md)
    return re.sub(r"\n{3,}", "\n\n", text).rstrip() + "\n"
