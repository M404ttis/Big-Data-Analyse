# Tag 6 (Modul 3), Fallstudie ShopNow: Prognose und Feedback im Online-Handel

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI) | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Für die ShopNow GmbH (Budget 700.000 €, messbare Ergebnisse in 12 Monaten): (1) **Kunden mit hoher Kaufwahrscheinlichkeit** identifizieren, (2) den **zukünftigen Umsatz prognostizieren**, (3) das **Kundenfeedback nach Stimmung** analysieren, (4) **Maßnahmen** ableiten. Dazu das Raster Baustein / Daten / Ergebnis / Maßnahme ausfüllen.

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Das Unternehmen

| Thema | Angabe |
|---|---|
| Firma | ShopNow GmbH, Online-Händler für Sport- und Freizeitbekleidung, 210 Mitarbeitende, 1,1 Mio. Kunden |
| Umsatz | 74 Mio. €, Wachstum zuletzt nur 2 % |
| Problem | 71 % der Warenkörbe werden nicht abgeschlossen. Viele Neukunden kaufen nur einmal |
| Daten | Kauf- und Klickdaten seit 4 Jahren, 95.000 Kundenbewertungen, 40.000 Service-E-Mails pro Jahr |
| Rahmen | Budget 700.000 €, Ergebnisse in 12 Monaten messbar |

### Shop und Daten im Detail

| Thema | Angabe |
|---|---|
| Besuche | 4,8 Mio. pro Monat, 1,9 % kaufen, Ø Warenkorb 68 € |
| Kunden | 1,1 Mio. Kundenkonten, davon 61 % mit nur einem Kauf. Kauf ohne Konto nicht möglich |
| Versand | 4,95 € unter 60 € Bestellwert, wird **erst im letzten Schritt** angezeigt |
| Retouren | 38 % der Artikel kommen zurück, eine Retoure kostet ca. 11 € |
| Datenbestände | Klickdaten ca. 9 TB, **nur bei Einwilligung** (ca. 64 % der Besuche). E-Mails **ohne Bezug zur Bestellung** |

### Was Sie außerdem erfahren

| Thema | Angabe |
|---|---|
| Team | 2 Analysten, 1 Data Engineer. Shop-Entwicklung extern, ein Entwicklertag kostet 900 € |
| Einkauf | Bestellt 6 Monate im Voraus. 2025 wurden Überbestände von 4,3 Mio. € abgeschrieben |
| Wettbewerb | Der größte Konkurrent liefert ab 30 € versandkostenfrei |
| Marketing | Kooperation mit zwei Profisportlern, 380.000 € pro Jahr, Vertrag bis 2028 |
| Logistik | Seit März versendet ein neues Lager in Erfurt |

### Abbruchstellen (Anteil der Abbrüche)

| Stelle | Warenkorb | Versandkosten | Registrierung | Zahlung |
|---|---:|---:|---:|---:|
| Anteil | 38 % | 27 % | 21 % | 14 % |

### Auszug aus den Kundenbewertungen

