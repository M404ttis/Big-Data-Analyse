# Tag 10 (Modul 3), Arbeitsauftrag 1: Umsatzzahlen eines Gartenmöbelherstellers zeigen

> [!IMPORTANT]
> **Auf einen Blick**
>
> - **Hauptbild: ein Liniendiagramm mit zwei Linien** (aktuelles Jahr kräftig, Vorjahr grau und gestrichelt), zwölf Monate auf der Achse. Es zeigt Saison, Vorjahresvergleich und Ausreißer in einem Blick. Die Tabelle gibt das nicht her.
> - **Die Saison ist extrem.** April bis Juni bringen 2.797 von 6.573 Tsd. € (42,6 %). Spitze Mai (1.004), Tiefpunkt November (281): Faktor 3,6. Das Vorjahr hat dieselbe Form (Faktor 3,5).
> - **Der Vorjahresvergleich ist gut:** +478 Tsd. € (+7,8 %), 11 von 12 Monaten liegen darüber. Der Plan (6,4 Mio. €) ist mit 6.573 Tsd. € um 173 Tsd. € (+2,7 %) übertroffen.
> - **Auffällig ist der August:** als einziger Monat unter dem Vorjahr (455 statt 480, -5,2 %). Das passt zum Teakholz-Ausfall und den zwei Bestsellern, die sechs Wochen nicht lieferbar waren. Ohne Ausfall wären grob 523 zu erwarten gewesen, es fehlen also rund **68 Tsd. €** (Schätzung).
> - **Ungeeignet:** ein **Kreisdiagramm** der Monate (Reihenfolge und Vorjahr gehen verloren, Oktober 4,9 % und Dezember 4,8 % sind nicht zu unterscheiden), außerdem **3D-Säulen** und alles, was **nur über die Farbe** funktioniert, denn der Bericht wird schwarz-weiß gedruckt.
> - **Zweites Bild: gestapelte Säulen je Quartal nach Vertriebsweg.** Der Onlineshop-Anteil steigt von 12,5 % (Q1) auf 21,3 % (Q4). Das ist aber vermutlich **Saison**, kein Trend: Der Online-Umsatz schwankt weniger als der Handel. Für einen Trend fehlt der Vorjahreswert je Vertriebsweg.

> [!NOTE]
> **Annahmen:** (1) "Aktuell" und "Vorjahr" sind volle Kalenderjahre in Tsd. € je Monat. Die Quartalssummen der zweiten Tabelle stimmen mit den Monaten überein (geprüft). (2) Der Plan von 6,4 Mio. € gilt für das ganze Jahr. Ein Monatsplan fehlt, er wird deshalb nur als Jahreszahl gezeigt. (3) Die Schätzung für den August setzt voraus, dass er sonst so gewachsen wäre wie die anderen elf Monate (+9,0 %). Der Rückgang von Juli auf August ist schon im Vorjahr da (-25 %), ein Teil davon ist also normale Saison. (4) Ob die Messe in Köln im Juni etwas bewirkt hat, geben die Zahlen nicht her: Der Juni liegt mit +9,3 % im Rahmen. Es gibt keine Angabe zum Messetermin oder zu Aufträgen von dort.

## Die Zahlen auf einen Blick

| Größe | Rechnung | Ergebnis |
|---|---|---:|
| Umsatz Vorjahr | Summe der 12 Monate | 6.095 Tsd. € |
| Umsatz aktuell | Summe der 12 Monate | 6.573 Tsd. € |
| Wachstum | 6.573 - 6.095 | +478 Tsd. € (+7,8 %) |
| Plan | 6.573 / 6.400 | +173 Tsd. € (+2,7 %) |
| Stärkste Monate | Apr bis Jun | 2.797 Tsd. € (42,6 %) |
| Spitze zu Tiefpunkt | Mai 1.004 / Nov 281 | Faktor 3,6 |
| Einziger Monat unter Vorjahr | August 455 gegen 480 | -25 Tsd. € (-5,2 %) |
| Anteil je Vertriebsweg | Fachhandel / Baumärkte / Onlineshop | 54,2 % / 30,2 % / 15,6 % |
| Online-Anteil je Quartal | Online / Gesamt | 12,5 / 14,6 / 16,8 / 21,3 % |

