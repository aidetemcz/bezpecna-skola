# Metodika MŠMT – Minimální standard bezpečnosti (Markdown)

Strojově čitelný přepis metodického doporučení
**Minimální standard bezpečnosti v regionálním školství**
(MŠMT, listopad 2024, č.j. MSMT-19322/2024-4) a všech jeho příloh.

Zdrojová PDF a formulář jsou v `../zdrojova-data/`. Soubory v této složce
vznikly automatickým převodem skriptem `../scripts/pdf_na_md.py`; obsah je
převzatý ze zdroje, není přeformulovaný.

## Značky druhu obsahu

Metodika rozlišuje tři druhy obsahu barevným pruhem v levém okraji stránky.
Barva pruhu je v přepisu zachovaná jako značka na začátku každého úseku:

| Značka v Markdownu | Původní barva | Význam |
| --- | --- | --- |
| `**[§ ZÁVAZNÉ]**` | žlutá | Závazná pravidla vycházející z platných právních předpisů. |
| `**[D DOPORUČENÍ]**` | zelená | Metodická podpora MŠMT školám. |
| `**[I INFORMACE]**` | modrá | Informativní text a odkazy na další zdroje. |

Značka platí až do další značky. Strojově se úseky dají číst například
`grep -n '^\*\*\[' soubor.md`.

## Hlavička souboru

Každý soubor začíná YAML hlavičkou s poli `title`, `dokument`, `cast`, `vydal`,
`cj`, `datum`, `zdroj` (cesta k původnímu PDF) a `stran`. Pole `kategorie`
vyjmenovává druhy obsahu, které se v souboru vyskytují.

## Soubory

| Soubor | Část | Název |
| --- | --- | --- |
| [`00-minimalni-standard-bezpecnosti.md`](00-minimalni-standard-bezpecnosti.md) | hlavní dokument | Minimální standard bezpečnosti v regionálním školství (metodické doporučení) |
| [`priloha-01-terminologie.md`](priloha-01-terminologie.md) | příloha č. 1 | Terminologie – výběr základních pojmů s přihlédnutím ke specifikům škol |
| [`priloha-02-legislativa.md`](priloha-02-legislativa.md) | příloha č. 2 | Legislativa |
| [`priloha-03-metodicke-materialy.md`](priloha-03-metodicke-materialy.md) | příloha č. 3 | Metodické materiály |
| [`priloha-04-dokumentace.md`](priloha-04-dokumentace.md) | příloha č. 4 | Dokumentace |
| [`priloha-05-evidence-bezpecnostnich-incidentu.md`](priloha-05-evidence-bezpecnostnich-incidentu.md) | příloha č. 5 | Evidence bezpečnostních incidentů |
| [`priloha-05-formular-zaznam-o-incidentu.md`](priloha-05-formular-zaznam-o-incidentu.md) | příloha č. 5 – formulář | Záznam o bezpečnostním incidentu (formulář) |
| [`priloha-06-bezpecnostni-analyza.md`](priloha-06-bezpecnostni-analyza.md) | příloha č. 6 | Bezpečnostní analýza včetně vyhodnocení ohroženosti |
| [`priloha-07-bezpecnostni-plan.md`](priloha-07-bezpecnostni-plan.md) | příloha č. 7 | Bezpečnostní plán |
| [`priloha-08-koordinacni-plan.md`](priloha-08-koordinacni-plan.md) | příloha č. 8 | Koordinační plán |
| [`priloha-09-vzdelavani.md`](priloha-09-vzdelavani.md) | příloha č. 9 | Vzdělávání |
| [`priloha-10-priklady-bezpecnostnich-opatreni.md`](priloha-10-priklady-bezpecnostnich-opatreni.md) | příloha č. 10 | Příklady bezpečnostních opatření ve školách |
| [`priloha-11-karta-skoly-izs.md`](priloha-11-karta-skoly-izs.md) | příloha č. 11 | Karta školy pro součinnost se složkami IZS při mimořádné události či bezpečnostním incidentu |

## Co se při převodu změnilo

- Nadpisy jsou v přepisu psané normálně, ve zdroji jsou verzálkami.
- Legenda barev na titulní straně hlavního dokumentu je v PDF grafická tabulka;
  v přepisu je z ní tabulka Markdownu se stejným zněním textu.
- Poznámky pod čarou jsou převedené na odkazy `[^n]` a shromážděné na konci
  souboru v oddílu „Poznámky pod čarou“.
- Formulář z přílohy č. 5 je ve zdroji `.docx` s tabulkou se sloučenými
  buňkami; v přepisu je z něj dvousloupcová tabulka.
- Grafika, loga a barevné pruhy se nepřenášejí, jejich význam nesou značky výše.

Kontrolní porovnání slovní zásoby zdroje a přepisu neukázalo žádný vypuštěný
text. Pro citaci a právní účely je závazné původní PDF ve `../zdrojova-data/`.
