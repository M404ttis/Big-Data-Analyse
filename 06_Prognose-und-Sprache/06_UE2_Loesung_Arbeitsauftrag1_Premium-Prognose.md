# Tag 6 (Modul 3), Arbeitsauftrag 1: Premium-Mitgliedschaft beim Outdoor-Händler

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI) | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Ohne Modell, nur mit eigenem Urteil, für vier neue Kunden (N1 bis N4): (1) **Kauft er Premium** (79 € im Jahr), ja oder nein? (2) **Wie viel Umsatz** bringt er im nächsten Jahr? (3) **Einschätzungen begründen.**

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Der Händler

| Thema | Angabe |
|---|---|
| Firma | Outdoor-Händler, drei Filialen und ein Onlineshop, Ø Bestellwert 96 € |
| Premium | 79 € im Jahr. Kostenloser Versand, 10 % Rabatt auf Bergsport, Reparaturservice für Zelte und Schuhe |
| Versand | Ohne Premium kostet jede Online-Bestellung 4,95 € |
| Kampagne | Im Frühjahr wirbt der Händler mit einem Kletter-Influencer |
| Sonstiges | Filiale Kempten wird erweitert, neue Kundenkarte aus Holz statt Plastik |

### Bisherige Kunden (Ergebnis bekannt)

| Kunde | Alter | Einkommen/Monat | Käufe in 12 Monaten | Kanal | Newsletter | Kunde seit | Premium gekauft? | Umsatz Folgejahr |
|---|---:|---:|---:|---|---|---:|---|---:|
| A | 34 | 3.200 € | 9 | online | ja | 2019 | ja | 1.150 € |
| B | 52 | 4.800 € | 2 | Filiale | ja | 2012 | nein | 310 € |
| C | 27 | 2.100 € | 11 | online | nein | 2022 | ja | 870 € |
| D | 45 | 5.500 € | 7 | online | ja | 2015 | ja | 1.640 € |
| E | 61 | 2.900 € | 1 | Filiale | nein | 2018 | nein | 120 € |
| F | 38 | 3.900 € | 4 | beides | ja | 2017 | nein | 520 € |
| G | 23 | 1.700 € | 6 | online | nein | 2024 | nein | 410 € |
| H | 49 | 4.200 € | 10 | beides | ja | 2016 | ja | 1.480 € |

### Neue Kunden (gesucht: Premium ja/nein, Umsatz Folgejahr)

