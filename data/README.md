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

Složka `05-rizikove-chovani/` je výjimka: Metodické doporučení k primární
prevenci rizikového chování se do fází nevejde, protože každá jeho příloha
obsahuje prevenci, intervenci i následnou péči k jednomu typu rizikového
chování. Je to jiná osa třídění, ne pátá fáze.

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

| Soubor | Původ | Název |
| --- | --- | --- |
| [`00-minimalni-standard-bezpecnosti.md`](01-ramec-a-legislativa/00-minimalni-standard-bezpecnosti.md) | Minimální standard MŠMT, hlavní dokument | Minimální standard bezpečnosti v regionálním školství (metodické doporučení) |
| [`Jak přemýšlíme o krizích.md`](01-ramec-a-legislativa/Jak%20p%C5%99em%C3%BD%C5%A1l%C3%ADme%20o%20kriz%C3%ADch.md) | KRIT (MV) | Jak přemýšlíme o krizích |
| [`Metodiky a návody.md`](01-ramec-a-legislativa/Metodiky%20a%20n%C3%A1vody.md) | KRIT (MV) | Metodiky a návody |
| [`O kartách pro starosty.md`](01-ramec-a-legislativa/O%20kart%C3%A1ch%20pro%20starosty.md) | KRIT (MV) | O kartách pro starosty |
| [`Pojmy a zkratky.md`](01-ramec-a-legislativa/Pojmy%20a%20zkratky.md) | KRIT (MV) | Pojmy a zkratky |
| [`Principy koordinace.md`](01-ramec-a-legislativa/Principy%20koordinace.md) | KRIT (MV) | Principy koordinace |
| [`amok-11-nejcastejsi-dotazy.md`](01-ramec-a-legislativa/amok-11-nejcastejsi-dotazy.md) | Krajské ředitelství policie hl. m. Prahy | Časté dotazy v rámci bezpečnostních incidentů |
| [`amok-12-koordinace-postupu-skoly.md`](01-ramec-a-legislativa/amok-12-koordinace-postupu-skoly.md) | Krajské ředitelství policie hl. m. Prahy | Návrh systému koordinace postupu školy |
| [`msmt-pokyn-bozp-37014-2005.md`](01-ramec-a-legislativa/msmt-pokyn-bozp-37014-2005.md) | Ministerstvo školství | Metodický pokyn k zajištění bezpečnosti a ochrany zdraví dětí, žáků a studentů ve školách a školských zařízeních zřizovaných MŠMT |
| [`mv-zaklady-ochrany-mekkych-cilu.md`](01-ramec-a-legislativa/mv-zaklady-ochrany-mekkych-cilu.md) | Ochrana měkkých cílů (MV) | Základy ochrany měkkých cílů |
| [`priloha-01-terminologie.md`](01-ramec-a-legislativa/priloha-01-terminologie.md) | Minimální standard MŠMT, příloha č. 1 | Terminologie – výběr základních pojmů s přihlédnutím ke specifikům škol |
| [`priloha-02-legislativa.md`](01-ramec-a-legislativa/priloha-02-legislativa.md) | Minimální standard MŠMT, příloha č. 2 | Legislativa |
| [`priloha-03-metodicke-materialy.md`](01-ramec-a-legislativa/priloha-03-metodicke-materialy.md) | Minimální standard MŠMT, příloha č. 3 | Metodické materiály |
| [`priloha-04-dokumentace.md`](01-ramec-a-legislativa/priloha-04-dokumentace.md) | Minimální standard MŠMT, příloha č. 4 | Dokumentace |

#### zakon-359-1999/

