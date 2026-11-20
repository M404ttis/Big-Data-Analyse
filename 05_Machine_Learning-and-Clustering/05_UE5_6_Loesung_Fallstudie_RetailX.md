# Tag 5 (Modul 3), Fallstudie: Kundensegmentierung bei RetailX

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI) | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** (1) **Merkmalswahl** prüfen, (2) jeden Cluster **ablesen und benennen**, (3) entscheiden, welche Cluster **eigene Segmente** werden, (4) **Maßnahmen** je Segment ableiten, (5) **Risiken** bewerten (z. B. falsche Einordnung).

**Dazu:** `05_UE5_6_Datenanalyse_RetailX.ipynb` rechnet alles auf den 600 Kunden der CSV nach.

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Das Unternehmen

| Thema | Angabe |
|---|---|
| Firma | RetailX GmbH, Händler für Wohnaccessoires, 85 Filialen und Webshop, 1.400 Mitarbeitende |
| Kunden | 620.000 aktive Karten (Kauf in den letzten 24 Monaten), weitere 280.000 inaktiv. Zielgruppen bisher nur nach Alter und Region |
| Umsatz | mit Kundenkarte 142 Mio. € = 63 % des Gesamtumsatzes |
| Kassendaten | alle Bons seit 2021, ca. 41 Mio. Onlinebestellungen im Shopsystem, nur per E-Mail-Adresse verknüpft |
| Einwilligung | Werbung per E-Mail bei 58 % der Karteninhaber erlaubt, 95.000 nutzen die App |
| Marketing | Gleicher Newsletter und gleiche Rabatte für alle. Öffnungsrate von 24 % (2023) auf 13 % gefallen. Jede 2. Bestellung nutzt einen 15-%-Code |
| Problem | Marketingbudget 9 Mio. € wirkt kaum messbar, viele Kunden kaufen nur einmal |
| Rahmen | Budget für das Projekt 600.000 €. Ergebnisse sollen im Weihnachtsgeschäft wirken, Kampagnen müssen bis Mitte September stehen |
| Team | 6 Personen im Kundenmarketing, 1 Datenanalystin seit 3 Monaten im Haus |
| Sonstiges | Nov/Dez bringen 31 % des Jahresumsatzes. 12 Filialen werden modernisiert, 3 geschlossen. Im Oktober startet eine Eigenmarke für Kerzen und Raumdüfte |

### Marketingbudget 9 Mio. €

| Posten | Prospekte | Rabattaktionen | Online-Werbung | Newsletter & App |
|---|---:|---:|---:|---:|
| Mio. € | 4,1 | 2,3 | 1,6 | 1,0 |

### Welche Merkmale vorliegen

| Merkmal | Beschreibung | Qualität |
|---|---|---|
| Kaufhäufigkeit | Einkäufe pro Jahr, online und in der Filiale | gut |
| Durchschnittsbon | Ausgabe pro Einkauf | gut |
| Rabattanteil | Anteil der Käufe mit Gutschein oder Aktion | gut |
| Letzter Kauf | Tage seit dem letzten Einkauf | gut |
| Warengruppen | z. B. Deko, Textil, Küche, Saisonware | mittel, teils grob |
| Kanal | Anteil der Onlinekäufe | lückenhaft vor 2023 |
| Alter | aus dem Kartenantrag, freiwillig | bei 38 % leer |
| Wohnort | Postleitzahl aus dem Kartenantrag | gut |

### So hat die Analystin gerechnet

| Thema | Angabe |
|---|---|
| Merkmale | Käufe pro Jahr, Ø Bon, Rabattanteil, Tage seit letztem Kauf |
| Skala | alle vier vorher auf eine gemeinsame Skala gebracht |
| Verfahren | k-Means, gerechnet für k = 1 bis 8, gewählt: k = 5 |
| Grundlage | Stichprobe von 600 aktiven Kunden (CSV-Datei) |

### Ergebnis: fünf Cluster, Durchschnitt je Kunde