| Kunde | Alter | Einkommen/Monat | Käufe in 12 Monaten | Kanal | Newsletter | Kunde seit |
|---|---:|---:|---:|---|---|---:|
| N1 | 31 | 2.800 € | 8 | online | ja | 2021 |
| N2 | 57 | 6.100 € | 3 | Filiale | nein | 2010 |
| N3 | 42 | 3.500 € | 6 | beides | ja | 2020 |
| N4 | 26 | 2.300 € | 12 | online | nein | 2023 |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Premium-Quote bisher | 4 von 8 (A, C, D, H) | 50 % |
> | Ø Käufe, Premium ja | (9 + 11 + 7 + 10) / 4 | 9,25 |
> | Ø Käufe, Premium nein | (2 + 1 + 4 + 6) / 4 | 3,25 |
> | Käufe: Spanne ja / nein | min bis max | 7 bis 11 / 1 bis 6 |
> | Ø Umsatz Folgejahr, Premium ja | (1.150 + 870 + 1.640 + 1.480) / 4 | 1.285 € |
> | Ø Umsatz Folgejahr, Premium nein | (310 + 120 + 520 + 410) / 4 | 340 € |
> | Umsatz Spanne: ja / nein | min bis max | 870 bis 1.640 € / 120 bis 520 € |
> | Versandkosten bei 9 Online-Bestellungen (Kunde A) | 9 × 4,95 € | 44,55 € |
> | Versandkosten bei 12 Online-Bestellungen (Kunde N4) | 12 × 4,95 € | 59,40 € |
> | Käufe nötig, bis Versand allein die 79 € deckt | 79 / 4,95 | 16 |
> | Einkommen: Spanne bisher | min bis max | 1.700 bis 5.500 € |
> | Einkommen N2 | liegt über dem bisherigen Maximum | 6.100 € |
> | Kunden mit Kanal "Filiale" | B, E (nein beide), N2 | 2 von 8 bisher |
>
> **Umsatz je Kauf nach bisherigem Kunden** (Umsatz Folgejahr geteilt durch Käufe)
>
> | Kunde | A | B | C | D | E | F | G | H |
> |---|---:|---:|---:|---:|---:|---:|---:|---:|
> | € | 128 | 155 | 79 | 234 | 120 | 130 | 68 | 148 |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Premium:** N1 **ja**, N4 **ja** (sicher), N2 **nein** (ziemlich sicher), N3 **unsicher, Tendenz nein**.
> - **Umsatz Folgejahr (Schätzung, Spanne):** N1 **ca. 1.000 €**, N2 **ca. 450 €**, N3 **ca. 700 €**, N4 **ca. 1.000 €**, jeweils **± 400 €**. Methode: **einfache lineare Regression** (Umsatz aus Käufen), bei N3 und N4 von Hand angepasst.
> - **Entscheidendes Merkmal: Käufe in 12 Monaten.** Alle Premium-Käufer hatten 7 oder mehr Käufe, alle anderen 6 oder weniger. Die Grenze liegt genau zwischen 6 und 7, N3 sitzt mit 6 Käufen direkt darunter.
> - **Umsatz** folgt ebenfalls den Käufen (Ø 1.285 € bei Premium, 340 € ohne). Das **Einkommen** hilft bei der Höhe nur bedingt, N2 liegt mit 6.100 € über allen bekannten Fällen.
> - **Vorsicht:** acht Vergleichskunden. Die Spannen sind groß, jede Zahl ist eine Schätzung. Der Umsatz steht **nach** dem Premium-Kauf, die Mitgliedschaft kann ihn selbst erhöhen.

> [!NOTE]
> **Annahmen:** (1) Die neuen Kunden verhalten sich wie die acht bisherigen. (2) Der Umsatz ist der gesamte Umsatz des Kunden im Folgejahr, nicht nur Premium-Aufschläge. (3) Der Zusammenhang zwischen Käufen und Umsatz ist annähernd eine Gerade. (4) Die Spanne ± 400 € ist die Streuung der acht bekannten Kunden um die Gerade, bei so wenigen Fällen eine grobe Größe. Die Rechnungen stehen im Python-Check, die Grafiken im Notebook.

## Schritt 1 · Premium: ja oder nein?

| Kunde | Premium? | Wie sicher? | Entscheidendes Merkmal |
|:---|:---|:---|:---|
| **N1** (31 J., 2.800 €, 8 Käufe, online) | **ja** | ziemlich sicher | 8 Käufe liegen über der Grenze (7). Online, Newsletter: gleiches Profil wie A (34 J., 9 Käufe, online, Newsletter, ja) |
| **N2** (57 J., 6.100 €, 3 Käufe, Filiale) | **nein** | ziemlich sicher | 3 Käufe, nur Filiale. Der Versandvorteil greift nicht, gleiches Profil wie B (2 Käufe, Filiale, nein). Das hohe Einkommen ändert nichts: D (5.500 €) kauft nur mit 7 Käufen |
| **N3** (42 J., 3.500 €, 6 Käufe, beides) | **nein, unsicher** | Münzwurf mit leichter Tendenz zu nein | 6 Käufe liegen genau an der Grenze. G (6 Käufe) kaufte nicht, D (7 Käufe) kaufte. Kanal "beides" kommt in beiden Gruppen vor (H ja, F nein) |
| **N4** (26 J., 2.300 €, 12 Käufe, online) | **ja** | sicher | 12 Käufe, mehr als jeder bisherige Kunde. Fast Zwilling von C (27 J., 2.100 €, 11 Käufe, online, ja) |

## Schritt 2 · Umsatz im nächsten Jahr

