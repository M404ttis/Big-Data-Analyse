# Tag 11 · UE 5–6 · Fallstudie InsightAnalytics: „Wo verlieren wir, und warum?“

Aufgabe: Analysefragen entwickeln, geeignete Visualisierungen wählen, Handlungsempfehlungen ableiten. Die Fallstudie liefert **keine Detaildaten**, sondern nur den Standardbericht und Rahmeninformationen. Das Ergebnis sind also gut begründete Fragen und Hypothesen, die an den Auftragsdaten (ca. 47.000 Aufträge) zu prüfen sind. Keine Ursache ist bereits bewiesen.

## Teil A: Fakten und Rechnungen

Aus dem Standardbericht lässt sich schon einiges ableiten:

| Kennzahl | Vorjahr | Aktuell | Veränderung |
|---|---|---|---|
| Umsatz | 8,45 Mio. € | 8,40 Mio. € | −0,6 % |
| Aufträge | 9.800 | 10.900 | +11,2 % |
| **Ø Umsatz je Auftrag** | **862 €** | **771 €** | **−10,6 %** |
| Kunden | 3.480 | 3.510 | +0,9 % |
| **Aufträge je Kunde** | **2,82** | **3,11** | **+10,3 %** |
| Umsatz je Kunde | 2.428 € | 2.393 € | −1,4 % |
| Ø Rabatt | 8,1 % | 9,6 % | +1,5 Pkt. |
| Rückgerechnetes Listenpreisvolumen (Umsatz / (1 − Rabatt)) | ca. 9,19 Mio. € | ca. 9,29 Mio. € | **+1,1 %** |
| Bearbeitung und Versand (95 € je Auftrag) | ca. 931.000 € | ca. 1.036.000 € | **+105.000 €** |
| Bearbeitungskosten in % des Umsatzes | 11,0 % | 12,3 % | +1,3 Pkt. |

Was daraus folgt:

1. **Die Kunden bestellen häufiger, aber kleiner.** Der Kundenstamm ist stabil, die Kunden bestellen 10 % öfter, doch jeder Auftrag ist 10,6 % kleiner. Der Umsatz je Kunde sinkt leicht. „Mehr Aufträge, mehr Kunden, gleicher Umsatz“ ist kein Wachstum, sondern **Zersplitterung**.
2. **Rabatte kosten rund 140.000 € Umsatz.** Bei gleichem Listenpreisvolumen und dem Vorjahresrabatt von 8,1 % läge der Umsatz bei ca. 8,54 Mio. €, also **+1,1 % statt −0,6 %**. Rechnung: 9,29 Mio. € × 1,5 Pkt. ≈ 139.000 €. Das Listenpreisvolumen wächst leicht, der gestiegene Rabatt frisst das Wachstum auf. (Annahme: Ø Rabatt bezogen auf den Listenpreis, gleichmäßig verteilt. Das ist eine Näherung.)
3. **Die Kosten steigen, obwohl der Umsatz stagniert.** 1.100 zusätzliche Aufträge kosten bei 95 € rund 105.000 € zusätzlich. Das ist fast so viel wie der Rabattverlust. Rabatt und Auftragskosten zusammen: etwa **245.000 €** mehr Belastung als im Vorjahr (ca. 2,9 % vom Umsatz). Die tatsächliche Marge kennen wir nicht (Kosten sind nicht im System). Der Effekt auf den Ertrag ist deshalb größer als der Umsatzeffekt.
4. **Der Standardbericht zeigt nur Summen.** Verschiebungen zwischen Regionen, Produktlinien und Kundentypen können sich darin gegenseitig aufheben.

**Als Ablenkung eingeordnet:** 25-jähriges Firmenjubiläum und Umzug ins neue Bürogebäude (kein Bezug zur Umsatzfrage).
**Relevant:** zwei unbesetzte Stellen in West seit Herbst, Onlineportal für Hochschulen seit Januar, Rabattspielraum bis 15 %, Wettbewerber mit neuem Servicestützpunkt im Süden.

## Teil B: Hypothesen zu „mehr Aufträge, gleicher Umsatz“

