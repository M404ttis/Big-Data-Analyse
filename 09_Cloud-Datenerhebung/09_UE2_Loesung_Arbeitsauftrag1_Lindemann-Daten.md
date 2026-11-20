# Tag 9 (Modul 3), Arbeitsauftrag 1: Daten bei Lindemann Küchentechnik

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Fakten und Rechnungen** aus dem Aufgabenblatt | [→ Teil A](#teil-a-fakten-und-rechnungen) |
> | **B** | **Lösungsentwurf** (KI) | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** (1) **Welche Daten entstehen** im Unternehmen? (2) **Welche sind strukturiert, welche unstrukturiert?** (3) **Welche Daten könnten besonders wertvoll sein?** Dazu das Raster Datenquelle / Welche Daten / Strukturiert? / Wie wertvoll, wofür.

---

# Teil A: Fakten und Rechnungen

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Das Unternehmen

| Thema | Angabe |
|---|---|
| Firma | Lindemann Küchentechnik GmbH. Stellt Küchenmaschinen und Zubehör selbst her, verkauft über einen **eigenen Onlineshop** |
| Größe | 380 Mitarbeitende, 120.000 Bestellungen pro Jahr, Kunden in Deutschland und Österreich |
| Produktion | 14 Spritzguss- und CNC-Maschinen, eigene Qualitätsprüfung, Lager mit Scannern |
| Kundenkontakt | Shop, Chat, Telefon-Hotline, Bewertungen auf der Produktseite |
| Umsatz | 41 Mio. € pro Jahr (Shop) |

### Was wo gespeichert wird

| Ort | Was genau | Menge |
|---|---|---|
| Shop-Datenbank | Kundenkonto, Bestellungen mit Artikel, Preis, Datum, Lieferadresse | 120.000 Bestellungen/Jahr |
| Shop-Protokoll | Jede Suche, jeder Klick, abgebrochene Warenkörbe mit Uhrzeit | ca. 30 Mio. Einträge/Jahr |
| Produktseiten | Bewertungen: 1 bis 5 Sterne, frei geschriebener Text, teils Fotos | 9.500/Jahr, 1.400 mit Foto |
| Hotline | Gesprächsaufnahmen (mit Einwilligung), dazu ein Ticket mit Anliegen-Kategorie | 26.000 Anrufe/Jahr |
| Chat | Komplette Chatverläufe mit Kunden | 11.000 Chats/Jahr |
| Maschinensteuerungen | Temperatur, Druck, Zykluszeit, alle 2 Sekunden | 14 Maschinen |
| Qualitätsprüfung | Foto jedes zehnten Teils plus Protokoll "in Ordnung / Fehler" mit Fehlerart | ca. 400.000 Fotos/Jahr |
| Lager | Scan bei jedem Ein- und Ausgang: Artikel, Lagerplatz, Zeit | ca. 2.000 Scans/Tag |
| Einkauf | Lieferscheine und Rechnungen als PDF per E-Mail | 85 Lieferanten |

### Was Sie außerdem erfahren

| Thema | Angabe |
|---|---|
| Retouren | Stabmixer S3: **14 %** zurückgeschickt. Häufigster Grund laut Hotline: "Deckel bricht" |
| Ausschuss | Spritzguss **3,2 %**, rund **600.000 €** pro Jahr |
| Shop | **71 %** der Warenkörbe werden abgebrochen |
| Marketing | **Plant** einen eigenen Video-Kanal mit Rezepten (gibt es noch nicht) |
| Sonstiges | 50-jähriges Bestehen 2027, Jobräder. Für die Datenfrage vermutlich ohne Bedeutung |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Ø Bestellwert | 41 Mio. € / 120.000 | 341,67 € |
> | Protokolleinträge je Bestellung | 30 Mio. / 120.000 | 250 |
> | Protokolleinträge pro Tag | 30 Mio. / 365 | rund 82.200 |
> | Warenkörbe gesamt (Annahme: 1 Bestellung = 1 abgeschlossener Korb, 29 % der Körbe) | 120.000 / 0,29 | rund 413.800 |
> | davon abgebrochen | 413.800 × 71 % | rund 293.800 |
> | 1 Prozentpunkt weniger Abbruch (Annahme: Ø Bestellwert) | 4.138 × 341,67 € | rund 1,41 Mio. € |
> | Kundenkontakte (Bewertung, Hotline, Chat) | 9.500 + 26.000 + 11.000 | 46.500 |
> | Anrufe je 100 Bestellungen | 26.000 / 120.000 × 100 | 21,7 |
> | Bewertungen mit Foto | 1.400 / 9.500 | 14,7 % |
> | Maschinen: Messzeilen pro Tag (Annahme: Dauerbetrieb) | 14 × 43.200 | 604.800 |
> | Maschinen: Werte pro Tag (3 Messgrößen) | 604.800 × 3 | 1,81 Mio. |
> | Teile pro Jahr (jedes zehnte fotografiert) | 400.000 × 10 | 4 Mio. |
> | Ausschussteile | 4 Mio. × 3,2 % | 128.000 |
> | Kosten je Ausschussteil | 600.000 € / 128.000 | 4,69 € |
> | Fotos fehlerhafter Teile (Annahme: Stichprobe repräsentativ) | 400.000 × 3,2 % | 12.800 |
> | Ausschuss im Verhältnis zum Umsatz | 600.000 € / 41 Mio. € | 1,46 % |
> | Lagerscans pro Jahr | 2.000 × 365 | 730.000 |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Neun Datenquellen sind vorhanden, eine ist geplant.** Shop-Datenbank, Shop-Protokoll, Bewertungen, Hotline, Chat (Verkauf und Kunden), Maschinensteuerungen, Qualitätsprüfung, Lager, Einkauf (Produktion und Einkauf). Der Video-Kanal ist erst geplant und zählt noch nicht.
> - **Strukturiert** sind nur drei Quellen ganz: Shop-Datenbank, Maschinen, Lager. Das Shop-Protokoll ist **semi-strukturiert** (Ereignisse mit Etiketten). **Gemischt** sind Bewertungen, Hotline und Qualitätsprüfung (je ein strukturierter Teil plus Text, Ton oder Foto). **Unstrukturiert** sind Chat und die PDF-Lieferscheine. Der Großteil des *Inhalts* (Aufnahmen, Texte, Fotos) ist also unstrukturiert, die Zeilenzahl liegt dagegen bei den Maschinen: rund 221 Mio. Zeilen im Jahr.
> - **Am wertvollsten ist die Verbindung, nicht die einzelne Quelle.** Beim Stabmixer S3 stehen 14 % Retouren, der Grund "Deckel bricht" (Hotline), die Bestellungen (Shop), die Fehlerfotos (Qualitätsprüfung) und die Maschinendaten (Spritzguss) in **vier getrennten Quellen**. Zusammen können sie die Ursache zeigen.
> - **Rang 1: Retouren-Kette** (Hotline, Shop, Qualität, Maschinen). **Rang 2: Maschinendaten plus Qualitätsprüfung** gegen 600.000 € Ausschuss pro Jahr. **Rang 3: Shop-Protokoll** gegen 71 % Warenkorbabbruch: 1 Prozentpunkt weniger Abbruch wäre rund 1,41 Mio. € Umsatz (Annahme).
> - **Nicht jedes Datum ist wertvoll.** Jobräder und das 50-jährige Bestehen sind keine Datenquellen. Die Lagerscans sind solide, aber allein wenig überraschend.
> - **Vorsicht:** Alle Wertangaben sind Hypothesen. Das Blatt nennt weder Retourenkosten noch Margen. Mehrere Quellen sind **personenbezogen** (Aufnahmen, Chats, Klicks, Küchenfotos).

> [!NOTE]
> **Annahmen:** (1) Eine Bestellung entspricht einem abgeschlossenen Warenkorb, damit lassen sich die 71 % Abbruch auf Körbe umrechnen. (2) Der Wert eines abgebrochenen Korbs ist der Ø Bestellwert (341,67 €). Abgebrochene Körbe sind vermutlich anders, das Blatt sagt es nicht. (3) Die Maschinen laufen durchgehend (365 Tage, 24 Stunden). (4) Der Deckel des Stabmixers kommt aus dem Spritzguss. Das Blatt sagt es nicht, es liegt nahe. (5) Die Stichprobe der Qualitätsprüfung (jedes zehnte Teil) ist repräsentativ. (6) Der Ausschuss von 3,2 % bezieht sich auf Stück. Alle Rechnungen stehen im Python-Check.

## Schritt 1 · Ergebnisraster

| Datenquelle | Welche Daten? | Strukturiert? | Wie wertvoll, wofür? |
|:---|:---|:---|:---|
| **Shop-Datenbank** | Kundenkonto, Bestellung, Artikel, Preis, Datum, Lieferadresse. 120.000 Bestellungen, 41 Mio. € | **Strukturiert**: feste Felder, Tabellen | **Hoch.** Kern des Geschäfts: Umsatz je Artikel, Kunde, Region. Ø Bestellwert 341,67 €. Schlüssel, um andere Quellen anzuhängen (Bestellung, Kunde) |
| **Shop-Protokoll** | Suchen, Klicks, abgebrochene Warenkörbe, Uhrzeit. 30 Mio. Einträge, 250 je Bestellung | **Semi-strukturiert**: Ereignisse mit Etiketten (Zeit, Aktion), aber je Ereignis andere Felder | **Hoch.** 71 % Abbruch: 293.800 verlorene Körbe. 1 Prozentpunkt weniger sind rund 1,41 Mio. € (Hypothese). **Personenbezogen**, Einwilligung beachten |
| **Bewertungen** | 1 bis 5 Sterne, Freitext, teils Foto. 9.500, davon 1.400 mit Foto (14,7 %) | **Gemischt**: Sterne strukturiert, Text und Foto **unstrukturiert** | **Mittel bis hoch.** Der Text nennt Gründe ("Deckel bricht"), die Sterne sind zählbar. Fotos zeigen Nutzung in echten Küchen. Nur 9.500 bei 120.000 Bestellungen (7,9 %): wer schreibt, ist nicht jeder (Auswahlverzerrung) |
| **Hotline** | Gesprächsaufnahme, Ticket mit Anliegen-Kategorie. 26.000 Anrufe (21,7 je 100 Bestellungen) | **Gemischt**: Ticket-Kategorie strukturiert, Aufnahme **unstrukturiert** (Ton) | **Hoch.** Nennt den Retourengrund ("Deckel bricht"). Erst mit Texterkennung auswertbar. Aufnahmen sind **personenbezogen** (Einwilligung liegt vor, Zweck und Löschfrist prüfen) |
| **Chat** | Komplette Chatverläufe. 11.000 Chats | **Unstrukturiert**: Freitext (nur Zeitstempel und Kennung strukturiert) | **Mittel.** Fragen vor dem Kauf zeigen, was im Shop unklar ist. Ähnlich wie Hotline, aber schon als Text, also leichter auszuwerten |
| **Maschinensteuerungen** | Temperatur, Druck, Zykluszeit alle 2 Sekunden, 14 Maschinen | **Strukturiert**: Zeitreihen. Menge: 604.800 Zeilen/Tag, rund 221 Mio. im Jahr (Annahme: Dauerbetrieb) | **Hoch, aber nur mit Verknüpfung.** Allein sind es Zahlen. Mit der Qualitätsprüfung zeigen sie, bei welchen Werten Ausschuss entsteht (600.000 €/Jahr). Verfahren: vorhersagen, bevor ein Fehler passiert |
| **Qualitätsprüfung** | Foto jedes zehnten Teils, Protokoll in Ordnung / Fehler mit Fehlerart. 400.000 Fotos | **Gemischt**: Protokoll strukturiert, Foto **unstrukturiert** | **Hoch.** 12.800 Fotos fehlerhafter Teile (Annahme) sind **Trainingsmaterial** für Bilderkennung. Beschriftet ist es schon (Fehlerart) |
| **Lager** | Scan bei Ein- und Ausgang: Artikel, Lagerplatz, Zeit. 2.000/Tag, 730.000/Jahr | **Strukturiert** | **Mittel.** Bestand, Lieferfähigkeit, Umschlag. Als Zeitreihe nützlich für Absatzprognosen. Allein wenig überraschend, hilft aber, Shop-Bestellung und Lieferzeit zu verbinden |
| **Einkauf (PDF)** | Lieferscheine und Rechnungen von 85 Lieferanten per E-Mail | **Unstrukturiert**: PDF (nur die E-Mail-Kopfzeile ist semi-strukturiert) | **Mittel, aber mit Aufwand.** Inhalt (Menge, Preis, Termin) steckt im Dokument und muss per Texterkennung heraus. Wert: Lieferzeiten und Preise vergleichen, Rechnungen automatisch prüfen |
| **Video-Kanal** (geplant) | Rezeptvideos, später Aufrufe und Kommentare | **Unstrukturiert** (Video), Abrufzahlen semi | **Noch kein Datenbestand.** Neue Quelle: Wer schaut was, führt es zum Kauf? Erst entscheiden, **welche Frage** damit beantwortet werden soll, dann erheben |

> [!NOTE]
> **Zählung:** 9 vorhandene Quellen = 3 strukturiert (Shop-Datenbank, Maschinen, Lager) + 1 semi-strukturiert (Shop-Protokoll) + 3 gemischt (Bewertungen, Hotline, Qualitätsprüfung) + 2 unstrukturiert (Chat, Einkauf). Die Einteilung "gemischt" ist meine Wortwahl: Die Folie kennt drei Typen, in einer Quelle können aber mehrere stecken.

## Schritt 2 · Die wertvollsten Daten

| Rang | Daten | Warum? | Wofür? |
|:---:|---|---|---|
| **1** | **Retouren-Kette Stabmixer S3**: Hotline (Grund), Shop-Datenbank (wer, wann), Qualitätsprüfung und Maschinen (Spritzguss) | **14 %** Retouren sind ein klares Warnzeichen. Der Grund "Deckel bricht" steht in der Hotline, die Ursache liegt womöglich in der Produktion. **Vier Quellen, die heute nicht verbunden sind** | Ursache finden (Werkstoff, Maschine, Charge?), Reklamationen und Retourenkosten senken, Rückruf vermeiden. Außerdem Kundenzufriedenheit |
| **2** | **Maschinendaten plus Qualitätsprüfung** | **600.000 €** Ausschuss pro Jahr (1,46 % vom Umsatz), 128.000 Teile. Die Daten sind **schon strukturiert und beschriftet** (in Ordnung oder Fehler). 12.800 Fotos fehlerhafter Teile | Vorhersage, bei welchen Temperatur- und Druckwerten Ausschuss entsteht. Bildprüfung automatisieren. Jeder Prozentpunkt weniger Ausschuss spart rund 190.000 € (600.000 / 3,2, Annahme: Kosten steigen linear) |
| **3** | **Shop-Protokoll** (Klicks, Warenkörbe) | **71 %** Abbruch: Das ist der größte sichtbare Hebel beim Umsatz. 1 Prozentpunkt entspricht rund 1,41 Mio. € (Hypothese, Ø Bestellwert) | Abbruchgründe finden (Versandkosten, Zahlungsarten, Seite zu langsam?), Warenkörbe erinnern, Shop verbessern. **Einwilligung** beachten |

> [!NOTE]
> **Warum nicht die Bewertungen oder die Hotline allein?** Sie sind **Rohstoff**: Texte und Töne, die erst mit Aufwand lesbar werden. Ihr Wert entsteht, wenn man sie an Bestellung und Produktion hängt (Rang 1). Allein beantworten sie nur "Was ärgert Kunden?", nicht "Warum?".

> [!NOTE]
> **Was bewusst fehlt:** Jobräder und das 50-jährige Bestehen sind Nebensätze ohne Datenbezug. Der Video-Kanal ist Zukunft, kein Bestand. Die Lagerscans sind sauber, aber ohne eigene Frage wenig wert. Nach der Folie "Nicht alles speichern" gilt: Jedes gespeicherte Datum kostet Speicher, Pflege und Sicherheit.

## Schritt 3 · Fehler, die man vermeiden sollte

| Falle | Warum? |
|---|---|
| **Alles speichern, weil es geht** | 221 Mio. Maschinenzeilen und 30 Mio. Klickeinträge im Jahr kosten Speicher und Pflege. Erst die Frage, dann die Daten (Folie "Gezielt erheben") |
| **Bewertungen für die Meinung aller halten** | 9.500 Bewertungen bei 120.000 Bestellungen (7,9 %). Wer schreibt, ist nicht repräsentativ. Erinnert an 1936: **Wie erhoben wird, zählt mehr als die Menge** |
| **Personenbezug übersehen** | Aufnahmen, Chats, Klicks und Küchenfotos sind personenbezogen. Zweck, Löschfrist, Einwilligung und Rechte klären, bevor man sie auswertet. In die Cloud nur mit Vertrag zur Auftragsverarbeitung |
| **Jede Quelle für sich auswerten** | Der größte Wert liegt in der **Verknüpfung** (Rang 1). Dafür braucht es gemeinsame Schlüssel (Bestellnummer, Artikelnummer, Chargennummer). Das Blatt sagt nicht, ob es sie gibt |

## Python-Check

```python
# python3 -I check.py   (nur Standardbibliothek)
bestell, umsatz = 120_000, 41_000_000
print("Ø Bestellwert:", round(umsatz / bestell, 2))
log = 30_000_000
print("Protokolleinträge je Bestellung:", log / bestell, "| pro Tag:", round(log / 365))
abbruch = 0.71
koerbe = bestell / (1 - abbruch)          # Annahme: 1 Bestellung = 1 abgeschlossener Warenkorb
print("Warenkörbe gesamt:", round(koerbe), "| abgebrochen:", round(koerbe * abbruch), "| 1 Prozentpunkt:", round(koerbe * 0.01))
print("1 Prozentpunkt weniger Abbruch in €:", round(koerbe * 0.01 * umsatz / bestell))
print("Kontakte Bewertung+Hotline+Chat:", 9_500 + 26_000 + 11_000, "| Anrufe je 100 Bestellungen:", round(26_000 / bestell * 100, 1))
print("Bewertungen mit Foto:", round(1_400 / 9_500 * 100, 1), "%")
zeilen_tag = 14 * (24 * 3600 // 2)
print("Maschinen: Messzeilen/Tag:", zeilen_tag, "| Werte/Tag (3 Größen):", zeilen_tag * 3, "| Zeilen/Jahr:", zeilen_tag * 365)
teile = 400_000 * 10
print("Teile/Jahr (jedes 10. fotografiert):", teile, "| Ausschuss 3,2 %:", round(teile * 0.032), "| € je Ausschussteil:", round(600_000 / (teile * 0.032), 2))
print("Fotos fehlerhafter Teile (3,2 % von 400.000):", round(400_000 * 0.032))
print("Ausschuss in % vom Umsatz:", round(600_000 / umsatz * 100, 2))
print("Lagerscans/Jahr:", 2_000 * 365)
```

**Ausgabe:**

```text
Ø Bestellwert: 341.67
Protokolleinträge je Bestellung: 250.0 | pro Tag: 82192
Warenkörbe gesamt: 413793 | abgebrochen: 293793 | 1 Prozentpunkt: 4138
1 Prozentpunkt weniger Abbruch in €: 1413793
Kontakte Bewertung+Hotline+Chat: 46500 | Anrufe je 100 Bestellungen: 21.7
Bewertungen mit Foto: 14.7 %
Maschinen: Messzeilen/Tag: 604800 | Werte/Tag (3 Größen): 1814400 | Zeilen/Jahr: 220752000
Teile/Jahr (jedes 10. fotografiert): 4000000 | Ausschuss 3,2 %: 128000 | € je Ausschussteil: 4.69
Fotos fehlerhafter Teile (3,2 % von 400.000): 12800
Ausschuss in % vom Umsatz: 1.46
Lagerscans/Jahr: 730000
```