**Methode:** einfache lineare Regression. Durch die acht bekannten Kunden wird die Gerade gelegt, die die Abstände (zum Quadrat) am kleinsten macht. Mittelwerte: 6,25 Käufe und 812,50 € Umsatz, daraus **Umsatz ≈ 102 € + 114 € × Käufe**. Jeder zusätzliche Kauf geht also mit rund 114 € mehr Umsatz einher.

| Kunde | Käufe | Gerade liefert | Meine Anpassung von Hand | Schätzung | Spanne (± 400 €) |
|:---|---:|---:|:---|---:|:---|
| **N1** | 8 | 102 + 114 × 8 = **1.011 €** | keine, nur gerundet | **ca. 1.000 €** | 600 bis 1.400 € |
| **N2** | 3 | 102 + 114 × 3 = **443 €** | keine, nur gerundet. Einkommen 6.100 € liegt über allem Bekannten, die Gerade kennt es nicht | **ca. 450 €** | 50 bis 850 € |
| **N3** | 6 | 102 + 114 × 6 = **784 €** | **minus ca. 85 €**, weil ich bei Premium eher auf nein tippe (G mit 6 Käufen: 410 €) | **ca. 700 €** | 300 bis 1.100 € |
| **N4** | 12 | 102 + 114 × 12 = **1.466 €** | **minus ca. 470 €**: der nächste Fall C (11 Käufe, 2.100 € Einkommen) machte nur 870 €. 870 € + ein Kauf (114 €) ≈ 985 € | **ca. 1.000 €** | 600 bis 1.400 € |

> [!NOTE]
> **Was Rechnung ist und was Urteil:** Die Spalte "Gerade liefert" ist reine Rechnung. Die Spalte "Anpassung von Hand" ist mein Urteil und nicht aus den Daten berechnet (bei N4 ist es sogar der größte Schritt). Die Spanne ± 400 € ist die Streuung der acht Kunden um die Gerade (rund 407 €). Sie ist so groß wie die Schätzungen selbst bei N2: bei acht Kunden ist jede dieser Zahlen sehr grob. Das Einkommen steckt nicht in der Geraden, es erklärt aber Abweichungen (Kunde D: 5.500 €, 7 Käufe, 1.640 €; Kunde C: 2.100 €, 11 Käufe, 870 €).

## Schritt 3 · Begründung: welche Merkmale zählen?

| Merkmal | Entscheidend, mitlaufend oder ignoriert? | Warum? |
|:---|:---|:---|
| **Käufe in 12 Monaten** | **entscheidend** | trennt Premium ja/nein ohne Überlappung (7 bis 11 gegen 1 bis 6). Korrelation mit Umsatz 0,74 |
| **Einkommen** | **nebensächlich** für ja/nein, **Hilfsmerkmal** für den Betrag | bei Premium kein klares Muster (C: 2.100 € ja, F: 3.900 € nein). Beim Umsatz erklärt es Abweichungen: D (5.500 €) gibt 1.640 € aus, C (2.100 €) bei mehr Käufen nur 870 €. N2 liegt über dem bekannten Bereich, dort ist jede Aussage Extrapolation |
| **Alter** | **mitlaufend** | läuft mit den Käufen, die Jüngeren kaufen hier häufiger (Korrelation Alter und Käufe: −0,58). Allein sagt Alter nichts (G: 23 J., nein; C: 27 J., ja). Der Zusammenhang läuft über die Käufe, nicht über das Alter selbst |
| **Kanal** | **plausibel, aber schwach belegt** | Die beiden bisherigen Filialkunden (B, E) kauften kein Premium, das passt zum Versandvorteil, der nur online greift. Nur zwei Fälle, also kein Beweis |
| **Newsletter** | **ignoriert** | keine Trennung: bei den Premium-Käufern 3 von 4 mit Newsletter, bei den übrigen 2 von 4. Bei 8 Fällen ist das Zufall |
| **Kunde seit** | **ignoriert** | kein Muster: langjährig (D, 2015) wie neu (C, 2022) kaufen Premium, wie langjährig (B, 2012) wie neu (G, 2024) nicht |
| **Kampagne, Kempten, Holzkarte** | **ignoriert** | kein Bezug zum Kaufverhalten der acht Kunden. Die Kampagne könnte Neukunden ändern, dazu gibt es keine Daten. Prognosen setzen voraus, dass die Zukunft der Vergangenheit ähnelt |