| Cluster | Kunden | Käufe pro Jahr | Ø Bon | Rabattanteil | Tage seit Kauf | Umsatzanteil |
|---|---:|---:|---:|---:|---:|---:|
| C1 | 27 % | 5,4 | 36 € | 71 % | 47 | 23 % |
| C2 | 30 % | 1,5 | 43 € | 30 % | 328 | 8 % |
| C3 | 15 % | 13,0 | 55 € | 13 % | 20 | 48 % |
| C4 | 9 % | 1,9 | 152 € | 15 % | 125 | 11 % |
| C5 | 19 % | 2,5 | 45 € | 31 % | 146 | 10 % |
| Alle | 100 % | 4,6 | 53 € | 37 % | 153 | 100 % |

### Nicht im Modell, nur zur Beschreibung

| Cluster | Häufigste Warengruppe | Anteil online | Ø Kunde seit | Ø Alter |
|---|---|---:|---:|---:|
| C1 | Saisonware (48 %) | 21 % | 2021 | 46 |
| C2 | Saisonware (40 %) | 15 % | 2019 | 46 |
| C3 | Deko (41 %) | 36 % | 2019 | 45 |
| C4 | Textil (69 %) | 46 % | 2020 | 48 |
| C5 | Saisonware (37 %) | 22 % | 2020 | 44 |
| Alle | Saisonware (34 %) | 24 % | 2020 | 46 |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Gesamtumsatz | 142 Mio. € / 63 % | ca. 225 Mio. € |
> | Umsatz je aktiver Karte | 142 Mio. € / 620.000 | 229 € |
> | Kontrolle: Käufe mal Bon (Alle) | 4,6 × 53 € | 244 € |
> | Marketing je aktiver Karte | 9 Mio. € / 620.000 | 14,52 € |
> | Marketing in % des Gesamtumsatzes | 9 / 225 | 4,0 % |
> | Anteil der Posten am Marketing | 4,1 / 2,3 / 1,6 / 1,0 von 9,0 | 46 % / 26 % / 18 % / 11 % |
> | Karten gesamt | 620.000 + 280.000 | 900.000 (69 % aktiv) |
> | Per E-Mail erreichbar | 620.000 × 58 % | ca. 360.000 |
> | App-Nutzer | 95.000 / 620.000 | 15 % |
> | Öffnungsrate | 13 / 24 − 1 | −46 % |
> | Kunden je Cluster *(Annahme: Stichprobe repräsentativ)* | 620.000 × 27 / 30 / 15 / 9 / 19 % | 167.400 / 186.000 / 93.000 / 55.800 / 117.800 |
> | Umsatz je Cluster *(Annahme: s. o.)* | 142 Mio. € × 23 / 8 / 48 / 11 / 10 % | 32,7 / 11,4 / 68,2 / 15,6 / 14,2 Mio. € |
> | Umsatz je Kunde und Cluster | Umsatz / Kunden | C1 195 €, C2 61 €, C3 733 €, C4 280 €, C5 121 € |
> | Umsatzanteil geteilt durch Kundenanteil | 23/27, 8/30, 48/15, 11/9, 10/19 | 0,85 / 0,27 / 3,2 / 1,2 / 0,53 |
> | Mehrfachkäufer-Hinweis: C2 plus C5 | 30 % + 19 % der Kunden, 8 % + 10 % des Umsatzes | 49 % der Kunden, 18 % des Umsatzes |
> | C3 plus C1 | 15 % + 27 % der Kunden, 48 % + 23 % des Umsatzes | 42 % der Kunden, 71 % des Umsatzes |
> | Ellbogen *(Index, k = 1 entspricht 100, aus der CSV gerechnet)* | k = 2 bis 8 | 64 / 42 / 21 / 16 / 14 / 12 / 11 |
> | Silhouette *(aus der CSV gerechnet)* | k = 2 bis 8 | 0,39 / 0,46 / **0,57** / 0,47 / 0,44 / 0,43 / 0,41 |
> | Korrelation Käufe und Tage seit Kauf *(CSV)* | r | −0,65 |
> | Alter fehlt in der CSV | 229 von 600 | 38 % |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Hauptbefund:** C3 (15 % der Kunden) bringt 48 % des Umsatzes, C1 und C3 zusammen 71 %. C2 und C5 (49 % der Kunden) bringen nur 18 %.
> - **Cluster:** C1 Rabatt-Jäger, C2 Eingeschlafene, C3 Stammkunden, C4 Großbon-Käufer, C5 Mittelfeld.
> - **Zweifel an k = 5:** Ellbogen und Silhouette sprechen für **k = 4** (Silhouette 0,57 gegen 0,47). C2 und C5 trennt nur die Linie **234 Tage** seit dem letzten Kauf. Sonst sind sie fast gleich (Bon 43 und 45 €, Rabatt 30 und 31 %).
> - **Empfehlung:** vier Segmente: Stammkunden, Rabatt-Jäger, Großbon-Käufer, Gelegenheitskäufer (C2 plus C5, gesteuert über die Zeit seit dem letzten Kauf). Das Marketing mit 6 Personen kann realistisch 3 bis 4 Segmente bespielen.
> - **Merkmalswahl:** Käufe und Tage seit Kauf überlappen (r = −0,65). Online-Anteil ergänzen, Alter weglassen (38 % leer, hängt mit nichts zusammen). Warengruppe nur zur Beschreibung.
> - **Messen:** mit Kontrollgruppe. Ohne sie bleibt unklar, ob Maßnahmen wirken.

