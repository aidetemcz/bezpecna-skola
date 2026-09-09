"""Vygeneruje data/*.md ze souboru ve zdrojova-data/.

Spusteni z korene repozitare:

    pip install pdfplumber python-docx
    python scripts/pdf_na_md.py

Strukturu stranky (nadpisy, odrazky, barevne pruhy kategorii, poznamky pod
carou) rozpoznava modul pdf_struktura.py.
"""
import sys, os, re, glob, json
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import pdfplumber, docx
from pdf_struktura import parse, to_markdown
import pdf_obecny

DOC = "Minimální standard bezpečnosti v regionálním školství"
CJ = "MSMT-19322/2024-4"
VYDAL = "MŠMT ve spolupráci s MV, Policejním prezidiem ČR a MV – GŘ HZS ČR"
DATUM = "2024-11"

# zdrojovy soubor -> (vystupni nazev, cast dokumentu)
MAP = [
    ("Minimální standard bezpečnosti v regionálním školství.pdf",
     "00-minimalni-standard-bezpecnosti.md", "hlavní dokument"),
    ("příloha č. 1 - Terminologie.pdf",
     "priloha-01-terminologie.md", "příloha č. 1"),
    ("příloha č. 2 - Legislativa.pdf",
     "priloha-02-legislativa.md", "příloha č. 2"),
    ("příloha č. 3 - Metodické materiály.pdf",
     "priloha-03-metodicke-materialy.md", "příloha č. 3"),
    ("příloha č. 4 - Dokumentace.pdf",
     "priloha-04-dokumentace.md", "příloha č. 4"),
    ("příloha č. 5 - Evidence bezpečnostních incidentů.pdf",
     "priloha-05-evidence-bezpecnostnich-incidentu.md", "příloha č. 5"),
    ("příloha č. 6 - Bezpečnostní analýza včetně vyhodnocení ohroženosti.pdf",
     "priloha-06-bezpecnostni-analyza.md", "příloha č. 6"),
    ("příloha č. 7 - Bezpečnostní plán.pdf",
     "priloha-07-bezpecnostni-plan.md", "příloha č. 7"),
    ("příloha č. 8 - Koordinační plán.pdf",
     "priloha-08-koordinacni-plan.md", "příloha č. 8"),
    ("příloha č. 9 - Vzdělávání.pdf",
     "priloha-09-vzdelavani.md", "příloha č. 9"),
    ("příloha č. 10 - Příklady bezpečnostních opatření ve školách.pdf",
     "priloha-10-priklady-bezpecnostnich-opatreni.md", "příloha č. 10"),
    ("příloha č. 11 - Karta školy pro součinnost se složkami IZS při mimořádné události či bezpečnostním incidentu.pdf",
     "priloha-11-karta-skoly-izs.md", "příloha č. 11"),
]
DOCX = ("příloha č. 5 - Evidence bezpečnostních incidentů - formulář.docx",
        "priloha-05-formular-zaznam-o-incidentu.md", "příloha č. 5 – formulář")

TITLES = {'00-minimalni-standard-bezpecnosti.md': 'Minimální standard bezpečnosti v regionálním školství (metodické doporučení)', 'priloha-01-terminologie.md': 'Terminologie – výběr základních pojmů s přihlédnutím ke specifikům škol', 'priloha-02-legislativa.md': 'Legislativa', 'priloha-03-metodicke-materialy.md': 'Metodické materiály', 'priloha-04-dokumentace.md': 'Dokumentace', 'priloha-05-evidence-bezpecnostnich-incidentu.md': 'Evidence bezpečnostních incidentů', 'priloha-06-bezpecnostni-analyza.md': 'Bezpečnostní analýza včetně vyhodnocení ohroženosti', 'priloha-07-bezpecnostni-plan.md': 'Bezpečnostní plán', 'priloha-08-koordinacni-plan.md': 'Koordinační plán', 'priloha-09-vzdelavani.md': 'Vzdělávání', 'priloha-10-priklady-bezpecnostnich-opatreni.md': 'Příklady bezpečnostních opatření ve školách', 'priloha-11-karta-skoly-izs.md': 'Karta školy pro součinnost se složkami IZS při mimořádné události či bezpečnostním incidentu'}

AMOK_VYDAL = "Krajské ředitelství policie hl. m. Prahy, pracovní skupina Měkké cíle"

