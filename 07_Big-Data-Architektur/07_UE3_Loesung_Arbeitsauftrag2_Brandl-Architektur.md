# Tag 7 (Modul 3), Arbeitsauftrag 2: Architekturwahl bei Brandl Haustechnik

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI) | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Die Geschäftsführung der Brandl Haustechnik GmbH hat **1 Mio. € für 2 Jahre**. (1) **Vor- und Nachteile** der drei Optionen bewerten, (2) eine **strategische Entscheidung** treffen, (3) die **langfristigen Risiken** benennen. Dazu das Raster Vorteile / Nachteile / Langfristige Risiken / Ihre Entscheidung.

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Die drei Optionen

| Option | Was konkret passiert | Einmalig | Laufend | Bis zum Nutzen | Was dafür nötig ist |
|---|---|---:|---:|---|---|
| **A) Data Warehouse** | ERP, CRM, Webshop täglich nach **festem Modell** zusammengeführt, Berichte greifen darauf zu. **Jede neue Quelle ist ein eigenes Projekt** | ca. 750.000 € | 90.000 €/Jahr | erste Berichte nach ca. **12 Monaten** | Fachbereiche müssen **Kennzahlen vorab festlegen** |
| **B) Data Lake** | **Alle** Daten (auch Klicks, Scanner, Messwerte) **roh** in günstigem Cloud-Speicher, Analysten werten je Frage aus | ca. 500.000 € | 60.000 €/Jahr, **wächst mit der Datenmenge** | Speicher steht nach ca. **4 Monaten** | **Analysten**, die Rohdaten selbst aufbereiten können |
| **C) Bestehende Systeme optimieren** | Schnittstelle CRM–ERP, gemeinsame Excel-Vorlagen, Berichtswerkzeug direkt auf dem ERP | ca. 200.000 € | 30.000 €/Jahr | ca. **5 Monate** | **ERP-Hersteller muss die Schnittstelle liefern** |

### Weitere Angaben

