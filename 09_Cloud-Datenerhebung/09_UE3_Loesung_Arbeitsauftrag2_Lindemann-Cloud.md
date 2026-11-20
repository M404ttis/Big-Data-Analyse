# Tag 9 (Modul 3), Arbeitsauftrag 2: Cloud, Hybrid oder On-Premise bei Lindemann

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI) | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Rolle: IT-Verantwortliche(r) bei Lindemann. (1) **Bewerten** Sie die drei Optionen nach Kosten, Sicherheit, Flexibilität. (2) **Treffen Sie eine Entscheidung.** (3) **Welche Risiken** bestehen langfristig? Budget: **650.000 € über 5 Jahre**.

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Die Lage

| Thema | Angabe |
|---|---|
| Ausgangslage | Eigener Serverraum voll, Server 7 Jahre alt. **Wartung läuft in 8 Monaten aus** |
| Maschinendaten | Heute **2 TB** pro Jahr, mit neuen Sensoren ca. **25 TB** pro Jahr |
| Schutzbedarf | Konstruktionsdaten und Kundendaten müssen **besonders geschützt** werden |
| Budget | **650.000 €** über 5 Jahre |
| IT-Team | 4 Personen, einer geht in einem Jahr in Rente, **niemand hat Cloud-Erfahrung** |
| Ausfall | Black Friday 2025: Shop **3 Stunden** offline, ca. **90.000 €** Umsatz verloren |
| Kunde | Elektromarktkette, **22 %** des Umsatzes, verlangt ein **ISO-27001-zertifiziertes** Rechenzentrum |
| Netz | 250 Mbit/s. Ausbau auf 1 Gbit/s: **600 € pro Monat** |
| Sonstiges | Neue Monitore im Büro. Für die Entscheidung vermutlich ohne Bedeutung |

### Die drei Optionen

| Option | Was passiert? | Einmalig | Laufend | Was bekannt ist |
|---|---|---:|---|---|
| **A) Vollständige Cloud** | Shop, ERP und Maschinendaten bei einem Anbieter mit **EU-Rechenzentrum**, Serverraum wird aufgegeben | 150.000 € (Umzug) | 9.000 €/Monat, +1.500 € je weitere 10 TB | Anbieter verspricht 99,95 % Verfügbarkeit |
| **B) Hybrid** | Shop und Analysen in der Cloud. **ERP, Konstruktionsdaten und Maschinensteuerung bleiben im Haus** | 120.000 € | 5.000 €/Monat Cloud + 2.000 €/Monat eigene Server | Zwei Welten müssen betreut und verbunden werden |
| **C) On-Premise** | Neue Server und Speicher im eigenen Haus, Betrieb durch eigene IT | 380.000 € (davon 60.000 € Klimatisierung) | ca. 4.000 €/Monat (Strom, Wartung, Ersatzteile) | Serverraum muss klimatisiert werden |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | **A über 5 Jahre** | 150.000 € + 60 × 9.000 € | **690.000 €** |
> | **B über 5 Jahre** | 120.000 € + 60 × (5.000 € + 2.000 €) | **540.000 €** |
> | **C über 5 Jahre** | 380.000 € + 60 × 4.000 € | **620.000 €** |
> | Rest zum Budget A | 650.000 € − 690.000 € | **−40.000 €** |
> | Rest zum Budget B | 650.000 € − 540.000 € | 110.000 € |
> | Rest zum Budget C | 650.000 € − 620.000 € | 30.000 € |
> | Mehr als B: A | 690.000 € − 540.000 € | 150.000 € |
> | Mehr als B: C | 620.000 € − 540.000 € | 80.000 € |
> | Mittlere Monatskosten A, B, C | Gesamt / 60 | 11.500 €, 9.000 €, 10.333 € |
> | Datenmenge in 5 Jahren (25 TB/Jahr) | 25 TB × 5 | 125 TB |
> | Wachstum der Maschinendaten | 25 TB / 2 TB | Faktor 12,5 |
> | Black Friday: Verlust je Stunde | 90.000 € / 3 h | 30.000 €/h |
> | 99,95 % Verfügbarkeit: erlaubter Ausfall je Jahr | 8.760 h × 0,05 % | 4,38 h |
> | Elektromarktkette: Umsatz je Jahr (Annahme: 41 Mio. € Gesamtumsatz) | 41 Mio. € × 22 % | 9,02 Mio. € |
> | Netz-Ausbau über 5 Jahre | 60 × 600 € | 36.000 € |
> | Maschinendaten im Mittel (25 TB/Jahr) | 25 TB / 1 Jahr | 6,3 Mbit/s (2,5 % der Leitung) |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Entscheidung (Vorschlag): B) Hybrid, mit Bedingungen.** 540.000 € über 5 Jahre, 110.000 € unter dem Budget. Shop und Analysen in die Cloud (Black Friday, Wachstum), **ERP, Konstruktionsdaten, Maschinensteuerung und Maschinen-Rohdaten bleiben im Haus**.
> - **A) Vollständige Cloud scheidet am Budget aus:** 690.000 € (**−40.000 €**) schon *ohne* Datenwachstum. Mit 25 TB Maschinendaten kommen Zuschläge dazu: 870.000 € bei 12 Monaten Rohdaten, 1,30 Mio. € bei "alles behalten" (Annahme: 10 TB im Preis, +1.500 € je weitere 10 TB).
> - **C) On-Premise passt knapp ins Budget** (620.000 €, nur 30.000 € Reserve), bietet aber **keine Flexibilität** für Spitzen wie den Black Friday. Dazu fehlen Zertifizierung und Personal (einer geht in Rente).
> - **Die Kostenlücke ist kleiner als die Fachlücke.** B ist nur 80.000 € billiger als C, aber das Team hat **keine Cloud-Erfahrung**. Von den 110.000 € Reserve gehen Schulung, Partner und Netzausbau (36.000 €) ab. Das Blatt nennt dafür keine Kosten.
> - **Die größte offene Frage ist ISO 27001.** Die Elektromarktkette bringt 22 % des Umsatzes (rund 9 Mio. € pro Jahr) und verlangt ein zertifiziertes Rechenzentrum. Bei B liegt das **ERP im eigenen Haus, das nicht zertifiziert ist**. Ob das genügt, hängt davon ab, **welche Daten der Kunde meint**. Das muss **vor** der Entscheidung geklärt werden.
> - **Vorsicht:** Alle Zahlen sind Planwerte vom Blatt. Zuschläge, Preissteigerung und Wachstum sind **Annahmen** und stehen im Python-Check.

