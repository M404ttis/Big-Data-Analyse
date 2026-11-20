#!/usr/bin/env python3
"""Misst, wie gut ein Bereinigungsskript die Prüfdaten repariert hat.

Aufruf:   python3 auswerten.py bereinigt_B.csv   (ohne Angabe: STANDARD, s. u.)

Verglichen werden drei Dateien: die Rohdaten (bestellungen_B.csv), die bereinigte Datei Ihres
Skripts und die Referenz mit dem richtigen Wert jeder Zelle (referenz_B.csv). Funktioniert ebenso
für die Übungsdaten A (dann werden referenz_A.csv und bestellungen_A.csv gesucht).

Fehlerhafte Werte (in den Rohdaten falsch):
  geheilt          jetzt richtig
  markiert         unverändert (auch: nur ins Zielformat umgeschrieben) oder geleert,
                   und die Zeile hat einen Hinweis   (ehrlich: „nicht sicher“)
  übersehen        unverändert, kein Hinweis
  falsch geändert  verändert, aber nicht auf den richtigen Wert
  mit Zeile gelöscht
Korrekte Werte und Zeilen:
  Schaden          korrekter Wert verändert, oder echte Bestellung gelöscht
Zeilen, die doppelt erfasst sind, gelten als erledigt, wenn genau eine der Zeilen übrig bleibt.
"""
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

import pandas as pd

HERE = Path(__file__).resolve().parent
SPALTEN = ["quelle", "kunde", "bestelldatum", "betrag", "plz", "ort", "artikelgruppe"]
ZAHL = re.compile(r"^-?\d+(\.\d+)?$")
STANDARD = "bereinigt_B.csv"   # wird geprüft, wenn beim Aufruf keine Datei angegeben ist


def lade(pfad):
    with open(pfad, encoding="utf-8") as f:
        kopf = f.readline()
    sep = ";" if kopf.count(";") >= kopf.count(",") else ","
    return pd.read_csv(pfad, sep=sep, dtype=str, keep_default_na=False, encoding="utf-8")


def finde(name):
    for d in [HERE, HERE.parent, HERE.parent.parent, Path.cwd()]:
        if (d / name).exists():
            return d / name
    sys.exit(f"{name} nicht gefunden – Aufruf: python3 auswerten.py <bereinigt.csv>")


def norm(spalte, v):
    """Gleiche Bedeutung = gleicher Wert: 1480 = 1480.0 = 1480.00 (nur im Zielformat)."""
    v = "" if v is None else str(v)
    if spalte == "betrag" and ZAHL.match(v):
        return f"{float(v):.2f}"
    if spalte == "plz" and re.match(r"^\d+\.0$", v):
        return v[:-2]
    if spalte == "bestelldatum" and re.match(r"^\d{4}-\d{2}-\d{2} 00:00:00$", v):
        return v[:10]
    return v


def pct(a, b):
    return f"{100 * a / b:5.1f} %" if b else "    – "