| Nr. | Hypothese | Gestützt durch | Prüfbar an |
|---|---|---|---|
| H1 | **Kleinere Aufträge**: Der Mix verschiebt sich zu Zubehör und Service (kleiner Wert je Auftrag) und weg von Geräten | Umsatz je Auftrag −10,6 % | Aufträge nach Produktlinie und Auftragsgröße über 5 Jahre |
| H2 | **Onlineportal der Hochschulen** erzeugt viele Kleinbestellungen (früher gebündelt über den Vertrieb) | Portal seit Januar | Aufträge nach Kundentyp und Bestellweg, Ø Auftragswert Hochschule vor/nach Januar |
| H3 | **Rabattdruck**: Außendienst gewährt zu großzügig (bis 15 %), vielleicht als Reaktion auf den Wettbewerber im Süden | Ø Rabatt +1,5 Pkt. | Rabatt nach Region, Betreuer, Produktlinie, Kundentyp |
| H4 | **West verliert**: zwei von drei Stellen unbesetzt, Kunden bestellen weniger oder wandern ab | Vakanz seit Herbst | Umsatz je Region und Monat, Betreuungsquote, Kunden ohne Aufträge |
| H5 | **Süd verliert** Geschäft (Service) an den Wettbewerber | Neuer Servicestützpunkt | Umsatz Service nach Region vor/nach Eröffnung, Abwanderung von Bestandskunden |
| H6 | **Ein einzelnes Segment** (z. B. Premium oder Klinik) bricht ein, andere wachsen leicht (Simpson-Effekt der Summe) | Standardbericht nur Summen | Umsatz je Segment mit Vorjahresvergleich |

## Teil C: Ergebnisraster

| Analysefrage | Benötigte Daten | Visualisierung | Mögliche Maßnahme |
|---|---|---|---|
| **1. In welchen Regionen, Produktlinien und Kundentypen ist der Umsatz gesunken oder gestiegen?** (Wo verlieren wir?) | Aufträge mit Region, Produktlinie, Kundentyp, Datum, Umsatz (2 Jahre) | **Wasserfall-/Δ-Balken** der Umsatzveränderung nach Segment, sortiert, mit Nulllinie (Verlierer rot, Gewinner blau); dazu Heatmap Region × Produktlinie als Δ % | Maßnahmen auf die größten Verlustsegmente richten statt Gesamtziel |
| **2. Hat sich die Auftragsgröße verändert, und wo?** | Auftragswert je Auftrag, Datum, Kundentyp, Produktlinie | **Histogramm bzw. Boxplot** des Auftragswerts, Vorjahr gegen aktuell; Linie Ø Auftragswert je Monat | Mindestbestellwert, Staffelpreise, Bündelangebote |
| **3. Wie hat sich der Produktmix verändert?** | Positionen mit Produktlinie, Menge, Listenpreis | **100 %-gestapelte Balken** je Jahr (Geräte-Linien, Service, Zubehör) | Geräteverkauf gezielt stärken, Zubehör/Service bündeln |
| **4. Welche Rolle spielen Rabatte? Wo steigen sie, und bringen sie Umsatz?** | Rabatt je Position, Region, Betreuer, Kundentyp, Produktlinie, Umsatz | **Balken Ø Rabatt je Betreuer/Region** (mit Rabattgrenze 15 %); **Streudiagramm** Rabatt vs. Auftragswert; Verteilung der Rabatte | Rabattrichtlinie, Freigabe ab 10 %, Auswertung je Betreuer |
| **5. Was bewirkt die Vakanz in West?** | Umsatz und Kunden je Region/Monat, Betreuer | **Liniendiagramm** Umsatz je Region mit Markierung „Herbst: 2 Stellen frei“; Kundenaktivität (Kunden mit ≥ 1 Auftrag je Quartal) | Stellen schnell besetzen, Schlüsselkunden übergangsweise zuordnen |
| **6. Was verändert das Onlineportal der Hochschulen?** | Aufträge nach Kundentyp und Bestellweg, Datum | **Liniendiagramm** Aufträge und Ø Wert Hochschule, Vorher/Nachher (Januar) | Portal mit Mindestmenge, Sammelbestellungen, Versandkosten |
| **7. Wie wirkt der Wettbewerber im Süden?** | Service-Umsatz und Kundenabgänge je Region, Datum | **Liniendiagramm** Service Süd vs. andere Regionen, Eröffnungsdatum markiert; Kundenabgänge je Quartal | Service-Offensive im Süden, Wartungsverträge, Bindung |
| **8. Was kostet uns die Auftragsflut?** | Aufträge, 95 € je Auftrag (Annahme), Auftragswert | **Kumulierte Kurve** der Aufträge nach Wert (Pareto) mit Marke „Auftragswert < Break-even“ | Kleinaufträge bündeln, Versandpauschale, Online-Bestellpflicht für Zubehör |
| **9. Welche Kunden sind gewachsen oder abgewandert?** | Kunde, Kunde seit, Umsatz je Jahr | **Dumbbell** Vorjahr → aktuell für die Top-20-Kunden; Streudiagramm Aufträge je Kunde vs. Umsatz je Kunde | Key-Account-Pflege, Rückgewinnung |