> [!NOTE]
> **Annahmen:** (1) Im Preis von A stecken **10 TB**, danach je angefangene 10 TB 1.500 € pro Monat. Das Blatt sagt nur "je weitere 10 TB". (2) B hat laut erster Tabelle 5.000 €/Monat Cloud, laut zweiter Tabelle **zusätzlich** 2.000 €/Monat für eigene Server. Ich rechne mit **7.000 €/Monat**. (3) Bei B gehen nur **verdichtete** Maschinendaten in die Cloud, die Rohdaten bleiben im Haus. Dann gibt es dort keinen Zuschlag. (4) Die 380.000 € bei C und die 2.000 €/Monat bei B reichen für das Datenwachstum. Das Blatt nennt die Kapazität nicht. (5) Preissteigerungen gelten nur für den Cloud-Anteil. (6) Der Umsatz von 41 Mio. € ist der Gesamtumsatz (aus Arbeitsauftrag 1). (7) Nicht eingerechnet: Personal, Schulung, Beratung, Zertifizierung, Lizenzen. Das Blatt nennt sie nicht.

## Schritt 1 · Bewertungsraster

| Kriterium | A) Cloud | B) Hybrid | C) On-Premise |
|:---|:---|:---|:---|
| **Kosten über 5 Jahre** | **690.000 €** (150.000 € + 60 × 9.000 €). **−40.000 € gegen das Budget.** Mit 25 TB Maschinendaten und 12 Monaten Rohdaten: **870.000 €**, bei "alles behalten": **1,30 Mio. €** | **540.000 €** (120.000 € + 60 × 7.000 €). **110.000 € Reserve.** Netz-Ausbau 36.000 € möglich: 576.000 € | **620.000 €** (380.000 € + 60 × 4.000 €). Nur **30.000 € Reserve**. Datenwachstum auf 125 TB: Kapazität offen, mögliche Mehrkosten nicht bezifferbar |
| **Sicherheit** | **Hoch bei zertifiziertem Anbieter** (ISO 27001, EU-Rechenzentrum, Vertrag nach Art. 28 DSGVO). Alle Daten außer Haus, auch die **Konstruktionsdaten** | **Gut verteilt**: Konstruktion, ERP und Steuerung bleiben im Haus. Kundendaten im Shop beim zertifizierten Anbieter. **Zwei Welten, zwei Sicherheitskonzepte.** Der eigene Serverraum ist **nicht zertifiziert** | **Volle Kontrolle**, aber auch volle Verantwortung. Kein Zertifikat vorhanden. Kleines Team (4, bald 3) muss Patches, Backups, Zugriffe allein stemmen |
| **Flexibilität** | **Sehr hoch.** Leistung wächst in Minuten (Folie: Spitzenlast). Black Friday abfangbar. Dafür **Zuschläge bei Wachstum** und Lock-in | **Hoch dort, wo es zählt**: Shop skaliert, Analysen wachsen mit. Steuerung bleibt bewusst fest | **Gering.** Kapazität wird **vorab** gekauft. Eine Spitze oder 25 TB statt 2 TB heißt: nachkaufen |
| **Langfristige Risiken** | **Preiserhöhung** (+10 % pro Jahr: +119.000 €), **Lock-in**, Datenwachstum, fehlendes Cloud-Wissen, Ausfall des einzigen Internetanschlusses legt ERP **und** Shop lahm | **Zwei Welten betreuen**, Schnittstelle zwischen beiden, Personal (Rente), ISO-Frage beim ERP im Haus. Preiserhöhung trifft nur 5.000 € (+10 % pro Jahr: +66.000 €) | **Veralten** nach 5 Jahren, **Ausfall** wie am Black Friday, Personalabhängigkeit, **Zertifizierung** nachholen, Wartung läuft in **8 Monaten** aus: Beschaffung unter Zeitdruck |
| **Meine Entscheidung** | **Nein.** Über Budget, schon vor dem Wachstum | **Ja**, mit den Bedingungen unten | **Zweite Wahl.** Passt ins Budget, ist aber starr. Fällt zurück, wenn das Team die zwei Welten von B nicht schafft |

