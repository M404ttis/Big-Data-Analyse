# Tag 11 · UE 3 · Arbeitsauftrag 2: Holm Agrarhandel, BI oder Python/R?

Aufgabe: Optionen bewerten, strategisch entscheiden, Risiken benennen. Rahmen: zwei Personen, Budget 40.000 € pro Jahr, erste Ergebnisse in drei Monaten.

## Teil A: Fakten und Rechnungen

**Kosten je Option (pro Jahr, in €)**

| Posten | A) BI für alle | B) Python/R | C) Kombination |
|---|---|---|---|
| Lizenzen / Werkzeuge | 25.000 | 10.000 | 30.000 |
| Python-Kurs, 1 Person (4.500) | – | 4.500 | 4.500 |
| Python-Kurs, beide Personen | – | 9.000 | 9.000 |
| Börsendaten Einkauf (4.800) | nicht nutzbar | 4.800 | 4.800 |
| **Summe, 1 Kurs, mit Börsendaten** | 25.000 | **19.300** | **39.300** |
| **Summe, 2 Kurse, mit Börsendaten** | 25.000 | **23.800** | **43.800** |
| Abstand zum Budget (40.000), 1 Kurs | 15.000 frei | 20.700 frei | **700 frei** |
| Abstand zum Budget, 2 Kurse | 15.000 frei | 16.200 frei | **−3.800 (überschritten)** |

Zusatzrechnungen:

- A kostet je Lizenz 25.000 / 40 = **625 €** pro Jahr. Mit dem Tableau-Rabatt (20 %) wären es 20.000, also 5.000 gespart. A deckt aber die Preisprognose des Einkaufs nicht ab. Der Rabatt ändert das nicht.
- C voll ausgereizt (30.000 + 4.500 + 4.800) liegt bei 39.300 und damit nur 700 € unter dem Budget. Ein zweiter Kurs sprengt es.
- C ohne Börsendaten im ersten Schritt: 34.500, Reserve 5.500.
- Von 30 Führungskräften plus Datenteam (2) und Marketing sind 40 Lizenzen in A knapp bemessen, aber plausibel.

Nicht entscheidungsrelevant: die Zahl der Beschäftigten (380). Die **14 Standorte** zählen dagegen (Kosten je Standort in den Berichten).

## Teil B: Bewertungsraster

Bewertung: ++ sehr gut, + gut, ○ mit Einschränkung, − schlecht.

| Anforderung | A) BI | B) Python/R | C) Kombination |
|---|---|---|---|
| **Monatsberichte Controlling** (30 Leser, gleiche Struktur, Handy) | **++** Dashboards mit mobiler App, Filter je Standort, Daten per ERP-Anbindung aktualisiert sich selbst. M365 ist im Haus | **○** Automatische PDFs sind technisch gut machbar (gleiche Struktur, parametrisiert, auch gedruckt für den Geschäftsführer). Auf dem Handy aber nur statisch, keine Filter | **++** wie A |
| **Kampagnenanalyse Marketing** (24 Kampagnen, Webshop, Newsletter, Kundenkarte) | **○** Gute Visualisierung, aber Verknüpfung der drei Quellen (Kunden-IDs) und Wirkungsanalyse (Neukunden je Kampagne, Vergleich mit Kontrollgruppe) geht nur eingeschränkt | **++** Daten zusammenführen, Wirkung rechnen, Test auf Signifikanz | **++** Python für die Analyse, Ergebnisse bei Bedarf ins Dashboard |
| **Preisprognosen Einkauf** (6 Monate, Dünger/Saatgut) | **−** Prognosen sind nicht Kern der Werkzeuge (nur einfache Trendlinien) | **++** Zeitreihenmodelle, Szenarien, Backtests | **++** |
| **Aufwand für das Team** (2 Personen, 3 Monate) | **+** Passt zu Person 1 (Excel/SQL, schneller Einstieg), keine Kurse nötig | **−** Alles per Code, Person 2 hat nur Grundkenntnisse, R nie genutzt, Kurs bis zur Produktivität dauert. 30 Berichte, Marketing, Prognose gleichzeitig ist zu viel | **○** Zwei Werkzeuge, aber **klare Aufgabenteilung**: Person 1 BI, Person 2 Python |
| **Risiken** | Deckt den Einkauf nicht ab. Lizenzkosten laufen jedes Jahr. Anbieterbindung. Rabattdruck | Sehr abhängig von einer Person (Code). Handy-Lesbarkeit. Zeitrahmen kaum haltbar | Budget fast aufgebraucht (700 € Reserve). Zwei Werkzeuge, zwei Wissensinseln |

## Teil C: Strategische Entscheidung

**Empfehlung: Option C, aber stufenweise eingeführt.**

