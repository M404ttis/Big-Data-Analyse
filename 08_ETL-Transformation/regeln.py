#!/usr/bin/env python3
"""Bereinigungsregeln für die Bestelldaten der Kranz Werkzeughandel GmbH – Vorlage.

Aufruf:   python3 regeln.py bestellungen_A.csv bereinigt_A.csv

So arbeiten Sie mit der Vorlage:
  * Schreiben Sie je Regelkarte eine Funktion nach dem Muster von regel_beispiel.
  * Tragen Sie die Funktion in die Liste REGELN ein (die Reihenfolge zählt).
  * Alle Werte werden als Text gelesen, leere Zellen sind "" (nicht NaN).
  * Kann eine Regel einen Wert nicht sicher korrigieren: Wert stehen lassen und mit
    markiere(...) einen Grund in die Spalte „hinweis“ schreiben.
  * Zeilen dürfen Sie löschen, aber die Spalte „zeile“ nie verändern.
  * Nach jedem Lauf zeigt der Änderungsbericht, was Ihr Skript verändert hat;
    alle Einzeländerungen stehen in aenderungen.csv.
"""
import sys
from pathlib import Path

import pandas as pd

KUNDENSTAMM = "kundenstamm.csv"   # im aktuellen Ordner oder neben diesem Skript


def lade(datei):
    return pd.read_csv(datei, sep=";", dtype=str, keep_default_na=False, encoding="utf-8")


def markiere(df, maske, grund):
    """Schreibt grund in die Spalte hinweis aller Zeilen, für die maske True ist."""
    alt = df.loc[maske, "hinweis"]
    df.loc[maske, "hinweis"] = alt.where(alt == "", alt + " | ") + grund
    return df


# ============================================================ Ihre Regeln
def regel_beispiel(df, stamm):
    """Beispiel – Wenn: ein Wert in der Spalte artikelgruppe beginnt oder endet mit Leerzeichen.
    Dann: Leerzeichen am Anfang und Ende entfernen.  Sonst: nichts tun."""
    df["artikelgruppe"] = df["artikelgruppe"].str.strip()
    return df


def regel_1(df, stamm):
    """Wenn: …   Dann: …   Außer / sonst markieren: …"""
    return df


def regel_2(df, stamm):
    """Wenn: …   Dann: …   Außer / sonst markieren: …"""
    return df


REGELN = [regel_beispiel, regel_1, regel_2]


# ============================================================ ab hier nichts ändern
def aenderungsbericht(vorher, nachher, datei="aenderungen.csv"):
    v = vorher.set_index("zeile")
    n = nachher.set_index("zeile")
    geloescht = [z for z in v.index if z not in n.index]
    zeilen = []
    for spalte in [c for c in v.columns if c in n.columns]:
        alt = v.loc[n.index, spalte].astype(str)
        neu = n[spalte].fillna("").astype(str)
        for z in alt.index[alt != neu]:
            zeilen.append({"zeile": z, "spalte": spalte, "vorher": alt[z], "nachher": neu[z]})
    pd.DataFrame(zeilen, columns=["zeile", "spalte", "vorher", "nachher"]).to_csv(
        datei, sep=";", index=False, encoding="utf-8")
    print(f"Zeilen: {len(v)} gelesen, {len(n)} geschrieben, {len(geloescht)} gelöscht")
    anzahl = pd.Series([z["spalte"] for z in zeilen], dtype=str).value_counts()
    for spalte in v.columns:
        if spalte != "zeile":
            print(f"  {spalte:15s} {anzahl.get(spalte, 0):5d} Werte geändert")
    print(f"  {'hinweis':15s} {(n['hinweis'] != '').sum():5d} Zeilen markiert")
    print(f"Einzelne Änderungen: {datei}")


def main():
    if len(sys.argv) != 3:
        sys.exit("Aufruf: python3 regeln.py <eingabe.csv> <ausgabe.csv>")
    df = lade(sys.argv[1])
    stamm_datei = Path(KUNDENSTAMM)
    if not stamm_datei.exists():
        stamm_datei = Path(__file__).resolve().with_name(KUNDENSTAMM)
    stamm = lade(stamm_datei)
    vorher = df.copy()
    df["hinweis"] = ""
    for regel in REGELN:
        df = regel(df, stamm)
        if "zeile" not in df.columns or df["zeile"].duplicated().any():
            sys.exit(f"{regel.__name__}: Spalte zeile fehlt oder ist doppelt")
    df = df.fillna("")
    df.to_csv(sys.argv[2], sep=";", index=False, encoding="utf-8")
    aenderungsbericht(vorher, df)


if __name__ == "__main__":
    main()