> [!NOTE]
> **Bedingungen für B:**
> 1. **ISO 27001 klären:** Welche Daten meint die Elektromarktkette? Reicht der zertifizierte Anbieter für den Shop, oder fällt auch das ERP darunter? Wenn ja: ERP in die Cloud (dann Richtung A, Budget neu prüfen) oder eigenen Serverraum zertifizieren (Kosten unbekannt).
> 2. **Verdichten statt alles hochladen:** Nur Kennzahlen und Zusammenfassungen der Maschinendaten in die Cloud. Rohdaten im Haus, mit **Löschfrist** (zum Beispiel 12 Monate roh).
> 3. **Budgetgrenze und Kostenwarnung** beim Anbieter (Folie "Kostenrisiko": Testserver vergessen, die Rechnung steigt unbemerkt).
> 4. **Ausstiegsweg** in den Vertrag (offene Standards, Datenexport).
> 5. **Partner und Schulung** einplanen, solange niemand Cloud-Erfahrung hat.

### Wie sich die Kosten bewegen (Sensitivität)

| Szenario | A) Cloud | B) Hybrid | C) On-Premise |
|:---|---:|---:|---:|
| **Wie auf dem Blatt** (ohne Zuschläge) | 690.000 € | 540.000 € | 620.000 € |
| **25 TB/Jahr, 12 Monate roh** (Zuschlag 3.000 €/Monat) | 870.000 € | 540.000 € (Rohdaten im Haus) | 620.000 € (Kapazität offen) |
| **25 TB/Jahr, alles behalten** (125 TB am Ende) | 1.302.000 € | 540.000 € (Rohdaten im Haus, Kapazität offen) | 620.000 € (Kapazität offen) |
| **Cloud-Preis +5 % pro Jahr** | 746.768 € | 571.538 € | 620.000 € |
| **Cloud-Preis +10 % pro Jahr** | 809.351 € | 606.306 € | 620.000 € |
| **Cloud-Preis +20 % pro Jahr** | 953.693 € | 686.496 € | 620.000 € |
| **Budget** | **650.000 €** | **650.000 €** | **650.000 €** |

