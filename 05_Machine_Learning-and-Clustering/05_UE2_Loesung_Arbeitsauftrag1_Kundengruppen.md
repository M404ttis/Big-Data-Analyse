# Tag 5 (Modul 3), Arbeitsauftrag 1: Kundengruppen beim Garten- und Heimwerkerfachhändler

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI) | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Ohne Algorithmus, nur mit dem Blick auf die Daten: (1) **Gruppen ähnlicher Kunden** bilden, (2) jede Gruppe **beschreiben und benennen**, (3) die **entscheidenden Unterschiede** benennen.

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Der Händler

| Thema | Angabe |
|---|---|
| Firma | Fachhändler für Garten- und Heimwerkerbedarf, zwei Filialen (Nord, Süd) |
| Kunden | 8.400 Kunden mit Kundenkarte (freiwillig). Kartenkunden bringen 61 % des Umsatzes |
| Bon | Ø Bon über alle Kunden: 68 € |
| Sortiment | Pflanzen, Werkzeug, Baustoffe, Gartenmöbel. Teuerste Artikel: Rasenmäher und Gartenhäuser |
| Rechnung | Kauf auf Rechnung gibt es **nur für Gewerbekunden** (Gärtner, Handwerker) |
| Sonstiges | Filiale Süd wird im Herbst umgebaut, der Inhaber plant ein Gartencafé |

### Auszug aus dem Kundenkartensystem (12 Kunden)

| Kunde | Alter | Käufe/Jahr | Umsatz/Jahr | Kunde seit | Filiale | Zahlart |
|---|---:|---:|---:|---:|---|---|
| K01 | 24 | 26 | 640 € | 2023 | Nord | Karte |
| K02 | 58 | 3 | 1.950 € | 2009 | Süd | bar |
| K03 | 41 | 18 | 2.300 € | 2016 | Nord | Rechnung |
| K04 | 29 | 22 | 590 € | 2022 | Süd | Karte |
| K05 | 63 | 2 | 2.400 € | 2008 | Nord | Karte |
| K06 | 35 | 4 | 210 € | 2020 | Nord | bar |
| K07 | 45 | 20 | 2.650 € | 2014 | Süd | Rechnung |
| K08 | 22 | 30 | 710 € | 2024 | Nord | Karte |
| K09 | 52 | 2 | 180 € | 2021 | Süd | bar |
| K10 | 61 | 4 | 2.100 € | 2011 | Nord | Karte |
| K11 | 38 | 16 | 1.980 € | 2018 | Süd | Rechnung |
| K12 | 47 | 3 | 240 € | 2019 | Nord | Karte |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Summe Umsatz im Auszug | 12 Kunden | 15.950 € |
> | Summe Käufe im Auszug | 12 Kunden | 150 |
> | Ø Umsatz je Kauf im Auszug | 15.950 € / 150 | 106 € (Ø Bon laut Händler: 68 €) |
> | Ø Umsatz je Kunde | 15.950 € / 12 | 1.329 € |
> | Ø Käufe je Kunde | 150 / 12 | 12,5 |
> | Spanne Alter | min bis max | 22 bis 63 Jahre |
> | Spanne Käufe/Jahr | min bis max | 2 bis 30 |
> | Spanne Umsatz/Jahr | min bis max | 180 € bis 2.650 € |
> | Kunden mit Zahlart Rechnung | K03, K07, K11 | 3 von 12 |
> | Anteil des Auszugs an allen Kartenkunden | 12 / 8.400 | 0,14 % |
>
> **Umsatz je Kauf nach Kunde** (Umsatz/Jahr geteilt durch Käufe/Jahr)
>
> | Kunde | K01 | K02 | K03 | K04 | K05 | K06 | K07 | K08 | K09 | K10 | K11 | K12 |
> |---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
> | € | 25 | 650 | 128 | 27 | 1.200 | 52 | 133 | 24 | 90 | 525 | 124 | 80 |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Vier Gruppen à drei Kunden**, gebildet über **Käufe pro Jahr** und **Umsatz pro Jahr** (zusammen: Umsatz je Kauf): **Gruppe 1** häufig, kleiner Bon (K01, K04, K08), **Gruppe 2** häufig, mittlerer Bon, alle auf Rechnung (K03, K07, K11), **Gruppe 3** selten, sehr großer Bon (K02, K05, K10), **Gruppe 4** selten, kleiner Bon (K06, K09, K12).
> - **Umsatz:** Gruppe 2 (43,5 %) und Gruppe 3 (40,4 %) bringen **84 % des Umsatzes** im Auszug, Gruppe 1 nur 12 % bei 52 % der Käufe, Gruppe 4 nur 4 %.
> - **Entscheidend:** Die Kombination aus Käufe und Umsatz. Einzeln trennt jedes der beiden Merkmale nur 5 von 6 Gruppenpaaren, **Umsatz je Kauf** trennt alle 6. Die **Zahlart Rechnung** erkennt Gruppe 2 sofort.
> - **Alter und Kunde seit:** laufen mit (Gruppe 1 jung und neu, Gruppe 3 alt und langjährig). Kunde seit trennt alle 6 Paare, Alter 5 von 6 (Gruppe 2 und 4 überlappen). Das sind Begleitmerkmale, keine Ursachen. **Filiale** trennt nichts.
> - **Vorsicht:** 12 von 8.400 Kunden, die Verteilung ist nicht repräsentativ (Ø Bon 106 € gegen 68 € laut Händler). Es sind **Hypothesen**, die die ganze Kundenkartendatei prüfen muss.