> [!NOTE]
> Alle Rechnungen stehen in Teil A und im Python-Check. Die Cluster-Tabelle der Folie lässt sich aus der CSV exakt nachrechnen. Hochrechnungen auf 620.000 Kunden setzen eine **repräsentative Stichprobe** voraus (Annahme). Namen, Deutungen und Maßnahmen sind **Hypothesen**, keine belegten Ursachen. Die Kosten der Maßnahmen sind in der Aufgabe nicht genannt und werden hier nicht geschätzt.

## Schritt 1 · Merkmalswahl prüfen

| Merkmal | Im Modell? | Ergänzen, weglassen, behalten? | Warum? |
|:---|:---|:---|:---|
| **Käufe pro Jahr** | ja | **behalten** | trägt am stärksten (C3: +2,0 Standardabweichungen). Überlappt mit „Tage seit Kauf“ (r = −0,65) |
| **Ø Bon** | ja | **behalten** | eigene Information (kaum Zusammenhang mit Käufen und Tagen), trennt C4 (+2,9) |
| **Rabattanteil** | ja | **behalten** | trennt C1 (+1,4) von C3 (−1,0), wichtig für die Rabattstrategie |
| **Tage seit letztem Kauf** | ja | **behalten, aber mit Vorsicht** | ein *Zustand* (ändert sich jeden Tag), kein Charakterzug. Ein Kunde wechselt allein durch Nichtkaufen den Cluster. Ohne dieses Merkmal ändern sich die Cluster deutlich (ARI 0,63 zur Analystin) |
| **Warengruppe** | nein | **nur beschreiben** | Text, nicht für k-Means geeignet. Hilft bei der Benennung (C4 = Textil 69 %) |
| **Online-Anteil** | nein | **ergänzen** | trennt C4 (46 %) und C3 (36 %) von C2 (15 %), wichtig für Kanalwahl. Lückenhaft vor 2023, daher prüfen. Mit Online-Anteil ARI 0,76 |
| **Alter** | nein | **weglassen** | fehlt bei 38 %, in allen Clustern ähnlich (44 bis 48), Korrelation mit allen Merkmalen ≈ 0 |
| **Wohnort (PLZ)** | nein | **für die Maßnahme ergänzen** | beschreibt nicht das Verhalten, aber nützlich für Filiale und Region (3 Schließungen, 12 Modernisierungen) |
| **Kunde seit** | nein | **nur beschreiben** | trennt kaum (2019 bis 2021). Als Modellmerkmal ändert es die Cluster (ARI 0,64) ohne klaren Gewinn |
| **Weitere Ideen** | nein | **ergänzen, wenn vorhanden** | Retouren, Marge je Kunde, Einwilligung E-Mail (58 %), App-Nutzung, Newsletter-Öffnung |

## Schritt 2 · Raster der Cluster

