# Metodiky k bezpečnosti ve školách (Markdown)

Strojově čitelné přepisy zdrojových dokumentů ze složky `../zdrojova-data/`.
Soubory vznikly automatickým převodem skriptem `../scripts/pdf_na_md.py`;
obsah je převzatý ze zdroje, není přeformulovaný ani zkracovaný.

Pro citaci a právní účely je závazné vždy původní PDF, ne tento přepis.

## Členění složky

Soubory jsou rozdělené podle **fáze, kterou řeší** — ne podle vydavatele.
Jedna fáze = jedna podsložka. Dokumenty od různých vydavatelů se tak potkávají
tam, kde se potkávají i v praxi: metodika MŠMT říká, co má škola mít
zpracované, policejní doporučení AMOK, co má člověk v tu chvíli udělat.

## Hlavička souboru

Každý soubor začíná YAML hlavičkou: `title`, `dokument` (celek, do kterého
patří), `vydal`, `zdroj` (cesta k původnímu souboru), `stran` a `faze`
(podsložka). Dokumenty MŠMT navíc nesou `cast`, `cj`, `datum` a `kategorie`.

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

## Korpus

### 01-ramec-a-legislativa/ — Rámec a legislativa

Co škola musí, co má zpracované a jakým jazykem se o bezpečnosti mluví.

| Soubor | Zdrojový dokument | Název |
| --- | --- | --- |
| [`00-minimalni-standard-bezpecnosti.md`](01-ramec-a-legislativa/00-minimalni-standard-bezpecnosti.md) | Minimální standard MŠMT, hlavní dokument | Minimální standard bezpečnosti v regionálním školství (metodické doporučení) |
| [`priloha-01-terminologie.md`](01-ramec-a-legislativa/priloha-01-terminologie.md) | Minimální standard MŠMT, příloha č. 1 | Terminologie – výběr základních pojmů s přihlédnutím ke specifikům škol |
| [`priloha-02-legislativa.md`](01-ramec-a-legislativa/priloha-02-legislativa.md) | Minimální standard MŠMT, příloha č. 2 | Legislativa |
| [`priloha-03-metodicke-materialy.md`](01-ramec-a-legislativa/priloha-03-metodicke-materialy.md) | Minimální standard MŠMT, příloha č. 3 | Metodické materiály |
| [`priloha-04-dokumentace.md`](01-ramec-a-legislativa/priloha-04-dokumentace.md) | Minimální standard MŠMT, příloha č. 4 | Dokumentace |
| [`amok-11-nejcastejsi-dotazy.md`](01-ramec-a-legislativa/amok-11-nejcastejsi-dotazy.md) | Doporučení AMOK (PČR) | Časté dotazy v rámci bezpečnostních incidentů |
| [`amok-12-koordinace-postupu-skoly.md`](01-ramec-a-legislativa/amok-12-koordinace-postupu-skoly.md) | Doporučení AMOK (PČR) | Návrh systému koordinace postupu školy |

### 02-prevence-a-priprava/ — Prevence a příprava

Co dělat, dokud se nic neděje: analýza rizik, opatření, výcvik, čtení varovných signálů.

| Soubor | Zdrojový dokument | Název |
| --- | --- | --- |
| [`priloha-06-bezpecnostni-analyza.md`](02-prevence-a-priprava/priloha-06-bezpecnostni-analyza.md) | Minimální standard MŠMT, příloha č. 6 | Bezpečnostní analýza včetně vyhodnocení ohroženosti |
| [`priloha-07-bezpecnostni-plan.md`](02-prevence-a-priprava/priloha-07-bezpecnostni-plan.md) | Minimální standard MŠMT, příloha č. 7 | Bezpečnostní plán |
| [`priloha-09-vzdelavani.md`](02-prevence-a-priprava/priloha-09-vzdelavani.md) | Minimální standard MŠMT, příloha č. 9 | Vzdělávání |
| [`priloha-10-priklady-bezpecnostnich-opatreni.md`](02-prevence-a-priprava/priloha-10-priklady-bezpecnostnich-opatreni.md) | Minimální standard MŠMT, příloha č. 10 | Příklady bezpečnostních opatření ve školách |
| [`amok-01-prevence-a-pripravenost.md`](02-prevence-a-priprava/amok-01-prevence-a-pripravenost.md) | Doporučení AMOK (PČR) | Prevence a připravenost měkkého cíle |
| [`amok-02-skoly-signaly-detekce-hodnoceni-reakce.md`](02-prevence-a-priprava/amok-02-skoly-signaly-detekce-hodnoceni-reakce.md) | Doporučení AMOK (PČR) | Školská zařízení – signály, detekce, hodnocení a okamžitá reakce |
| [`amok-03-instituce-indikatory-hrozby.md`](02-prevence-a-priprava/amok-03-instituce-indikatory-hrozby.md) | Doporučení AMOK (PČR) | Instituce – indikátory hrozby v rámci ochrany měkkých cílů |
| [`amok-08-dny-otevrenych-dveri.md`](02-prevence-a-priprava/amok-08-dny-otevrenych-dveri.md) | Doporučení AMOK (PČR) | Jednoduchá doporučení k organizaci dnů otevřených dveří |
| [`vegrichtova-indikatory-radikalizace.md`](02-prevence-a-priprava/vegrichtova-indikatory-radikalizace.md) | Další metodiky | Indikátory radikalizace v kontextu ochrany obyvatelstva a měkkých cílů před násilnými incidenty |

