"""Prevod vicesloupcove sazby na jednosloupcove poradi cteni.

pdf_obecny.py cte stranku po uctovych linkach shora dolu. U brozur sazenych
do dvou az ctyr sloupcu tim vznikne promichany text: radek levého sloupce,
radek pravého, zase levého. Tenhle modul stranku nejdriv rozdeli na sloupce
podle svislych mezer (chodbicek), radky prerovna do poradi cteni a vrati
nahradni stranku, kterou uz pdf_obecny zpracuje spravne.

Radky, ktere chodbicku prekracuji (nadpisy pres celou sirku, siroke tabulky),
zustavaji na svem miste a deli stranku na pasma - sloupce se radi zvlast
v kazdem pasmu.
"""
import re
from collections import Counter

BIN = 1.0          # sirka kose histogramu v bodech
MIN_GUTTER = 11.0  # nejuzsi mezera, ktera se jeste povazuje za chodbicku
TOL = 0.004        # kos s mene nez 0.4 % znaku stranky plati za prazdny


def _segments(chars, tol=3.2, gap=8.0):
    """Znaky -> souvisle useky textu.

    Radek se nesmi brat pres celou sirku stranky: text leveho a praveho
    sloupce lezi ve stejne vysce a splynul by v jeden radek - presne ta chyba,
    kterou tenhle modul resi. Useky se proto v miste vetsi vodorovne mezery
    deli. Nadpis pres celou sirku zustane jednim usekem, protoze v nem zadna
    takova mezera neni.
    """
    rows = []
    for ch in sorted(chars, key=lambda c: (round(c["bottom"], 1), c["x0"])):
        if rows and abs(ch["bottom"] - rows[-1]["ref"]) <= tol:
            r = rows[-1]
            r["chars"].append(ch)
            r["ref"] = sum(c["bottom"] for c in r["chars"]) / len(r["chars"])
        else:
            rows.append({"ref": ch["bottom"], "chars": [ch]})

    out = []
    for r in rows:
        cur, prev_x1 = [], None
        for c in sorted(r["chars"], key=lambda c: c["x0"]):
            if prev_x1 is not None and c["x0"] - prev_x1 > gap:
                out.append({"ref": r["ref"], "chars": cur})
                cur = []
            cur.append(c)
            prev_x1 = max(prev_x1 or c["x1"], c["x1"])
        if cur:
            out.append({"ref": r["ref"], "chars": cur})

    res = []
    for ln in out:
        vis = [c for c in ln["chars"] if c["text"].strip()]
        if not vis:
            continue
        ln["x0"] = min(c["x0"] for c in vis)
        ln["x1"] = max(c["x1"] for c in vis)
        ln["text"] = "".join(c["text"] for c in ln["chars"]).strip()
        if ln["text"]:
            res.append(ln)
    return res


def _gutters(chars, width):
    """Svisle mezery bez textu, ktere deli stranku na sloupce."""
    vis = [c for c in chars if c["text"].strip()]
    if len(vis) < 120:
        return []
    nbins = int(width / BIN) + 2
    hist = [0] * nbins
    for c in vis:
        for b in range(max(0, int(c["x0"] / BIN)), min(nbins, int(c["x1"] / BIN) + 1)):
            hist[b] += 1
    limit = max(1, len(vis) * TOL)
    left = next((i for i, v in enumerate(hist) if v > limit), 0)
    right = next((i for i in range(nbins - 1, -1, -1) if hist[i] > limit), nbins - 1)
    out, run = [], None
    for i in range(left, right + 1):
        if hist[i] <= limit:
            run = i if run is None else run
        else:
            if run is not None and (i - run) * BIN >= MIN_GUTTER:
                out.append(((run + i) / 2 * BIN, (i - run) * BIN))
            run = None
    return [x for x, _ in out]