| Thema | Angabe |
|---|---|
| Rahmen | **Budget 1 Mio. € für 2 Jahre**. Daten wachsen stark. Künftige Anforderungen unklar |
| Rolle | Brandl Haustechnik GmbH (Großhandel Heizung und Sanitär, 9 Standorte), Sie beraten die Geschäftsführung |
| Wachstum | Webshop **+40 % pro Jahr**. Neues Lager liefert Scannerdaten |
| Neue Datenquelle | Ab nächstem Jahr senden Heizungen beim Kunden Messwerte. **2027: 8.000 Geräte, je 12 Messwerte pro Stunde** |
| Unklar | Welche Auswertungen in zwei Jahren gebraucht werden, **weiß heute niemand** |
| Datenmengen | ERP **400 GB**. Webshop-Klicks **2 TB pro Jahr** |
| Team | **6 Personen IT, 1 Datenanalystin**. **Niemand** hat bisher Datenpipelines gebaut |
| Wünsche | Geschäftsführung: **einheitliche Monatsberichte** und **Umsatz je Kunde über alle Kanäle** |
| ERP | Der Hersteller beendet die Wartung der aktuellen Version **Ende 2029** |
| Sonstiges | Der neue Katalog wird gerade gedruckt. Brandl prüft einen **zehnten Standort** |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> Annahme für alle Kosten: die laufenden Kosten fallen für **beide** Jahre an.
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Kosten A über 2 Jahre | 750.000 € + 2 × 90.000 € | 930.000 € |
> | Kosten B über 2 Jahre | 500.000 € + 2 × 60.000 € | 620.000 € |
> | Kosten C über 2 Jahre | 200.000 € + 2 × 30.000 € | 260.000 € |
> | Rest vom Budget bei A | 1.000.000 € − 930.000 € | 70.000 € |
> | Rest vom Budget bei B | 1.000.000 € − 620.000 € | 380.000 € |
> | Rest vom Budget bei C | 1.000.000 € − 260.000 € | 740.000 € |
> | Anteil am Budget (A / B / C) | 930 / 620 / 260 von 1.000 | 93 % / 62 % / 26 % |
> | A + C zusammen | 930.000 € + 260.000 € | 1.190.000 € (über Budget) |
> | B + C zusammen | 620.000 € + 260.000 € | 880.000 € (passt) |
> | A + B zusammen | 930.000 € + 620.000 € | 1.550.000 € (über Budget) |
> | Lake, wenn die laufenden Kosten um 40 % pro Jahr steigen (Annahme) | 60.000 € + 60.000 € × 1,4 | 144.000 € statt 120.000 € |
> | Heizungsmesswerte pro Tag | 8.000 × 12 × 24 | 2.304.000 |
> | Heizungsmesswerte pro Jahr | 2.304.000 × 365 | rund 841 Mio. |
> | Heizungsmesswerte pro Sekunde | 2.304.000 / 86.400 | rund 27 |
> | Heizung im Vergleich zu Lagerbuchungen (6.000 pro Tag, aus Aufgabe 1) | 2.304.000 / 6.000 | 384-fach |
> | Webshop-Klicks 2027 (Annahme: 2 TB sind 2026) | 2 TB × 1,4 | 2,8 TB |
> | Webshop-Klicks 2028 | 2,8 TB × 1,4 | 3,92 TB |
> | Webshop-Klicks im Verhältnis zum ERP | 2 TB / 0,4 TB | 5-fach |
> | Standorte: Zuwachs durch den zehnten | 10 / 9 − 1 | +11,1 % |
> | Start Januar 2027 (Annahme): Nutzen ab | A +12, B +4, C +5 Monate | Jan 2028 / Mai 2027 / Jun 2027 |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Entscheidung (Vorschlag):** **Option B, Data Lake**, aber **nicht roh und ohne Plan**. Auf dem Lake entsteht früh eine **kleine, geprüfte Schicht** für die zwei Wünsche der Geschäftsführung (Umsatz je Kunde über alle Kanäle, einheitlicher Monatsbericht). Der Rest des Budgets geht in **Personal und Qualifizierung**, denn Option B scheitert im Alltag an Können, nicht an Technik.
> - **Warum B:** Künftige Anforderungen sind **unklar**, die Daten wachsen stark (Heizung 841 Mio. Messwerte pro Jahr, 384-mal mehr pro Tag als die Lagerbuchungen). Ein Warehouse braucht ein **festes Modell**, und **jede neue Quelle ist ein eigenes Projekt**. B ist mit **4 Monaten** vor dem Heizungsstart bereit (A erst nach **12 Monaten**), kostet **620.000 €** und lässt **380.000 € Reserve**.
> - **Warum nicht A:** Mit **930.000 €** bleiben nur **70.000 €** Puffer. Die ersten Berichte kommen erst Anfang 2028, die Heizungsdaten sind im festen Modell nicht vorgesehen.
> - **Warum nicht C allein:** Mit **260.000 €** am günstigsten und mit 5 Monaten schnell, aber die Schnittstelle hängt am **ERP-Hersteller**, dessen Version **Ende 2029 ausläuft**. C löst Klicks, Scanner und Heizung **nicht**, und Excel bleibt.
> - **Größtes Risiko:** **Datensumpf**. Ein Lake ohne Pipeline-Erfahrung (niemand im Team hat bisher eine gebaut) füllt sich, ohne dass jemand Zahlen bekommt. Gegenmittel: erst **ein** Anwendungsfall (Kunde über alle Kanäle), eine feste Verantwortliche je Datenquelle, **Entscheidungspunkt nach 6 Monaten**. Wenn das Team bis dahin nicht trägt, ist **A** der sichere Rückweg.
> - **Vorsicht:** Das ist eine **Abwägung**, keine Rechnung. Das Blatt nennt **keine Personalkosten**, keinen Nutzen in Euro und keine Preise für eine kuratierte Schicht. Eine Gegenposition ("zuerst Warehouse, weil die Wünsche klassische Berichte sind") ist vertretbar.

