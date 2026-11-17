# Tag 4 (Modul 3), Arbeitsauftrag 1: Kundenservice-Workflow bei Kaiser Haushaltswaren

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Mattis Lösung**: Fakten, Rechnungen, leeres Ergebnisraster | [→ Teil A](#teil-a-mattis-lösung) |
> | **B** | **Lösungsentwurf** (KI): zum Vergleichen, *nach* dem eigenen Entwurf lesen | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Für die sechs Arbeitsschritte von Frau Petersen klären: (1) Welche Schritte sind **immer gleich**? (2) Welche erfordern **menschliches Denken**? (3) Welche Teile könnten **automatisiert** werden?

---

# Teil A: Mattis Lösung

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Die Situation

| Thema | Angabe |
|---|---|
| Firma | Kaiser Haushaltswaren GmbH, Online-Shop, 2.300 Artikel |
| Person | Frau Petersen, Kundenservice, seit 9 Jahren dabei, 30 Stunden pro Woche |
| Menge | rund 50 ähnliche E-Mails pro Tag, das kostet „fast einen ganzen Arbeitstag“ |
| Ihre Einschätzung | „Das meiste ist immer dasselbe – aber nicht alles.“ |

### Die sechs Schritte

| Nr. | Was sie tut |
|:---:|---|
| 1 | Liest die E-Mail und sucht die Bestellnummer |
| 2 | Schlägt die Bestellung im Shop-System nach |
| 3 | Kopiert die Sendungsnummer aus dem Versandsystem |
| 4 | Passt einen Textbaustein an und schickt die Antwort |
| 5 | Bei Schäden: prüft das Foto, entscheidet über Ersatz oder Gutschrift |
| 6 | Bei sehr verärgerten Kunden: ruft an und sucht eine Lösung |

### Das Postfach an einem typischen Tag

| Anliegen | Anzahl | Was Frau Petersen dafür braucht |
|---|---:|---|
| „Wo ist mein Paket?“ | 21 | Bestellnummer, Sendungsstatus aus dem Versandsystem |
| Rücksendung oder Umtausch | 11 | Bestellung, Rücksendeetikett aus dem Shop-System |
| Ware beschädigt, mit Foto | 6 | Foto, Bestellwert; Gutschrift bis 50 € darf sie selbst geben |
| Rechnung oder Zahlung | 5 | Buchhaltungsansicht im Shop-System |
| Verärgerte Stammkunden | 3 | Kaufhistorie, Telefon, Ermessen |
| Sonstiges (Produktfragen, Lob) | 4 | Produktdatenblatt, manchmal Rückfrage im Einkauf |

### Was sie außerdem erfahren

| Thema | Angabe |
|---|---|
| Vorlagen | 64 Textbausteine in einem Word-Ordner, manche seit 2019 nicht aktualisiert |
| Systeme | Shop-System und Versandsystem: getrennte Anmeldungen, keine Verbindung |
| Spitzen | Montags fast doppelt so viele Anfragen, im Dezember dreimal so viele |
| Team | 5 Personen im Service |
| Shop | im Frühjahr neues Design |

### Die drei Beispiel-E-Mails

| Von | Auszug |
|---|---|
| Kundin A | „Ich habe am 3. bestellt (Nr. 40871) und noch nichts bekommen. Wo bleibt mein Paket?“ |
| Kunde B | „Der Topf kam mit einer Delle an, Foto anbei. Ich möchte ihn zurückschicken.“ |
| Kundin C | „Zum dritten Mal falsche Farbe geliefert. Ich bin seit 10 Jahren Kundin und überlege, woanders zu bestellen.“ |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | E-Mails pro Tag | 21 + 11 + 6 + 5 + 3 + 4 | 50 |
> | Anteil „Wo ist mein Paket?“ | 21 / 50 | 42 % |
> | Anteil Rücksendung oder Umtausch | 11 / 50 | 22 % |
> | Anteil Schaden / Rechnung / Stammkunden / Sonstiges | 6, 5, 3, 4 von 50 | 12 % / 10 % / 6 % / 8 % |
> | Paket plus Rücksendung | 21 + 11 | 32 E-Mails = 64 % |
> | Fälle mit Ermessen (Schaden, verärgerte Stammkunden) | 6 + 3 | 9 E-Mails = 18 % |
> | Arbeitstag *(Annahme: 30 Std. auf 5 Tage verteilt)* | 30 Std. / 5 | 6 Std. = 360 Min. |
> | Zeit je E-Mail *(Annahme: alle gleich lang)* | 360 Min. / 50 | 7,2 Min. |
> | Montag *(„fast doppelt“, grob ×2)* | 50 × 2 | ca. 100 E-Mails = 12 Std. Arbeit |
> | Dezember *(„dreimal“)* | 50 × 3 | ca. 150 E-Mails = 18 Std. Arbeit |
> | Alter der ältesten Textbausteine | 2019 bis 2026 | bis zu 7 Jahre |

## Schritt 1 · Ergebnisraster

| Schritt | Immer gleich? | Menschliches Denken nötig? | Automatisierbar? |
|:---:|:---|:---|:---|
| **1 Lesen, Bestellnummer suchen** <br><br><br> | nein | Nummern ändern sich, aber mit gleichem Format | automatisierung mit RegEx oder auslesen mit KI |
| **2 Bestellung nachschlagen** <br><br><br> | sobald Best.Nr bekannt, immer gleich | nein | im besten Fall verpflichtender Bestell eMail als quasi-ID in DB festhalten, dann Schnittstelle mit look-up | 
| **3 Sendungsnummer kopieren** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **4 Textbaustein anpassen, senden** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **5 Schaden: Foto prüfen, entscheiden** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **6 Anruf bei verärgerten Kunden** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Hauptbefund:** Die Schritte 2 und 3 (nachschlagen, Nummer kopieren) sind reine Routine. Schritt 1 und 4 sind größtenteils Routine, brauchen aber KI, weil die Eingabe **Freitext** ist. Schritt 5 und 6 gehören zum Menschen.
> - **Zeitgewinn:** 32 bis 37 von 50 E-Mails (64 bis 74 %) sind Standardfälle. Bei grob 75 % Zeitersparnis auf diesen Fällen sind das **ca. 3 Stunden pro Tag** von 6.
> - **Nicht abgeben:** Entscheidung über Gutschrift oberhalb 50 € und das Gespräch mit verärgerten Stammkunden (Kundin C).
> - **Vorbedingung:** Shop- und Versandsystem sind nicht verbunden. Ohne Schnittstelle bleibt Schritt 3 Handarbeit, und der Entwurf aus Schritt 4 hat keinen Status.
> - **Erste Frage an das Unternehmen:** Dürfen Kundendaten in ein KI-System, und wo wird es betrieben (Datenschutz)?

> [!NOTE]
> Alle Rechnungen stehen in Teil A und im Python-Check. Die Zeitersparnis beruht auf zwei **Annahmen**: 6-Stunden-Tag und gleiche Dauer je E-Mail. Verärgerte Kunden dauern in Wirklichkeit länger, der Gewinn wäre dann etwas kleiner. Die Einordnung folgt der Checkliste und dem Entscheidungsbaum der Folien (Tag 4, Folien 23 bis 25).

## Schritt 1 · Ergebnisraster

| Schritt | Immer gleich? | Menschliches Denken nötig? | Automatisierbar? |
|:---:|:---|:---|:---|
| **1 Lesen, Bestellnummer suchen** | teils: Ziel immer gleich, aber Freitext. Nummer steht mal im Text, mal fehlt sie | nein, nur bei fehlender Nummer (Rückfrage) | **ja, mit KI:** liest Freitext, erkennt Anliegen und Nummer |
| **2 Bestellung nachschlagen** | ja, jedes Mal gleich | nein | **ja, klassisch** (Abfrage per Nummer) |
| **3 Sendungsnummer kopieren** | ja | nein | **ja, klassisch**, aber nur mit Schnittstelle zwischen den Systemen |
| **4 Textbaustein anpassen, senden** | überwiegend: 64 Bausteine decken die Standardfälle ab | bei Standard nein, bei Sonderfällen ja (Ton, Ausnahmen) | **teilweise:** Standard automatisch (Paketstatus), sonst KI-Entwurf, Mensch gibt frei |
| **5 Schaden: Foto prüfen, entscheiden** | nein, jeder Fall anders | **ja:** Schaden beurteilen, Ersatz oder Gutschrift, Grenze 50 € | **nur Assistenz:** KI sortiert Fotos vor, **Mensch entscheidet** |
| **6 Anruf bei verärgerten Kunden** | nein | **ja:** Zuhören, Ermessen, Kundenbindung | **nein**, höchstens Vorbereitung (Kaufhistorie zusammenfassen) |

### Wo steht jedes Anliegen?

| Anliegen | Anzahl | Weg |
|---|---:|---|
| „Wo ist mein Paket?“ | 21 | Schritte 1 bis 4 weitgehend automatisch (Teilautomatisierung mit Stichprobe) |
| Rücksendung oder Umtausch | 11 | wie oben, Etikett aus dem Shop-System; Ausnahmen beim Menschen |
| Rechnung oder Zahlung | 5 | vorbereiten per Regel, Mensch gibt bei Abweichung frei |
| Ware beschädigt | 6 | Assistenz: Mensch entscheidet |
| Verärgerte Stammkunden | 3 | Mensch |
| Sonstiges | 4 | KI-Entwurf möglich, Mensch prüft (Rückfrage im Einkauf) |

## Schritt 2 · Gesamtbild

- **Dreiteilung der Folien:** Klassisch automatisieren (Schritte 2, 3), KI-Unterstützung (Schritte 1, 4, Vorsortieren bei 5), Mensch (Entscheidung bei 5, Schritt 6).
- **Einstufung nach den Folien:** Paketanfragen sind „sehr häufig“, „jedes Mal gleich“, „Eingaben digital“ und Fehler sind leicht zu erkennen. Sie sind die besten Kandidaten. Schäden und Stammkunden erfüllen die Checkliste nicht.
- **Vorarbeit:** 64 Textbausteine aufräumen (manche seit 2019 veraltet), sonst automatisiert man alte Fehler. Der Shop bekommt im Frühjahr ein neues Design: Schnittstelle erst danach bauen oder von Anfang an tolerant gegen Änderungen.
- **Risiken:** KI darf keine falschen Zusagen machen (Gutschrift, Lieferdatum) und nichts erfinden (Halluzination, Tag 4 Einstieg). Daher Teilautomatisierung mit Stichprobe, nicht Vollautomatisierung. Personenbezogene Daten gehören nicht in ein öffentliches KI-Tool.
- **Spitzen:** Montag (ca. 100 E-Mails) und Dezember (ca. 150) sind der eigentliche Nutzen, weil das Team dann nicht mit Personal skalieren muss.
- **Nicht abgeben:** Gutschrift über 50 € und Gespräche mit verärgerten Stammkunden. Kundin C ist nicht ein Textbaustein-Fall, sondern ein Kundenverlust.

## Python-Check

```python
# python3 -I check.py
anzahl = [21, 11, 6, 5, 3, 4]
n = sum(anzahl)
print(n, [round(a / n * 100) for a in anzahl])         # 50; 42, 22, 12, 10, 6, 8 %
print(sum(anzahl[:2]), sum(anzahl[:2]) / n)            # 32; 0,64
print(anzahl[2] + anzahl[4], (anzahl[2] + anzahl[4]) / n)  # 9; 0,18
minuten = 30 / 5 * 60 / n                              # Annahme: 6-Std.-Tag
print(minuten)                                         # 7,2 Min. je E-Mail
for standard in (32, 37):                              # Annahme: 75 % Ersparnis
    print(standard * minuten * 0.75 / 60)              # 2,9 bis 3,3 Std.
print(100 * minuten / 60, 150 * minuten / 60)          # Montag, Dezember: 12; 18 Std.
```

Ergebnis: 50 E-Mails pro Tag, 32 Standardfälle (64 %), 9 mit Ermessen (18 %), 7,2 Min. je E-Mail. Zeitersparnis bei 75 %: 2,9 bis 3,3 Std. pro Tag. Montag ca. 12 Std., Dezember ca. 18 Std. Arbeit.
