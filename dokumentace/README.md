# Bezpečná škola — dokumentace

Repozitář drží **strojově čitelný korpus českých metodik k bezpečnosti ve školách**
a návrh konverzační aplikace, která nad ním má stát.

| Dokument | Co v něm je |
| --- | --- |
| **README.md** *(tento soubor)* | Co jsou data, odkud jsou, jak jsou uspořádaná, výpis korpusu |
| [`provazanost-dat.md`](provazanost-dat.md) | Diagram provázanosti dokumentů — co na co navazuje, co korpus pokrývá a co ne |
| [`mapa-akteru.md`](mapa-akteru.md) | Kdo je kdo, kdy se na koho obrátit a s čím |
| [`navrh-aplikace.md`](navrh-aplikace.md) | Návrh chatovací aplikace pro ředitele a školy |

---

## 1. Co jsou ta data

Ve složce [`data/`](../data/) je **121 souborů, zhruba 342 000 slov**
(~615 000 tokenů) od sedmi vydavatelů.

Data mají dva původy:

- **Přepsané z PDF a DOCX** — 71 souborů, 764 stran. Originály jsou
  v [`zdrojova-data/`](../zdrojova-data/), převod dělá
  [`scripts/pdf_na_md.py`](../scripts/pdf_na_md.py). Přepis je věrný, ne
  shrnutý; kontrola slovní zásoby neukázala u žádného souboru vypuštěný obsah.
- **Nahrané rovnou v Markdownu** — 50 souborů: metodiky KRIT (z jejich
  publikačního webu) a zákon č. 359/1999 Sb. rozdělený po částech.

Pro citaci a právní účely platí vždy původní zdroj, ne přepis.

### Vydavatelé

| Vydavatel | Souborů | Slov |
| --- | ---: | ---: |
| MŠMT — primární prevence, BOZ, záškoláctví, spolupráce s PČR | 36 | ~150 000 |
| KRIT — Krizový informační tým Ministerstva vnitra | 37 | ~47 000 |
| Zákon č. 359/1999 Sb., o sociálně-právní ochraně dětí | 14 | ~50 000 |
| MV — Centrum proti terorismu a hybridním hrozbám (měkké cíle) | 6 | ~35 000 |
| MŠMT + MV – GŘ HZS — Škola a neštěstí: Jsme připraveni! | 1 | ~29 000 |
| MŠMT (ve spolupráci s MV, Policejním prezidiem ČR a MV – GŘ HZS) | 13 | ~12 500 |
| Krajské ředitelství policie hl. m. Prahy — Měkké cíle | 12 | ~9 500 |
| doc. PhDr. Barbora Vegrichtová, Ph.D., MBA a kol. | 1 | ~7 500 |
| MPSV — Odbor ochrany práv dětí | 1 | ~700 |

Data pokrývají několik odlišných pohledů na stejný problém, a v tom je jejich
cena: **MŠMT** říká, co má škola mít zpracované a co je závazné — a v přílohách
k primární prevenci i co dělat u jednotlivých typů rizikového chování žáka.
**Policie** říká, co má člověk v tu chvíli udělat. **KRIT** řeší, co a jak
komunikovat — a přináší i karty pro starosty k desítkám typů mimořádných
událostí. **MV** dodává metodiky k ochraně měkkých cílů, na které se metodika
MŠMT odkazuje. **MPSV a zákon 359/1999** pokrývají, komu se případ předává
a za jakých podmínek.

> **Pozor na adresáta.** Ne všechno je psané pro školu. Z metodik KRIT je
> škole adresovaná **jediná** — příručka pro školní prostředí; zbytek míří na
> starosty nebo na instituce veřejné správy a je pro školu použitelný, ale ne
> adresovaný. Rozpis je v [`provazanost-dat.md`](provazanost-dat.md),
> kapitola 3, a má přímý dopad na to, co smí aplikace řediteli radit.

---

## 2. Jak jsou uspořádaná

Ne podle vydavatele, ale **podle fáze, kterou dokument řeší**. Ředitel v krizi
nehledá „přílohu č. 7", hledá „co teď". Jedna fáze = jedna podsložka.

