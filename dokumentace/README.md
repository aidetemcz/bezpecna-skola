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

Ve složce [`data/`](../data/) je **28 přepisů** z pěti zdrojových dokumentů:
**150 stran, zhruba 37 000 slov.** Originály (PDF a jeden `.docx`) jsou
v [`zdrojova-data/`](../zdrojova-data/), převod dělá
[`scripts/pdf_na_md.py`](../scripts/pdf_na_md.py).

Přepis je **věrný, ne shrnutý**. Kontrolní porovnání slovní zásoby zdroje
a výstupu neukázalo u žádného souboru vypuštěný obsah. Pro citaci a právní
účely platí vždy původní PDF.

### Vydavatelé

| Vydavatel | Souborů |
| --- | --- |
| MŠMT (ve spolupráci s MV, Policejním prezidiem ČR a MV – GŘ HZS) | 13 |
| Krajské ředitelství policie hl. m. Prahy — pracovní skupina Měkké cíle | 12 |
| KRIT — Krizový informační tým Ministerstva vnitra | 1 |
| MPSV — Odbor ochrany práv dětí | 1 |
| doc. PhDr. Barbora Vegrichtová, Ph.D., MBA a kol. | 1 |

Data pokrývají tři odlišné pohledy na stejný problém, a v tom je jejich cena:
**MŠMT** říká, co má škola mít zpracované a co je závazné. **Policie** říká, co
má člověk v tu chvíli udělat. **KRIT a MPSV** řeší, co přijde potom —
komunikace a předání případu.

---

## 2. Jak jsou uspořádaná

Ne podle vydavatele, ale **podle fáze, kterou dokument řeší**. Ředitel v krizi
nehledá „přílohu č. 7", hledá „co teď". Jedna fáze = jedna podsložka.

| Složka | Fáze | Souborů | Stran | Slov |
| --- | --- | ---: | ---: | ---: |
| [`01-ramec-a-legislativa/`](../data/01-ramec-a-legislativa/) | Co musíme mít a jak se to jmenuje | 7 | 29 | 7 600 |
| [`02-prevence-a-priprava/`](../data/02-prevence-a-priprava/) | Dokud se nic neděje | 9 | 52 | 15 500 |
| [`03-krizova-reakce/`](../data/03-krizova-reakce/) | První minuty a hodiny | 6 | 52 | 11 300 |
| [`04-po-krizi-a-navrat/`](../data/04-po-krizi-a-navrat/) | Stabilizace, evidence, předání | 6 | 17 | 2 600 |

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
| `krit-akutni-komunikace-ve-skolnim-prostredi.md` | KRIT, MV | Krizová komunikace — vzorové formulace, pořadí adresátů |

### 04 — Po krizi a návrat

| Soubor | Zdroj | O čem to je |
| --- | --- | --- |
| `priloha-05-evidence-bezpecnostnich-incidentu.md` | MŠMT, příloha 5 | Proč a jak evidovat incidenty |
| `priloha-05-formular-zaznam-o-incidentu.md` | MŠMT, příloha 5 | Formulář záznamu (převedený z `.docx`) |
| `priloha-08-koordinacni-plan.md` | MŠMT, příloha 8 | Návrat do rutinního provozu |
| `amok-05-bezprostredne-po-utoku.md` | PČR, AMOK 5 | Stabilizace situace |
| `amok-06-zpet-do-bezneho-rezimu.md` | PČR, AMOK 6 | Obnova provozu a následná péče |
| `mpsv-metodicka-prirucka-pro-kuratory.md` | MPSV | Kurátor pro děti a mládež jako koordinátor případu |

---

## 4. Co s tím dál

Data jsou připravená k použití v promptu — celý korpus je zhruba **66 000
tokenů**, největší jednotlivá fáze kolem **28 000**. To znamená, že se dá vložit
deterministicky podle zvolené fáze, bez RAG a bez embeddingů; stejný přístup,
jaký používá [Katalog podpůrných opatření](https://github.com/aidetemcz/podpurna-opatreni).

Návrh, jak z toho udělat použitelný nástroj pro ředitele, je
v [`navrh-aplikace.md`](navrh-aplikace.md).
