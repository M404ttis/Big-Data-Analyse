# Tag 6 (Modul 3), Arbeitsauftrag 2: Kundenbewertungen nach Stimmung sortieren (Elektronik-Shop)

> [!NOTE]
> | Teil | Inhalt | Springen |
> |:---:|---|:---:|
> | **A** | **Mattis Lösung**: Fakten, Rechnungen, leere Raster | [→ Teil A](#teil-a-mattis-lösung) |
> | **B** | **Lösungsentwurf** (KI): zum Vergleichen, *nach* dem eigenen Entwurf lesen | [→ Teil B](#teil-b-lösungsentwurf) |

**Aufgabe:** Sechs echte Bewertungen (ohne Sterne, ohne Produktangabe): (1) jede einordnen als **positiv, neutral oder negativ**, (2) **Unsicherheiten** benennen, (3) **zusätzliche Informationen** nennen, die helfen würden. Die Einordnungen dienen später als Trainingsbeispiele.

---

# Teil A: Mattis Lösung

## Schritt 0 · Daten, Zahlen, Fakten aus dem Aufgabenblatt

### Das Vorhaben

| Thema | Angabe |
|---|---|
| Ziel | Bewertungen automatisch nach Stimmung sortieren. Vorher ordnen Menschen Beispiele ein, die später als **Trainingsbeispiele** dienen |
| Menge | Rund 14.000 neue Bewertungen pro Jahr, 92 % Deutsch, 6 % Englisch |
| Folgen | **Negativ:** der Kundendienst meldet sich binnen 24 Stunden. **Positiv:** das Zitat kann auf die Produktseite |
| Bisher | Zwei Werkstudierende lesen stichprobenartig jede zehnte Bewertung |
| Anbieter | Wirbt mit "97 % Genauigkeit", gemessen an **englischen Hotelbewertungen** |
| Shop | 6.500 Artikel. Bewertungen im Schnitt 23 Wörter lang, 8 % enthalten Emojis |
| Sonstiges | Die meisten Umsätze kommen von Kopfhörern und Smartwatches, Firmensitz in Leipzig |

### Die sechs Bewertungen

| Nr. | Bewertung |
|---:|---|
| 1 | „Produkt ist gut, aber Lieferung war langsam.“ |
| 2 | „Na toll. Nach zwei Wochen schon kaputt. Genau, was ich gebraucht habe.“ |
| 3 | „Macht, was es soll.“ |
| 4 | „Hab’s meiner Schwiegermutter geschenkt – sie hat sich nicht beschwert ;-)“ |
| 5 | „Nicht schlecht für den Preis.“ |
| 6 | „Der Kundendienst hat sofort reagiert, trotzdem kommt der Ersatz erst nächste Woche.“ |

> [!NOTE]
> **Daraus ergeben sich (reine Rechnung, keine Bewertung)**
>
> | Größe | Rechnung | Ergebnis |
> |---|---|---:|
> | Deutsche Bewertungen pro Jahr | 14.000 × 92 % | 12.880 |
> | Englische Bewertungen pro Jahr | 14.000 × 6 % | 840 |
> | Andere oder unbekannte Sprache | 14.000 × (100 − 92 − 6) % | 280 (2 %) |
> | Heute gelesen (jede zehnte) | 14.000 / 10 | 1.400 |
> | Heute ungelesen | 14.000 − 1.400 | 12.600 (90 %) |
> | Bewertungen mit Emojis | 14.000 × 8 % | 1.120 |
> | Anbieter-Genauigkeit 97 %, Fehlerquote | 100 % − 97 % | 3 % |
> | Anbieter-Daten und Shop-Daten | Hotel, englisch gegen Elektronik, 92 % deutsch | zwei Unterschiede |
> | Wörter je Bewertung, Nr. 1 bis 6 | 7, 12, 4, 10, 5, 12 (Zählung mit Python, "Hab’s" zählt als 2) | Ø 8,3, Shop-Ø: 23 |

## Schritt 1 · Ergebnisraster

| Nr. | Ihre Einordnung (positiv / neutral / negativ) | Wie sicher? (1–5) | Was würde helfen? |
|:---|:---|:---|:---|
| **1 Produkt gut, Lieferung langsam** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **2 "Na toll", nach zwei Wochen kaputt** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **3 "Macht, was es soll"** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **4 Geschenk für Schwiegermutter, nicht beschwert ;-)** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **5 "Nicht schlecht für den Preis"** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |
| **6 Kundendienst schnell, Ersatz kommt später** <br><br><br> | <br><br><br> | <br><br><br> | <br><br><br> |