# zahlavi, ktere se u jednostrankovych dokumentu neda odhalit opakovanim
SKIP_LINES = ["KRAJSKÉ ŘEDITELSTVÍ POLICIE HL. MĚSTA PRAHY",
              "PRACOVNÍ SKUPINA: MĚKKÉ CÍLE",
              "PRACOVNÍ SKUPINA: RADIKALIZACE",
              "STÁLÝ TÝM VYJEDNAVAČŮ"]

# dalsi dokumenty bez vlastniho barevneho kodovani:
# (zdroj, vystup, nazev, vydal, datum, skupina)
MAP2 = [
 ("Doporučení AMOK - 1 - Prevence a připravenost.pdf", "amok-01-prevence-a-pripravenost.md",
  "Prevence a připravenost měkkého cíle", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 2 - ŠKOLY - Signály, detekce, hodnocení, reakce.pdf",
  "amok-02-skoly-signaly-detekce-hodnoceni-reakce.md",
  "Školská zařízení – signály, detekce, hodnocení a okamžitá reakce", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 3 - INSTITUCE - Indikátory hrozby - OMC.pdf",
  "amok-03-instituce-indikatory-hrozby.md",
  "Instituce – indikátory hrozby v rámci ochrany měkkých cílů", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 4 - Okamžitá reakce na útok.pdf", "amok-04-okamzita-reakce-na-utok.md",
  "Okamžitá reakce na útok", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 5 - Bezprostředně po útoku.pdf", "amok-05-bezprostredne-po-utoku.md",
  "Bezprostředně po útoku", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 6 - Zpět do běžného režimu.pdf", "amok-06-zpet-do-bezneho-rezimu.md",
  "Zpět do běžného režimu – obnova provozu a následná péče", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 7 - Podezření na zbraň ve škole.pdf", "amok-07-podezreni-na-zbran-ve-skole.md",
  "Podezření na zbraň ve škole", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 8 - Dny oteřených dvěří atd.pdf", "amok-08-dny-otevrenych-dveri.md",
  "Jednoduchá doporučení k organizaci dnů otevřených dveří", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 9 - Obecná doporučení OMC.pdf", "amok-09-obecna-doporuceni.md",
  "Obecná doporučení postupu při bezpečnostních incidentech", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 10 - Základní pravidla krizové komunikace.pdf",
  "amok-10-zasady-krizove-komunikace.md",
  "Základní zásady deeskalace konfliktů a krizové komunikace", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 11 - Nejčastější dotazy.pdf", "amok-11-nejcastejsi-dotazy.md",
  "Časté dotazy v rámci bezpečnostních incidentů", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("Doporučení AMOK - 12 - Koordinace postupu školy.pdf", "amok-12-koordinace-postupu-skoly.md",
  "Návrh systému koordinace postupu školy", AMOK_VYDAL, "", "Doporučení AMOK"),
 ("3_TZ_RVPPK_09_2017.pdf", "mpsv-metodicka-prirucka-pro-kuratory.md",
  "Metodická příručka pro kurátory pro děti a mládež",
  "Ministerstvo práce a sociálních věcí, Odbor ochrany práv dětí", "2017-09", "Další metodiky"),
 ("Metodika - Vegrichtová a kol..pdf", "vegrichtova-indikatory-radikalizace.md",
  "Indikátory radikalizace v kontextu ochrany obyvatelstva a měkkých cílů před násilnými incidenty",
  "doc. PhDr. Barbora Vegrichtová, Ph.D., MBA a kol.", "", "Další metodiky"),
]

CAT_ORDER = ["zavazne", "doporuceni", "informace"]


def yaml_str(s):
    return '"' + s.replace('"', '\\"') + '"'


def meta_lines(title, cast, src, pages, cats):
    m = [
        f"title: {yaml_str(title)}",
        f"dokument: {yaml_str(DOC)}",
        f"cast: {yaml_str(cast)}",
        f"vydal: {yaml_str(VYDAL)}",
        f"cj: {yaml_str(CJ)}",
        f"datum: {yaml_str(DATUM)}",
        f"zdroj: {yaml_str('zdrojova-data/' + src)}",
        f"stran: {pages}",
    ]
    if cats:
        m.append("kategorie: [" + ", ".join(cats) + "]")
    return m


def build_pdf(src, out, cast, outdir):
    path = os.path.join("zdrojova-data", src)
    blocks, notes = parse(path)
    with pdfplumber.open(path) as pdf:
        pages = len(pdf.pages)
    title = TITLES[out]
    cats = [c for c in CAT_ORDER if any(b["cat"] == c for b in blocks)]
    md = to_markdown(blocks, notes, meta_lines(title, cast, src, pages, cats), title)
    if out.startswith("00-"):
        md = fix_legend(md)
    open(os.path.join(outdir, out), "w", encoding="utf-8").write(md)
    return out, title, len(md)


LEGEND_TABLE = """Text je logicky členěn na tři různé druhy obsahu dle barev:

| Druh obsahu | Značka | Popis |
| --- | --- | --- |
| Závazné části | § | Takto označené části žlutou barvou poskytují informace o souvisejících závazných pravidlech vycházejících z platných právních předpisů, které v dané souvislosti považuje MŠMT za stěžejní. |
| Doporučení | D | Takto označené části zelenou barvou obsahují metodickou podporu MŠMT školám. |
| Informace | I | Takto označené části modrou barvou slouží jako informativní text, kde MŠMT upozorňuje na některé zásadní skutečnosti, odkazuje na jiné zdroje informací, stanoviska jiných správních úřadů apod. |"""


def fix_legend(md):
    """Trojsloupcovou legendu barev z titulni strany prepise na tabulku.

    V PDF je to graficka tabulka, ktera se pri extrakci textu rozpadne na
    promichane radky; obsah odpovida puvodnim trem radkum legendy.
    """
    start = md.index("Text je logicky členěn")
    end = md.index("zdroje informací, stanoviska jiných správních úřadů apod.")
    end = md.index("\n", end)
    scrambled = md[start:end]
    for probe in ("žlutou", "zelenou", "modrou", "Závazné části", "Doporučení", "Informace"):
        assert probe in scrambled, f"legenda: chybí {probe!r} - zkontroluj zdroj"
    return md[:start] + LEGEND_TABLE + md[end:]


def build_generic(entry, outdir):
    src, out, title, vydal, datum, skupina = entry
    path = os.path.join("zdrojova-data", src)
    with pdfplumber.open(path) as pdf:
        blocks, body = pdf_obecny.parse(pdf, skip_extra=SKIP_LINES)
        pages = len(pdf.pages)
    meta = [f"title: {yaml_str(title)}", f"dokument: {yaml_str(skupina)}",
            f"vydal: {yaml_str(vydal)}"]
    if datum:
        meta.append(f"datum: {yaml_str(datum)}")
    meta += [f"zdroj: {yaml_str('zdrojova-data/' + src)}", f"stran: {pages}"]
    md = pdf_obecny.to_markdown(blocks, body, meta, title)
    open(os.path.join(outdir, out), "w", encoding="utf-8").write(md)
    return out, title, len(md)


def build_docx(outdir):
    """Formular z .docx: tabulka se sloucenymi bunkami -> oddily s polozkami."""
    src, out, cast = DOCX
    d = docx.Document(os.path.join("zdrojova-data", src))
    head = re.sub(r"\s+", " ", next((p.text.strip() for p in d.paragraphs if p.text.strip()), ""))

    rows = []
    for r in d.tables[0].rows:
        cells, prev = [], None
        for c in r.cells:                      # vodorovne sloucene bunky se opakuji
            txt = re.sub(r"\s+", " ", c.text.strip())
            if txt != prev:
                cells.append(txt)
            prev = txt
        rows.append([c for c in cells if c])

    body, section = [], None
    header = []
    for i, cells in enumerate(rows):
        if i < 2:                              # zahlavi formulare: datum, cas, misto, zpracoval
            header += cells
            continue
        label = cells[0] if cells else ""
        items = cells[1:]
        if label and label != section:
            section = label
            title, _, note = label.partition(": (")
            body.append("")
            body.append("## " + title.rstrip(":"))
            if note:
                body.append("")
                body.append("(" + note)
            body.append("")
        for it in items:
            body.append("- " + it)

    md = ["---"] + meta_lines("Záznam o bezpečnostním incidentu (formulář)",
                              cast, src, 1, []) + ["---", "",
          "# Záznam o bezpečnostním incidentu", "",
          "Formulář z přílohy č. 5. Nadpisy jsou předtištěné oddíly formuláře,",
          "odrážky jednotlivá pole k vyplnění.", "",
          "## Záhlaví", "",
          "- " + head.replace(":", ":", 1)]
    md += ["- " + h.rstrip(":") + ":" for h in header]
    md += body
    text = re.sub(r"\n{3,}", "\n\n", "\n".join(md)).rstrip() + "\n"
    open(os.path.join(outdir, out), "w", encoding="utf-8").write(text)
    return out, "Záznam o bezpečnostním incidentu (formulář)", 0


README_HEAD = """# Metodiky k bezpečnosti ve školách (Markdown)

Strojově čitelné přepisy zdrojových dokumentů ze složky `../zdrojova-data/`.
Soubory vznikly automatickým převodem skriptem `../scripts/pdf_na_md.py`;
obsah je převzatý ze zdroje, není přeformulovaný ani zkracovaný.

Pro citaci a právní účely je závazné vždy původní PDF, ne tento přepis.

## Hlavička souboru

Každý soubor začíná YAML hlavičkou: `title`, `dokument` (celek, do kterého
patří), `vydal`, `zdroj` (cesta k původnímu souboru) a `stran`. Dokumenty MŠMT
navíc nesou `cast`, `cj`, `datum` a `kategorie`.

## Značky druhu obsahu (jen metodika MŠMT)

Metodika MŠMT rozlišuje tři druhy obsahu barevným pruhem v levém okraji
stránky. Barva pruhu je v přepisu zachovaná jako značka na začátku úseku:

| Značka v Markdownu | Původní barva | Význam |
| --- | --- | --- |
| `**[§ ZÁVAZNÉ]**` | žlutá | Závazná pravidla vycházející z platných právních předpisů. |
| `**[D DOPORUČENÍ]**` | zelená | Metodická podpora MŠMT školám. |
| `**[I INFORMACE]**` | modrá | Informativní text a odkazy na další zdroje. |

Značka platí až do další značky; úseky se dají číst například
`grep -n '^\\*\\*\\[' soubor.md`. Ostatní dokumenty vlastní kategorizaci obsahu
nemají, jejich struktura vychází z nadpisů.

## Soubory
"""

README_TAIL = """
## Co se při převodu změnilo

- Nadpisy metodiky MŠMT jsou psané normálně, ve zdroji jsou verzálkami.
- Legenda barev na titulní straně metodiky MŠMT je v PDF grafická tabulka;
  v přepisu je z ní tabulka Markdownu se stejným zněním textu.
- Poznámky pod čarou jsou převedené na odkazy `[^n]` a shromážděné na konci
  souboru v oddílu „Poznámky pod čarou".
- Formulář z přílohy č. 5 je ve zdroji `.docx` s tabulkou se sloučenými
  buňkami; v přepisu je z něj osnova oddílů a polí.
- Opakující se záhlaví a zápatí stránek a čísla stran se nepřenášejí.
- Grafika, loga a barevné pruhy se nepřenášejí; význam pruhů nesou značky výše.

Kontrolní porovnání slovní zásoby zdroje a přepisu neukázalo u žádného
dokumentu vypuštěný text.

## Co ve složce záměrně není

`Příručka KK ve školách.pdf` (KRIT, Ministerstvo vnitra) nese na titulní straně
doložku **„DOKUMENT NENÍ URČEN K VEŘEJNÉ DISTRIBUCI NEBO ZVEŘEJNĚNÍ"**, proto
z ní přepis nevznikl.
"""


def write_readme(outdir, made):
    rows = []
    for group, items in made:
        rows.append("")
        rows.append(f"### {group}")
        rows.append("")
        rows.append("| Soubor | Část | Název |")
        rows.append("| --- | --- | --- |")
        for out, title, label in items:
            rows.append(f"| [`{out}`]({out}) | {label} | {title} |")
    open(os.path.join(outdir, "README.md"), "w", encoding="utf-8").write(
        README_HEAD + "\n".join(rows) + "\n" + README_TAIL)


if __name__ == "__main__":
    outdir = "data"
    os.makedirs(outdir, exist_ok=True)

    msmt = []
    for src, out, cast in MAP:
        o, title, _ = build_pdf(src, out, cast, outdir)
        msmt.append((o, title, cast))
        if out == "priloha-05-evidence-bezpecnostnich-incidentu.md":
            o2, t2, _ = build_docx(outdir)
            msmt.append((o2, t2, DOCX[2]))

    groups = {}
    for e in MAP2:
        o, title, _ = build_generic(e, outdir)
        groups.setdefault(e[5], []).append((o, title, e[0].replace(".pdf", "")))

    made = [("Minimální standard bezpečnosti v regionálním školství (MŠMT, 2024)", msmt)]
    made += [(g, items) for g, items in groups.items()]
    write_readme(outdir, made)
    for group, items in made:
        print(f"\n== {group}")
        for o, title, label in items:
            print(f"   {o:52} {title[:52]}")