> [!NOTE]
> **Annahmen:** (1) Die laufenden Kosten fallen für beide Jahre an, auch während der Aufbauzeit. (2) Start im Januar 2027, die Heizungsdaten starten frühestens 2027. (3) Die 2 TB Webshop-Klicks sind der Stand 2026, das Wachstum von 40 % gilt für die Klicks, nicht für alle Daten. Der Lake-Kostenanstieg um 40 % ist eine Annahme von mir, das Blatt sagt nur "wächst mit der Datenmenge". (4) Die Größe eines Messwerts (zum Beispiel 100 bis 200 Byte) ist von mir gesetzt: 84 bis 168 GB pro Jahr, also **klein gegen die Klicks**. Das Problem der Heizungen ist die **Anzahl** der Zeilen, nicht der Speicherplatz. (5) Eine Stelle kostet im Rechenbeispiel 100.000 € pro Jahr. Das ist **nicht** aus dem Blatt. (6) Katalogdruck und zehnter Standort halte ich für **Nebensache**: der zehnte Standort erhöht die Zahl der Standorte um 11,1 %, ändert die Wahl aber nicht. (7) Ob Heizungsmesswerte Personenbezug haben, hängt vom Vertrag mit den Endkunden ab: **Rechtslage prüfen**. Alle Rechnungen stehen im Python-Check.

## Schritt 1 · Bewertungsraster

| Kriterium | A) Warehouse | B) Lake | C) Optimieren |
|:---|:---|:---|:---|
| **Vorteile** | **Eine geprüfte Zahl**: gemeinsames Modell, Kennzahlen-Glossar, passt zu **Monatsbericht** und **Umsatz je Kunde**. Schnelle, stabile Berichte für viele Nutzer. Entkoppelt Berichte vom ERP: bei einem ERP-Wechsel ändern sich nur die Ladeprozesse. Klare Verantwortung | **Alle Daten** (auch Klicks, Scanner, Heizung) landen in günstigem Speicher. **Kein Festlegen im Voraus**, passt zu unklaren Anforderungen. **620.000 €**, **380.000 € Reserve**. Speicher nach **4 Monaten**, also vor dem Heizungsstart. Wächst mit | **Billigste Option** (260.000 €), **schnell** (5 Monate), **wenig Umstellung**. Kein neues Know-how nötig. Bleibt im bekannten Werkzeug |
| **Nachteile** | **930.000 €**, nur **70.000 €** Puffer. **12 Monate** bis zum ersten Bericht. Kennzahlen müssen **vorab** feststehen, obwohl niemand die künftigen Auswertungen kennt. **Jede neue Quelle ist ein Projekt** (Scanner, Heizung, Klicks). Team ohne Pipeline-Erfahrung | **Keine fertigen Berichte**: jede Frage braucht Aufbereitung der Rohdaten. Es braucht **Analysten mit Können**, das Team hat **1 Analystin**. Ohne Glossar entstehen wieder **zwei Zahlen für einen Umsatz**. Kosten **wachsen mit der Datenmenge** | **Löst die Integration nur zwischen CRM und ERP**: Webshop, Excel, Scanner und Heizung bleiben außen vor. **Abhängig vom ERP-Hersteller**. Excel-Vorlagen bleiben Handarbeit. Skaliert nicht mit starkem Wachstum |
| **Langfristige Risiken** | **Starrheit**: neue Fragen und Quellen kosten jedes Mal Zeit und Geld. Heizungsdaten (841 Mio. Zeilen pro Jahr) belasten ein klassisches Modell. Kennzahlen-Streit zwischen Fachbereichen verzögert den Start. Durch den hohen Anteil am Budget **keine Reserve für Überraschungen**. | **Datensumpf**: viel gespeichert, wenig genutzt. **Fachkräfte** fehlen oder wandern ab. **Datenschutz**: Rohdaten mit Kundenbezug in der Cloud, Zugriffsrechte nötig. Kosten laufen mit dem Wachstum weg (Webshop 3,92 TB 2028). Gefahr, dass es **ohne Nutzer** bleibt | **Sackgasse**: die ERP-Version läuft **Ende 2029** aus, die Schnittstelle müsste neu gebaut werden. **Technische Schulden** und Hersteller-Abhängigkeit. In zwei Jahren steht man vor demselben Problem und hat 260.000 € ausgegeben |
| **Passt zu den Wünschen der Geschäftsführung?** | **Ja, sehr gut**, aber erst ab Anfang 2028 | **Nur mit Zusatzarbeit**: eine kuratierte Schicht muss die zwei Wünsche liefern | **Teilweise**: Bericht aus dem ERP ja, **Umsatz über alle Kanäle** (Webshop) nicht |
| **Passt zu den Heizungsdaten?** | **Schlecht**: nicht im festen Modell, eigenes Projekt | **Gut**: Rohdaten landen einfach im Speicher | **Nein** |
| **Passt zum Team (6 IT, 1 Analystin)?** | **Mittel**: klare Regeln, aber Aufbau zu groß ohne Erfahrung | **Schlecht ohne Hilfe**, **mittel** mit Einstellung und Schulung | **Gut**: Bekanntes bleibt Bekanntes |