| Soubor | Původ | Název |
| --- | --- | --- |
| [`00-README_zakon.md`](01-ramec-a-legislativa/zakon-359-1999/00-README_zakon.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`01-cast-prvni-uvodni-ustanoveni.md`](01-ramec-a-legislativa/zakon-359-1999/01-cast-prvni-uvodni-ustanoveni.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`02-cast-druha-zakladni-ustanoveni.md`](01-ramec-a-legislativa/zakon-359-1999/02-cast-druha-zakladni-ustanoveni.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`03-cast-treti-opatreni-socialne-pravni-ochrany.md`](01-ramec-a-legislativa/zakon-359-1999/03-cast-treti-opatreni-socialne-pravni-ochrany.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`04-cast-ctvrta-nektere-sluzby.md`](01-ramec-a-legislativa/zakon-359-1999/04-cast-ctvrta-nektere-sluzby.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`05-cast-pata-pestounska-pece.md`](01-ramec-a-legislativa/zakon-359-1999/05-cast-pata-pestounska-pece.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`06-cast-sesta-poverene-osoby.md`](01-ramec-a-legislativa/zakon-359-1999/06-cast-sesta-poverene-osoby.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`07-cast-sedma-inspekce.md`](01-ramec-a-legislativa/zakon-359-1999/07-cast-sedma-inspekce.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`08-cast-osma-zaopatrovaci-prispevek.md`](01-ramec-a-legislativa/zakon-359-1999/08-cast-osma-zaopatrovaci-prispevek.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`09-cast-devata-spolecna-ustanoveni.md`](01-ramec-a-legislativa/zakon-359-1999/09-cast-devata-spolecna-ustanoveni.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`10-cast-desata-prestupky.md`](01-ramec-a-legislativa/zakon-359-1999/10-cast-desata-prestupky.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`11-cast-jedenacta-rizeni-mistni-prislusnost.md`](01-ramec-a-legislativa/zakon-359-1999/11-cast-jedenacta-rizeni-mistni-prislusnost.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`12-cast-dvanacta-prechodna-zaverecna-ustanoveni.md`](01-ramec-a-legislativa/zakon-359-1999/12-cast-dvanacta-prechodna-zaverecna-ustanoveni.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |
| [`13-poznamky-pod-carou.md`](01-ramec-a-legislativa/zakon-359-1999/13-poznamky-pod-carou.md) | Zákon č. 359/1999 Sb. | Zákon o sociálně-právní ochraně dětí |


### 02-prevence-a-priprava/ — Prevence a příprava

Co dělat, dokud se nic neděje: analýza rizik, opatření, výcvik, čtení varovných signálů.

| Soubor | Původ | Název |
| --- | --- | --- |
| [`amok-01-prevence-a-pripravenost.md`](02-prevence-a-priprava/amok-01-prevence-a-pripravenost.md) | Krajské ředitelství policie hl. m. Prahy | Prevence a připravenost měkkého cíle |
| [`amok-02-skoly-signaly-detekce-hodnoceni-reakce.md`](02-prevence-a-priprava/amok-02-skoly-signaly-detekce-hodnoceni-reakce.md) | Krajské ředitelství policie hl. m. Prahy | Školská zařízení – signály, detekce, hodnocení a okamžitá reakce |
| [`amok-03-instituce-indikatory-hrozby.md`](02-prevence-a-priprava/amok-03-instituce-indikatory-hrozby.md) | Krajské ředitelství policie hl. m. Prahy | Instituce – indikátory hrozby v rámci ochrany měkkých cílů |
| [`amok-08-dny-otevrenych-dveri.md`](02-prevence-a-priprava/amok-08-dny-otevrenych-dveri.md) | Krajské ředitelství policie hl. m. Prahy | Jednoduchá doporučení k organizaci dnů otevřených dveří |
| [`msmt-spoluprace-skol-s-pcr.md`](02-prevence-a-priprava/msmt-spoluprace-skol-s-pcr.md) | Ministerstvo školství | Spolupráce škol a školských zařízení s Policií ČR při prevenci a při vyšetřování kriminality dětí a mládeže |
| [`mv-10-principu-zodolneni.md`](02-prevence-a-priprava/mv-10-principu-zodolneni.md) | Ochrana měkkých cílů (MV) | 10 principů zodolnění měkkého cíle |
| [`mv-bezpecnostni-plan-mekkeho-cile.md`](02-prevence-a-priprava/mv-bezpecnostni-plan-mekkeho-cile.md) | Ochrana měkkých cílů (MV), 2. upravené vydání | Bezpečnostní plán měkkého cíle aneb co by nemělo být opomenuto při jeho zpracování |
| [`mv-koordinacni-plany-pro-mekke-cile.md`](02-prevence-a-priprava/mv-koordinacni-plany-pro-mekke-cile.md) | Ochrana měkkých cílů (MV) | Jak se připravit na závažnou situaci? Koordinační plány pro měkké cíle |
| [`mv-vyhodnoceni-ohrozenosti-mekkeho-cile.md`](02-prevence-a-priprava/mv-vyhodnoceni-ohrozenosti-mekkeho-cile.md) | Ochrana měkkých cílů (MV) | Vyhodnocení ohroženosti měkkého cíle aneb co, kdy, kde a od koho vám hrozí |
| [`priloha-06-bezpecnostni-analyza.md`](02-prevence-a-priprava/priloha-06-bezpecnostni-analyza.md) | Minimální standard MŠMT, příloha č. 6 | Bezpečnostní analýza včetně vyhodnocení ohroženosti |
| [`priloha-07-bezpecnostni-plan.md`](02-prevence-a-priprava/priloha-07-bezpecnostni-plan.md) | Minimální standard MŠMT, příloha č. 7 | Bezpečnostní plán |
| [`priloha-09-vzdelavani.md`](02-prevence-a-priprava/priloha-09-vzdelavani.md) | Minimální standard MŠMT, příloha č. 9 | Vzdělávání |
| [`priloha-10-priklady-bezpecnostnich-opatreni.md`](02-prevence-a-priprava/priloha-10-priklady-bezpecnostnich-opatreni.md) | Minimální standard MŠMT, příloha č. 10 | Příklady bezpečnostních opatření ve školách |
| [`vegrichtova-indikatory-radikalizace.md`](02-prevence-a-priprava/vegrichtova-indikatory-radikalizace.md) | doc. PhDr. Barbora Vegrichtová | Indikátory radikalizace v kontextu ochrany obyvatelstva a měkkých cílů před násilnými incidenty |


### 03-krizova-reakce/ — Krizová reakce

Co dělat v prvních minutách a hodinách incidentu.

| Soubor | Původ | Název |
| --- | --- | --- |
| [`Akutní komunikace.md`](03-krizova-reakce/Akutn%C3%AD%20komunikace.md) | KRIT (MV) | Akutní komunikace |
| [`Holding lines.md`](03-krizova-reakce/Holding%20lines.md) | KRIT (MV) | Holding lines |
| [`Komunikace s veřejností.md`](03-krizova-reakce/Komunikace%20s%20ve%C5%99ejnost%C3%AD.md) | KRIT (MV) | Komunikace s veřejností |
| [`Rodná karta incidentu (RKI).md`](03-krizova-reakce/Rodn%C3%A1%20karta%20incidentu%20%28RKI%29.md) | KRIT (MV) | Rodná karta incidentu (RKI) |
| [`Rámec pro krizová sdělení (FOIPS).md`](03-krizova-reakce/R%C3%A1mec%20pro%20krizov%C3%A1%20sd%C4%9Blen%C3%AD%20%28FOIPS%29.md) | KRIT (MV) | Rámec pro krizová sdělení (FOIPS) |
| [`Sociálně citlivá témata.md`](03-krizova-reakce/Soci%C3%A1ln%C4%9B%20citliv%C3%A1%20t%C3%A9mata.md) | KRIT (MV) | Sociálně citlivá témata |
| [`Systém včasného varování.md`](03-krizova-reakce/Syst%C3%A9m%20v%C4%8Dasn%C3%A9ho%20varov%C3%A1n%C3%AD.md) | KRIT (MV) | Systém včasného varování |
| [`Varování před hrozícím nebezpečím.md`](03-krizova-reakce/Varov%C3%A1n%C3%AD%20p%C5%99ed%20hroz%C3%ADc%C3%ADm%20nebezpe%C4%8D%C3%ADm.md) | KRIT (MV) | Varování před hrozícím nebezpečím |
| [`Zapojení NNO a dobrovolníků.md`](03-krizova-reakce/Zapojen%C3%AD%20NNO%20a%20dobrovoln%C3%ADk%C5%AF.md) | KRIT (MV) | Zapojení NNO a dobrovolníků |
| [`amok-04-okamzita-reakce-na-utok.md`](03-krizova-reakce/amok-04-okamzita-reakce-na-utok.md) | Krajské ředitelství policie hl. m. Prahy | Okamžitá reakce na útok |
| [`amok-07-podezreni-na-zbran-ve-skole.md`](03-krizova-reakce/amok-07-podezreni-na-zbran-ve-skole.md) | Krajské ředitelství policie hl. m. Prahy | Podezření na zbraň ve škole |
| [`amok-09-obecna-doporuceni.md`](03-krizova-reakce/amok-09-obecna-doporuceni.md) | Krajské ředitelství policie hl. m. Prahy | Obecná doporučení postupu při bezpečnostních incidentech |
| [`amok-10-zasady-krizove-komunikace.md`](03-krizova-reakce/amok-10-zasady-krizove-komunikace.md) | Krajské ředitelství policie hl. m. Prahy | Základní zásady deeskalace konfliktů a krizové komunikace |
| [`krit-akutni-komunikace-ve-skolnim-prostredi.md`](03-krizova-reakce/krit-akutni-komunikace-ve-skolnim-prostredi.md) | KRIT – Krizový informační tým Ministerstva vnitra | Příručka Akutní komunikace ve školním prostředí |
| [`priloha-11-karta-skoly-izs.md`](03-krizova-reakce/priloha-11-karta-skoly-izs.md) | Minimální standard MŠMT, příloha č. 11 | Karta školy pro součinnost se složkami IZS při mimořádné události či bezpečnostním incidentu |

#### krit-karty-pro-starosty/

| Soubor | Původ | Název |
| --- | --- | --- |
| [`Bombová výhrůžka ve škole.md`](03-krizova-reakce/krit-karty-pro-starosty/Bombov%C3%A1%20v%C3%BDhr%C5%AF%C5%BEka%20ve%20%C5%A1kole.md) | KRIT (MV) | Bombová výhrůžka ve škole |
| [`Dlouhodobé sucho.md`](03-krizova-reakce/krit-karty-pro-starosty/Dlouhodob%C3%A9%20sucho.md) | KRIT (MV) | Dlouhodobé sucho |
| [`Eskalace projevů nenávisti a násilí.md`](03-krizova-reakce/krit-karty-pro-starosty/Eskalace%20projev%C5%AF%20nen%C3%A1visti%20a%20n%C3%A1sil%C3%AD.md) | KRIT (MV) | Eskalace projevů nenávisti a násilí |
| [`Evakuace.md`](03-krizova-reakce/krit-karty-pro-starosty/Evakuace.md) | KRIT (MV) | Evakuace |
| [`Extrémní teploty.md`](03-krizova-reakce/krit-karty-pro-starosty/Extr%C3%A9mn%C3%AD%20teploty.md) | KRIT (MV) | Extrémní teploty |
| [`Hrozba povodně.md`](03-krizova-reakce/krit-karty-pro-starosty/Hrozba%20povodn%C4%9B.md) | KRIT (MV) | Hrozba povodně |
| [`Jednání s obránci Ukrajiny.md`](03-krizova-reakce/krit-karty-pro-starosty/Jedn%C3%A1n%C3%AD%20s%20obr%C3%A1nci%20Ukrajiny.md) | KRIT (MV) | Jednání s obránci Ukrajiny |
| [`Katastrofické mimořádné události.md`](03-krizova-reakce/krit-karty-pro-starosty/Katastrofick%C3%A9%20mimo%C5%99%C3%A1dn%C3%A9%20ud%C3%A1losti.md) | KRIT (MV) | Katastrofické mimořádné události |
| [`Lesní požár.md`](03-krizova-reakce/krit-karty-pro-starosty/Lesn%C3%AD%20po%C5%BE%C3%A1r.md) | KRIT (MV) | Lesní požár |
| [`Narušení dodávek elektřiny.md`](03-krizova-reakce/krit-karty-pro-starosty/Naru%C5%A1en%C3%AD%20dod%C3%A1vek%20elekt%C5%99iny.md) | KRIT (MV) | Narušení dodávek elektřiny |
| [`Narušení dodávek plynu a tepla.md`](03-krizova-reakce/krit-karty-pro-starosty/Naru%C5%A1en%C3%AD%20dod%C3%A1vek%20plynu%20a%20tepla.md) | KRIT (MV) | Narušení dodávek plynu a tepla |
| [`Narušení dodávek vody.md`](03-krizova-reakce/krit-karty-pro-starosty/Naru%C5%A1en%C3%AD%20dod%C3%A1vek%20vody.md) | KRIT (MV) | Narušení dodávek vody |
| [`Nález nevybuchlé munice.md`](03-krizova-reakce/krit-karty-pro-starosty/N%C3%A1lez%20nevybuchl%C3%A9%20munice.md) | — | Nález nevybuchlé munice |
| [`Ohrožení veřejných míst.md`](03-krizova-reakce/krit-karty-pro-starosty/Ohro%C5%BEen%C3%AD%20ve%C5%99ejn%C3%BDch%20m%C3%ADst.md) | KRIT (MV) | Ohrožení veřejných míst |
| [`Požár v obci.md`](03-krizova-reakce/krit-karty-pro-starosty/Po%C5%BE%C3%A1r%20v%20obci.md) | KRIT (MV) | Požár v obci |
| [`Přívalové srážky.md`](03-krizova-reakce/krit-karty-pro-starosty/P%C5%99%C3%ADvalov%C3%A9%20sr%C3%A1%C5%BEky.md) | KRIT (MV) | Přívalové srážky |
| [`Vichřice nebo tornádo.md`](03-krizova-reakce/krit-karty-pro-starosty/Vich%C5%99ice%20nebo%20torn%C3%A1do.md) | KRIT (MV) | Vichřice nebo tornádo |
| [`Vznik povodně.md`](03-krizova-reakce/krit-karty-pro-starosty/Vznik%20povodn%C4%9B.md) | KRIT (MV) | Vznik povodně |
| [`Únik nebezpečných látek.md`](03-krizova-reakce/krit-karty-pro-starosty/%C3%9Anik%20nebezpe%C4%8Dn%C3%BDch%20l%C3%A1tek.md) | KRIT (MV) | Únik nebezpečných látek |
| [`Útok ozbrojeného útočníka.md`](03-krizova-reakce/krit-karty-pro-starosty/%C3%9Atok%20ozbrojen%C3%A9ho%20%C3%BAto%C4%8Dn%C3%ADka.md) | KRIT (MV) | Útok ozbrojeného útočníka |


### 04-po-krizi-a-navrat/ — Po krizi a návrat

Stabilizace, evidence, předání případu dál a návrat do běžného provozu.

| Soubor | Původ | Název |
| --- | --- | --- |
| [`Případová studie – Povodně 2024.md`](04-po-krizi-a-navrat/P%C5%99%C3%ADpadov%C3%A1%20studie%20%E2%80%93%20Povodn%C4%9B%202024.md) | KRIT (MV) | Případová studie – Povodně 2024 |
| [`Vyhodnocení po incidentu.md`](04-po-krizi-a-navrat/Vyhodnocen%C3%AD%20po%20incidentu.md) | KRIT (MV) | Vyhodnocení po incidentu |
| [`amok-05-bezprostredne-po-utoku.md`](04-po-krizi-a-navrat/amok-05-bezprostredne-po-utoku.md) | Krajské ředitelství policie hl. m. Prahy | Bezprostředně po útoku |
| [`amok-06-zpet-do-bezneho-rezimu.md`](04-po-krizi-a-navrat/amok-06-zpet-do-bezneho-rezimu.md) | Krajské ředitelství policie hl. m. Prahy | Zpět do běžného režimu – obnova provozu a následná péče |
| [`mpsv-metodicka-prirucka-pro-kuratory.md`](04-po-krizi-a-navrat/mpsv-metodicka-prirucka-pro-kuratory.md) | Ministerstvo práce a sociálních věcí | Metodická příručka pro kurátory pro děti a mládež |
| [`mv-metodika-koordinace-po-zavaznem-incidentu.md`](04-po-krizi-a-navrat/mv-metodika-koordinace-po-zavaznem-incidentu.md) | Ochrana měkkých cílů (MV) | Metodika koordinace měkkého cíle pro fáze po závažném incidentu aneb jak se vyrovnat s nastalou závažnou situací |
| [`priloha-05-evidence-bezpecnostnich-incidentu.md`](04-po-krizi-a-navrat/priloha-05-evidence-bezpecnostnich-incidentu.md) | Minimální standard MŠMT, příloha č. 5 | Evidence bezpečnostních incidentů |
| [`priloha-05-formular-zaznam-o-incidentu.md`](04-po-krizi-a-navrat/priloha-05-formular-zaznam-o-incidentu.md) | Minimální standard MŠMT, příloha č. 5 – formulář | Záznam o bezpečnostním incidentu (formulář) |
| [`priloha-08-koordinacni-plan.md`](04-po-krizi-a-navrat/priloha-08-koordinacni-plan.md) | Minimální standard MŠMT, příloha č. 8 | Koordinační plán |
| [`skola-a-nestesti-jsme-pripraveni.md`](04-po-krizi-a-navrat/skola-a-nestesti-jsme-pripraveni.md) | MŠMT ve spolupráci s MV – GŘ HZS ČR | Škola a neštěstí: Jsme připraveni! (metodika pro školy a školská zařízení) |


### 05-rizikove-chovani/ — Rizikové chování

Typy rizikového chování žáků a co s nimi — od návykových látek přes šikanu po sebevražedné chování. Jde napříč fázemi: každá příloha má prevenci, intervenci i následnou péči.

| Soubor | Původ | Název |
| --- | --- | --- |
| [`00-md-primarni-prevence-uvodni-cast.md`](05-rizikove-chovani/00-md-primarni-prevence-uvodni-cast.md) | MD k primární prevenci, úvodní část | Metodické doporučení k primární prevenci rizikového chování — úvodní část |
| [`msmt-zaskolactvi.md`](05-rizikove-chovani/msmt-zaskolactvi.md) | Ministerstvo školství | Metodické doporučení k prevenci a postihu záškoláctví a omlouvání žáků z vyučování |

#### priloha-05-sablony/

| Soubor | Původ | Název |
| --- | --- | --- |
| [`sablona-oznameni-na-ospod.md`](05-rizikove-chovani/priloha-05-sablony/sablona-oznameni-na-ospod.md) | MD k primární prevenci, příloha č. 5, šablona 1 | Šablona oznámení na OSPOD (žádost o prošetření podle § 10 zákona č. 359/1999 Sb.) |
| [`sablona-oznameni-na-pcr.md`](05-rizikove-chovani/priloha-05-sablony/sablona-oznameni-na-pcr.md) | MD k primární prevenci, příloha č. 5, šablona 2 | Šablona oznámení na PČR nebo státní zastupitelství (podezření ze spáchání trestného činu) |
| [`sablona-seznam-regionalnich-odborniku.md`](05-rizikove-chovani/priloha-05-sablony/sablona-seznam-regionalnich-odborniku.md) | MD k primární prevenci, příloha č. 5, šablona 3 | Šablona seznamu regionálních odborníků spolupracujících se školou (syndrom CAN) |

#### priloha-24-karty/

| Soubor | Původ | Název |
| --- | --- | --- |
| [`karta-08-bezpecnostni-plan-pro-zaky.md`](05-rizikove-chovani/priloha-24-karty/karta-08-bezpecnostni-plan-pro-zaky.md) | MD k primární prevenci, příloha č. 24, příloha 8 | Bezpečnostní plán pro žáky |
| [`karta-09-varovne-znaky-sebevrazedneho-jednani.md`](05-rizikove-chovani/priloha-24-karty/karta-09-varovne-znaky-sebevrazedneho-jednani.md) | MD k primární prevenci, příloha č. 24, příloha 9 | Varovné znaky sebevražedného jednání |
| [`karta-11-podpurny-rozhovor-s-zakem.md`](05-rizikove-chovani/priloha-24-karty/karta-11-podpurny-rozhovor-s-zakem.md) | MD k primární prevenci, příloha č. 24, příloha 11 | Podpůrný rozhovor s žákem |
| [`karta-12-krizovy-plan-pozustala-trida.md`](05-rizikove-chovani/priloha-24-karty/karta-12-krizovy-plan-pozustala-trida.md) | MD k primární prevenci, příloha č. 24, příloha 12 | Krizový plán pozůstalá třída |
| [`karta-13-pri-rozhovoru-s-ditetem-nezapomente.md`](05-rizikove-chovani/priloha-24-karty/karta-13-pri-rozhovoru-s-ditetem-nezapomente.md) | MD k primární prevenci, příloha č. 24, příloha 13 | Při rozhovoru s dítětem nezapomeňte |
| [`karta-14-me-dite-ma-myslenky-na-sebevrazdu.md`](05-rizikove-chovani/priloha-24-karty/karta-14-me-dite-ma-myslenky-na-sebevrazdu.md) | MD k primární prevenci, příloha č. 24, příloha 14 | Mé dítě má myšlenky na sebevraždu |

#### prilohy/

| Soubor | Původ | Název |
| --- | --- | --- |
| [`priloha-01-navykove-latky.md`](05-rizikove-chovani/prilohy/priloha-01-navykove-latky.md) | MD k primární prevenci, příloha č. 1 | Návykové látky |
| [`priloha-02-rizikove-chovani-v-doprave.md`](05-rizikove-chovani/prilohy/priloha-02-rizikove-chovani-v-doprave.md) | MD k primární prevenci, příloha č. 2 | Rizikové chování v dopravě |
| [`priloha-03-poruchy-prijmu-potravy.md`](05-rizikove-chovani/prilohy/priloha-03-poruchy-prijmu-potravy.md) | MD k primární prevenci, příloha č. 3 | Poruchy příjmu potravy |
| [`priloha-04-alkohol.md`](05-rizikove-chovani/prilohy/priloha-04-alkohol.md) | MD k primární prevenci, příloha č. 4 | Alkohol |
| [`priloha-05-tyrane-zneuzivane-zanedbavane-dite.md`](05-rizikove-chovani/prilohy/priloha-05-tyrane-zneuzivane-zanedbavane-dite.md) | MD k primární prevenci, příloha č. 5 | Týrané, zneužívané a zanedbávané dítě |
| [`priloha-06-skolni-sikana.md`](05-rizikove-chovani/prilohy/priloha-06-skolni-sikana.md) | MD k primární prevenci, příloha č. 6 | Školní šikana |
| [`priloha-07-kyberneticka-agrese.md`](05-rizikove-chovani/prilohy/priloha-07-kyberneticka-agrese.md) | MD k primární prevenci, příloha č. 7 | Kybernetická agrese |
| [`priloha-08-homofobie.md`](05-rizikove-chovani/prilohy/priloha-08-homofobie.md) | MD k primární prevenci, příloha č. 8 | Homofobie |
| [`priloha-09-extremismus-rasismus-xenofobie.md`](05-rizikove-chovani/prilohy/priloha-09-extremismus-rasismus-xenofobie.md) | MD k primární prevenci, příloha č. 9 | Extremismus, rasismus, xenofobie, antisemitismus |
| [`priloha-10-vandalismus.md`](05-rizikove-chovani/prilohy/priloha-10-vandalismus.md) | MD k primární prevenci, příloha č. 10 | Vandalismus |
| [`priloha-12-kradeze.md`](05-rizikove-chovani/prilohy/priloha-12-kradeze.md) | MD k primární prevenci, příloha č. 12 | Krádeže |
| [`priloha-13-tabakove-vyrobky.md`](05-rizikove-chovani/prilohy/priloha-13-tabakove-vyrobky.md) | MD k primární prevenci, příloha č. 13 | Tabákové výrobky |
| [`priloha-14-krizove-situace-spojene-s-nasilim.md`](05-rizikove-chovani/prilohy/priloha-14-krizove-situace-spojene-s-nasilim.md) | MD k primární prevenci, příloha č. 14 | Krizové situace spojené s násilím |
| [`priloha-15-netolismus.md`](05-rizikove-chovani/prilohy/priloha-15-netolismus.md) | MD k primární prevenci, příloha č. 15 | Netolismus |
| [`priloha-16-sebeposkozovani.md`](05-rizikove-chovani/prilohy/priloha-16-sebeposkozovani.md) | MD k primární prevenci, příloha č. 16 | Sebepoškozování |
| [`priloha-17-nova-nabozenska-hnuti.md`](05-rizikove-chovani/prilohy/priloha-17-nova-nabozenska-hnuti.md) | MD k primární prevenci, příloha č. 17 | Nová náboženská hnutí |
| [`priloha-18-rizikove-sexualni-chovani.md`](05-rizikove-chovani/prilohy/priloha-18-rizikove-sexualni-chovani.md) | MD k primární prevenci, příloha č. 18 | Rizikové sexuální chování |
| [`priloha-19-prislusnost-k-subkulturam.md`](05-rizikove-chovani/prilohy/priloha-19-prislusnost-k-subkulturam.md) | MD k primární prevenci, příloha č. 19 | Příslušnost k subkulturám |
| [`priloha-21-hazardni-hrani.md`](05-rizikove-chovani/prilohy/priloha-21-hazardni-hrani.md) | MD k primární prevenci, příloha č. 21 | Hazardní hraní |
| [`priloha-22-formular-krizovy-plan-pas.md`](05-rizikove-chovani/prilohy/priloha-22-formular-krizovy-plan-pas.md) | MD k primární prevenci, příloha č. 22 – formulář | Krizový plán pro prevenci vzniku problémových situací týkajících se žáka s PAS (formulář) |
| [`priloha-22-zaci-s-pas.md`](05-rizikove-chovani/prilohy/priloha-22-zaci-s-pas.md) | MD k primární prevenci, příloha č. 22 | Žáci s PAS |
| [`priloha-23-psychicka-krize-dusevni-onemocneni.md`](05-rizikove-chovani/prilohy/priloha-23-psychicka-krize-dusevni-onemocneni.md) | MD k primární prevenci, příloha č. 23 | Psychická krize a duševní onemocnění |
| [`priloha-24-sebevrazedne-chovani.md`](05-rizikove-chovani/prilohy/priloha-24-sebevrazedne-chovani.md) | MD k primární prevenci, příloha č. 24 | Sebevražedné chování |


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
- Brožury Ministerstva vnitra jsou sázené do dvou až čtyř sloupců, u některých
  na šířku dvoustrany. Modul `../scripts/pdf_sloupce.py` stránku před převodem
  rozdělí podle svislých mezer a řádky přerovná do pořadí čtení; nadpisy přes
  celou šířku zůstávají na svém místě a dělí stránku na pásma.
- Slova rozdělená na konci řádku úzkého sloupce (`aktua-lizovat`) jsou v přepisu
  spojená zpět. Složeniny psané s pomlčkou to nepostihuje, ty mají pomlčku bez
  mezery.
- Šablony dopisů a formuláře z `.docx` se převádějí i s tabulkami; prázdné buňky
  zůstávají prázdné, aby bylo vidět, co se vyplňuje.

Kontrolní porovnání slovní zásoby zdroje a přepisu neukázalo u žádného
dokumentu vypuštěný text; rozdílem jsou výše uvedená opakovaná razítka,
stránková výplň, průběžná záhlaví a zápatí (adresa ministerstva, číslo
jednací, běžící název) a u brožur MV zpětně spojená dělená slova.