| Složka | Fáze | Souborů | Slov |
| --- | --- | ---: | ---: |
| [`01-ramec-a-legislativa/`](../data/01-ramec-a-legislativa/) | Co musíme mít a jak se to jmenuje | 28 | 81 000 |
| [`02-prevence-a-priprava/`](../data/02-prevence-a-priprava/) | Dokud se nic neděje | 14 | 33 600 |
| [`03-krizova-reakce/`](../data/03-krizova-reakce/) | První minuty a hodiny | 35 | 41 700 |
| [`04-po-krizi-a-navrat/`](../data/04-po-krizi-a-navrat/) | Stabilizace, evidence, předání | 10 | 43 200 |
| [`05-rizikove-chovani/`](../data/05-rizikove-chovani/) | *(jiná osa — viz níže)* | 34 | 142 300 |

Podsložky drží velké celky pohromadě, aby nepřeválcovaly zbytek:
[`zakon-359-1999/`](../data/01-ramec-a-legislativa/zakon-359-1999/) (14 souborů,
50 000 slov),
[`krit-karty-pro-starosty/`](../data/03-krizova-reakce/krit-karty-pro-starosty/)
(20 karet k typům mimořádných událostí) a v `05` přílohy Metodického doporučení
k primární prevenci.

Bez textu zákona, který je objemem výjimečný, vypadá rozložení takto:
rámec ~31 000, prevence ~33 600, krize ~41 700, po krizi ~43 200,
rizikové chování ~142 300 slov.

### Pátá složka není pátá fáze

`05-rizikove-chovani/` stojí mimo časovou osu. Přílohy Metodického doporučení
k primární prevenci jsou členěné podle **typu rizikového chování** — šikana,
návykové látky, sebepoškozování, sebevražedné chování — a každá z nich obsahuje
prevenci, intervenci i následnou péči najednou. Rozpustit je do fází by
znamenalo je rozřezat; nechat je pohromadě znamená přiznat, že korpus má dvě
osy třídění, ne jednu. Pro aplikaci z toho plyne, že volba režimu
(prevence / krize / po krizi) tuhle složku sama nevybere — je potřeba druhá
cesta, přes typ problému.

Toto členění je zároveň **kostrou navrhované aplikace** — viz
[`navrh-aplikace.md`](navrh-aplikace.md).

### Hlavička každého souboru

```yaml
title:    "Bezpečnostní plán"
dokument: "Minimální standard bezpečnosti v regionálním školství"
cast:     "příloha č. 7"
vydal:    "MŠMT ve spolupráci s MV, Policejním prezidiem ČR a MV – GŘ HZS ČR"
cj:       "MSMT-19322/2024-4"
datum:    "2024-11"
zdroj:    "../../zdrojova-data/příloha č. 7 - Bezpečnostní plán.pdf"
stran:    2
faze:     "02-prevence-a-priprava"
kategorie: [doporuceni]
```

### Značky závaznosti

Metodika MŠMT sama rozlišuje tři druhy obsahu barevným pruhem na okraji stránky.
Barvy jsou z PDF vytěžené a v přepisu zachované jako značky:

| Značka | Původní barva | Význam |
| --- | --- | --- |
| `**[§ ZÁVAZNÉ]**` | žlutá | Vyplývá z platných právních předpisů |
| `**[D DOPORUČENÍ]**` | zelená | Metodická podpora MŠMT |
| `**[I INFORMACE]**` | modrá | Informativní text a odkazy |

Značka platí až do další značky. Strojově: `grep -n '^\*\*\[§' soubor.md`.

**Pro aplikaci je to zásadní rozlišení.** Odpověď „tohle musíte ze zákona" a
„tohle vám doporučujeme" nesmí splynout — a jen dokumenty MŠMT tuto informaci
nesou. Policejní doporučení AMOK jsou celá v rovině doporučení.

---

## 3. Výpis korpusu

### 01 — Rámec a legislativa