## Schritt 2 · Unsicherheiten

| Quelle der Unsicherheit | Welche Bewertungen? | Warum unsicher? |
|:---|:---|:---|
| **Mehrere Themen in einer Bewertung** <br><br><br> | <br><br><br> | <br><br><br> |
| **Ironie und Sarkasmus** <br><br><br> | <br><br><br> | <br><br><br> |
| **Verneinung und Abschwächung** ("nicht schlecht") <br><br><br> | <br><br><br> | <br><br><br> |
| **Ohne Wertung, nur Aussage** <br><br><br> | <br><br><br> | <br><br><br> |
| **Fehlender Kontext** (Produkt, Sterne, Erwartung) <br><br><br> | <br><br><br> | <br><br><br> |
| **Die 97 % des Anbieters** <br><br><br> | <br><br><br> | <br><br><br> |

## Schritt 3 · Zusätzliche Informationen

| Information | Hilft bei welcher Bewertung? | Wie genau? |
|:---|:---|:---|
| **Sternebewertung** <br><br><br> | <br><br><br> | <br><br><br> |
| **Produkt oder Kategorie** <br><br><br> | <br><br><br> | <br><br><br> |
| **Vorgang im Kundendienst** <br><br><br> | <br><br><br> | <br><br><br> |
| **Mehrere Einordner und Vergleich** <br><br><br> | <br><br><br> | <br><br><br> |

---

# Teil B: Lösungsentwurf

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Einordnung:** Nr. 2 **negativ** (Sarkasmus, sicher), Nr. 1, 3, 5 **neutral**, Nr. 4 **neutral, ganz unsicher**, Nr. 6 **eher negativ**. Nur **Nr. 2 ist eindeutig**, bei den anderen fünf kann man mit guten Gründen anders entscheiden.
> - **Das ist der Punkt der Aufgabe:** Wenn schon Menschen uneins sind, sind die **Trainingsbeispiele** unscharf, und ein Modell lernt diese Unschärfe mit. Wichtig sind also klare Regeln für die Einordner (Beispiel: gemischte Bewertungen als "neutral") und mehrere Einordner je Bewertung.
> - **Die 97 % des Anbieters** gelten für englische Hotelbewertungen. Der Shop hat zu 92 % deutsche Elektronik-Bewertungen mit Ironie, Verneinung und Emojis. Die Zahl lässt sich **nicht übertragen**. Nötig ist ein eigener Test mit eigenen, von Menschen eingeordneten Bewertungen.
> - **Folgen im Betrieb:** "negativ" löst einen Anruf des Kundendienstes aus, "positiv" ein Zitat auf der Produktseite. Falsch eingeordnet heißt: ein zufriedener Kunde wird angerufen oder ein Spott-Zitat steht auf der Produktseite (Nr. 2 und Nr. 4 sind genau solche Fälle).
> - **Vorsicht:** Die Einordnungen sind **meine Lesart**, es gibt keine "richtige" Lösung. Die Sicherheiten (1 bis 5) sind subjektive Selbsteinschätzungen.

> [!NOTE]
> **Annahmen:** (1) Drei Klassen, "gemischt" gibt es nicht, deshalb landen gemischte Bewertungen bei neutral. (2) Eine Bewertung wird **als Ganzes** eingeordnet, nicht nach Themen getrennt. (3) Das Ziel ist die Folge im Betrieb (Anruf oder Zitat). Die Rechnungen und die Wortlisten-Probe stehen im Python-Check.

## Schritt 1 · Ergebnisraster