## Schritt 2 · Meine Entscheidung

| Frage | Meine Antwort |
|:---|:---|
| **Meine Wahl** | **Option B (Data Lake)**, ergänzt um eine **kleine kuratierte Schicht** für Kunde und Umsatz. Das ist **kein reines B**, sondern ein Lake mit Ziel |
| **Warum diese?** | (1) **Unklare Anforderungen** sprechen gegen ein festes Modell. (2) **Heizungsdaten** (2.304.000 Zeilen pro Tag) und **Klicks** (3,92 TB 2028) passen nicht in ein klassisches Warehouse, ohne dass jede Quelle ein Projekt wird. (3) **4 Monate** bis zum Speicher: bereit, bevor die Heizungen senden. (4) **380.000 € Reserve** für das, was B braucht: Menschen |
| **Warum nicht die anderen?** | **A**: 930.000 €, Puffer 70.000 €, erster Bericht erst nach 12 Monaten, Heizung nicht im Modell. **C**: ERP-Version läuft Ende 2029 aus, die Schnittstelle zwischen CRM und ERP bringt Webshop, Scanner und Heizung nicht näher. Als Dauerlösung ungeeignet |
| **Kombination der Optionen? Was passt ins Budget?** | Möglich ist **nur B + C** (880.000 €). A + C kostet 1.190.000 €, A + B 1.550.000 €. **B + C lässt 120.000 € Rest**, das reicht kaum für Personal. Darum nehme ich **B allein** (620.000 €) und halte **380.000 €** für Personal, Schulung und die kuratierte Schicht. **C** nur als **kleine Notlösung**, falls der Monatsbericht schneller gebraucht wird: ein Export aus dem ERP, nicht die große Schnittstelle |
| **Was passiert, wenn die Heizungsdaten kommen?** | Sie landen **roh** im Lake (rund 84 bis 168 GB pro Jahr bei 100 bis 200 Byte je Messwert, **Annahme**). Die Last liegt bei der **Zeilenzahl** (rund 27 pro Sekunde, stetig). Bei A wäre es ein **neues Projekt** mit Modell und Kennzahlen. **Ob** daraus ein Geschäft entsteht (Wartung nach Messwerten, Störungsmeldung), ist offen: zuerst **sammeln und anschauen**, dann entscheiden |
| **Was ich nicht weiß und was ich zuerst klären würde** | (1) **Personalkosten**: Wer baut und betreibt die Pipelines? Einstellung oder externe Hilfe? (2) **Was heißt "Umsatz"**: brutto oder netto, nach Auftrags- oder Rechnungsdatum? Das Glossar kommt **vor** der Technik. (3) **Starttermin der Heizungsdaten** und **Datenschutz** der Messwerte. (4) Ob der **ERP-Hersteller** 2029 einen Nachfolger anbietet, das beeinflusst jede Option. (5) Ob 40 % Wachstum für die **Kosten** des Lake gilt |

## Schritt 3 · Langfristige Risiken