| Soubor | Zdroj | O čem to je |
| --- | --- | --- |
| `00-minimalni-standard-bezpecnosti.md` | MŠMT, hlavní dokument | Zastřešující metodické doporučení, tři roviny bezpečnosti |
| `priloha-01-terminologie.md` | MŠMT, příloha 1 | 24 pojmů — lockdown, invakuace, měkký cíl, PZTS… |
| `priloha-02-legislativa.md` | MŠMT, příloha 2 | Trestní zákoník, školský zákon, zákoník práce, GDPR |
| `priloha-03-metodicke-materialy.md` | MŠMT, příloha 3 | Rozcestník na navazující metodiky |
| `priloha-04-dokumentace.md` | MŠMT, příloha 4 | Co škola musí a co má mít zpracované |
| `amok-11-nejcastejsi-dotazy.md` | PČR, AMOK 11 | FAQ napříč situacemi |
| `amok-12-koordinace-postupu-skoly.md` | PČR, AMOK 12 | Návrh systému koordinace, monitoring, evidence |
| `Jak přemýšlíme o krizích.md` | KRIT | Myšlenkový rámec — co je krize a jak se k ní stavět |
| `Pojmy a zkratky.md` | KRIT | Slovníček krizové komunikace |
| `Principy koordinace.md` | KRIT | Kdo koordinuje koho a podle čeho |
| `Metodiky a návody.md` | KRIT | Rozcestník po metodikách KRIT |
| `O kartách pro starosty.md` | KRIT | K čemu karty slouží a jak je číst |
| `msmt-pokyn-bozp-37014-2005.md` | MŠMT, čj. 37 014/2005-25 | Metodický pokyn k zajištění BOZ dětí, žáků a studentů |
| `mv-zaklady-ochrany-mekkych-cilu.md` | MV, CTHH | Základy ochrany měkkých cílů — pojmy, systém, principy |

#### `zakon-359-1999/` — zákon č. 359/1999 Sb., o sociálně-právní ochraně dětí

14 souborů, ~50 000 slov, znění k 1. 1. 2026. Rozdělený po částech, s poznámkami
pod čarou zvlášť. Pro školu je klíčová **ČÁST TŘETÍ — Opatření sociálně-právní
ochrany** (~14 000 slov), která popisuje, co OSPOD dělá a za jakých podmínek.
Zbytek (pěstounská péče, zaopatřovací příspěvek, inspekce) se školy týká
okrajově, ale je v korpusu pro úplnost.

### 02 — Prevence a příprava

| Soubor | Zdroj | O čem to je |
| --- | --- | --- |
| `priloha-06-bezpecnostni-analyza.md` | MŠMT, příloha 6 | Vyhodnocení ohroženosti — vstup do všeho ostatního |
| `priloha-07-bezpecnostni-plan.md` | MŠMT, příloha 7 | Struktura bezpečnostního plánu školy |
| `priloha-09-vzdelavani.md` | MŠMT, příloha 9 | Minimální standard výcviku, nároky na lektory |
| `priloha-10-priklady-bezpecnostnich-opatreni.md` | MŠMT, příloha 10 | Katalog režimových, technických a ostatních opatření |
| `amok-01-prevence-a-pripravenost.md` | PČR, AMOK 1 | Prevence a připravenost měkkého cíle |
| `amok-02-skoly-signaly-detekce-hodnoceni-reakce.md` | PČR, AMOK 2 | Varovné signály u žáků a co s nimi |
| `amok-03-instituce-indikatory-hrozby.md` | PČR, AMOK 3 | Indikátory hrozby na úrovni instituce |
| `amok-08-dny-otevrenych-dveri.md` | PČR, AMOK 8 | Akce s veřejností v budově |
| `vegrichtova-indikatory-radikalizace.md` | Vegrichtová a kol. | Indikátory radikalizace, praktické příklady |
| `mv-vyhodnoceni-ohrozenosti-mekkeho-cile.md` | MV, CTHH, 2025 | Detailní metodika k tomu, co příloha 6 jen rámuje |
| `mv-bezpecnostni-plan-mekkeho-cile.md` | MV, CTHH, 2025 | Totéž pro plán — 2. upravené vydání |
| `mv-koordinacni-plany-pro-mekke-cile.md` | MV, CTHH, 2025 | Jak se připravit na závažnou situaci |
| `mv-10-principu-zodolneni.md` | MV, CTHH | Deset principů na dvě strany |
| `msmt-spoluprace-skol-s-pcr.md` | MŠMT, čj. MSMT-6167/2025-1 | Kdy a jak škola spolupracuje s policií |