> [!NOTE]
> **Was ich mir merken würde (Hypothesen):**
> - Ja/nein war leichter als der Betrag: die Grenze bei 7 Käufen ist scharf, der Betrag streut stark (bei den Premium-Käufern mit 7 bis 11 Käufen zwischen 870 und 1.640 €).
> - **Warum kaufen die Häufigkäufer Premium?** Der Gratisversand allein rechnet sich selten (A: 44,55 € Versand gegen 79 € Beitrag). Also spielen vermutlich Rabatt und Reparaturservice mit, oder sie sind einfach treue Kunden. Das erlauben die Daten nicht zu entscheiden.
> - **Der Umsatz steht nach dem Premium-Kauf.** Der Unterschied 1.285 € gegen 340 € ist also nicht nur Wirkung der Käufe vorher, die Mitgliedschaft selbst (10 % Rabatt, kein Versand) kann Käufe auslösen. Wer daraus ableitet "Premium bringt 945 € mehr Umsatz", verwechselt Korrelation und Ursache.

## Python-Check

```python
# python3 -I check.py   (benötigt numpy, pandas)
import numpy as np
import pandas as pd

d = pd.DataFrame({
    "kunde":   list("ABCDEFGH"),
    "alter":   [34, 52, 27, 45, 61, 38, 23, 49],
    "eink":    [3200, 4800, 2100, 5500, 2900, 3900, 1700, 4200],
    "kaeufe":  [9, 2, 11, 7, 1, 4, 6, 10],
    "premium": [1, 0, 1, 1, 0, 0, 0, 1],
    "umsatz":  [1150, 310, 870, 1640, 120, 520, 410, 1480],
})
n = pd.DataFrame({"kunde": ["N1", "N2", "N3", "N4"], "alter": [31, 57, 42, 26],
                  "eink": [2800, 6100, 3500, 2300], "kaeufe": [8, 3, 6, 12]})

print(d.groupby("premium").kaeufe.agg(["mean", "min", "max"]))   # ja: 9,25 (7-11), nein: 3,25 (1-6)
print(d.groupby("premium").umsatz.agg(["mean", "min", "max"]))   # ja: 1285, nein: 340
print(d.corr(numeric_only=True).round(2))                        # kaeufe-umsatz 0,74; alter-kaeufe -0,58
print((d.umsatz / d.kaeufe).round(0).tolist())                   # Umsatz je Kauf

# Premium-Regel: ab 7 Käufen
n["premium_regel"] = n.kaeufe >= 7                               # N1 ja, N2 nein, N3 nein (knapp), N4 ja

# Umsatz: einfache lineare Regression (Gerade aus Käufen)
b, a = np.polyfit(d.kaeufe, d.umsatz, 1)                         # 102 + 114 je Kauf
rest = d.umsatz - (a + b * d.kaeufe)
print(round(a), round(b), round(rest.std(ddof=2)))               # Streuung ca. 407
print((a + b * n.kaeufe).round(0).tolist())                      # 1011, 443, 784, 1466
```

Ergebnis: Die Regel "ab 7 Käufen Premium" ordnet alle acht bekannten Kunden richtig ein und gibt für N1 ja, N2 nein, N3 nein (knapp), N4 ja. Die Gerade aus Käufen (Umsatz ≈ 102 € + 114 € × Käufe) liefert 1.011 / 443 / 784 / 1.466 €, bei einer Streuung von rund 400 € um die bekannten Punkte. Das ist der Grund für die breiten Spannen. Meine Schätzungen sind diese Werte, bei N3 und N4 von Hand angepasst (siehe Schritt 2). Grafiken: `06_UE2_Premium_Prognose.ipynb`.