| Sterne | Bewertung |
|---:|---|
| 2 | „Schöne Jacke, aber die Größen fallen komplett anders aus als angegeben.“ |
| 4 | „Schnelle Lieferung. Rücksendung war leider kompliziert.“ |
| 1 | „Versandkosten erst ganz am Ende gesehen – Kauf abgebrochen.“ |
| 5 | „Top Qualität, bestelle immer wieder.“ |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Käufe pro Monat | 4,8 Mio. × 1,9 % | 91.200 |
> | Käufe pro Jahr | 91.200 × 12 | 1.094.400 |
> | Umsatz pro Jahr (Kontrolle) | 1.094.400 × 68 € | 74,4 Mio. € (Angabe: 74 Mio.) |
> | Warenkörbe pro Monat, wenn 29 % abgeschlossen werden | 91.200 / 0,29 | 314.483 |
> | Abgebrochene Warenkörbe pro Monat | 314.483 − 91.200 | 223.283 |
> | Abbrüche an der Stelle Versandkosten | 223.283 × 27 % | 60.286 pro Monat |
> | Abbrüche an der Stelle Registrierung | 223.283 × 21 % | 46.889 pro Monat |
> | Wert von **1 Prozentpunkt** der Versandkosten-Abbrecher, wenn sie kaufen | 603 Warenkörbe × 68 € × 12 | ca. 492.000 € pro Jahr |
> | Einmalkäufer | 1,1 Mio. × 61 % | 671.000 |
> | Wiederkäufer | 1,1 Mio. − 671.000 | 429.000 |
> | Wert von **1 Prozentpunkt** der Einmalkäufer mit zweitem Kauf | 6.710 Kunden × 68 € | ca. 456.000 € |
> | Überbestand 2025 im Verhältnis zum Umsatz | 4,3 Mio. / 74 Mio. | 5,8 % |
> | Wert von 10 % weniger Überbestand | 4,3 Mio. × 10 % | 430.000 € |
> | Retouren pro Jahr, wenn je Bestellung 1 Artikel | 1.094.400 × 38 % | ca. 415.900 |
> | Retourenkosten pro Jahr (Größenordnung, siehe Annahme in Teil B) | 415.900 × 11 € | ca. 4,6 Mio. € |
> | Anteil der Besuche mit Einwilligung | 64 % von 4,8 Mio. | 3,07 Mio. pro Monat |
> | Entwicklertage, die das Budget höchstens hergibt | 700.000 € / 900 € | 777 |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Zuerst der Shop, dann das Modell.** Die zwei größten Abbruchstellen **Versandkosten (27 %)** und **Registrierung (21 %)** sind keine Fälle für Prognosen: die Versandkosten erst im letzten Schritt anzuzeigen und ein Konto zu verlangen sind Entscheidungen im Shop. Pro Prozentpunkt der Versandkosten-Abbrecher, die doch kaufen, sind das rechnerisch ca. **492.000 € Umsatz pro Jahr**.
> - **Kaufwahrscheinlichkeit:** ein Modell für die **671.000 Einmalkäufer** (Wiederkauf ja/nein). Das geht mit den Kaufdaten allein, ohne Klickdaten und damit ohne Einwilligungsproblem. Pro Prozentpunkt zusätzlicher Zweitkäufer ca. **456.000 €**.
> - **Umsatzprognose:** gebraucht für den **Einkauf**, der 6 Monate vorher bestellt und 2025 **4,3 Mio. €** abgeschrieben hat. Prognose pro Warengruppe und Monat, mit Bandbreite.
> - **Stimmung:** 95.000 Bewertungen und 40.000 E-Mails, nach **Thema und Stimmung** sortiert. Die Beispiele zeigen vier Themen: Größen, Rücksendung, Versandkosten, Qualität. Größe und Rücksendung hängen mit den **38 % Retouren** zusammen.
> - **Budget (Vorschlag):** 150.000 Shop-Umbau und Tests, 120.000 Wiederkauf-Modell, 120.000 Prognose Einkauf, 60.000 Feedback-Analyse, 50.000 Datenschutz und Einwilligung, 40.000 Messung, 160.000 Reserve = **700.000 €**.
> - **Vorsicht:** Das Aufgabenblatt nennt kaum Preise und keine Wirkungen. Alle Wirkungen sind Rechenbeispiele pro Prozentpunkt, keine Prognosen. Die Maßnahmen sind Hypothesen, die Tests in den ersten Monaten prüfen müssen.

> [!NOTE]
> **Annahmen:** (1) Die Abbruchstellen sind Anteile **aller Abbrüche** (Summe 100 %). (2) Ein abgebrochener Warenkorb hat im Schnitt den Wert 68 €, tatsächlich unbekannt. (3) Käufe = abgeschlossene Warenkörbe, 71 % Abbruch bezogen auf alle Warenkörbe. (4) Für die Retouren-Rechnung: ein Artikel je Bestellung, eine Retoure je Artikel. Das gibt die **Größenordnung**, nicht einen Mindestwert. (5) Die Budgetaufteilung ist mein Vorschlag, die Preise je Posten fehlen im Aufgabenblatt. Alle Rechnungen stehen im Python-Check.

