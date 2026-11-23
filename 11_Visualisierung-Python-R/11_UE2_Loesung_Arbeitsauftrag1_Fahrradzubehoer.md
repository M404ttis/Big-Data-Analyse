# Tag 11 · UE 2 · Arbeitsauftrag 1: Fahrradzubehör, Fragen an die Tabelle

Aufgabe: Nicht programmieren, sondern wie eine Analystin denken. Welche Fragen lassen sich mit den Daten beantworten, welche Visualisierung passt, welche Erkenntnis ist zu erwarten?

## Teil A: Fakten und Rechnungen

Alle Zahlen in Tsd. €, Datenstand Rechnungen 2025 ohne Retouren.

**Plausibilität:** Die Zeilensummen stimmen (z. B. Nord 410 + 620 + 180 + 240 = 1.450). Gesamt 2025: **6.900**, Vorjahr **6.610**, also **+4,4 %**.

| Region | Gesamt | Vorjahr | Δ absolut | Δ % | Umsatz je Händler | Umsatz je Außendienst | Profi-Anteil |
|---|---|---|---|---|---|---|---|
| Nord | 1.450 | 1.390 | +60 | +4,3 % | 22,7 | 725 | 12,4 % |
| Süd | 1.890 | 1.640 | +250 | +15,2 % | 23,3 | 630 | 28,6 % |
| West | 1.400 | 1.520 | −120 | −7,9 % | 19,4 | 700 | 6,4 % |
| Ost | 830 | 810 | +20 | +2,5 % | 21,8 | 830 | 7,2 % |
| Mitte | 1.330 | 1.250 | +80 | +6,4 % | 24,2 | 665 | 16,5 % |

| Produktlinie | Umsatz | Anteil | Marge | Rohertrag | Anteil Rohertrag | Menge (Stück, ca.) |
|---|---|---|---|---|---|---|
| Einsteiger | 1.950 | 28,3 % | 22 % | 429 | 17,8 % | 39.800 |
| Standard | 2.700 | 39,1 % | 33 % | 891 | 37,0 % | 30.300 |
| Profi | 1.090 | 15,8 % | 41 % | 447 | 18,6 % | 5.800 |
| Ersatzteile | 1.160 | 16,8 % | 55 % | 638 | 26,5 % | 82.900 |
| **Gesamt** | **6.900** | 100 % | Ø 34,9 % | **2.405** | 100 % | |

Zur Profi-Frage:

- Der Profi-Rohertrag (447) liegt **über** dem der Einsteiger-Linie (429), obwohl sie 79 % mehr Umsatz macht.
- Fällt Profi weg, entfallen 447 von 2.405 Rohertrag (−18,6 %), der Umsatz sinkt um 15,8 %.
- Süd macht 49,5 % des gesamten Profi-Umsatzes (540 von 1.090), Süd + Nord zusammen 66 %.
- Ohne Profi hätte Süd nur 1.350 statt 1.890 (−29 %) und läge unter dem Vorjahr (1.640).

## Teil B: Ergebnisraster

| Fragestellung | Visualisierung | Erwartete Erkenntnis |
|---|---|---|
| **1. Wie hat sich der Umsatz je Region gegenüber dem Vorjahr verändert?** | Hantel-/Dumbbell-Diagramm (Vorjahr → 2025 je Region) oder Balken der Δ % mit Nulllinie, nach Δ sortiert | Süd wächst mit +15 % deutlich, Mitte +6 %, Nord +4 %, Ost +2 %, **West ist als einzige Region im Minus (−8 %)**. Das Gesamtplus von 4,4 % verdeckt diese Spreizung |
| **2. Wie viel trägt jede Region zum Gesamtumsatz bei?** | Horizontale Balken, nach Größe sortiert (kein Kreisdiagramm bei 5 Teilen mit ähnlicher Größe) | Süd (27 %) und Nord (21 %) sind die größten, Ost (12 %) die kleinste Region |
| **3. Wie setzt sich der Umsatz je Region aus den Produktlinien zusammen?** | Gestapelte Balken je Region, optional 100 %-Variante für den Mix | Süd ist profilastig (29 % Profi), West fast ohne Profi (6 %) und einsteigerlastig. Regionen haben unterschiedliche Sortimentsprofile |
| **4. Welche Produktlinie bringt wie viel Umsatz und wie viel Rohertrag?** | Gruppierte Balken Umsatz vs. Rohertrag je Linie (eine Achse in €, keine zweite Skala) | Standard ist der Motor (39 % Umsatz, 37 % Rohertrag). Ersatzteile haben 17 % Umsatz, aber 27 % Rohertrag. Einsteiger: viel Umsatz, wenig Ertrag |
| **5. Lohnt es sich, die Profi-Linie einzustellen?** | Balken Umsatz-Anteil vs. Rohertrag-Anteil je Linie, dazu Profi je Region (wo hängt sie dran?) | Profi ist ein kleiner, aber **ertragsstarker** Teil (18,6 % des Rohertrags, mehr als Einsteiger). Einstellen träfe v. a. Süd. Ohne weitere Daten (Kosten, Cross-Selling) eher nicht empfehlbar |
| **6. Wo ist der Vertrieb produktiv, wo gibt es Auffälligkeiten?** | Streudiagramm Händleranzahl vs. Umsatz je Region (5 Punkte, beschriftet) oder Balken Umsatz je Händler / je Außendienst | Je Händler liegen die Regionen eng (19–24), West fällt ab. Je Außendienst führt Ost (830) bei nur einer Person, seit Juli unbesetzt: Risiko für 2026 |
| **7. Wie stark ist der Rohertrag nach Region?** | Balken Rohertrag je Region, optional gestapelt nach Linie | Süd bringt 682 von 2.405 (28 %). West liegt mit 480 trotz fast gleichem Umsatz hinter Nord (501), weil es viele Einsteiger und kaum Profi verkauft. Der Produktmix bestimmt den Ertrag, nicht nur der Umsatz |
| **8. Wie ist der Produktmix je Region im Vergleich?** | Heatmap Region × Produktlinie (sequenziell, eine Farbe, Zahlen in den Zellen) | Auf einen Blick: Hotspots Süd/Profi (540) und Süd/Standard (710), kalte Zellen Ost/Profi (60) und West/Profi (90) |

