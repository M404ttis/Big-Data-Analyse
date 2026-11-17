# Tag 2 (Modul 3), Arbeitsauftrag 3: Datenstrategie statt neuer Speicher bei Hollmann Möbelwerke GmbH

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Mattis Lösung**: Fakten, Rechnungen, leere Raster | [→ Teil A](#teil-a-mattis-lösung) |
> | **B** | **Lösungsentwurf** (KI): zum Vergleichen, *nach* dem eigenen Entwurf lesen | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Bei 440 TB (Speicher zu 88 % voll) festlegen, (1) wo sich die Menge **ohne Informationsverlust** verringern lässt, (2) **was bleibt, wie lange, in welcher Form**, (3) **wo nicht gekürzt** werden darf, (4) die **Ersparnis in TB und € pro Jahr** schätzen.

---

# Teil A: Mattis Lösung

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Die acht Datenbestände

| Kategorie | TB | Zuwachs TB/Jahr | Was gespeichert wird | Wer nutzt es wie |
|---|---:|---:|---|---|
| Logfiles | 148 | 46 | alle Meldungen aller Server, Programme, Maschinensteuerungen seit 2014, auch Testausgaben | IT: letzte 2–3 Wochen. Sicherheitsprüfung: Anmeldungen letzte 12 Monate (0,4 TB/Jahr). Älteres nie geöffnet |
| Maschinendaten | 96 | 28 | Temperatur, Feuchte, Laufzeit, jede Sekunde seit 2017 | Instandhaltung: letzte 3 Monate sekundengenau. Qualität: Stundenwerte über Jahre |
| Datensicherungen | 74 | 12 | jede Nacht Sicherung aller Systeme, jede seit 2019 | 31 Rücksicherungen in 6 Jahren, immer aus den letzten 2 Wochen |
| Netzlaufwerke | 41 | 5 | Ordner je Abteilung, Produktkatalog 14-mal abgelegt | 63 % der Dateien seit über 3 Jahren nicht geöffnet |
| CAD & Fotos | 38 | 4 | jede Zwischenspeicherung als Version (Ø 60 je Bauteil), Katalogfotos im Rohformat | Konstruktion holt freigegebene Versionen, bei Ersatzteilen auch 15 Jahre alte |
| E-Mail-Archiv | 21 | 2,5 | alle Mails aller Mitarbeitenden seit 2009 mit Anhängen | Rechnungen und Aufträge teils per Mail, Suche etwa einmal pro Woche |
| Video | 18 | 3 | 24 Kameras, Daueraufzeichnung seit 2020 | zweimal angesehen, jeweils am Tag nach einem Einbruch |
| ERP | 4 | 0,3 | Aufträge, Rechnungen, Buchungen seit 2016 | täglich: Controlling, Vertrieb, Einkauf |

### Rahmen

| Thema | Angabe |
|---|---|
| Speicher | 500 TB Kapazität, zu 88 % belegt. Erweiterung um 250 TB: 120.000 € einmalig |
| Kosten | 290 € je TB und Jahr (Strom, Kühlung, Wartung, Spiegelung in Werk B) |
| Aufbewahrung | Rechnungen und Buchungsbelege 8 Jahre, Geschäftsbriefe 6 Jahre, Konstruktionsunterlagen bis 10 Jahre nach dem letzten Verkauf |
| IT-Team | 6 Personen, Umzug in neuen Serverraum in Werk A 2027 |
| Sonstiges | 75-jähriges Bestehen nächstes Jahr, neue Website geht im Mai online |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Gesamtbestand | Summe der acht Kategorien | 440 TB |
> | Zuwachs gesamt | 46 + 28 + 12 + 5 + 4 + 2,5 + 3 + 0,3 | 100,8 TB pro Jahr |
> | Freier Platz | 500 − 440 | 60 TB |
> | Speicher voll in | 60 / 100,8 × 12 Monate | ca. 7 Monaten |
> | Laufende Kosten heute | 440 TB × 290 € | 127.600 € pro Jahr |
> | Preis Erweiterung | 120.000 € / 250 TB | 480 € je TB einmalig |
> | Erweiterung reicht für | 250 / 100,8 | ca. 2,5 Jahre |
> | Größte drei (Logfiles, Maschinen, Sicherungen) | (148 + 96 + 74) / 440 | 318 TB = 72 % des Bestands |
> | Anteil Logfiles am Zuwachs | 46 / 100,8 | 46 % |
> | Nie angefasste Netzlaufwerk-Dateien | 63 % × 41 TB | ca. 25,8 TB |
> | Kosten Video je Ansicht | 18 TB × 290 € = 5.220 € pro Jahr, zwei Ansichten in 6 Jahren | ca. 5.220 € pro Jahr für 2 Ansichten |
> | Rücksicherungen | 31 / 6 Jahre | ca. 5 pro Jahr |

## Schritt 1 · Ergebnisraster

| Kategorie | Was bleibt, wie lange, in welcher Form? | Ersparnis (TB) | Ersparnis (€/Jahr) |
|:---|:---|:---:|:---:|
| **Logfiles** | 0,4TB Anmeldungen + 3TB für Störungen | 144 | 290€*144= |
| **Maschinendaten** | 2Jahre für ML, 56TB | 40TB | |
| **Datensicherungen** | 2xdie letzte Datensicherung speichern, unterschiedliche Orte | 73,5 TB | 73,5 |
| **Netzlaufwerke** | 1 Katalog des letzten Jahres | 40TB | |
| **CAD & Fotos** | nur letzte CAD Version gesaved, Fotos nur einmal 0,5 CAD + 0,5 Fotos| 37 | |
| **E-Mail-Archiv** | Rechnungen als uniques ins ERP, Anhänge löschen, Mails als text behalten | 20TB | |
| **Video** | nur die letzten 2 Wochen  | | |
| **ERP** | <br><br> | | |
| **Summe** | | | |

## Schritt 2 · Wo darf nicht gekürzt werden?

| Was | Warum nicht? |
|:---|:---|
| 1 | <br><br> |
| 2 | <br><br> |
| 3 | <br><br> |

## Schritt 3 · Gesamtbild

| Frage | Meine Antwort |
|:---|:---|
| Belegung nach der Bereinigung | <br><br> |
| Erweiterung nötig? | <br><br> |
| Wie wird es dauerhaft verhindert? | <br><br> |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Ergebnis:** ca. **366 TB weniger** (von 440 auf 74 TB), das sind ca. **106.000 € pro Jahr** (von 127.600 auf 21.000 €). Die Erweiterung für 120.000 € entfällt.
> - **Hebel:** Logfiles, Maschinendaten und Sicherungen machen 72 % des Bestands aus und bringen ca. 304 der 366 TB. Alle drei haben eine Nutzung, die nur wenige Wochen oder Monate zurückreicht.
> - **Nicht gekürzt:** ERP, freigegebene CAD-Versionen, Rechnungs- und Auftragsmails, aktuelle Sicherungen und Sicherheitslogs, Katalogfotos im Rohformat bis nach Jubiläum und Website.
> - **Wichtiger als das Löschen:** Der Zuwachs von 100,8 TB pro Jahr sinkt durch **automatische Löschfristen** auf ca. 10 TB pro Jahr. Ohne sie wäre der Speicher in 7 Monaten wieder voll.

> [!NOTE]
> **Annahmen**, die nicht auf dem Blatt stehen: CAD und Fotos je zur Hälfte (19 TB), von 60 Versionen bleiben ca. 3 freigegebene. Von den nie geöffneten Netzlaufwerk-Dateien lassen sich 80 % löschen oder als Duplikat entfernen. Vom E-Mail-Archiv sind ca. 30 % älter als 8 Jahre. Die Sicherungen sind inkrementell, eine Nacht entspricht ca. 0,03 TB (Zuwachs 12 TB / 365). Der Zuwachs von ca. 10 TB pro Jahr nach der Bereinigung ist eine Überschlagsrechnung (Netzlaufwerke 5 + CAD & Fotos 4 + ERP 0,3, alle rollierenden Bestände wachsen nicht mehr). Die Rechtsfristen sind die des Blatts, nicht geprüft. Mit der Dauer der Videoaufbewahrung muss der Datenschutz einverstanden sein.

## Schritt 1 · Ergebnisraster

| Kategorie | Was bleibt, wie lange, in welcher Form? | TB | €/Jahr |
|:---|:---|---:|---:|
| **Logfiles** | **Sekundengenaue Logs 3 Wochen** (ca. 3 TB, gerundet 4 TB). **Anmelde-Logs 12 Monate** gefiltert (0,4 TB). Testausgaben nicht mehr schreiben. Alles ältere löschen | 144 | 41.760 |
| **Maschinendaten** | **Sekundenwerte 3 Monate** (7 TB). Danach **Stundenwerte** (Mittel, Min, Max), dauerhaft für die Qualitätsauswertung (< 0,1 TB). Reduktion um den Faktor 3.600 | 88 | 25.520 |
| **Datensicherungen** | **14 Nächte** plus **12 Monatssicherungen** (ca. 2 TB). Ältere löschen, da nie benötigt | 72 | 20.880 |
| **Netzlaufwerke** | **Duplikate entfernen** (Produktkatalog 14 mal), nie geöffnete Dateien nach Ankündigung an die Abteilungen löschen. Was unter eine Aufbewahrungsfrist fällt (Geschäftsbriefe 6 Jahre), geht ins Archiv | 21 | 6.090 |
| **CAD & Fotos** | **CAD:** freigegebene Versionen bis 10 Jahre nach letztem Verkauf, Zwischenstände nach Freigabe löschen. **Fotos:** Rohformat bleibt bis nach Jubiläum und Website-Start, danach in kalten Speicher | 18 | 5.220 |
| **E-Mail-Archiv** | **Rechnungen und Aufträge 8 Jahre**, Geschäftsbriefe 6 Jahre, Rest kürzer. Alles über 8 Jahre löschen, Anhänge nur einmal speichern | 6 | 1.740 |
| **Video** | **14 Tage Schleife**. Material zu einem Einbruch wird als Vorfall separat bis zum Abschluss gesichert | 17,5 | 5.075 |
| **ERP** | **Unverändert.** Täglich genutzt, Belege 8 Jahre | 0 | 0 |
| **Summe** | | **366,5** | **106.285** |

**Danach:** 73,5 TB belegt (14,7 % von 500 TB), Kosten ca. 21.300 € pro Jahr.

## Schritt 2 · Wo darf nicht gekürzt werden?

| Was | Warum nicht? |
|:---|:---|
| **ERP** | täglich genutzt, Rechnungen und Buchungsbelege müssen 8 Jahre bleiben, nur 4 TB |
| **Freigegebene CAD-Versionen** | 10 Jahre nach dem letzten Verkauf, Ersatzteilanfragen holen 15 Jahre alte Stände |
| **Rechnungs- und Auftragsmails** | kommen zum Teil per Mail, Frist 6 bis 8 Jahre. Die Suche pro Woche zeigt: das Archiv wird genutzt |
| **Sicherungen der letzten 14 Tage, Anmelde-Logs 12 Monate** | alle 31 Rücksicherungen kamen aus diesem Zeitraum, die Sicherheitsprüfung nutzt 12 Monate |
| **Stundenwerte der Maschinen** | Qualitätsauswertungen laufen über Jahre |
| **Katalogfotos im Rohformat** | 75-jähriges Jubiläum und neue Website im Mai brauchen Originale, Archivierung erst danach |

## Schritt 3 · Gesamtbild

- **Reihenfolge:** erst bereinigen, dann umziehen. Der Serverraum-Umzug 2027 überträgt dann 74 statt 440 TB.
- **Schnell und sicher:** Logfiles, Maschinendaten, Sicherungen und Video (ca. 321 TB) haben klare Nutzungsfenster und brauchen nur eine technische Löschregel. Netzlaufwerke, CAD und Mails brauchen **Abstimmung mit Fachbereichen und Rechtsabteilung**.
- **Dauerhaft:** Löschfristen je Kategorie als automatische Regel (Aufbewahrungsplan mit verantwortlicher Person je Kategorie), Prüfung einmal im Jahr.
- **Beitrag zu Green Data:** weniger gespeicherte Daten heißen weniger Strom und Kühlung, ca. 366 TB × 290 € = 106.000 € pro Jahr.

## Python-Check

```python
# python3 -I check.py
kat = {"Logfiles": (148, 46), "Maschinen": (96, 28), "Sicherungen": (74, 12), "Netz": (41, 5),
       "CAD&Fotos": (38, 4), "Mail": (21, 2.5), "Video": (18, 3), "ERP": (4, 0.3)}
gesamt = sum(v[0] for v in kat.values())          # 440
zuwachs = sum(v[1] for v in kat.values())         # 100.8
print(gesamt, zuwachs, 500 - gesamt, (500 - gesamt) / zuwachs * 12, gesamt * 290)

ersparnis = {"Logfiles": 148 - 4, "Maschinen": 96 - 8, "Sicherungen": 74 - 2,
             "Netz": round(0.63 * 41 * 0.8), "CAD&Fotos": round(19 * (1 - 3 / 60)),
             "Mail": round(21 * 0.3), "Video": 18 - 0.5, "ERP": 0}
summe = sum(ersparnis.values())
print(summe, summe * 290, gesamt - summe, (gesamt - summe) / 500, (gesamt - summe) * 290)
print(46 * 3 / 52 + 0.4, 28 * 3 / 12, 96 / 3600, 14 * 12 / 365)
```

Ergebnis: 440 TB, Zuwachs 100,8 TB pro Jahr, Speicher in ca. 7,1 Monaten voll, 127.600 € pro Jahr. Ersparnis 366,5 TB = 106.285 € pro Jahr, Rest 73,5 TB (14,7 %), 21.315 € pro Jahr. Logfile-Fenster ca. 3,05 TB, Maschinen-Sekundenwerte 7 TB, Stundenwerte 0,027 TB, 14 Sicherungsnächte 0,46 TB.
