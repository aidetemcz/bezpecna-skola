# Metodiky k bezpečnosti ve školách (Markdown)

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
`grep -n '^\*\*\[' soubor.md`. Ostatní dokumenty vlastní kategorizaci obsahu
nemají, jejich struktura vychází z nadpisů.

## Soubory

### Minimální standard bezpečnosti v regionálním školství (MŠMT, 2024)

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

### Doporučení AMOK

| Soubor | Část | Název |
| --- | --- | --- |
| [`amok-01-prevence-a-pripravenost.md`](amok-01-prevence-a-pripravenost.md) | Doporučení AMOK - 1 - Prevence a připravenost | Prevence a připravenost měkkého cíle |
| [`amok-02-skoly-signaly-detekce-hodnoceni-reakce.md`](amok-02-skoly-signaly-detekce-hodnoceni-reakce.md) | Doporučení AMOK - 2 - ŠKOLY - Signály, detekce, hodnocení, reakce | Školská zařízení – signály, detekce, hodnocení a okamžitá reakce |
| [`amok-03-instituce-indikatory-hrozby.md`](amok-03-instituce-indikatory-hrozby.md) | Doporučení AMOK - 3 - INSTITUCE - Indikátory hrozby - OMC | Instituce – indikátory hrozby v rámci ochrany měkkých cílů |
| [`amok-04-okamzita-reakce-na-utok.md`](amok-04-okamzita-reakce-na-utok.md) | Doporučení AMOK - 4 - Okamžitá reakce na útok | Okamžitá reakce na útok |
| [`amok-05-bezprostredne-po-utoku.md`](amok-05-bezprostredne-po-utoku.md) | Doporučení AMOK - 5 - Bezprostředně po útoku | Bezprostředně po útoku |
| [`amok-06-zpet-do-bezneho-rezimu.md`](amok-06-zpet-do-bezneho-rezimu.md) | Doporučení AMOK - 6 - Zpět do běžného režimu | Zpět do běžného režimu – obnova provozu a následná péče |
| [`amok-07-podezreni-na-zbran-ve-skole.md`](amok-07-podezreni-na-zbran-ve-skole.md) | Doporučení AMOK - 7 - Podezření na zbraň ve škole | Podezření na zbraň ve škole |
| [`amok-08-dny-otevrenych-dveri.md`](amok-08-dny-otevrenych-dveri.md) | Doporučení AMOK - 8 - Dny oteřených dvěří atd | Jednoduchá doporučení k organizaci dnů otevřených dveří |
| [`amok-09-obecna-doporuceni.md`](amok-09-obecna-doporuceni.md) | Doporučení AMOK - 9 - Obecná doporučení OMC | Obecná doporučení postupu při bezpečnostních incidentech |
| [`amok-10-zasady-krizove-komunikace.md`](amok-10-zasady-krizove-komunikace.md) | Doporučení AMOK - 10 - Základní pravidla krizové komunikace | Základní zásady deeskalace konfliktů a krizové komunikace |
| [`amok-11-nejcastejsi-dotazy.md`](amok-11-nejcastejsi-dotazy.md) | Doporučení AMOK - 11 - Nejčastější dotazy | Časté dotazy v rámci bezpečnostních incidentů |
| [`amok-12-koordinace-postupu-skoly.md`](amok-12-koordinace-postupu-skoly.md) | Doporučení AMOK - 12 - Koordinace postupu školy | Návrh systému koordinace postupu školy |

### Další metodiky

| Soubor | Část | Název |
| --- | --- | --- |
| [`mpsv-metodicka-prirucka-pro-kuratory.md`](mpsv-metodicka-prirucka-pro-kuratory.md) | 3_TZ_RVPPK_09_2017 | Metodická příručka pro kurátory pro děti a mládež |
| [`vegrichtova-indikatory-radikalizace.md`](vegrichtova-indikatory-radikalizace.md) | Metodika - Vegrichtová a kol. | Indikátory radikalizace v kontextu ochrany obyvatelstva a měkkých cílů před násilnými incidenty |

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