## 1. Wie würde ich die Daten darstellen?

**Bild 1 (Hauptfolie): Umsatz je Monat, aktuelles Jahr gegen Vorjahr.** Zwei Linien, Monate von Januar bis Dezember. Die Überschrift sagt die Botschaft: *"Umsatz 7,8 % über Vorjahr, nur der August liegt darunter."*

```mermaid
%%{init: {"themeVariables": {"xyChart": {"plotColorPalette": "#1B5E20, #9E9E9E"}}}}%%
xychart-beta
    title "Umsatz je Monat in Tsd. EUR (grün: aktuell, grau: Vorjahr)"
    x-axis [Jan, Feb, Mär, Apr, Mai, Jun, Jul, Aug, Sep, Okt, Nov, Dez]
    y-axis "Tsd. EUR" 0 --> 1100
    line [335, 362, 571, 842, 1004, 951, 702, 455, 430, 322, 281, 318]
    line [310, 345, 520, 780, 910, 870, 640, 480, 390, 300, 260, 290]
```

Für die Folie selbst (Beamer und Schwarz-Weiß-Druck):

- **Direkt beschriften statt Legende:** "aktuell" und "Vorjahr" am Linienende, Maximum (Mai 1.004) und Tiefpunkt (Nov 281) mit Zahl.
- **Nicht nur Farbe:** aktuell dick und durchgezogen in **Dunkelgrün**, Vorjahr dünn, **gestrichelt, grau**. Dunkelgrün wird im Druck dunkelgrau. Das **Sand** der Firmenfarben wäre auf Weiß zu hell und eignet sich nur für Flächen, nicht für Linien.
- **Eine Markierung für den August** (Pfeil mit "Teakholz-Lieferausfall, zwei Bestseller sechs Wochen nicht lieferbar"). Der Juni bekommt keine Messe-Beschriftung, weil sich ein Effekt nicht belegen lässt.
- **Beamer:** große Schrift (mindestens 18 pt), wenig Gitterlinien, nicht mehr als zwei Linien.

**Bild 2: Abweichung zum Vorjahr in Prozent je Monat** (Säulen, Nulllinie in der Mitte). Das beantwortet "Wo sieht man den Vergleich zum Vorjahr?" am schnellsten. Alle Säulen liegen im Plus bis auf den August.

```mermaid
%%{init: {"themeVariables": {"xyChart": {"plotColorPalette": "#1B5E20"}}}}%%
xychart-beta
    title "Abweichung zum Vorjahr in Prozent"
    x-axis [Jan, Feb, Mär, Apr, Mai, Jun, Jul, Aug, Sep, Okt, Nov, Dez]
    y-axis "Prozent" -10 --> 12
    bar [8.1, 4.9, 9.8, 7.9, 10.3, 9.3, 9.7, -5.2, 10.3, 7.3, 8.1, 9.7]
```

**Bild 3: Umsatz je Quartal nach Vertriebsweg** als **gestapelte Säulen** (Fachhandel unten, Baumärkte, Onlineshop oben, Gesamtsumme über jeder Säule). Mit den Zahlen der Aufgabe:

| Vertriebsweg | Q1 | Q2 | Q3 | Q4 | Jahr | Anteil |
|:---|---:|---:|---:|---:|---:|---:|
| Fachhandel | 720 | 1.510 | 850 | 480 | 3.560 | 54,2 % |
| Baumärkte | 390 | 880 | 470 | 245 | 1.985 | 30,2 % |
| Onlineshop | 158 | 407 | 267 | 196 | 1.028 | 15,6 % |
| **Gesamt** | **1.268** | **2.797** | **1.587** | **921** | **6.573** | 100 % |

Im Schwarz-Weiß-Druck werden die drei Schichten durch **Schraffur** oder drei Graustufen und direkte Beschriftung unterschieden. Wer die Anteile je Quartal sehen will, nimmt stattdessen auf 100 % gestapelte Säulen. Sie zeigen den steigenden Online-Anteil klar, verstecken aber, dass Q2 mehr als dreimal so groß ist wie Q4.

**Zusätzlich ein Zahlenfeld:** *"Jahresumsatz 6,57 Mio. € - Plan 6,4 Mio. € - +2,7 %"*. Der Plan hat nur einen Jahreswert, eine Linie würde einen Monatsplan vortäuschen.