| Risiko | Welche Option trifft es? | Woran würde ich es merken? | Was tue ich dagegen? |
|:---|:---|:---|:---|
| **Fester Zuschnitt passt nicht mehr** | **A** am stärksten. Auch C (Excel-Vorlagen) | Neue Frage der Geschäftsführung, Antwort dauert Monate, Fachbereiche streiten um Kennzahlen | Bei B: Rohdaten bleiben erhalten, neue Sicht nur ergänzen. Kennzahlen im **Glossar** festhalten |
| **Daten liegen, aber niemand nutzt sie** | **B** am stärksten | Speicher wächst, aber **kein Bericht** nutzt ihn. Analystin ist ausgelastet mit Aufbereiten | **Ein Anwendungsfall zuerst**, Verantwortliche je Quelle, **Entscheidungspunkt nach 6 Monaten**: ohne Nutzen weiter in Richtung A |
| **Kosten wachsen mit den Daten** | **B** (laufend), **A** (neue Quellen) | Rechnung steigt schneller als das Geschäft. Bei +40 % pro Jahr 144.000 € statt 120.000 € in 2 Jahren | **Aufbewahrungsfristen** festlegen, Rohdaten älterer Jahre günstiger ablegen, Kosten monatlich ansehen |
| **ERP-Wartung endet 2029** | **C** am stärksten. A und B nur an der Ladestelle | Hersteller kündigt Nachfolger an oder nicht. Schnittstelle bricht bei Update | **Nichts Teures direkt an die ERP-Version binden.** Daten im Lake bleiben, nur die **Ladeprozesse** ändern sich. ERP-Entscheidung früh planen |
| **Abhängigkeit von Hersteller, Cloud oder einzelnen Personen** | C: **Hersteller**. B: **Cloud-Anbieter** und **wenige Fachleute**. A: **Datenbank-Anbieter** | Eine Person ist krank oder geht, und niemand versteht die Pipeline | Dokumentation, **zwei Personen je Pipeline**, offene Formate im Lake, Ausstiegsplan |
| **Datenschutz und Zugriffsrechte** | **B** (Rohdaten mit Personenbezug), alle bei Heizungsdaten | Außendienst sieht Daten, die er nicht sehen darf. Heizungsdaten lassen Rückschlüsse auf Haushalte zu (Anwesenheit). **Rechtslage prüfen** | Rollen und Rechte von Anfang an, **Personenbezug früh trennen oder entfernen**, Verträge mit Cloud-Anbieter prüfen |

## Python-Check

```python
from itertools import combinations

budget, jahre = 1_000_000, 2
opt = {  # einmalig, laufend pro Jahr
    "A Warehouse": (750_000, 90_000),
    "B Lake": (500_000, 60_000),
    "C Optimieren": (200_000, 30_000),
}
tot = {k: e + l * jahre for k, (e, l) in opt.items()}
for k, s in tot.items():
    print(k, f"{s:,}", "Rest", f"{budget - s:,}", f"{s / budget:.0%}")
# A 930.000 (70.000 Rest, 93 %), B 620.000 (380.000, 62 %), C 260.000 (740.000, 26 %)

for r in (2, 3):
    for c in combinations(opt, r):
        s = sum(tot[x] for x in c)
        print(" + ".join(x[0] for x in c), f"{s:,}", "passt" if s <= budget else "zu teuer")
# A+B 1.550.000 und A+C 1.190.000 und A+B+C 1.810.000 zu teuer, B+C 880.000 passt

l1, l2 = 60_000, 60_000 * 1.4        # Annahme: +40 % pro Jahr
print(f"{l1 + l2:,.0f}")             # 144.000 statt 120.000

pro_tag = 8_000 * 12 * 24            # 2.304.000
pro_jahr = pro_tag * 365             # 840.960.000
print(f"{pro_tag:,} {pro_jahr:,} {pro_tag / 86_400:.1f} {pro_tag / 6_000:.0f}")
# 2.304.000  840.960.000  26.7 pro Sekunde  384-fach gegenüber den Lagerbuchungen
for b in (100, 200):                 # Annahme: Byte je Messwert
    print(f"{pro_jahr * b / 1e9:.0f} GB pro Jahr")   # 84 / 168

v = 2.0                              # TB 2026
for y in (2026, 2027, 2028):
    print(y, f"{v:.2f} TB"); v *= 1.4    # 2,00 / 2,80 / 3,92
print(f"{(10 / 9 - 1) * 100:.1f} %")     # 11,1 % mehr Standorte
print((budget - tot["B Lake"]) / 100_000)  # 3,8 Stellenjahre (Annahme 100.000 €)
```