### 03 — Krizová reakce

| Soubor | Zdroj | O čem to je |
| --- | --- | --- |
| `priloha-11-karta-skoly-izs.md` | MŠMT, příloha 11 | Karta pro veliteli zásahu — co IZS potřebuje vědět |
| `amok-04-okamzita-reakce-na-utok.md` | PČR, AMOK 4 | UTEČ – SCHOVEJ SE – BOJUJ, povely, barikádování |
| `amok-07-podezreni-na-zbran-ve-skole.md` | PČR, AMOK 7 | Podezření na zbraň nebo nebezpečný předmět |
| `amok-09-obecna-doporuceni.md` | PČR, AMOK 9 | Obecný postup při bezpečnostním incidentu |
| `amok-10-zasady-krizove-komunikace.md` | PČR, AMOK 10 | Deeskalace konfliktu, jednání s agresorem |
| `krit-akutni-komunikace-ve-skolnim-prostredi.md` | KRIT, MV | Krizová komunikace ve škole — vzorové formulace, pořadí adresátů |
| `Akutní komunikace.md` | KRIT | Co dělat s komunikací v prvních hodinách |
| `Rodná karta incidentu (RKI).md` | KRIT | Sdílený živý dokument držící jeden obraz situace |
| `Rámec pro krizová sdělení (FOIPS).md` | KRIT | Struktura krizového sdělení |
| `Holding lines.md` | KRIT | Co říct, když ještě nic nevíte |
| `Komunikace s veřejností.md` | KRIT | Komunikační karta |
| `Sociálně citlivá témata.md` | KRIT | Když téma rozděluje veřejnost |
| `Systém včasného varování.md` | KRIT | Jak zachytit problém dřív, než vyroste |
| `Varování před hrozícím nebezpečím.md` | KRIT | Varovná sdělení |
| `Zapojení NNO a dobrovolníků.md` | KRIT | Práce s pomáhajícími organizacemi |

#### `krit-karty-pro-starosty/` — karty podle typu události

20 karet KRIT, každá k jednomu typu mimořádné události. Psané pro starosty, ale
pro školu použitelné — struktura je vždy stejná: co se děje, co komunikovat,
na co si dát pozor.

| Skupina | Karty |
| --- | --- |
| Bezpečnost a společnost | Útok ozbrojeného útočníka · Bombová výhrůžka ve škole · Eskalace projevů nenávisti a násilí · Ohrožení veřejných míst · Nález nevybuchlé munice · Jednání s obránci Ukrajiny |
| Infrastruktura a havárie | Narušení dodávek elektřiny · plynu a tepla · vody · Únik nebezpečných látek · Požár v obci · Lesní požár |
| Počasí a voda | Hrozba povodně · Vznik povodně · Přívalové srážky · Vichřice nebo tornádo · Extrémní teploty · Dlouhodobé sucho |
| Průřezové | Evakuace · Katastrofické mimořádné události |

### 04 — Po krizi a návrat

| Soubor | Zdroj | O čem to je |
| --- | --- | --- |
| `priloha-05-evidence-bezpecnostnich-incidentu.md` | MŠMT, příloha 5 | Proč a jak evidovat incidenty |
| `priloha-05-formular-zaznam-o-incidentu.md` | MŠMT, příloha 5 | Formulář záznamu (převedený z `.docx`) |
| `priloha-08-koordinacni-plan.md` | MŠMT, příloha 8 | Návrat do rutinního provozu |
| `amok-05-bezprostredne-po-utoku.md` | PČR, AMOK 5 | Stabilizace situace |
| `amok-06-zpet-do-bezneho-rezimu.md` | PČR, AMOK 6 | Obnova provozu a následná péče |
| `mpsv-metodicka-prirucka-pro-kuratory.md` | MPSV | Kurátor pro děti a mládež jako koordinátor případu |
| `Vyhodnocení po incidentu.md` | KRIT | Co si z incidentu odnést |
| `Případová studie – Povodně 2024.md` | KRIT | Rozbor reálné krizové komunikace |
| `skola-a-nestesti-jsme-pripraveni.md` | MŠMT + MV – GŘ HZS, 2023 | 84 stran: příprava, komunikace, právní minimum, psychosociální pomoc, návodné postupy |
| `mv-metodika-koordinace-po-zavaznem-incidentu.md` | MV, CTHH, 2025 | Jak projít fází po incidentu s co nejmenšími ztrátami |