## Schritt 1 · Wo geht Umsatz verloren?

| Stelle | Anteil der Abbrüche | Warum bricht der Kunde ab? | Was lässt sich ändern? |
|:---|:---|:---|:---|
| **Warenkorb** (38 %) | 84.800 pro Monat | größter Anteil, aber die Ursache ist unklar. Typisch: Preisvergleich, Stöbern, Warenkorb als Merkliste. Kunde ist an dieser Stelle oft **nicht eingeloggt**, also nicht ansprechbar | schwer: nur mit Klickdaten (nur 64 % Einwilligung) erkennbar. Hier hilft **Wiederkehr statt Druck** (Merkliste, Erinnerung bei Konto) |
| **Versandkosten** (27 %) | 60.300 pro Monat | Die 4,95 € erscheinen **erst im letzten Schritt**. Die Bewertung "Versandkosten erst ganz am Ende gesehen" bestätigt das. Der Konkurrent liefert ab 30 € frei, ShopNow erst ab 60 € | **Versand früh anzeigen** (Produktseite, Warenkorb). **Versandschwelle prüfen** (Test mit 40 oder 50 € statt 60 €). Beides **ohne ML**, nur Entwicklertage |
| **Registrierung** (21 %) | 46.900 pro Monat | Kauf **ohne Konto nicht möglich**. Ein Zwang zum Konto ist ein bekannter Abbruchgrund | **Gastkauf** mit Konto-Angebot nach dem Kauf. Erst prüfen, ob der Verlust an Kundendaten tragbar ist |
| **Zahlung** (14 %) | 31.300 pro Monat | fehlende Zahlart, technische Fehler, Misstrauen | Zahlarten und Fehlerquote prüfen. Kleinster Hebel, aber meist technisch lösbar |

## Schritt 2 · Ergebnisraster

| Baustein | Welche Daten? | Welches Ergebnis? | Welche Maßnahme? |
|:---|:---|:---|:---|
| **Kaufwahrscheinlichkeit** (Klasse: kauft ja/nein) | **Kaufdaten** der 1,1 Mio. Konten (4 Jahre): Käufe, Tage seit letztem Kauf, Ø Warenkorb, Warengruppe, **Retourenquote**, Newsletter, Erstkaufkanal. **Klickdaten** nur ergänzend, nur mit Einwilligung (64 %) | **Wahrscheinlichkeit pro Kunde**, z. B. "kauft in den nächsten 90 Tagen" (Wiederkauf). Dazu eine **Schwelle**: ab wann wird gehandelt | **Einmalkäufer** (671.000) mit mittlerer Wahrscheinlichkeit gezielt ansprechen. Kunden mit **sehr hoher** Wahrscheinlichkeit brauchen keinen Gutschein, sie kaufen ohnehin |
| **Umsatzprognose** (Zahl: Euro pro Monat) | **Kaufdaten 4 Jahre** (48 Monate, mehrere Saisons), je Warengruppe. Dazu Saison, Aktionskalender, Preisänderungen, Wettereffekte (Sportbekleidung) | **Umsatz je Warengruppe und Monat**, 6 Monate voraus, mit **Bandbreite** (nicht eine Zahl). Dazu **Netto nach Retouren** | **Bestellmengen des Einkaufs** an der Prognose ausrichten: bei breiter Bandbreite eher an der unteren Grenze bestellen und nachordern, statt Überbestände abzuschreiben |
| **Stimmung im Feedback** (Klasse: positiv / neutral / negativ, nach Thema) | **95.000 Bewertungen** (mit Sternen: Sterne sind ein erster Anhaltspunkt) und **40.000 Service-E-Mails** (ohne Sterne, ohne Bestellbezug) | **Stimmung je Thema** (Größen, Retoure, Versand, Qualität, Service), als Rangliste der häufigsten **negativen** Themen mit Anzahl | **Größenberatung** am Artikel (Retouren senken), **Rücksendeprozess** vereinfachen, Versandkosten-Hinweis früh, Qualitätsmängel an den Einkauf melden |

## Schritt 3 · Maßnahmen und Budget

