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

Ve složce [`data/`](../data/) je **78 souborů, zhruba 127 000 slov**
(~228 000 tokenů) od šesti vydavatelů.

Data mají dva původy:

- **Přepsané z PDF** — 28 souborů, 150 stran. Originály jsou
  v [`zdrojova-data/`](../zdrojova-data/), převod dělá
  [`scripts/pdf_na_md.py`](../scripts/pdf_na_md.py). Přepis je věrný, ne
  shrnutý; kontrola slovní zásoby neukázala u žádného souboru vypuštěný obsah.
- **Nahrané rovnou v Markdownu** — 50 souborů: metodiky KRIT (z jejich
  publikačního webu) a zákon č. 359/1999 Sb. rozdělený po částech.

Pro citaci a právní účely platí vždy původní zdroj, ne přepis.

### Vydavatelé

| Vydavatel | Souborů | Slov |
| --- | ---: | ---: |
| KRIT — Krizový informační tým Ministerstva vnitra | 37 | ~40 000 |
| Zákon č. 359/1999 Sb., o sociálně-právní ochraně dětí | 14 | ~50 000 |
| MŠMT (ve spolupráci s MV, Policejním prezidiem ČR a MV – GŘ HZS) | 13 | ~19 000 |
| Krajské ředitelství policie hl. m. Prahy — Měkké cíle | 12 | ~15 000 |
| MPSV — Odbor ochrany práv dětí | 1 | ~2 500 |
| doc. PhDr. Barbora Vegrichtová, Ph.D., MBA a kol. | 1 | ~7 500 |

Data pokrývají několik odlišných pohledů na stejný problém, a v tom je jejich
cena: **MŠMT** říká, co má škola mít zpracované a co je závazné. **Policie**
říká, co má člověk v tu chvíli udělat. **KRIT** řeší, co a jak komunikovat —
a přináší i karty pro starosty k desítkám typů mimořádných událostí. **MPSV
a zákon 359/1999** pokrývají, komu se případ předává a za jakých podmínek.

---

## 2. Jak jsou uspořádaná

Ne podle vydavatele, ale **podle fáze, kterou dokument řeší**. Ředitel v krizi
nehledá „přílohu č. 7", hledá „co teď". Jedna fáze = jedna podsložka.

| Složka | Fáze | Souborů | Slov |
| --- | --- | ---: | ---: |
| [`01-ramec-a-legislativa/`](../data/01-ramec-a-legislativa/) | Co musíme mít a jak se to jmenuje | 26 | 64 600 |
| [`02-prevence-a-priprava/`](../data/02-prevence-a-priprava/) | Dokud se nic neděje | 9 | 15 900 |
| [`03-krizova-reakce/`](../data/03-krizova-reakce/) | První minuty a hodiny | 35 | 41 100 |
| [`04-po-krizi-a-navrat/`](../data/04-po-krizi-a-navrat/) | Stabilizace, evidence, předání | 8 | 5 300 |

Dvě složky mají vnořené podsložky, aby velké celky nepřeválcovaly zbytek:
[`zakon-359-1999/`](../data/01-ramec-a-legislativa/zakon-359-1999/) (14 souborů,
50 000 slov) a
[`krit-karty-pro-starosty/`](../data/03-krizova-reakce/krit-karty-pro-starosty/)
(20 karet k typům mimořádných událostí).

Bez textu zákona, který je objemem výjimečný, vypadá rozložení takto:
rámec ~14 500, prevence ~15 900, krize ~41 100, po krizi ~5 300 slov.

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

---

## 4. Co s tím dál

Korpus má dnes zhruba **228 000 tokenů**. To je pořád hluboko pod kontextovým
oknem, ale **už je to moc na to, aby se celý vkládal do každého promptu** —
zvlášť text zákona (~90 000 tokenů) je potřeba jen občas. Návrh proto počítá
s vložením zvolené fáze a **dočítáním velkých dokumentů na vyžádání**; podrobně
v [`navrh-aplikace.md`](navrh-aplikace.md).

Návrh, jak z toho udělat použitelný nástroj pro ředitele, je
v [`navrh-aplikace.md`](navrh-aplikace.md).