def _columns(chars, width):
    """Hranice sloupcu, nebo prazdny seznam u jednosloupcove stranky.

    Chodbicka z histogramu jeste nemusi byt chodbicka - kratky odstavec nebo
    zubata prava hrana ji udelaji taky. Prava chodbicka se pozna tim, ze ji
    neprekracuje skoro zadny radek a ze sloupce vedle ni nesou dost textu.
    """
    vis = [c for c in chars if c["text"].strip()]
    if len(vis) < 120:
        return []
    lines = _segments(chars)
    if len(lines) < 8:
        return []
    cand = _gutters(chars, width)
    cross_limit = max(1, len(lines) * 0.08)
    cand = [x for x in cand
            if sum(1 for ln in lines if ln["x0"] < x < ln["x1"]) <= cross_limit]
    if not cand:
        return []

    def cols_of(gs):
        edges = [0.0] + list(gs) + [width]
        return list(zip(edges, edges[1:]))

    def shares(cols):
        return [sum(1 for c in vis if a <= (c["x0"] + c["x1"]) / 2 < b) / len(vis)
                for a, b in cols]

    # sloupec, ktery skoro nic nenese, neni sloupec - chodbicku vedle nej zrus
    while cand:
        cols = cols_of(cand)
        sh = shares(cols)
        i = min(range(len(sh)), key=lambda k: sh[k])
        if sh[i] >= 0.10:
            break
        drop = i - 1 if i == len(cols) - 1 else i
        cand.pop(drop)
    if len(cand) < 1 or len(cand) > 5:
        return []
    return cols_of(cand)


def _reorder(lines, cols):
    """Radky do poradi cteni: pasmo po pasmu, v pasmu sloupec po sloupci."""
    tagged = []
    for ln in lines:
        hit = [i for i, (a, b) in enumerate(cols) if ln["x0"] < b and ln["x1"] > a]
        tagged.append((ln, hit[0] if len(hit) == 1 else None))
    out, band = [], [[] for _ in cols]

    def flush():
        for col in band:
            out.extend(col)
            col.clear()

    for ln, col in tagged:
        if col is None:                 # radek pres vic sloupcu ukoncuje pasmo
            flush()
            out.append(ln)
        else:
            band[col].append(ln)
    flush()
    return out


class _Page:
    """Nahradni stranka: stejne znaky, jine souradnice."""

    def __init__(self, page, chars):
        self.height, self.width = page.height, page.width
        self.chars = chars


def prerovnat(page, left=56.0):
    """Vrati nahradni stranku s useky v poradi cteni, nebo None.

    Zahlavi a zapati zustavaji pri okrajich stranky, aby je pdf_obecny poznal
    a odstranil; telo se rozlozi mezi ne.
    """
    chars = page.chars
    cols = _columns(chars, page.width)
    if len(cols) < 2:
        return None
    segs = _segments(chars)
    if not segs:
        return None
    h = page.height
    head = [s for s in segs if min(c["top"] for c in s["chars"]) < h * 0.08]
    foot = [s for s in segs if min(c["top"] for c in s["chars"]) > h * 0.90]
    body = _reorder([s for s in segs if s not in head and s not in foot], cols)

    new = []

    def place(items, y0, y1):
        step = (y1 - y0) / max(1, len(items))
        for i, ln in enumerate(items):
            base = next((a for a, b in cols if ln["x0"] < b and ln["x1"] > a), 0.0)
            wide = ln["x1"] - ln["x0"] > page.width * 0.6
            shift = 0.0 if wide else base - left
            y = y0 + i * step
            for c in ln["chars"]:
                d = dict(c)
                d["x0"], d["x1"] = c["x0"] - shift, c["x1"] - shift
                d["top"] = d["bottom"] = d["doctop"] = y
                new.append(d)

    place(head, h * 0.02, h * 0.06)
    place(body, h * 0.12, h * 0.86)
    place(foot, h * 0.93, h * 0.97)
    return _Page(page, new)


HYPH = re.compile(r"(?<=[a-záčďéěíňóřšťúůýž]{2})-\s+(?=[a-záčďéěíňóřšťúůýž])")


def spojit_deleni(md):
    """Slova rozdelena na konci radku sloupce: "správ- cům" -> "správcům".

    Slozeniny psane s pomlckou maji v textu pomlcku bez mezery, takze se
    tohle pravidlo jich netyka.
    """
    return HYPH.sub("", md)