## 2. Welche Darstellung macht Trends am besten sichtbar?

Das **Liniendiagramm**, weil die Linie die **Reihenfolge der Monate** zeigt und das Auge Steigung und Richtung dort am besten liest. Zwei Linien übereinander machen sofort klar, dass die Form gleich ist (Anstieg bis Mai, Einbruch im Herbst) und das aktuelle Jahr fast überall oben liegt.

Was man darin lesen kann:

- **Saison:** Der Umsatz steigt von 335 im Januar auf 1.004 im Mai und fällt auf 281 im November. Das Vorjahr verläuft genauso, die Saison ist also **kein einmaliges Ereignis**.
- **Wachstum:** Der Abstand der beiden Linien ist fast überall ähnlich groß (+5 bis +10 %), das Wachstum ist gleichmäßig.
- **Ausreißer:** Im August kreuzt die aktuelle Linie unter die graue. Das ist der einzige Monat, der auffällt.

Für die Frage "Wann entscheidet sich das Geschäftsjahr?" zeigt Bild 3, dass **Q2** 42,6 % vom Jahr trägt und der **Fachhandel** darin 1.510 von 2.797 Tsd. € (54,0 %).

## 3. Welche Darstellung wäre ungeeignet, und warum?

| Darstellung | Warum ungeeignet |
|---|---|
| **Kreisdiagramm mit zwölf Monaten** | Zwölf Stücke sind kaum lesbar. Die **Zeitreihenfolge** geht verloren. Oktober (4,9 %) und Dezember (4,8 %) sehen gleich aus. Für das Vorjahr bräuchte man einen zweiten Kreis, den Vergleich macht dann niemand. Der August-Einbruch bleibt unsichtbar. |
| **3D-Säulen oder 3D-Kreis** | Die Perspektive verzerrt: Hintere Säulen wirken kleiner, Zahlen lassen sich nicht ablesen. Es gibt keinen Informationsgewinn gegenüber 2D. |
| **Säulen mit abgeschnittener Achse** (zum Beispiel erst ab 250) | Die Säulenhöhe soll den Wert zeigen. Wer bei 250 beginnt, lässt den November (281) fast verschwinden und den Mai übertrieben aussehen. Bei Säulen immer bei **null** beginnen. |
| **Nur Farbe zur Unterscheidung** | Der Bericht wird schwarz-weiß gedruckt. Zwei ähnlich helle Farben (zum Beispiel Sand und Hellgrün) werden zu **derselben Graustufe**. Linienstil, Schraffur und Beschriftung verwenden. |
| **Die Tabelle allein** | 24 Zahlen nebeneinander: Man muss rechnen, um die Saison oder den August zu finden. Die meisten lesen sie deshalb nicht. Als Anhang sinnvoll, als Hauptbild nicht. |
| **Ein Diagramm mit allem** (Monate, Vorjahr, Vertriebsweg, Plan) | Zu viele Linien und Farben. Besser zwei oder drei einfache Bilder mit je einer Aussage. |

## Ergebnisraster (Darstellung, was sie gut zeigt, was sie verschleiert)

| Darstellung | Was sie gut zeigt | Was sie verschleiert |
|:---|:---|:---|
| **Tabelle** (heute) | Exakte Werte zum Nachschlagen | Saison, Trend und Ausreißer. Man muss selbst vergleichen und rechnen |
| **Liniendiagramm, 2 Linien** | Saison, Verlauf, Vorjahresvergleich, Ausreißer (August) | Exakte Werte (nur mit Beschriftung), Prozentabweichung, Vertriebsweg |
| **Gruppierte Säulen** (je Monat zwei Säulen) | Vergleich Monat gegen Vorjahr, Zahlen gut ablesbar | Den Verlauf über das Jahr. Bei 24 Säulen wird es voll, die Saison ist weniger auffällig als in der Linie |
| **Abweichungssäulen in %** | Wachstum je Monat, August als einziges Minus | Die **Größe** der Umsätze: +10 % im Mai (94 Tsd. €) und +10 % im September (40 Tsd. €) sehen gleich aus |
| **Gestapelte Säulen je Quartal** | Gesamtumsatz und Anteile der Vertriebswege je Quartal | Die Veränderung der mittleren Schicht (Baumärkte): Sie sitzt nicht auf der Nulllinie, ihre Höhe ist schwer abzulesen |
| **Kreisdiagramm** | Anteil am Ganzen, nur bei wenigen Teilen (Jahresanteil der drei Vertriebswege geht) | Zeitreihenfolge, Vorjahr, kleine Unterschiede. Bei zwölf Monaten ungeeignet |