> [!NOTE]
> Alle Rechnungen stehen im Python-Check. Die Gruppen ergeben sich aus dem Blick auf die Daten, die Namen und Deutungen sind **Hypothesen**. Der k-Means-Lauf im Python-Check dient nur zur Gegenprobe, die Aufgabe selbst verlangt keinen Algorithmus.

## Schritt 1 · Ergebnisraster

| Gruppe | Kunden | Beschreibung | Name |
|:---|:---|:---|:---|
| **1** | K01, K04, K08 | 22 bis 30 Käufe im Jahr, aber nur 590 bis 710 € Umsatz (ca. 25 € je Kauf). Jung (22 bis 29), erst seit 2022 bis 2024 Kunde, Zahlart Karte | **Laufkundschaft jung** (Kleinkäufer: Pflanzen, Kleinteile) |
| **2** | K03, K07, K11 | 16 bis 20 Käufe, 1.980 bis 2.650 € Umsatz (ca. 125 bis 133 € je Kauf). Mittleres Alter (38 bis 45), Kunde seit 2014 bis 2018, **alle auf Rechnung** | **Profis / Gewerbekunden** |
| **3** | K02, K05, K10 | nur 2 bis 4 Käufe, aber 1.950 bis 2.400 € Umsatz (525 bis 1.200 € je Kauf). Alt (58 bis 63), Kunde seit 2008 bis 2011, Zahlung bar oder Karte | **Anschaffer / Stammkunden mit Großkäufen** (Rasenmäher, Gartenhaus) |
| **4** | K06, K09, K12 | 2 bis 4 Käufe, nur 180 bis 240 € Umsatz (52 bis 90 € je Kauf). Alter 35 bis 52 | **Gelegenheitskäufer** (Randkunden, wenig Bindung) |

### Gruppen im Zahlenvergleich

| Gruppe | Kunden | Ø Alter | Ø Käufe | Ø Umsatz | Umsatz Summe | Anteil Umsatz | Anteil Käufe | Umsatz je Kauf |
|:---|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 Laufkundschaft jung | 3 | 25,0 | 26 | 647 € | 1.940 € | 12,2 % | 52,0 % | 25 € |
| 2 Profis | 3 | 41,3 | 18 | 2.310 € | 6.930 € | 43,5 % | 36,0 % | 128 € |
| 3 Anschaffer | 3 | 60,7 | 3 | 2.150 € | 6.450 € | 40,4 % | 6,0 % | 717 € |
| 4 Gelegenheitskäufer | 3 | 44,7 | 3 | 210 € | 630 € | 3,9 % | 6,0 % | 70 € |

## Schritt 2 · Entscheidende Unterschiede

| Merkmal | Trennt es die Gruppen? | Warum? |
|:---|:---|:---|
| **Käufe pro Jahr** | **fast:** trennt 5 von 6 Gruppenpaaren | nur Gruppe 3 und 4 überlappen (beide 2 bis 4 Käufe) |
| **Umsatz pro Jahr** | **fast:** trennt 5 von 6 Gruppenpaaren | nur Gruppe 2 und 3 überlappen (beide ca. 2.000 bis 2.650 €) |
| **Umsatz je Kauf** | **ja, trennt alle 6 Paare:** 25 / 70 / 128 / 717 € | verbindet beide Merkmale, jede Gruppe liegt in einem eigenen Bereich |
| **Alter** | **fast:** trennt 5 von 6 Paaren (Gruppe 1 jung, Gruppe 3 alt) | Gruppe 2 (38 bis 45) und Gruppe 4 (35 bis 52) überlappen, Alter allein genügt nicht |
| **Kunde seit** | **ja, trennt alle 6 Paare:** Gruppe 1 2022 bis 24, Gruppe 4 2019 bis 21, Gruppe 2 2014 bis 18, Gruppe 3 2008 bis 11 | beschreibt die Kundendauer, ist eher Begleitmerkmal als Ursache. Bei nur 12 Kunden kann es Zufall sein |
| **Zahlart** | **nur für Gruppe 2:** alle drei auf Rechnung, sonst niemand | Rechnung nur für Gewerbekunden, bestätigt die Deutung als Profis |
| **Filiale** | **nein:** jede Gruppe enthält Nord und Süd | kein erkennbarer Zusammenhang |