| Cluster | Was ihn unterscheidet | Name | Maßnahme | Risiko |
|:---|:---|:---|:---|:---|
| **C1** (27 %, 23 % Umsatz) | **Rabattanteil +1,4 Standardabweichungen (71 %)**, kleiner Bon (36 €, −0,5), recht oft (5,4), zuletzt vor 47 Tagen | **Rabatt-Jäger** | Rabatt nicht pauschal erhöhen, Anreize für höheren Bon (Staffel, Zugabe), Rabattquote testen. Newsletter mit Aktionen | Marge sinkt weiter, Abhängigkeit von Aktionen. Vorsicht: Teil dieser Kunden würde auch ohne Rabatt kaufen |
| **C2** (30 %, 8 % Umsatz) | **Lange her (328 Tage, +1,3)**, 1,5 Käufe, Online nur 15 % | **Eingeschlafene** | günstige Reaktivierung (E-Mail, nur bei Einwilligung), danach Kosten begrenzen | Werbekosten verpuffen, 38 % ohne Altersangabe und vermutlich teils ohne E-Mail-Einwilligung |
| **C3** (15 %, 48 % Umsatz) | **Käufe +2,0 (13,0)**, Rabatt −1,0 (13 %), zuletzt vor 20 Tagen, Deko, 36 % online | **Stammkunden** | Bindung statt Rabatt: Vorab-Zugang Eigenmarke (Kerzen, Raumdüfte), App-Vorteile, persönliche Ansprache | Als „Schnäppchenjäger“ behandelt ärgern sie sich. Zu viele Aktionen gewöhnen sie an Rabatt. Verlust trifft fast die Hälfte des Umsatzes |
| **C4** (9 %, 11 % Umsatz) | **Ø Bon 152 € (+2,9)**, 1,9 Käufe, Textil 69 %, 46 % online | **Großbon-Käufer (Textil)** | Online-Newsletter mit Textil und Wohnen, Kollektionen, kein Rabatt nötig (15 %) | kleine Gruppe (52 Kunden in der Stichprobe): Zufall möglich. Wenige Käufe, Muster unsicher |
| **C5** (19 %, 10 % Umsatz) | **fällt nirgends auf:** alle vier Merkmale leicht unter dem Durchschnitt (−0,5 bis 0) | **Mittelfeld** (noch nicht gebunden) | Zweitkauf-Anreiz, z. B. kleine Aufmerksamkeit nach dem ersten Kauf, nicht Rabatt | Cluster ohne klares Profil: Maßnahme trifft vieles gleichzeitig. Die Kunden rutschen nach C2, wenn sie nicht kaufen |

> [!NOTE]
> **Abstand zum Durchschnitt (Leitfrage der Folie):** Gemessen in Standardabweichungen vom Gesamtmittel. Faustregel (Annahme): ab ±0,5 merklich, ab ±1 stark. Danach prägen C1 den Rabatt, C2 die Zeit, C3 die Käufe und den fehlenden Rabatt, C4 den Bon. C5 prägt kein Merkmal.

## Schritt 3 · Eigene Segmente?

| Cluster | Eigenes Segment? | Warum? |
|:---|:---|:---|
| **C1** | **ja** | klares Verhalten (Rabatt), 27 % der Kunden, 23 % des Umsatzes, eigene Maßnahme |
| **C2** | **mit C5 zusammen** | ähnliches Profil wie C5, unterscheidet sich nur in der Tageszahl, wenig Umsatz (8 %) |
| **C3** | **ja, die wichtigste Gruppe** | 48 % des Umsatzes bei 15 % der Kunden |
| **C4** | **ja, aber klein** | klarer Bon, Textil, online. 9 % der Kunden, der Cluster muss stabil bleiben (Zufallsrisiko) |
| **C5** | **mit C2 zusammen** | kein klares Profil (alle Abstände zwischen −0,5 und 0). Bei k = 4 liegen 91 von 114 gemeinsam mit C2 |

- **Wie viele Segmente kann das Marketing bespielen?** Mit 6 Personen und einer neuen Analystin realistisch 3 bis 4. Deshalb vier Segmente (Stammkunden, Rabatt-Jäger, Großbon-Käufer, Gelegenheitskäufer). Innerhalb der Gelegenheitskäufer reicht eine Regel nach der Zeit seit dem letzten Kauf (z. B. über 234 Tage: Reaktivierung).
- **Folge für die Newsletter-Öffnungsrate:** Gleiche Ansprache für alle ist der Grund für die sinkende Rate. Vier Newsletter-Varianten statt eines.

## Schritt 4 · Risiken und Messung