## Antworten auf die Fragen der Folien

- **Welche Skizze zeigt die Saison am besten?** Das Liniendiagramm mit zwei Jahren. Bild 3 zeigt sie nur grob in vier Quartalen.
- **Wo sieht man den Vergleich zum Vorjahr?** Im Liniendiagramm (Abstand der Linien) und am genauesten in den Abweichungssäulen in Prozent.
- **Welcher Monat fällt auf, und warum?** Der **August**: als einziger unter dem Vorjahr (455 gegen 480, -5,2 %), während die anderen elf Monate zwischen +4,9 % und +10,3 % liegen. Mögliche Ursache nach dem Blatt: Teakholz-Lieferausfall, zwei Bestseller sechs Wochen nicht lieferbar. Das ist eine **plausible Erklärung, kein Beweis**. Eine Lieferstatistik oder die Absatzzahlen der beiden Bestseller würden es belegen. Auffällig ist auch der **Mai** als Spitze, aber das ist Saison und liegt im Vorjahr genauso.

## Fehler, die man vermeiden sollte

- **Die Botschaft in den Titel schreiben**, nicht nur "Umsatz pro Monat". Der Titel sagt, was man sehen soll.
- **Nicht jede Zahl zeigen.** Ein Bild pro Aussage: Saison und Vorjahr (Linie), Vertriebswege (gestapelte Säulen), Plan (eine Zahl).
- **Einen Trend nicht behaupten, wo nur Saison ist.** Der steigende Online-Anteil von 12,5 % auf 21,3 % ist ohne Vorjahreswert je Vertriebsweg **kein Beleg für Online-Wachstum**.
- **Nicht ohne Beleg erklären.** Messe im Juni und Kollektion "Lago" sind genannt, aber ohne Bezug zu den Monatszahlen. Sie gehören nicht als Ursache ins Diagramm.

## Python-Check