> [!NOTE]
> **Deutung und Folgen (Hypothesen):**
> **Gruppe 2 und 3** tragen 84 % des Umsatzes und gehören gepflegt (Gewerbekonditionen, Beratung bei Anschaffungen). **Gruppe 1** hat viele Käufe, aber kleinen Bon: Chance für Zusatzverkäufe (Gartencafé, Aktionen). **Gruppe 4** ist die Randgruppe: günstig anwerben, nicht kostspielig binden. Filiale spielt keine Rolle, der Umbau in Süd trifft alle Gruppen.

## Schritt 3 · Gesamtbild

- **Nicht schlussfolgern:** „Das Alter bestimmt die Gruppe“. Alter läuft nur mit (Korrelation), ob Gruppe 3 wegen des Alters große Käufe tätigt, zeigen die Daten nicht.
- **Zahlen mit Kontext:** 3 Kunden je Gruppe sind zu wenig für Anteile. 12 von 8.400 Kunden (0,14 %). Ø Bon 106 € im Auszug gegen 68 € laut Händler: der Auszug ist **keine Zufallsstichprobe**.
- **Plausibilität:** Gruppe 2 sind sehr wahrscheinlich Gewerbekunden (Rechnung gibt es nur für sie), Gruppe 3 passt zu den teuersten Artikeln (Rasenmäher, Gartenhäuser). Beide Deutungen sind Hypothesen, die der Händler bestätigen müsste.
- **Fehlt:** Warengruppe je Kauf, Datum der Käufe, Nicht-Kartenkunden (39 % des Umsatzes bleiben unsichtbar), Marge.

## Python-Check

```python
# python3 -I check.py   (benötigt pandas, scikit-learn)
import pandas as pd
from sklearn.cluster import KMeans

d = pd.read_csv("05_kundenkarte_auszug.csv", sep=";", encoding="utf-8-sig").dropna()
d["je_kauf"] = d.umsatz_pro_jahr_eur / d.kaeufe_pro_jahr
print(d.umsatz_pro_jahr_eur.sum(), d.kaeufe_pro_jahr.sum())          # 15950; 150
print(d.umsatz_pro_jahr_eur.sum() / d.kaeufe_pro_jahr.sum())         # 106,3

# Gruppen von Hand
gruppen = {1: ["K01", "K04", "K08"], 2: ["K03", "K07", "K11"],
           3: ["K02", "K05", "K10"], 4: ["K06", "K09", "K12"]}
for g, ids in gruppen.items():
    x = d[d.kunde.isin(ids)]
    print(g, x.alter.mean(), x.kaeufe_pro_jahr.mean(), x.umsatz_pro_jahr_eur.sum(),
          x.umsatz_pro_jahr_eur.sum() / d.umsatz_pro_jahr_eur.sum(),
          x.umsatz_pro_jahr_eur.sum() / x.kaeufe_pro_jahr.sum())

# Gegenprobe: k-Means mit k = 4, Merkmale standardisiert (z-Wert)
M = d[["alter", "kaeufe_pro_jahr", "umsatz_pro_jahr_eur"]].astype(float)
Z = (M - M.mean()) / M.std(ddof=0)
d["cluster"] = KMeans(4, n_init=50, random_state=0).fit_predict(Z)
print(d.groupby("cluster").kunde.apply(list))                        # dieselben vier Dreiergruppen

# ohne Standardisierung dominiert der Umsatz (Euro-Spanne gross, Alter klein)
d["roh"] = KMeans(4, n_init=50, random_state=0).fit_predict(M)
print(d.groupby("roh").kunde.apply(list))                            # K02/K10/K11 und K03/K05/K07 vermischt
```

Ergebnis: Die Handgruppen {K01, K04, K08}, {K03, K07, K11}, {K02, K05, K10}, {K06, K09, K12} entstehen auch bei k-Means mit k = 4 auf standardisierten Merkmalen (Silhouette 0,71). **Ohne Standardisierung** sind es andere Gruppen ({K02, K10, K11} und {K03, K05, K07} vermischt), weil die Euro-Spanne den Abstand dominiert. Das ist die praktische Lehre: Merkmale vor dem Clustern auf gleiche Skala bringen.