| Risiko | Wie schlimm? | Gegenmittel |
|:---|:---|:---|
| **Falsche Einordnung** (treuer Kunde als Rabatt-Jäger behandelt) | mittel bis hoch: Verlust von Stammkunden (48 % des Umsatzes) | für C3 nie Rabattwerbung als Standard. Segment bei jeder Kampagne neu berechnen |
| **Cluster sind kein Naturgesetz:** k, Merkmale und Startwert verändern das Ergebnis | mittel | Stabilität prüfen (ARI), mit mehreren Merkmalssätzen vergleichen |
| **Tage seit Kauf ändert sich täglich** | mittel | Segment mit Datum speichern, regelmäßig neu rechnen |
| **Stichprobe 600 von 620.000** | mittel | ganze Kundenbasis auswerten, bevor Budget fließt |
| **Datenschutz und Einwilligung** (nur 58 % per E-Mail erreichbar) | hoch | nur mit Einwilligung anschreiben, Segmente ohne sensible Daten bilden, Alter nicht nutzen |
| **Kannibalisierung und Marge** | mittel | Rabatt-Jäger nicht mit mehr Rabatt „belohnen“ |
| **Zeitdruck** (Kampagnen bis Mitte September, Weihnachtsgeschäft) | hoch | mit C3, C1, C4 zuerst, kleine Pilotkampagne, keine Neuaufbauten |

**Wie messen, ob die Segmentierung wirkt?** Mit Kontrollgruppe (A/B-Test): Ein Teil der Kunden jedes Segments bekommt weiter den alten Newsletter. Verglichen werden Öffnungsrate (heute 13 %), Wiederkaufrate, Ø Bon, Rabattquote und Umsatz je Kunde.

## Python-Check

```python
# python3 -I check.py   (benötigt pandas, numpy, scikit-learn)
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

d = pd.read_csv("05_retailx_kunden_stichprobe.csv", sep=";", encoding="utf-8-sig").dropna(subset=["kunde"])
F = ["kaeufe_pro_jahr", "durchschnittsbon_eur", "rabattanteil_prozent", "tage_seit_letztem_kauf"]
Z = (d[F] - d[F].mean()) / d[F].std(ddof=0)
print(len(d), d.alter.isna().sum(), d[F].corr().iloc[0, 3])        # 600; 229; -0,65

for k in range(1, 9):
    km = KMeans(k, n_init=50, random_state=0).fit(Z)
    print(k, round(km.inertia_ / 2400 * 100, 1),
          round(silhouette_score(Z, km.labels_), 2) if k > 1 else "-")  # Index; Silhouette

d["c"] = KMeans(5, n_init=50, random_state=0).fit_predict(Z)
d["umsatz"] = d.kaeufe_pro_jahr * d.durchschnittsbon_eur
g = d.groupby("c").agg(n=("kunde", "count"), kaeufe=("kaeufe_pro_jahr", "mean"),
                       bon=("durchschnittsbon_eur", "mean"), rabatt=("rabattanteil_prozent", "mean"),
                       tage=("tage_seit_letztem_kauf", "mean"), umsatz=("umsatz", "sum"))
g["kunden%"] = g.n / 6
g["umsatz%"] = g.umsatz / g.umsatz.sum() * 100
print(g.round(1))                                                  # entspricht der Folie

print(142 / 0.63, 142e6 / 620000, 9e6 / 620000, 620000 * 0.58)    # 225,4; 229; 14,5; 359.600
print([round(142e6 * a / (620000 * b)) for a, b in
       [(.23, .27), (.08, .30), (.48, .15), (.11, .09), (.10, .19)]])  # 195, 61, 733, 280, 121
```

Ergebnis: 600 Kunden, Alter fehlt bei 229 (38 %). Ellbogen-Index 64 / 42 / 21 / 16 / 14 / 12 / 11 für k = 2 bis 8, Silhouette 0,39 / 0,46 / 0,57 / 0,47 / 0,44 / 0,43 / 0,41. Die Cluster stimmen mit der Folie überein (C3: 15 %, 13,0 Käufe, 48 % Umsatz). C2 und C5 trennt die Grenze 234 Tage. Umsatz je Kunde und Cluster: 195 / 61 / 733 / 280 / 121 €.