## Teil C: Plenum-Fragen

**Welche Frage ist am spannendsten?** Die Profi-Frage (5), weil sie eine Entscheidung betrifft und ein Bauchgefühl ("Profi ist klein, also weg") durch die Rohertragsrechnung widerlegt wird.

**Welche Region und welche Linie fallen auf?**

- **Süd** wächst als einzige stark (+15 %), getragen von Profi (540).
- **West** schrumpft (−8 %). Der Verlust der Kette im März erklärt wohl den Rückgang (−120 gegenüber dem Vorjahr), die Daten selbst zeigen das aber nicht.
- **Ost** wirkt stabil, aber: Umsatz teilweise über den Nord-Großhändler gebucht (verzerrt Ost nach unten, Nord nach oben), Außendienst seit Juli unbesetzt.
- Linie: **Profi** (klein, aber ertragsstark und regional konzentriert) und **Ersatzteile** (kleiner Umsatz, hohe Marge).

**Welche Daten fehlen für eine Antwort?**

| Fehlende Daten | Wofür |
|---|---|
| Vorjahr **je Produktlinie** (nur Gesamt je Region vorhanden) | Trend der Profi-Linie, Wachstumstreiber in Süd |
| **Monats- bzw. Quartalswerte** | Zeitpunkt des Einbruchs in West (März?), Effekt Neuer Großhändler Nord (ab Mai), Saison, Hausmesse Süd |
| Ost-Umsatz **über den Nord-Großhändler** | Regionen fair vergleichen, sonst zählt der Umsatz in der falschen Region |
| **Kosten** (Vertrieb, Lager, Marketing, Fixkosten je Linie) | Marge ist nur Rohertrag, nicht Gewinn. Ohne Kosten keine Einstellungsentscheidung |
| **Verbundkäufe** (kaufen Profi-Kunden auch Ersatzteile/Zubehör?) | Cross-Selling-Effekt bei Profi-Einstellung |
| Retouren (Daten sind ohne Retouren) | Nettoumsatz, Qualität je Linie |
| Plan-/Zielwerte, Kundenzahl je Händler (Top-Händler-Konzentration) | Beurteilung, ob +4 % gut oder schlecht ist, Klumpenrisiko |
| Margen je Region (Marge hier nur je Linie) | Annahme: gleiche Marge in jeder Region. Die Rohertragsrechnung ist eine **Näherung** |

**Bewusst nicht verwendet:** Katalog-Redesign und Firmensitz seit 1987 in Kassel haben keinen Bezug zu den Fragen (Ablenkung). "Zentrallager und Werksverkauf in Kassel" in Mitte kann Mitte dagegen verzerren (Direktverkauf, kein Händlerumsatz), daher bei Mitte Vorsicht beim Vergleich je Händler.

## Teil D: Passende und unpassende Formen

| Aufgabe | Passend | Unpassend |
|---|---|---|
| Vergleich Region zu Vorjahr | Hantel, Δ-Balken mit Nulllinie | 3D-Säulen, Doppelachse |
| Anteile (Region, Linie) | Sortierte Balken, 100 %-Stapel | Kreis bei vielen ähnlichen Teilen |
| Region × Produkt | Gestapelt, Heatmap | 20 Einzelbalken in Regenbogenfarben |
| Umsatz vs. Rohertrag | Gruppierte Balken auf einer Achse | Zwei Y-Achsen |
| Zusammenhang Händler vs. Umsatz | Streudiagramm (aber nur 5 Punkte, nur Orientierung) | Aus fünf Punkten eine Trendlinie ableiten |

Hinweis zum Streudiagramm: Bei nur fünf Regionen ist eine Korrelation statistisch nicht belastbar. Als Beschriftungsgrafik taugt es, als Beweis nicht.

## Python-Kontrollrechnung (vollständig umgesetzt in `11_UE2_Loesung_Arbeitsauftrag1_Fahrradzubehoer.ipynb`)

```python
import pandas as pd

df = pd.DataFrame(
    {"Einsteiger": [410, 380, 520, 290, 350],
     "Standard":   [620, 710, 480, 330, 560],
     "Profi":      [180, 540,  90,  60, 220],
     "Ersatzteile":[240, 260, 310, 150, 200]},
    index=["Nord", "Süd", "West", "Ost", "Mitte"])
vorjahr = pd.Series([1390, 1640, 1520, 810, 1250], index=df.index)
marge = pd.Series({"Einsteiger": .22, "Standard": .33, "Profi": .41, "Ersatzteile": .55})

df["Gesamt"] = df.sum(axis=1)
print(df["Gesamt"].sum(), vorjahr.sum())                 # 6900 6610
print(((df["Gesamt"] / vorjahr - 1) * 100).round(1))     # Nord 4.3, Süd 15.2, West -7.9 ...
rohertrag = (df[marge.index] * marge).sum()
print(rohertrag.round(0), (rohertrag / rohertrag.sum()).round(3))
```