> [!NOTE]
> **Was die Tabelle zeigt:** B bleibt bis rund **+15 % Preiserhöhung pro Jahr** im Budget. C ist am **stabilsten**, solange die Kapazität reicht, aber auch am teuersten, wenn alles glatt läuft. A ist in **keinem** Szenario im Budget. Die Preise für den **Platz im eigenen Haus** (Kapazität bei B und C) kennt das Blatt nicht: das ist die größte Unsicherheit der Tabelle.

## Schritt 2 · Welche Daten dürfen das Haus nicht verlassen?

| Daten | Darf in die Cloud? | Warum? |
|:---|:---|:---|
| **Konstruktionsdaten** | **Nein (Vorschlag).** Bleiben im Haus | Das Blatt verlangt "besonders geschützt". Das ist das **Know-how** der Firma (Entwürfe, Werkzeuge). Bei einem Fehler oder Anbieterwechsel wäre der Schaden nicht umkehrbar. Zugriffe auf wenige Personen begrenzen |
| **Kundendaten** | **Ja, aber geschützt.** "Besonders schützen" heißt nicht "im Haus lassen" | Der Shop mit Kundenkonten läuft bei B ohnehin in der Cloud. Nötig: **EU-Rechenzentrum, Verschlüsselung, Vertrag zur Auftragsverarbeitung (Art. 28 DSGVO)**, Zugriffsrechte, Löschfristen. Lindemann bleibt **Verantwortlicher**, der Anbieter ist nur Auftragsverarbeiter |
| **Maschinensteuerung** | **Nein.** Bleibt im Haus | Steuert Maschinen in Echtzeit. Bei Internet-Ausfall dürfen die Maschinen **nicht stehen**. Auch ein Sicherheitsthema (Zugriff von außen) |
| **Maschinen-Rohdaten** (2 bis 25 TB/Jahr) | **Nein, nur verdichtet.** | Ohne Verdichtung wachsen die Zuschläge (Cloud: bis zu 18.000 €/Monat im Jahr 5). Verdichtete Werte reichen für Auswertungen. Im Mittel nur 6,3 Mbit/s, die **Leitung** wäre kein Problem (2,5 % von 250 Mbit/s), aber das **Erstladen** von 10 TB dauert bei voller Leitung rund 3,7 Tage |
| **ERP** | **Offen** (ISO-Frage) | Bei B bleibt es im Haus. Nur wenn die Elektromarktkette dort **ihre Daten** vermutet und Zertifizierung verlangt, ändert sich das |

## Schritt 3 · Langfristige Risiken

| Risiko | Wie groß? | Gegenmittel |
|:---|:---|:---|
| **Preiserhöhung beim Cloud-Anbieter** | Bei B nur 5.000 €/Monat betroffen: **+5 % pro Jahr = +31.500 €**, **+10 %: +66.300 €**, **+20 %: +146.500 €**. Bei A (9.000 €/Monat) rund das Doppelte. Dazu kommen **Wechselkosten**, wenn man festsitzt (nicht beziffert, das Blatt nennt sie nicht) | **Offene Standards**, Ausstiegsplan, Daten regelmäßig exportieren. Preisklauseln im Vertrag (Deckel). Kostenwarnung und Budgetgrenze. Bei starker Erhöhung: Teile zurückholen können (Hybrid erleichtert das) |
| **Personal** | **Hoch.** 4 Personen, einer geht in einem Jahr in Rente, niemand kennt die Cloud. Zwei Welten bei B bedeuten **mehr** Aufgaben, nicht weniger | Schulung **vor** dem Umzug. Externer Partner für die ersten 12 Monate. Nachfolge für die Rente jetzt planen. Dokumentation der Schnittstelle |
| **Ausfall** | Am Black Friday 2025: 3 Stunden, **30.000 € pro Stunde**. Das Versprechen von 99,95 % erlaubt **4,38 Stunden** Ausfall pro Jahr, das wäre **mehr** als 2025 (3 h = 99,966 %). Der Anbieter verspricht also **nicht** "kein Ausfall". Dazu der **einzige Internetanschluss**: Fällt er aus, sind Shop (und bei A auch ERP) weg | Zweite Leitung oder Mobilfunk-Backup. Shop in **mehreren Rechenzentren** des Anbieters. Notfallplan und Lasttest **vor** dem nächsten Black Friday. Bei Hybrid läuft die Produktion bei Netzausfall weiter |
| **Zeit** | Die Server-Wartung läuft in **8 Monaten** aus, die Server sind 7 Jahre alt. Cloud-Umzug ohne Erfahrung dauert. Neue Hardware bei C braucht Lieferzeit | **Plan mit Puffer** (siehe unten). Wartung der alten Server **kurz verlängern**, falls möglich (Kosten unbekannt). **Nicht kurz vor dem Black Friday** den Shop umziehen |
| **Datenmenge** | 12,5-faches Wachstum (2 auf 25 TB pro Jahr), 125 TB in 5 Jahren | Verdichten, Löschfristen ("nicht alles speichern"), Speicherplanung im Haus jährlich prüfen |
| **ISO 27001** | **22 % des Umsatzes** (rund 9 Mio. € pro Jahr, 45 Mio. € in 5 Jahren) hängen an der Zusage. Das ist **viel größer** als jeder Unterschied der Optionen (80.000 € bis 150.000 €) | Klären, **was genau** verlangt wird. Anbieter mit Zertifikat wählen. Prüfung der Unterlagen in den Vertrag |