### 03-krizova-reakce/ — Krizová reakce

Co dělat v prvních minutách a hodinách incidentu.

| Soubor | Zdrojový dokument | Název |
| --- | --- | --- |
| [`priloha-11-karta-skoly-izs.md`](03-krizova-reakce/priloha-11-karta-skoly-izs.md) | Minimální standard MŠMT, příloha č. 11 | Karta školy pro součinnost se složkami IZS při mimořádné události či bezpečnostním incidentu |
| [`amok-04-okamzita-reakce-na-utok.md`](03-krizova-reakce/amok-04-okamzita-reakce-na-utok.md) | Doporučení AMOK (PČR) | Okamžitá reakce na útok |
| [`amok-07-podezreni-na-zbran-ve-skole.md`](03-krizova-reakce/amok-07-podezreni-na-zbran-ve-skole.md) | Doporučení AMOK (PČR) | Podezření na zbraň ve škole |
| [`amok-09-obecna-doporuceni.md`](03-krizova-reakce/amok-09-obecna-doporuceni.md) | Doporučení AMOK (PČR) | Obecná doporučení postupu při bezpečnostních incidentech |
| [`amok-10-zasady-krizove-komunikace.md`](03-krizova-reakce/amok-10-zasady-krizove-komunikace.md) | Doporučení AMOK (PČR) | Základní zásady deeskalace konfliktů a krizové komunikace |
| [`krit-akutni-komunikace-ve-skolnim-prostredi.md`](03-krizova-reakce/krit-akutni-komunikace-ve-skolnim-prostredi.md) | Další metodiky | Příručka Akutní komunikace ve školním prostředí |

### 04-po-krizi-a-navrat/ — Po krizi a návrat

Stabilizace, evidence, předání případu dál a návrat do běžného provozu.

| Soubor | Zdrojový dokument | Název |
| --- | --- | --- |
| [`priloha-05-evidence-bezpecnostnich-incidentu.md`](04-po-krizi-a-navrat/priloha-05-evidence-bezpecnostnich-incidentu.md) | Minimální standard MŠMT, příloha č. 5 | Evidence bezpečnostních incidentů |
| [`priloha-05-formular-zaznam-o-incidentu.md`](04-po-krizi-a-navrat/priloha-05-formular-zaznam-o-incidentu.md) | Minimální standard MŠMT, příloha č. 5 – formulář | Záznam o bezpečnostním incidentu (formulář) |
| [`priloha-08-koordinacni-plan.md`](04-po-krizi-a-navrat/priloha-08-koordinacni-plan.md) | Minimální standard MŠMT, příloha č. 8 | Koordinační plán |
| [`amok-05-bezprostredne-po-utoku.md`](04-po-krizi-a-navrat/amok-05-bezprostredne-po-utoku.md) | Doporučení AMOK (PČR) | Bezprostředně po útoku |
| [`amok-06-zpet-do-bezneho-rezimu.md`](04-po-krizi-a-navrat/amok-06-zpet-do-bezneho-rezimu.md) | Doporučení AMOK (PČR) | Zpět do běžného režimu – obnova provozu a následná péče |
| [`mpsv-metodicka-prirucka-pro-kuratory.md`](04-po-krizi-a-navrat/mpsv-metodicka-prirucka-pro-kuratory.md) | Další metodiky | Metodická příručka pro kurátory pro děti a mládež |

## Co se při převodu změnilo

- Nadpisy metodiky MŠMT jsou psané normálně, ve zdroji jsou verzálkami.
- Legenda barev na titulní straně metodiky MŠMT je v PDF grafická tabulka;
  v přepisu je z ní tabulka Markdownu se stejným zněním textu.
- Poznámky pod čarou jsou převedené na odkazy `[^n]` a shromážděné na konci
  souboru v oddílu „Poznámky pod čarou".
- Formulář z přílohy č. 5 je ve zdroji `.docx` s tabulkou se sloučenými
  buňkami; v přepisu je z něj osnova oddílů a polí.
- Opakující se záhlaví a zápatí stránek a čísla stran se nepřenášejí.
- Razítka opakovaná na více stranách (např. doložka o distribuci v příručce
  KRIT) zůstávají jednou, na titulní straně; další výskyty se vypouštějí.
- Grafika, loga a barevné pruhy se nepřenášejí; význam pruhů nesou značky výše.

Kontrolní porovnání slovní zásoby zdroje a přepisu neukázalo u žádného
dokumentu vypuštěný text; jediným rozdílem jsou výše uvedená opakovaná
razítka a stránková výplň.