| Maßnahme | Wirkung auf | Aufwand | Reihenfolge | Kosten (Schätzung, Vorschlag) |
|:---|:---|:---|:---|:---|
| **Versandkosten früher zeigen oder senken** | 27 % der Abbrüche. Pro Prozentpunkt ca. 492.000 € Umsatz pro Jahr | klein: wenige Entwicklertage plus **A/B-Test** der Schwelle. Kosten der Schwelle: Entgang der 4,95 € bei Bestellungen zwischen neuer und alter Schwelle | **1** (Monat 1 bis 3) | Teil von 150.000 € für Shop-Umbau und Tests (bei 900 € je Tag ca. 167 Entwicklertage) |
| **Kauf ohne Konto (Gastkauf)** | 21 % der Abbrüche | mittel: Umbau in Shop und Datenhaltung. Weniger Konten bedeuten weniger Daten für die Modelle | **2** (Monat 2 bis 5) | Teil von 150.000 € |
| **Wiederkauf-Modell für Einmalkäufer** | 61 % Einmalkäufer. Pro Prozentpunkt zweiter Kauf ca. 456.000 € | mittel: Modell, Zielgruppen, **Kontrollgruppe**, Gutscheine | **3** (Pilot ab Monat 4, Messung bis Monat 12) | 120.000 € |
| **Umsatzprognose für den Einkauf** | 4,3 Mio. € Abschreibung. Pro 10 % weniger ca. 430.000 € | mittel bis hoch: nur wirksam, wenn der Einkauf die Prognose in der Bestellung **wirklich nutzt** | **4** (Start Monat 3, erste Bestellrunde Monat 6 bis 9) | 120.000 € |
| **Feedback-Analyse (Größen, Retouren)** | Retouren (Größenordnung 4,6 Mio. € pro Jahr) und Abbruch durch Versandkosten | klein bis mittel: Bewertungen und E-Mails per Sprachmodell oder Klassifikator nach Thema und Stimmung | **parallel ab Monat 1**, liefert Themen für die anderen Maßnahmen | 60.000 € |

> [!NOTE]
> **Warum diese Reihenfolge (Hypothese):** Die Maßnahmen im Shop sind **billig, schnell und schnell messbar**, sie brauchen keine Datenwissenschaft und bringen das Geld, das später die Modelle mitfinanziert. Der Wiederkauf-Pilot braucht Zeit für Testgruppen und Wartezeit bis zum zweiten Kauf. Die Prognose für den Einkauf zeigt ihren Nutzen erst nach den Bestellrunden. Von den vier Bausteinen ist die Feedback-Analyse der günstigste Start: sie liefert Hinweise, wo Retouren und Abbrüche herkommen, bevor Geld in die anderen fließt.

## Schritt 4 · Risiken und Messung

| Thema | Was kann schiefgehen? | Wie messen oder absichern? |
|:---|:---|:---|
| **Einwilligung (64 %)** | Klickmodelle sehen nur 64 % der Besuche, und das ist **keine Zufallsauswahl**: wer einwilligt, verhält sich anders als wer ablehnt. Das Modell gilt dann für die Einwilligenden, nicht für alle. Kundenprofile für Werbung brauchen eine eigene Rechtsprüfung (DSGVO) | Kaufdaten der Konten als Hauptquelle. Klickdaten nur ergänzend. Rechtslage **vor** dem Start prüfen (Posten Datenschutz im Budget) |
| **E-Mails ohne Bestellbezug** | Eine Beschwerde lässt sich keinem Artikel, keiner Retoure und keinem Kunden zuordnen. Man kennt das Thema, aber nicht den Hebel | Themen und Häufigkeit nutzen. Für die Zukunft **Bestellnummer** im Kontaktformular verlangen |
| **Erfolgsmessung in 12 Monaten** | Zu viele Änderungen gleichzeitig, am Ende ist nicht klar, was gewirkt hat | **Kontrollgruppe** und **A/B-Test** je Maßnahme. Kennzahlen vorher festlegen: Abbruchquote (71 %), Einmalkäufer (61 %), Überbestand (4,3 Mio. €), Retouren (38 %) |
| **Störfaktoren** (Lager Erfurt, Sportler, Konkurrent) | **Erfurt** (seit März): Lieferzeiten und Retouren können sich geändert haben, alte Daten passen dann nur bedingt. **Sportler** (380.000 € bis 2028) sind ein fester Posten und kein Hebel der Studie. **Konkurrent** (ab 30 € frei): ein Grund für die Schwelle, aber nicht der einzige | Daten **vor und nach März** getrennt prüfen. Sportler-Vertrag unverändert lassen und im Marketing-Kalender als bekannten Effekt führen. Schwelle nur im Test ändern |