> **Pozor na zařazení `skola-a-nestesti-jsme-pripraveni.md`.** Leží ve fázi
> „po krizi", protože tam korpus nejvíc chybělo a protože tam míří jeho těžiště
> — práce se zasaženými a následná péče. Velká část dokumentu je ale příprava:
> komunikační a mediální strategie školy, role a odpovědnosti, nácvik. Je to
> druhý soubor po příručce KRIT, který patří do dvou režimů; jestli takových
> přibude třetí, bude lepší zavést v hlavičce pole `faze` jako seznam.

### 05 — Rizikové chování

Metodické doporučení k primární prevenci rizikového chování (MŠMT,
čj. 21291/2010-28) — úvodní část a 22 tematických příloh. Členěné podle typu
chování, ne podle fáze.

| Soubor | Původ | O čem to je |
| --- | --- | --- |
| `00-md-primarni-prevence-uvodni-cast.md` | MŠMT, úvodní část | Rámec primární prevence: kdo co dělá, co je školní preventivní program |
| `msmt-zaskolactvi.md` | MŠMT, 2026 | Prevence a postih záškoláctví, omlouvání žáků |

#### `prilohy/` — 22 tematických příloh

Návykové látky · Rizikové chování v dopravě · Poruchy příjmu potravy · Alkohol ·
Týrané, zneužívané a zanedbávané dítě (CAN) · Školní šikana · Kybernetická
agrese · Homofobie · Extremismus, rasismus, xenofobie, antisemitismus ·
Vandalismus · Krádeže · Tabákové výrobky · **Krizové situace spojené s násilím** ·
Netolismus · Sebepoškozování · Nová náboženská hnutí · Rizikové sexuální chování ·
Příslušnost k subkulturám · Hazardní hraní · Žáci s PAS (+ formulář krizového
plánu) · Psychická krize a duševní onemocnění · Sebevražedné chování

Chybí přílohy č. 11 a 20 — v korpusu nejsou, protože nebyly mezi zdroji.

#### `priloha-05-sablony/` — tři šablony dopisů

Oznámení na OSPOD (žádost o prošetření podle § 10 zákona č. 359/1999 Sb.),
oznámení na PČR nebo státní zastupitelství a seznam regionálních odborníků.
Převedené z `.docx` i s tabulkami a prázdnými poli. **Pro průvodce dopisem
v aplikaci je tohle nejcennější kus celého doplnění** — jsou to úřední
struktury, ne náš odhad, jak má takový dopis vypadat.

#### `priloha-24-karty/` — šest karet k sebevražednému chování

Samostatné přílohy 8–14 přílohy č. 24, psané jako praktické návody: bezpečnostní
plán pro žáka, varovné znaky, podpůrný rozhovor, krizový plán pro pozůstalou
třídu a dvě karty pro zákonné zástupce. Příloha 10 („Co dělat kdy: míra rizika
sebevraždy a vhodné reakce pedagoga") v korpusu chybí — zdrojové PDF je grafika
bez textové vrstvy, viz Mezery v [`provazanost-dat.md`](provazanost-dat.md).

---

## 4. Co s tím dál

Korpus má dnes zhruba **615 000 tokenů**, tedy skoro trojnásobek toho, s čím
počítal původní návrh aplikace. Vkládat celý ho nešlo už předtím; teď se
**nevejde do promptu ani celá jedna fáze** — složka `05` sama má ~256 000
tokenů. Dvouvrstvý model z [`navrh-aplikace.md`](navrh-aplikace.md) (jádro
v promptu, zbytek přes `precti_dokument`) tím neztrácí platnost, ale posouvá se
hranice: do vždy-vloženého jádra patří míň, do dočítání víc, a složka `05`
potřebuje vlastní rejstřík podle typu problému, protože ji volba režimu
nevybere. Čísla v kapitole 2 a 3 návrhu je proto potřeba přepočítat.

Návrh, jak z toho udělat použitelný nástroj pro ředitele, je
v [`navrh-aplikace.md`](navrh-aplikace.md).
