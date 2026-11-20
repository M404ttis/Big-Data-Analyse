# Transferprojekt (UE 8): Kessler Pumpen AG

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI), bewusst kurz | [→ Teil B](#teil-b-lösungsentwurf) |

**Rolle:** Chief Data Officer, berichtet an den Vorstand. **Auftrag:** datengetriebene Geschäftsstrategie als Entscheidungsvorlage in 6 Monaten, in Entscheidungen denken, nicht in Einzelmaßnahmen. Die Titelfolie nennt „5 Outputs“, die Folien 7–8 listen **6 Ergebnisse**. Hier sind es sechs.

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Unternehmen und Markt

| Thema | Angabe |
|---|---|
| Firma | Hersteller von Industriepumpen (Wasserwirtschaft, Chemie), Bielefeld, 650 Mitarbeitende |
| Umsatz | 140 Mio. €, Ersatzteilgeschäft 22 % davon, sinkend |
| Ersatzteile | 30,8 Mio. € (vor 3 Jahren 36 Mio. €), Marge ca. 38 %, Kunden kaufen zunehmend bei Nachbauern |
| Installierte Pumpen | 18.000: 7.500 Wasserwerke, 4.200 Chemie, Rest Industrie, Ø Alter 9 Jahre |
| Wettbewerb | Asiatische Anbieter 20 % günstiger. Ein deutscher Wettbewerber bietet Zustandsüberwachung für 39 € je Pumpe und Monat, Kundenzahlen unbekannt |

### Service und Sensorik

| Thema | Angabe |
|---|---|
| Service | 46 Techniker, ca. 9.000 Einsätze pro Jahr, 60 % ungeplant, Ø 1.100 € je Einsatz |
| Nachrüstsensor | ca. 450 € je Pumpe + 8 € Datenübertragung pro Monat |
| Neupumpen | ca. 300 € Mehrkosten mit Sensor |

### Datenlage

| System | Inhalt | Qualität | Zuständig |
|---|---|---|---|
| ERP (seit 2012) | Aufträge, Kunden, Ersatzteile | Kunden teils mehrfach angelegt | IT |
| Service-Tickets (seit 2019) | Störungen, Einsätze, Ursachen | Ursache in 45 % „Sonstiges“ | Service |
| Prüfstand (seit 2008) | Messwerte von ca. 60.000 Pumpen bei Auslieferung | vollständig, nur lokal (Dateien auf einem Rechner) | Qualität |
| Händlerportal | Bestellungen der Vertriebspartner | keine Angabe des Endkunden | Vertrieb |
| Installierte Pumpen | – | keine Daten nach Auslieferung | niemand |

### Rahmen

| Thema | Angabe |
|---|---|
| Budget, Team | 600.000 € für 2 Jahre, 2 IT-Mitarbeitende für Datenthemen, kein Data-Science-Team |
| Kunden | Zwei große Wasserverbände dürfen laut Satzung keine Betriebsdaten außer Haus geben |
| Vorgeschichte | „Kundenportal“ 2019 begonnen, nach 9 Monaten ohne Ergebnis gestoppt |
| Sonstiges | 100-jähriges Jubiläum 2027 (Jubiläumsbuch), neue Lackieranlage 2,3 Mio. € aus dem Werksbudget |
| Kernentscheidung (Folie 9) | Sofort Sensorik einbauen (schneller Anschluss, hohe Kosten ohne gesicherte Nachfrage, Betriebsdaten in 6 Monaten) **oder** erst vorhandene Daten nutzen (Tickets und Prüfstand, geringe Kosten, schnelle Erkenntnisse, Risiko: Markt dann verteilt) |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Servicekosten pro Jahr | 9.000 Einsätze × 1.100 € | 9,9 Mio. € |
> | davon ungeplant | 60 % × 9.000 = 5.400 Einsätze × 1.100 € | 5,94 Mio. € |
> | Einsätze je Techniker und Jahr | 9.000 / 46 | ca. 196 |
> | Ungeplante Einsätze je Pumpe und Jahr | 5.400 / 18.000 | 0,3 (ca. 330 € je Pumpe) |
> | Anteil Wasserwerke / Chemie / Rest | 7.500, 4.200, 6.300 von 18.000 | 42 % / 23 % / 35 % |
> | Rückgang Ersatzteilumsatz | 30,8 / 36 − 1 | −14,4 % in 3 Jahren (ca. −5,1 % pro Jahr) |
> | Entgangener Ersatzteilumsatz | 36 − 30,8 Mio. € | 5,2 Mio. € pro Jahr |
> | Entgangene Marge | 5,2 Mio. € × 38 % | ca. 1,98 Mio. € pro Jahr |
> | Ersatzteilumsatz je Pumpe und Jahr | 30,8 Mio. € / 18.000 | ca. 1.711 € |
> | Ersatzteilmarge je Pumpe und Jahr | 1.711 € × 38 % | ca. 650 € |
> | Sensorkosten je Pumpe, 1. Jahr | 450 € + 12 × 8 € | 546 € |
> | Sensorkosten je Pumpe, 5 Jahre | 450 € + 60 × 8 € | 930 € (186 € pro Jahr, 15,50 € pro Monat) |
> | Preis des Wettbewerbs je Pumpe und Jahr | 39 € × 12 | 468 € |
> | Alle Pumpen nachrüsten | 18.000 × 450 € | 8,1 Mio. € (13,5-faches Budget) |
> | Pumpen, die das Budget allein für Sensoren trägt | 600.000 € / 450 € | 1.333 (7,4 % der Flotte) |
> | Ersatzteilumsatz in 3 Jahren bei gleichem Trend *(Annahme: −5,1 % jährlich)* | 30,8 Mio. € × 0,949³ | ca. 26,4 Mio. € (−4,4 Mio. €, Marge −1,7 Mio. €) |


---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Vision:** Kessler verkauft nicht nur Pumpen, sondern **Verfügbarkeit**. Der Hebel ist **nicht** die Abo-Gebühr, sondern der **Ersatzteilumsatz** (30,8 Mio. €, Marge ca. 650 € je Pumpe und Jahr), der um 5 % pro Jahr schrumpft.
> - **Entscheidung:** **Erst Daten, dann Sensor-Pilot mit 300 Pumpen**, kein Komplett-Einbau (8,1 Mio. €).
> - **Budget:** 300.000 € für Jahr 1, die zweiten 300.000 € nur bei erfüllten Kriterien.
> - **Risiko:** Der Pilot kostet höchstens ca. **193.000 €** (32 % des Budgets), wenn niemand zahlt.

> [!NOTE]
> Zahlen aus dem Aufgabenblatt sind in Teil A nachgerechnet. Alle anderen sind als **Annahme** markiert. Rechtliche Aussagen sind nicht geprüft.

## 1 · Vision

**In 5 Jahren verdient Kessler an der Pumpe, am Zustand der Pumpe und an den Teilen, die der Zustand auslöst.**

- Ein Kunde merkt: **weniger ungeplante Ausfälle**, Ersatzteil und Techniker kommen **geplant** statt im Notfall.
- Das ist ein anderes Geschäftsmodell als „Pumpe verkaufen“ (Folien: *datenbasierter Service*, später *Pay-per-Use*).
- Warum so? Der Verlust steckt im Ersatzteilgeschäft: **−5,2 Mio. € Umsatz, −2 Mio. € Marge pro Jahr** gegenüber vor 3 Jahren. Ein Abo allein bringt wenig: 1.000 überwachte Pumpen × 300 € (**Annahme**) = 0,3 Mio. € pro Jahr.

## 2 · Drei Kernentscheidungen

| # | Entscheidung | Zurückgestellt |
|:---:|---|---|
| **1** | **Daten zuerst:** Tickets und Prüfstand über die Seriennummer verbinden, Ursache zum Pflichtfeld machen. Kosten klein, Ergebnis in 3–4 Monaten. | Eigene große Datenplattform, Data-Science-Team |
| **2** | **Sensor-Pilot mit 300 Pumpen** (Chemie und Industrie), danach erst Ausbau. | Nachrüstung der ganzen Flotte (8,1 Mio. €), Sensor-Pflicht in Neupumpen (+300 €, die Pumpe ist schon 20 % teurer als die asiatische) |
| **3** | **Zustandsüberwachung als Service-Vertrag** mit Preistest (20–39 € je Monat), verknüpft mit Ersatzteil-Lieferung. | Neues Kundenportal (2019 gescheitert), die beiden Wasserverbände |

**Widerspruchsfrei:** 1 liefert die Fehlerbilder für 2, 2 liefert Daten und Kunden für 3. Alles bleibt innerhalb von 2 IT-Leuten, mit externem Partner für Integration.

## 3 · Risikoanalyse

| Frage | Zahl |
|---|---:|
| Pilot, wenn **niemand** die Sensorpumpe will: 300 × 450 € + 300 × 8 € × 24 Monate | **ca. 193.000 €** (32 % des Budgets) |
| **Teuerste Fehlentscheidung:** Sensorik breit einbauen, z. B. 5.000 Pumpen (28 % der Flotte) ohne Nachfragenachweis | **ca. 2,7 Mio. €** im 1. Jahr (4,5-faches Budget) |
| **Nichtstun:** Ersatzteilumsatz in 3 Jahren bei gleichem Trend (**Annahme**) | **−4,4 Mio. € Umsatz, −1,7 Mio. € Marge pro Jahr** |

**Frühwarnzeichen im Pilot:**

| Kennzahl | Warnwert (**Annahme**) |
|---|---|
| Pumpen, die stabil Daten senden | unter 90 % |
| Pilotkunden, die einen bezahlten Vertrag wollen | unter 30 % |
| Ungeplante Einsätze im Pilot gegenüber Vergleichspumpen | kein Rückgang |
| Ersatzteilbestellungen bei Kessler (Pilotpumpen gegenüber Vergleichspumpen) | kein Anstieg |

Der Vergleich geht gegen **ähnliche Pumpen ohne Sensor** (gleiches Alter, gleiche Branche), nicht gegen „vorher“.

## 4 · Investitionsstrategie

| Stufe | Zeitraum | Budget | Inhalt |
|:---:|---|---:|---|
| **1** | Monat 1–12 | **300.000 €** | Datenanalyse 60.000 €, 300 Sensoren 135.000 €, Datenübertragung 29.000 €, Integration und Plattform (Partner) 50.000 €, Vertragsangebot und Preistest 25.000 € |
| **2** | Monat 13–24 | **300.000 €** | 400 weitere Sensoren 180.000 €, Datenübertragung 67.000 €, Plattform 30.000 €, Reserve 23.000 € |

**Freigabe von Stufe 2 nach 12 Monaten** (alle vier, Schwellen **Annahme**):

1. Mindestens **90 %** der Pilotpumpen senden stabil.
2. Mindestens **100 Pumpen** mit **unterschriebenem bezahltem Vertrag** (≥ 20 € im Monat).
3. Das Modell meldet mindestens **50 %** der ungeplanten Ausfälle **mindestens 2 Wochen vorher**.
4. Keine Verletzung der Datenvorgaben von Kunden.

Danach decken 300.000 € nur rund 700 Pumpen ab (3,9 % der Flotte). **Der weitere Ausbau muss sich über die Kunden finanzieren** (Abo oder Sensor als Leasing), nicht über das Budget.

## 5 · Governance

| Frage | Regelung |
|---|---|
| **Datenzugang** | CDO entscheidet im **Datenrat** (CDO, Service, Vertrieb, Qualität, IT, Datenschutz). Grundsatz: nur Daten, für die es einen Zweck und das Einverständnis des Kunden gibt. |
| **Preise für Datenservices** | Vertrieb schlägt vor, **Vorstand gibt frei**. Anfangs Preistest, dann Festlegung. |
| **Neue Datenprojekte** | Antrag an den Datenrat mit Nutzen, Kosten und Messgröße. Ohne Messgröße kein Start (Lehre aus dem Kundenportal 2019). |
| **Kundendaten im ERP** | **Eigentümer: Vertrieb** (Inhalt und Bereinigung der Dubletten), **IT** technisch zuständig. |
| **Wasserverbände** | Betriebsdaten bleiben **beim Kunden** (Auswertung vor Ort), Kessler bekommt nur Ergebnisse und Alarme. Ob das nach deren Satzung reicht, ist **nicht geprüft**. |

## 6 · Entscheidung trotz Lücke

**Unbekannt:** Ob Kunden für Zustandsüberwachung zahlen. Belegt ist nur der Wettbewerbspreis (39 €), nicht dessen Absatz.

**Entscheidung:** Pilot mit 300 Pumpen **jetzt**, Ausbau nur bei Zahlungsnachweis.

| Argument | Zahl |
|---|---|
| Wir brauchen mindestens | ca. **15,50 € pro Monat** (Sensor und Daten über 5 Jahre, ohne Plattform) |
| Wettbewerb nimmt | **39 €** |
| Eine Pumpe kostet uns durch ungeplanten Einsatz | ca. **330 €** im Jahr |
| Eine Pumpe bringt uns als Ersatzteilmarge | ca. **650 €** im Jahr |

**Bewusst eingegangenes Risiko:** bis zu **193.000 €** im Pilot, und der **Markt verteilt sich weiter**, weil wir erst Daten auswerten und dann ausbauen. Das Risiko ist begrenzt, ein 6-monatiges Warten kostet dagegen sicher Marge.

---

## 7 · Python-Check

```python
# python3 -I check.py
print("Service:", 9000 * 1100, "ungeplant:", 0.6 * 9000 * 1100)
print("Ersatzteile Rückgang:", round(30.8 / 36 - 1, 3), "Marge entgangen:", round((36 - 30.8) * 0.38, 2))
print("Ersatzteilmarge je Pumpe:", round(30.8e6 / 18000 * 0.38))
print("Sensor 1. Jahr / 5 Jahre / pro Monat:", 450 + 8 * 12, 450 + 8 * 60, (450 + 8 * 60) / 60)
print("Flotte nachrüsten:", 18000 * 450, "Budget deckt Pumpen:", round(600000 / 450))
print("Pilot-Verlust:", 300 * 450 + 300 * 8 * 24)
print("5.000 Pumpen Jahr 1:", 5000 * 450 + 5000 * 8 * 12)
print("Stufe 1:", 60 + 135 + 28.8 + 50 + 25, "Stufe 2:", 180 + 38.4 + 28.8 + 30 + 22.8)
```