### Umsetzung in 8 Monaten (Vorschlag)

| Monat | Schritt |
|:---:|---|
| **0 bis 1** | ISO-27001-Frage mit der Elektromarktkette klären. Anbieter auswählen (EU, zertifiziert, Ausstieg, Preisdeckel). Partner und Schulung beauftragen |
| **1 bis 3** | Cloud-Konto, Rechte, Budgetgrenze und Kostenwarnung. Netz prüfen (zweite Leitung, Ausbau auf 1 Gbit/s: 600 € pro Monat, 36.000 € in 5 Jahren) |
| **3 bis 6** | Shop in die Cloud, mit **Lasttest** (Black-Friday-Last). Verdichtung der Maschinendaten bauen. Eigene Server (B): Ersatz oder neue Wartung |
| **6 bis 8** | Alte Server abschalten, Dokumentation, Notfallübung. Puffer für Verzögerungen |

> [!NOTE]
> **Was bewusst fehlt:** Die neuen Büromonitore sind für die Entscheidung ohne Bedeutung. **Nicht beziffert** sind Schulung, Partner, Personal und eine Zertifizierung des eigenen Serverraums. Dafür bleiben bei B **110.000 €** (abzüglich Netzausbau **74.000 €**). Ob das reicht, nennt das Blatt nicht.

> [!NOTE]
> **Was gegen meine Entscheidung sprechen würde:** (1) Die Elektromarktkette verlangt das ERP in einem zertifizierten Rechenzentrum. Dann wäre A fachlich richtig, aber nur mit **mehr Budget**. (2) Das Team schafft zwei Welten nicht. Dann bliebe C, mit 30.000 € Reserve. (3) Die Preise im eigenen Haus steigen stärker als geplant, weil 125 TB Maschinendaten viel Platz brauchen. Das Blatt nennt die Preise nicht.

## Python-Check