def main():
    datei = sys.argv[1] if len(sys.argv) > 1 else finde(STANDARD)
    aus = lade(datei)
    if "zeile" not in aus.columns:
        sys.exit("Die bereinigte Datei hat keine Spalte zeile")
    teil = aus["zeile"].iloc[0][0]
    ref = lade(finde(f"referenz_{teil}.csv")).set_index("zeile")
    roh = lade(finde(f"bestellungen_{teil}.csv")).set_index("zeile")
    if aus["zeile"].duplicated().any():
        sys.exit("Spalte zeile enthält doppelte Werte")
    fremd = set(aus["zeile"]) - set(ref.index)
    if fremd:
        print(f"Warnung: {len(fremd)} unbekannte Zeilen werden ignoriert")
    aus = aus.set_index("zeile")
    hinweis = aus["hinweis"] if "hinweis" in aus.columns else pd.Series("", index=aus.index)
    da = set(aus.index)

    # ---------------------------------------------------- Zeilen
    dub = ref[ref["soll"] == "dublette"]
    partner = defaultdict(set)
    for z, r in dub.iterrows():
        partner[r["dublette_von"]].add(z)
        partner[z].add(r["dublette_von"])
    dub_ok = dub_offen = 0
    for z, r in dub.iterrows():
        gruppe = {z, r["dublette_von"]}
        n = len(gruppe & da)
        dub_ok += n == 1
        dub_offen += n == 2
    verlust = Counter()
    for z, r in ref[ref["soll"] == "behalten"].iterrows():
        if z not in da and not (partner[z] & da):
            verlust[r["falle"] or "sonstige Bestellung"] += 1

    # ---------------------------------------------------- Zellen
    fehl = defaultdict(Counter)   # fehlerart -> ergebnis -> anzahl
    schaden = Counter()           # falle -> anzahl
    schaden_spalte = Counter()
    korrekt_n = 0
    for z, r in ref[ref["soll"] == "behalten"].iterrows():
        drin = z in da
        if not drin and partner[z] & da:
            continue                                # durch die andere Zeile ersetzt
        for s in SPALTEN:
            art = r["fehler_" + s]
            wahr, alt = norm(s, r[s]), norm(s, roh.at[z, s])
            neu = norm(s, aus.at[z, s]) if drin and s in aus.columns else None
            if art:
                if not drin:
                    e = "mit Zeile gelöscht"
                elif neu == wahr:
                    e = "geheilt"
                elif neu in (alt, "") or (s == "betrag" and neu == norm(s, r["betrag_wie_roh"])):
                    e = "markiert" if hinweis.get(z, "") else "übersehen"
                else:
                    e = "falsch geändert"
                fehl[art][e] += 1
            elif drin:
                korrekt_n += 1
                if neu != wahr:
                    schaden[r["falle"] or "sonstige Werte"] += 1
                    schaden_spalte[s] += 1
    ohne_anlass = sum(1 for z in da & set(ref.index)
                      if hinweis.get(z, "") and ref.at[z, "soll"] == "behalten"
                      and not any(ref.at[z, "fehler_" + s] for s in SPALTEN))

    # ---------------------------------------------------- Ausgabe
    ERG = ["geheilt", "markiert", "übersehen", "falsch geändert", "mit Zeile gelöscht"]
    summe = Counter()
    for c in fehl.values():
        summe.update(c)
    n_fehl = sum(summe.values())
    print(f"\nAuswertung {datei}  (Daten {teil}: {len(ref)} Zeilen)\n")
    print(f"Fehlerhafte Werte: {n_fehl}")
    for e in ERG:
        print(f"  {e:20s} {summe[e]:5d}   {pct(summe[e], n_fehl)}")
    print(f"\nKorrekte Werte: {korrekt_n}")
    print(f"  verändert (Schaden) {sum(schaden.values()):5d}   {pct(sum(schaden.values()), korrekt_n)}")
    for k, v in schaden.most_common():
        print(f"      {k:32s} {v:4d}")
    if schaden_spalte:
        print("      je Spalte: " + ", ".join(f"{k} {v}" for k, v in schaden_spalte.most_common()))
    print(f"\nDoppelt erfasste Zeilen: {len(dub)}")
    print(f"  aufgelöst            {dub_ok:5d}")
    print(f"  beide noch da        {dub_offen:5d}")
    print(f"Echte Bestellungen gelöscht (Schaden): {sum(verlust.values())}")
    for k, v in verlust.most_common():
        print(f"      {k:32s} {v:4d}")
    print(f"Zeilen mit Hinweis, obwohl alles korrekt war: {ohne_anlass}")

    print("\nJe Fehlerart:")
    kopf = "".join(f"{e[:10]:>11s}" for e in ERG)
    print(f"  {'':32s}{'Anzahl':>7s}{kopf}")
    for art, c in sorted(fehl.items(), key=lambda kv: -sum(kv[1].values())):
        print(f"  {art:32s}{sum(c.values()):7d}" + "".join(f"{c[e]:11d}" for e in ERG))

    print("\nFür die Ergebnistafel:")
    print(f"  geheilt {pct(summe['geheilt'], n_fehl).strip()} · markiert {summe['markiert']} · "
          f"falsch geändert {summe['falsch geändert']} · Schaden {sum(schaden.values())} Werte "
          f"+ {sum(verlust.values())} Zeilen · Doppelte aufgelöst {dub_ok}/{len(dub)}")


if __name__ == "__main__":
    main()