| Phase | Zeitraum | Inhalt | Wer |
|---|---|---|---|
| 1 | Monat 1–3 | **Controlling-Monatsberichte** als BI-Dashboard mit Handy-Ansicht und PDF-Export für den Geschäftsführer | Person 1 (Excel/SQL, M365 vorhanden) |
| 1 parallel | Monat 1–3 | Python-Kurs für **eine** Person, danach erste Auswertung zu 3–4 der 24 Kampagnen | Person 2 |
| 2 | Monat 4–6 | Kampagnenanalyse für alle 24 Kampagnen | Person 2 |
| 3 | ab Monat 6 | Preisprognose, zunächst mit **eigenen Einkaufspreisen**. Börsendaten (4.800 €) erst, wenn der Test zeigt, dass sie die Prognose verbessern | Person 2 |

Begründung:

- **Controlling zuerst**, weil es der klarste Bedarf ist (30 Leser, gleiche Struktur, feste Datenquelle ERP) und der schnellste sichtbare Erfolg innerhalb von drei Monaten.
- **BI hier**, weil es auf dem Handy am besten funktioniert und zu den Fähigkeiten von Person 1 passt.
- **Python dort, wo Analyse zählt** (Marketing, Prognose), weil BI das nicht leistet.
- **Rabatt nicht annehmen**, wenn das nur der Frist wegen geschieht. Eine Lizenzentscheidung unter Zeitdruck ist ein Verkaufsargument, kein Sachargument. Wenn ohnehin Tableau gewünscht wäre, kann der Rabatt in der Verhandlung bleiben. Mit M365 im Haus ist Power BI jedoch naheliegender (Integration, Anmeldung, Lizenzprüfung).
- **Budget**: 34.500 € im Grundstock (30.000 + ein Kurs), 5.500 € Reserve. Börsendaten und ein zweiter Kurs erst nach Phase 2.
- **Alternative B** wäre mit 19.300 € billiger und für Controlling per PDF vertretbar, scheitert aber an der Arbeitslast für zwei Personen und an der fehlenden Handy-Interaktivität.

## Teil D: Risiken und Gegenmaßnahmen

| Risiko | Wirkung | Gegenmaßnahme |
|---|---|---|
| **Eine Person kündigt** | Wissen und laufende Berichte hängen an einer Person (Person 1: BI, Person 2: Python) | Dokumentation, Code in Versionsverwaltung (Git), Berichte parametrisiert und einfach gehalten, gegenseitige Einarbeitung (je ein Tag pro Monat), Vertretung über externe Dienstleister oder Werkstudierende. Excel/SQL und Power BI sind am Markt leicht zu besetzen |
| **Budget** | Nur 700 € Reserve, wenn alles gebucht wird | Stufenplan, Börsendaten und zweiten Kurs verschieben, Kosten monatlich mit dem Controlling prüfen |
| **Zeit** | Drei Monate für zwei Personen und drei Anforderungen | Nur **Controlling** in Phase 1 fest zusagen, Marketing als Pilot, Einkauf später. Erwartungen schriftlich klären |
| **Datenqualität** | Kunden-IDs in Webshop, Newsletter und Kundenkarte passen evtl. nicht zusammen | Früh eine Stichprobe prüfen (siehe Tag 8). Wenn sie fehlt, Kampagnenwirkung nur eingeschränkt belastbar |
| **Prognosegüte** | Preisprognose für sechs Monate ist unsicher, Dünger wird von Weltmärkten bestimmt | Prognose mit Unsicherheitsband statt Einzelwert, Backtest gegen einfache Vergleichsprognose, Entscheidung nicht allein davon abhängig machen |
| **Akzeptanz** | 30 Führungskräfte müssen die Berichte wirklich nutzen, Geschäftsführer liest gedruckt | Druckfähige PDF-Version desselben Berichts, Einführung mit zwei bis drei Pilotnutzern, Feedback nach dem ersten Monat |
| **Rechte und Datenschutz** | Kampagnendaten (Kundenkarte) sind personenbezogen | Auswertung aggregiert, Zugriffsrechte im BI-Werkzeug je Standort und Rolle, Datenschutz vor Start klären |
| **Lizenzbindung** | Jahreslizenz, Preissteigerung | Vertragsdauer und Kündigungsfrist prüfen, mit Rabatt nur bei kurzer Bindung annehmen |

## Teil E: Plenum-Leitfragen

**Welche Option haben Sie gewählt?** C, stufenweise: BI für Controlling, Python für Marketing und Einkauf.

**Was passiert, wenn eine der zwei Personen kündigt?** Ohne Vorsorge fällt die Hälfte der Leistung aus (wer BI kann oder wer Python kann). Gegenmaßnahmen sind Dokumentation, Git, Standardwerkzeuge, Tandem-Einarbeitung und ein externer Backup-Kontakt. Fällt Person 2 aus, sind Marketing und Einkauf pausiert, Controlling läuft weiter. Fällt Person 1 aus, laufen die Dashboards vorerst weiter, Änderungen aber nicht.

**Welche Anforderung kommt zuerst?** Controlling. Klarer Bedarf, feste Struktur, saubere Quelle, größter Leserkreis, schnell erreichbar, und es schafft Vertrauen für die späteren Projekte.