```python
# python3 -I check.py   (nur Standardbibliothek)
monate = ["Jan","Feb","Mär","Apr","Mai","Jun","Jul","Aug","Sep","Okt","Nov","Dez"]
vor = [310,345,520,780,910,870,640,480,390,300,260,290]
akt = [335,362,571,842,1004,951,702,455,430,322,281,318]
weg = {"Fachhandel":[720,1510,850,480],"Baumärkte":[390,880,470,245],"Onlineshop":[158,407,267,196]}
gesamt_q = [1268,2797,1587,921]

sv, sa = sum(vor), sum(akt)
print(f"Summe Vorjahr {sv}  aktuell {sa}  Wachstum {sa-sv} ({(sa/sv-1)*100:.1f} %)")
print(f"Plan 6.400: Ist {sa}  Abweichung {sa-6400} ({(sa/6400-1)*100:+.1f} %)")
print("Abweichung je Monat zum Vorjahr:")
for m,v,a in zip(monate,vor,akt):
    print(f"  {m}: {a-v:+4d}  {(a/v-1)*100:+5.1f} %")
print("Monate über Vorjahr:", sum(a>v for v,a in zip(vor,akt)), "von 12")
q = lambda l:[sum(l[i:i+3]) for i in (0,3,6,9)]
print("Quartale aktuell", q(akt), " Vorjahr", q(vor))
print("Quartalssummen = Vertriebsweg-Gesamt?", q(akt)==gesamt_q, " Summe Wege je Q:", [sum(w[i] for w in weg.values()) for i in range(4)])
tot = {k:sum(v) for k,v in weg.items()}
print("Jahr je Weg", tot, " Summe", sum(tot.values()))
for k,v in tot.items(): print(f"  Anteil {k}: {v/sa*100:.1f} %")
print("Online-Anteil je Quartal:", [f"{weg['Onlineshop'][i]/gesamt_q[i]*100:.1f} %" for i in range(4)])
print("Fachhandel-Anteil je Quartal:", [f"{weg['Fachhandel'][i]/gesamt_q[i]*100:.1f} %" for i in range(4)])
top3 = sorted(akt)[-3:]
print(f"Apr-Jun: {sum(akt[3:6])} = {sum(akt[3:6])/sa*100:.1f} % vom Jahr;  Mai-Jul: {sum(akt[4:7])}")
print(f"Spitze Mai {max(akt)} / Tiefpunkt Nov {min(akt)} = Faktor {max(akt)/min(akt):.1f}")
print(f"Vorjahr: Spitze {max(vor)} (Mai) / Tiefpunkt {min(vor)} (Nov) = Faktor {max(vor)/min(vor):.1f}")
# August: Rückgang Juli->August
print(f"Jul->Aug  Vorjahr {(vor[7]/vor[6]-1)*100:.1f} %  aktuell {(akt[7]/akt[6]-1)*100:.1f} %")
# Annahme: August hätte das Wachstum der übrigen Monate gehabt
rest_v = sum(v for i,v in enumerate(vor) if i!=7); rest_a = sum(a for i,a in enumerate(akt) if i!=7)
g = rest_a/rest_v-1
print(f"Wachstum ohne August {g*100:.1f} %  -> August erwartet {vor[7]*(1+g):.0f}, fehlen {vor[7]*(1+g)-akt[7]:.0f} Tsd. €")
print(f"Kreisdiagramm: kleinster Monat Nov {akt[10]/sa*100:.1f} %, größter Mai {akt[4]/sa*100:.1f} %; Nov vs Dez {akt[10]/sa*100:.1f} % / {akt[11]/sa*100:.1f} %")
# 2 Monate mit ähnlichen Werten im Kreis
print("Beispiel Oktober vs Dezember:", akt[9], akt[11], "->", f"{akt[9]/sa*100:.1f} % vs {akt[11]/sa*100:.1f} %")
```

Ausgabe:

```text
Summe Vorjahr 6095  aktuell 6573  Wachstum 478 (7.8 %)
Plan 6.400: Ist 6573  Abweichung 173 (+2.7 %)
Abweichung je Monat zum Vorjahr:
  Jan:  +25   +8.1 %
  Feb:  +17   +4.9 %
  Mär:  +51   +9.8 %
  Apr:  +62   +7.9 %
  Mai:  +94  +10.3 %
  Jun:  +81   +9.3 %
  Jul:  +62   +9.7 %
  Aug:  -25   -5.2 %
  Sep:  +40  +10.3 %
  Okt:  +22   +7.3 %
  Nov:  +21   +8.1 %
  Dez:  +28   +9.7 %
Monate über Vorjahr: 11 von 12
Quartale aktuell [1268, 2797, 1587, 921]  Vorjahr [1175, 2560, 1510, 850]
Quartalssummen = Vertriebsweg-Gesamt? True  Summe Wege je Q: [1268, 2797, 1587, 921]
Jahr je Weg {'Fachhandel': 3560, 'Baumärkte': 1985, 'Onlineshop': 1028}  Summe 6573
  Anteil Fachhandel: 54.2 %
  Anteil Baumärkte: 30.2 %
  Anteil Onlineshop: 15.6 %
Online-Anteil je Quartal: ['12.5 %', '14.6 %', '16.8 %', '21.3 %']
Fachhandel-Anteil je Quartal: ['56.8 %', '54.0 %', '53.6 %', '52.1 %']
Apr-Jun: 2797 = 42.6 % vom Jahr;  Mai-Jul: 2657
Spitze Mai 1004 / Tiefpunkt Nov 281 = Faktor 3.6
Vorjahr: Spitze 910 (Mai) / Tiefpunkt 260 (Nov) = Faktor 3.5
Jul->Aug  Vorjahr -25.0 %  aktuell -35.2 %
Wachstum ohne August 9.0 %  -> August erwartet 523, fehlen 68 Tsd. €
Kreisdiagramm: kleinster Monat Nov 4.3 %, größter Mai 15.3 %; Nov vs Dez 4.3 % / 4.8 %
Beispiel Oktober vs Dezember: 322 318 -> 4.9 % vs 4.8 %
```