```python
# python3 -I check2.py   (nur Standardbibliothek)
from math import ceil
M = 60   # Monate in 5 Jahren
A = 150_000 + 9_000 * M
B = 120_000 + (5_000 + 2_000) * M
C = 380_000 + 4_000 * M
print("5 Jahre ohne Zuschläge  A:", A, " B:", B, " C:", C)
print("Budget 650.000: Rest    A:", 650_000 - A, " B:", 650_000 - B, " C:", 650_000 - C)
print("Monatlich im Mittel     A:", round(A / M), " B:", round(B / M), " C:", round(C / M))
print("Aufpreis zu B           A:", A - B, " C:", C - B)
# Datenwachstum Cloud (Annahme: im Preis stecken 10 TB, je angefangene 10 TB weitere 1.500 €/Monat)
def zuschlag(tb): return max(0, ceil((tb - 10) / 10)) * 1_500
roh12 = sum(zuschlag(25) * 12 for _ in range(5))
alles = sum(zuschlag(25 * j) * 12 for j in range(1, 6))
print("Zuschlag Cloud, 25 TB konstant (12 Monate roh):", roh12, "| alles behalten:", alles, [zuschlag(25 * j) for j in range(1, 6)])
print("A mit 12 Monaten roh:", A + roh12, "| A alles behalten:", A + alles)
print("B, falls Maschinendaten roh in der Cloud (12 Monate):", B + roh12, "| B, Rohdaten im Haus, nur verdichtet in der Cloud:", B)
# Preiserhöhung nur auf den Cloud-Anteil
def cloud(monat, p): return sum(monat * 12 * (1 + p) ** j for j in range(5))
for p in (0, .05, .10, .20):
    print(f"Preis +{int(p*100):2d} % pro Jahr   A Cloud:", round(cloud(9_000, p)), "Mehr:", round(cloud(9_000, p) - cloud(9_000, 0)),
          "| B Cloud:", round(cloud(5_000, p)), "Mehr:", round(cloud(5_000, p) - cloud(5_000, 0)))
# Ausfall
print("Black Friday: 90.000 € / 3 h =", 90_000 // 3, "€ pro Stunde")
down = 8_760 * 0.0005
print("99,95 % erlaubt Ausfall pro Jahr:", round(down, 2), "h | bei 30.000 €/h:", round(down * 30_000), "€ | bei Ø-Umsatz/h (41 Mio./8.760):", round(down * 41_000_000 / 8_760), "€")
print("2025 tatsächlich: 3 h =", round(3 / 8_760 * 100, 3), "% Ausfall, Verfügbarkeit", round(100 - 3 / 8_760 * 100, 3), "%")
# Kunde, Netz
print("Elektromarktkette 22 % von 41 Mio. €:", round(41_000_000 * 0.22), "pro Jahr, 5 Jahre:", round(41_000_000 * 0.22 * 5))
print("Ausbau Netz 1 Gbit:", 600 * M, "€ in 5 Jahren")
mbit = 25e12 * 8 / (365 * 24 * 3600) / 1e6
print("25 TB/Jahr im Mittel:", round(mbit, 1), "Mbit/s =", round(mbit / 250 * 100, 1), "% von 250 Mbit/s")
tage = 10e12 * 8 / 250e6 / 86400
print("10 TB einmal hochladen bei 250 Mbit/s (volle Leitung):", round(tage, 1), "Tage | bei 1 Gbit/s:", round(tage / 4, 1), "Tage")
print("Datenmenge 5 Jahre (25 TB/Jahr):", 25 * 5, "TB | heute 2 TB/Jahr, Faktor", 25 / 2)
```

**Ausgabe:**

```text
5 Jahre ohne Zuschläge  A: 690000  B: 540000  C: 620000
Budget 650.000: Rest    A: -40000  B: 110000  C: 30000
Monatlich im Mittel     A: 11500  B: 9000  C: 10333
Aufpreis zu B           A: 150000  C: 80000
Zuschlag Cloud, 25 TB konstant (12 Monate roh): 180000 | alles behalten: 612000 [3000, 6000, 10500, 13500, 18000]
A mit 12 Monaten roh: 870000 | A alles behalten: 1302000
B, falls Maschinendaten roh in der Cloud (12 Monate): 720000 | B, Rohdaten im Haus, nur verdichtet in der Cloud: 540000
Preis + 0 % pro Jahr   A Cloud: 540000 Mehr: 0 | B Cloud: 300000 Mehr: 0
Preis + 5 % pro Jahr   A Cloud: 596768 Mehr: 56768 | B Cloud: 331538 Mehr: 31538
Preis +10 % pro Jahr   A Cloud: 659351 Mehr: 119351 | B Cloud: 366306 Mehr: 66306
Preis +20 % pro Jahr   A Cloud: 803693 Mehr: 263693 | B Cloud: 446496 Mehr: 146496
Black Friday: 90.000 € / 3 h = 30000 € pro Stunde
99,95 % erlaubt Ausfall pro Jahr: 4.38 h | bei 30.000 €/h: 131400 € | bei Ø-Umsatz/h (41 Mio./8.760): 20500 €
2025 tatsächlich: 3 h = 0.034 % Ausfall, Verfügbarkeit 99.966 %
Elektromarktkette 22 % von 41 Mio. €: 9020000 pro Jahr, 5 Jahre: 45100000
Ausbau Netz 1 Gbit: 36000 € in 5 Jahren
25 TB/Jahr im Mittel: 6.3 Mbit/s = 2.5 % von 250 Mbit/s
10 TB einmal hochladen bei 250 Mbit/s (volle Leitung): 3.7 Tage | bei 1 Gbit/s: 0.9 Tage
Datenmenge 5 Jahre (25 TB/Jahr): 125 TB | heute 2 TB/Jahr, Faktor 12.5
```