| Nr. | Einordnung | Wie sicher? (1–5) | Was würde helfen? |
|:---|:---|:---:|:---|
| **1 Produkt gut, Lieferung langsam** | **neutral** (gemischt) | 3 | **Sterne** (4 Sterne oder 2?). Das Produkt ist gut, die Lieferung ist die Schuld der Logistik, nicht des Produkts. Für die Produktseite wäre die Bewertung eher positiv, für den Kundendienst kein Fall |
| **2 "Na toll", nach zwei Wochen kaputt** | **negativ** | 5 | Hier ist nichts nötig. "Na toll" und "genau, was ich gebraucht habe" sind erkennbar ironisch, "kaputt nach zwei Wochen" ist ein Mangel. Hilfreich wäre nur das **Produkt**, damit der Kundendienst gezielt anruft |
| **3 "Macht, was es soll"** | **neutral** | 3 | **Sterne**. Der Satz ist nüchtern, kann aber Lob ("erfüllt seinen Zweck") oder ein verhaltener Tadel ("nicht mehr") sein |
| **4 Geschenk für Schwiegermutter, nicht beschwert ;-)** | **neutral** | 2 | **Sterne** und **Produkt**. Über das Produkt steht nichts, es geht um die Reaktion der Beschenkten. "Nicht beschwert" ist ein Lob mit Augenzwinkern, das Smiley kann aber auch Ironie bedeuten |
| **5 "Nicht schlecht für den Preis"** | **neutral** (leicht positiv) | 3 | **Preis und Produkt**. "Nicht schlecht" ist abgeschwächtes Lob, "für den Preis" ist eine Einschränkung. Je nach Preisklasse ist es Lob oder Kritik. **Sterne** helfen |
| **6 Kundendienst schnell, Ersatz kommt später** | **eher negativ** | 3 | **Vorgang im Kundendienst**. Die Bewertung lobt den Kundendienst, aber es gab offenbar ein defektes Produkt (Ersatz!). "Trotzdem" zeigt, dass der Ärger überwiegt. Wichtig: **der Kundendienst ist schon in Kontakt**, ein Anruf nach 24 Stunden wäre überflüssig oder lästig |

## Schritt 2 · Unsicherheiten

| Quelle der Unsicherheit | Welche Bewertungen? | Warum unsicher? |
|:---|:---|:---|
| **Mehrere Themen in einer Bewertung** | Nr. 1, 6 | Produkt, Lieferung und Kundendienst werden getrennt bewertet, aber die Aufgabe verlangt eine Klasse. Nr. 1: Produkt gut, Lieferung schlecht. Nr. 6: Kundendienst gut, Ersatz spät |
| **Ironie und Sarkasmus** | Nr. 2 (klar), Nr. 4 (möglich) | Wörter wie "toll" und "genau" sagen das Gegenteil. Beim Lesen ist es klar, am Text selbst nicht. Bei Nr. 4 kann das Smiley auch Ironie signalisieren |
| **Verneinung und Abschwächung** | Nr. 5, 4 | "Nicht schlecht" ist nicht dasselbe wie "gut". "Nicht beschwert" ist nicht "begeistert". Beide liegen zwischen neutral und leicht positiv |
| **Ohne Wertung, nur Aussage** | Nr. 3, 4 | "Macht, was es soll" sagt, dass das Produkt funktioniert, aber nicht, wie der Kunde das findet |
| **Fehlender Kontext** | alle | Ohne Sterne, Produkt, Preis und Erwartung fehlt der Maßstab. Dieselben Worte können bei einem 20-€-Kabel und einer 300-€-Smartwatch etwas anderes bedeuten |
| **Die 97 % des Anbieters** | Gesamtvorhaben | Gemessen an englischen Hotelbewertungen. Der Shop hat Deutsch (92 %), Elektronik, im Schnitt 23 Wörter, 8 % Emojis. Sprache, Thema und Stil sind anders. Genauigkeit sagt außerdem nichts darüber, bei **welchen** Bewertungen der Fehler passiert |

### Wie ein Computer Nr. 2 und Nr. 4 lesen könnte

Ein einfaches Verfahren zählt positive und negative **Wörter**. Das ist hier ein selbst gebautes Spielzeug (Wortliste im Python-Check), kein echtes Produkt. Moderne Sprachmodelle lesen den Zusammenhang besser, machen aber bei Ironie ebenfalls Fehler.

| Nr. | Wortlisten-Lesart | Tatsächlich | Warum falsch? |
|:---|:---|:---|:---|
| **2** | **positiv** (toll, genau gegen kaputt) | negativ | "Na toll" und "genau, was ich gebraucht habe" sind ironisch. Zwei Lobwörter überstimmen ein Problemwort |
| **4** | **negativ** ("beschwert") | neutral, leicht positiv | "Nicht" wird ignoriert. Das Wort "beschwert" zählt als negativ, obwohl es verneint ist |
| 5 | negativ ("schlecht") | neutral, leicht positiv | gleicher Fehler: "nicht schlecht" ist keine Kritik |
| 6 | positiv ("sofort") | eher negativ | das Lob für den Kundendienst überdeckt den Ärger über den späten Ersatz |