> [!NOTE]
> **Fallen, die in der Aufgabe stecken (Hypothesen):**
> - **Wer hohe Kaufwahrscheinlichkeit hat, kauft ohnehin.** Ein Gutschein für diese Kunden kostet Marge ohne Wirkung. Sinnvoll sind eher die Kunden im **mittleren** Bereich. Welche Gruppe wirklich auf eine Aktion reagiert, zeigt nur ein Test mit Kontrollgruppe.
> - **Umsatz ist nicht Gewinn.** 38 % Retouren zu je 11 € fressen einen Teil des Umsatzes. Eine Prognose, die nur den Bruttoumsatz kennt, bestellt zu viel.
> - **Die Prognose braucht eine Entscheidung.** "Was wird damit entschieden?" lautet die Leitfrage: hier die **Bestellmenge in 6 Monaten**. Ohne diese Entscheidung ist die Prognose nur eine Zahl.
> - **Sterne sind nicht Stimmung.** Eine 1-Sterne-Bewertung "Kauf abgebrochen" zeigt, dass auch **Nichtkäufer** bewerten. Sterne können als erster Hinweis dienen, ersetzen die Themenanalyse nicht.
> - **Stichprobe:** vier Bewertungen sind keine Aussage über 95.000. Die Themen (Größen, Rücksendung, Versandkosten, Qualität) sind Hypothesen, bis die Auswertung die Häufigkeiten zeigt.

## Python-Check

```python
# python3 -I check.py   (nur Standardbibliothek)
besuche, kaufquote, warenkorb = 4_800_000, 0.019, 68

kaeufe_monat = besuche * kaufquote                              # 91.200
kaeufe_jahr = kaeufe_monat * 12                                 # 1.094.400
print(kaeufe_monat, kaeufe_jahr, kaeufe_jahr * warenkorb)       # Umsatz 74,4 Mio

karten = kaeufe_monat / 0.29                                    # 314.483 Warenkörbe pro Monat
abbruch = karten - kaeufe_monat                                 # 223.283
for stelle, anteil in {"Warenkorb": .38, "Versand": .27, "Registrierung": .21, "Zahlung": .14}.items():
    print(stelle, round(abbruch * anteil))                      # 84.847 / 60.286 / 46.889 / 31.260

versand = abbruch * 0.27
print(round(versand * 0.01 * warenkorb * 12))                   # 1 Prozentpunkt: ca. 492.000 €/Jahr

einmal = 1_100_000 * 0.61                                       # 671.000
print(einmal, 1_100_000 - einmal, einmal * 0.01 * warenkorb)    # 1 Prozentpunkt: ca. 456.000 €

print(4_300_000 / 74_000_000, 4_300_000 * 0.10)                 # 5,8 %, 430.000 €
retouren = kaeufe_jahr * 0.38                                   # Annahme: 1 Artikel je Bestellung
print(round(retouren), round(retouren * 11))                    # 415.872 / 4,57 Mio €
print(700_000 / 900, 150_000 / 900)                             # 777 / 167 Entwicklertage
print(150 + 120 + 120 + 60 + 50 + 40 + 160)                     # Budget in Tsd. € = 700
```

Ergebnis: Käufe und Umsatz passen zur Angabe (74,4 gegen 74 Mio. €). Die Wirkungen sind **Rechenbeispiele pro Prozentpunkt**, die Prozentpunkte selbst sind nicht belegt. Die Retouren-Rechnung beruht auf der Annahme eines Artikels je Bestellung und gibt nur die Größenordnung.