Hinweis zu 1: Ein Kreisdiagramm taugt hier nicht. Für Veränderungen zählt der Vergleich mit dem Vorjahr, nicht der Anteil.

## Teil D: Handlungsempfehlungen an die Geschäftsführung

**Erste Antwort auf „Wo verlieren wir, und warum?“:** Nicht bei der Zahl der Kunden oder Aufträge, sondern **im Wert je Auftrag**. Aufträge werden kleiner, Rabatte größer, Bearbeitungskosten steigen. Der Umsatz stagniert, der Ertrag leidet vermutlich stärker.

| Zeitraum | Empfehlung | Begründung |
|---|---|---|
| **Sofort (Monat 1)** | Auswertung der Auftragsdaten nach Region, Produktlinie, Kundentyp und Betreuer (Fragen 1, 2, 4) | Prüft H1–H6 und zeigt, wo das Problem wirklich liegt, bevor Maßnahmen beschlossen werden |
| **Sofort** | **Rabatt-Transparenz**: Bericht Ø Rabatt je Betreuer und Region monatlich an den Vertrieb | Rabattanstieg kostet ca. 140.000 €. Freigabe ab einer Schwelle (z. B. 10 %) statt freier Entscheidung bis 15 % |
| **Kurzfristig (Monat 1–3)** | **West-Vakanz** schließen oder überbrücken (Vertretung, Innendienst für Schlüsselkunden) | Zwei Stellen sind ein Drittel der Betreuungskapazität im Gebiet |
| **Kurzfristig** | **Kleinaufträge** prüfen: Mindestbestellwert, Bündelung, Versandpauschale, Portal mit Sammelbestellung | 1.100 zusätzliche Aufträge verursachen etwa 105.000 € Zusatzkosten |
| **Mittelfristig** | **Süd**: Servicekonzept (Wartungsverträge, Reaktionszeiten), falls H5 sich bestätigt | Antwort auf den Wettbewerber, ohne nur über den Preis zu gehen |
| **Mittelfristig** | Monatliches **Dashboard** in Power BI (vorhanden): Umsatz, Aufträge, Auftragswert, Rabatt je Region/Linie/Kundentyp | Standardbericht zeigt nur Summen, nötig ist die Aufteilung |
| **Datenlücken schließen** | **Kosten und Marge je Linie** ins Reporting aufnehmen (ERP), Bestellweg als Feld | Ohne Margen keine Aussage zum Ertrag, ohne Bestellweg keine Portalanalyse |

Priorisierung nach Wirkung und Aufwand: Rabatt-Transparenz (hoher Effekt, geringer Aufwand) vor Mindestbestellwert (mittlerer Effekt, Kundenrisiko) vor Süd-Servicekonzept (hoher Aufwand).

## Teil E: Python-Kontrollrechnung

```python
v, a = 8.45e6, 8.40e6          # Umsatz Vorjahr / aktuell
nv, na = 9800, 10900           # Aufträge
kv, ka = 3480, 3510            # Kunden
rv, ra = 0.081, 0.096          # Ø Rabatt

print(v / nv, a / na, a / na / (v / nv) - 1)        # 862, 771, -10,6 %
print(nv / kv, na / ka)                              # 2,82 -> 3,11
liste_v, liste_a = v / (1 - rv), a / (1 - ra)
print(liste_a / liste_v - 1)                         # +1,1 % Listenvolumen
print(liste_a * (ra - rv))                           # ca. 139.000 € Rabattverlust
print((na - nv) * 95)                                # 104.500 € Zusatzkosten
```