> [!NOTE]
> **Was daraus für den Shop folgt (Hypothesen):**
> - **Eigenen Test bauen:** Für den Test genügen einige hundert **deutsche** Bewertungen des Shops, von zwei Personen eingeordnet. Die Größe ist eine Schätzung, kein berechneter Wert. Der Anbieter muss auf genau diesen Daten messen.
> - **Klare Regeln für die Einordner:** Wie werden gemischte Bewertungen, Ironie und Aussagen ohne Wertung behandelt? Ohne Regeln sind die Trainingsbeispiele selbst uneinheitlich.
> - **Unsichere Fälle nicht automatisch behandeln:** Bewertungen ohne klare Stimmung (neutral, ironisch, gemischt) gehen zur Durchsicht an einen Menschen, nur klare Fälle laufen automatisch. Bei Nr. 2 und Nr. 6 wäre ein automatischer Anruf bzw. ein automatisches Zitat ein Fehler.
> - **Stichprobe heute:** Von den 14.000 Bewertungen liest heute niemand 12.600. Die Frage ist also nicht "Computer oder Mensch", sondern: was passiert mit den 90 %, die heute gar nicht gelesen werden?

## Schritt 3 · Zusätzliche Informationen

| Information | Hilft bei welcher Bewertung? | Wie genau? |
|:---|:---|:---|
| **Sternebewertung** | alle, besonders 1, 3, 4, 5 | gibt den Maßstab an. Bei 1 und 3 entscheidet sie, ob neutral zu positiv oder negativ kippt |
| **Produkt oder Kategorie** | 2, 4, 5 | zeigt, ob "kaputt nach zwei Wochen" einen Kopfhörer betrifft (Umsatzträger) und was "für den Preis" bedeutet |
| **Vorgang im Kundendienst** | 6, 2 | zeigt, ob der Kunde schon Kontakt hatte. Verhindert den überflüssigen Anruf |
| **Mehrere Einordner und Vergleich** | 1, 3, 4, 5 | zeigt, wo die Bewertung wirklich mehrdeutig ist. Je mehr Abweichung, desto weniger taugt sie als Trainingsbeispiel |
| **Bestellung und Lieferung** | 1 | trennt die Beschwerde über die Logistik von der über das Produkt |

## Python-Check

```python
# python3 -I check.py   (benötigt nur die Standardbibliothek)
import re

n = 14_000
print(n * 0.92, n * 0.06, n * (1 - 0.92 - 0.06))   # 12880, 840, 280
print(n / 10, n - n / 10, n * 0.08)                 # 1400 gelesen, 12600 ungelesen, 1120 mit Emojis

bewertungen = {
    1: "Produkt ist gut, aber Lieferung war langsam.",
    2: "Na toll. Nach zwei Wochen schon kaputt. Genau, was ich gebraucht habe.",
    3: "Macht, was es soll.",
    4: "Hab’s meiner Schwiegermutter geschenkt – sie hat sich nicht beschwert ;-)",
    5: "Nicht schlecht für den Preis.",
    6: "Der Kundendienst hat sofort reagiert, trotzdem kommt der Ersatz erst nächste Woche.",
}
print([len(re.findall(r"\w+", t)) for t in bewertungen.values()])   # Wörter: 7, 12, 4, 10, 5, 12 ("Hab’s" zählt als zwei)

# Spielzeug-Wortliste: selbst erfunden, KEIN echtes Produkt, ignoriert Verneinung und Ironie
positiv = {"gut", "toll", "genau", "sofort"}
negativ = {"langsam", "kaputt", "schlecht", "beschwert"}
for nr, text in bewertungen.items():
    wörter = re.findall(r"\w+", text.lower())
    punkte = sum(w in positiv for w in wörter) - sum(w in negativ for w in wörter)
    print(nr, punkte, "positiv" if punkte > 0 else "negativ" if punkte < 0 else "neutral")
# 1: neutral, 2: positiv (falsch), 3: neutral, 4: negativ (falsch), 5: negativ (falsch), 6: positiv (falsch)
```

Ergebnis: Die Spielzeug-Wortliste liegt bei den Nummern 2, 4, 5 und 6 **daneben**: Ironie (Nr. 2), Verneinung (Nr. 4 und 5) und ein Lob mit Ärger (Nr. 6) erkennt sie nicht. Das ist kein Test eines echten Anbieters, es zeigt nur, **welche Sorte Fehler** bei Stimmungsanalyse typisch ist. Die 97 % des Anbieters sagen nichts über diese Fälle, weil sie an englischen Hotelbewertungen gemessen wurden.
