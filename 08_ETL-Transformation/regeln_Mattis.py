#!/usr/bin/env python3
"""Bereinigungsregeln für die Bestelldaten der Kranz Werkzeughandel GmbH – Mattis Lösung (Entwurf).

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
import datetime
import difflib
import re
import sys
import unicodedata
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

# ============================================================ Hilfsfunktionen
RECHTSFORMEN = r"\b(gmbh und co kg|gmbh|e k|ek|kg|ohg|ag|ug)\b"
MONATE = {"januar": 1, "jan": 1, "februar": 2, "feb": 2, "märz": 3, "maerz": 3, "mär": 3,
          "mrz": 3, "april": 4, "apr": 4, "mai": 5, "juni": 6, "jun": 6, "juli": 7, "jul": 7,
          "august": 8, "aug": 8, "september": 9, "sep": 9, "sept": 9, "oktober": 10, "okt": 10,
          "november": 11, "nov": 11, "dezember": 12, "dez": 12}
TEXTSPALTEN = ["quelle", "kunde", "bestelldatum", "betrag", "plz", "ort", "artikelgruppe"]

# Muster für Datumsformate (Gruppen: siehe regel_4)
ISO = r"(\d{4})[-/.](\d{1,2})[-/.](\d{1,2})"                 # 2025-03-14
DEUTSCH = r"(\d{1,2})\.(\d{1,2})\.(\d{4}|\d{2})"             # 14.03.2025 oder 14.03.25
SCHRAEG = r"(\d{1,2})[/-](\d{1,2})[/-](\d{4}|\d{2})"         # 03/14/2025 oder 14/03/2025


def markiere_zeile(df, zeilenindex, grund):
    """Schreibt einen Hinweis in genau eine Zeile (benutzt markiere aus der Vorlage)."""
    return markiere(df, df.index == zeilenindex, grund)


def schluessel(text):
    """Vergleichsschlüssel für Namen: Kleinschreibung, nur Buchstaben und Ziffern.
    'KFZ-Werkstatt Engel GmbH & Co. KG' -> 'kfz werkstatt engel gmbh und co kg'."""
    t = unicodedata.normalize("NFKC", text).casefold().replace("&", " und ")
    t = re.sub(r"(?<=\b[a-zäöüß])\.(?=[a-zäöüß]\b)", "", t)   # G.m.b.H. -> gmbh, e.K. -> ek
    t = re.sub(r"[^0-9a-zäöüß]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def kern(text):
    """Wie schluessel, aber ohne Rechtsform: 'tischlerei funk e k' -> 'tischlerei funk'."""
    return re.sub(r"\s+", " ", re.sub(RECHTSFORMEN, "", schluessel(text))).strip()


def plz_normal(text):
    """Gibt (PLZ, in_Ordnung) zurück: vierstellig -> führende 0 davor, 'D-34117' -> '34117'."""
    t = re.sub(r"^(DE|D)[\s-]*", "", text.strip(), flags=re.I).replace(" ", "")
    if re.fullmatch(r"\d{5}", t):
        return t, True
    if re.fullmatch(r"\d{4}", t):
        return "0" + t, True
    return text.strip(), text.strip() == ""


def jahr(text):
    return int(text) if len(text) == 4 else 2000 + int(text)


def tag_pruefen(j, mo, tg):
    """Gibt das Datum als JJJJ-MM-TT zurück, wenn es das Datum wirklich gibt."""
    try:
        return datetime.date(j, mo, tg).isoformat(), None
    except ValueError:
        return None, "Datum gibt es nicht (z. B. 31.02.)"


def datum_lesen(text, slash_modus):
    """Gibt (JJJJ-MM-TT, None) zurück oder (None, Grund), wenn das Datum nicht sicher lesbar ist."""
    t = text.strip()
    if t == "":
        return None, "Datum fehlt"
    m = re.fullmatch(ISO, t)
    if m:
        return tag_pruefen(int(m[1]), int(m[2]), int(m[3]))
    m = re.fullmatch(DEUTSCH, t)                      # Punkt bedeutet: Tag.Monat.Jahr
    if m:
        return tag_pruefen(jahr(m[3]), int(m[2]), int(m[1]))
    m = re.fullmatch(SCHRAEG, t)                      # Schrägstrich: Reihenfolge ist offen
    if m:
        a, b, j = int(m[1]), int(m[2]), jahr(m[3])
        if a > 12:                                    # erste Zahl kann kein Monat sein
            return tag_pruefen(j, b, a)
        if b > 12:                                    # zweite Zahl kann kein Monat sein
            return tag_pruefen(j, a, b)
        if slash_modus == "TM":
            return tag_pruefen(j, b, a)
        if slash_modus == "MT":
            return tag_pruefen(j, a, b)
        return None, "Datum nicht eindeutig (Tag/Monat oder Monat/Tag?)"
    m = re.fullmatch(r"(\d{1,2})\.?\s*([A-Za-zÄÖÜäöüß]+)\.?,?\s*(\d{4})", t)   # 5. Oktober 2025
    if m and m[2].casefold() in MONATE:
        return tag_pruefen(int(m[3]), MONATE[m[2].casefold()], int(m[1]))
    m = re.fullmatch(r"([A-Za-zÄÖÜäöüß]+)\.?\s*(\d{4})", t)                    # Februar 2025
    if m and m[1].casefold() in MONATE:
        return None, "Tag fehlt (nur Monat und Jahr bekannt)"
    return None, "Datum nicht lesbar"


def lerne_slash_modus(df):
    """Bestimmt je Quelle, ob Schrägstrich-Daten Tag/Monat ('TM') oder Monat/Tag ('MT') sind.
    Beleg: Eine Zahl größer als 12 kann kein Monat sein. Gibt es Belege für beide
    Reihenfolgen in derselben Quelle (oder keinen), bleibt die Quelle unentschieden."""
    belege = {}
    for quelle, text in zip(df["quelle"], df["bestelldatum"]):
        m = re.fullmatch(SCHRAEG, text.strip())
        if not m:
            continue
        a, b = int(m[1]), int(m[2])
        if a > 12 >= b:
            belege.setdefault(quelle, set()).add("TM")
        if b > 12 >= a:
            belege.setdefault(quelle, set()).add("MT")
    return {q: next(iter(s)) for q, s in belege.items() if len(s) == 1}


def betrag_lesen(text):
    """Gibt ('1250.80', None) zurück oder (None, Grund). Nimmt € und EUR weg, erkennt Dezimalkomma,
    Tausenderpunkt und Tausenderkomma. Das letzte Trennzeichen mit 1 bis 2 Stellen dahinter ist
    das Dezimalzeichen. Genau 3 Stellen dahinter heißt: Tausendertrenner (Euro hat 2 Dezimalstellen)."""
    t = text.strip()
    if t == "":
        return None, "Betrag fehlt"
    uebrig = re.sub(r"€|euro|eur|[\d.,\-\s'’()]", "", t, flags=re.I)    # was bleibt, wenn man Erlaubtes streicht?
    if uebrig or not re.search(r"\d", t):
        return None, "Betrag nicht lesbar"
    negativ = "-" in t or (t.startswith("(") and t.endswith(")"))
    zahl = re.sub(r"[^\d.,]", "", t)
    if re.fullmatch(r"\d+\.\d{6,}", zahl):                       # Rechenrest: 3.7799999999999998
        wert = float(zahl)
        if wert < 10:                    # '3.78' ist als Euro-Betrag unplausibel: gemeint war '3.780' (Tausenderpunkt)
            return ("-" if negativ else "") + f"{round(wert * 1000):.2f}", None
        gerundet = round(wert, 2)
        if abs(gerundet - wert) < 1e-6:
            return ("-" if negativ else "") + f"{gerundet:.2f}", None
    zeichen = re.findall(r"[.,]", zahl)
    if not zeichen:                                              # 406
        ganz, dez = zahl, "00"
    elif re.fullmatch(r"\d+[.,]\d{1,2}", zahl):                  # 117,13 oder 117.13
        ganz, dez = re.split(r"[.,]", zahl)
    elif re.fullmatch(r"\d{1,3}([.,]\d{3})+[.,]\d{1,2}", zahl):  # 1.250,80 oder 1,250.80
        dezzeichen = zeichen[-1]
        if zeichen[:-1].count(dezzeichen) or len(set(zeichen[:-1])) != 1:
            return None, "Betrag nicht eindeutig (Trennzeichen)"
        ganz, dez = zahl[:zahl.rfind(dezzeichen)], zahl[zahl.rfind(dezzeichen) + 1:]
        ganz = re.sub(r"[.,]", "", ganz)
    elif re.fullmatch(r"[1-9]\d{0,2}([.,]\d{3})+", zahl) and len(set(zeichen)) == 1:   # 1.250 oder 12,500
        ganz, dez = re.sub(r"[.,]", "", zahl), "00"
    else:
        return None, "Betrag nicht eindeutig (Trennzeichen)"
    return ("-" if negativ else "") + ganz + "." + dez.ljust(2, "0"), None


def stamm_vorbereiten(stamm):
    """Kundenstamm mit Vergleichsschlüsseln und fünfstelliger PLZ (im Stamm fehlt oft die führende 0)."""
    st = stamm[stamm["kunde"].str.strip() != ""].copy()
    st["k"] = st["kunde"].map(schluessel)
    st["kern"] = st["kunde"].map(kern)
    st["plz5"] = st["plz"].map(lambda p: plz_normal(p)[0])
    return st.reset_index(drop=True)


def finde_kunde(name, plz, ort, st):
    """Sucht den Kunden im Stamm. Gibt (Stammzeile oder None, Hinweis oder None) zurück."""
    k = schluessel(name)
    treffer = st[st["k"] == k]                                   # 1. Stufe: gleich nach Normalisieren
    if treffer.empty and kern(name):
        treffer = st[st["kern"] == kern(name)]                   # 2. Stufe: gleich ohne Rechtsform
    if treffer.empty:
        aehnlich = difflib.get_close_matches(k, st["k"].tolist(), n=1, cutoff=0.85)
        zusatz = ""
        if aehnlich:
            zusatz = f", ähnlich: {st.loc[st['k'] == aehnlich[0], 'kunde'].iloc[0]} (nicht übernommen)"
        return None, "Kunde nicht im Kundenstamm" + zusatz
    if treffer["kundennr"].nunique() > 1:                        # derselbe Name, mehrere Betriebe
        plz_ok = plz_normal(plz)[0]
        eng = treffer[treffer["plz5"] == plz_ok] if plz_ok else treffer.iloc[0:0]
        if len(eng) != 1 and ort:
            eng = treffer[treffer["ort"].map(schluessel) == schluessel(ort)]
        if len(eng) != 1:
            nummern = ", ".join(sorted(treffer["kundennr"]))
            return None, f"Kunde mehrdeutig (Kundenstamm: {nummern}), PLZ/Ort entscheidet nicht"
        treffer = eng
    return treffer.iloc[0], None


# ============================================================ Ihre Regeln
def regel_1_leerzeilen(df, stamm):
    """Wenn: eine Zeile in allen Spalten (außer hinweis) leer ist.
    Dann: Zeile löschen.   Außer: nichts, denn eine leere Zeile enthält keine Bestellung."""
    inhalt = df[TEXTSPALTEN].apply(lambda s: s.str.strip(" ,;") != "")
    echte_id = df["zeile"].str.fullmatch(r"[A-Z]-\d+")       # ',,,,' in zeile ist Export-Müll, keine Bestellnummer
    return df[inhalt.any(axis=1) | echte_id].copy()


def regel_2_leerzeichen(df, stamm):
    """Wenn: ein Text mit Leerzeichen beginnt oder endet, oder zwei Leerzeichen hintereinander hat.
    Dann: Leerzeichen am Rand entfernen, doppelte zu einem machen.   Außer: Spalte zeile (nie ändern)."""
    for spalte in TEXTSPALTEN:
        df[spalte] = df[spalte].str.strip().str.replace(r"\s{2,}", " ", regex=True)
        if spalte in ("quelle", "kunde", "ort", "artikelgruppe"):          # Export-Rest: 'Handwerkzeug,,,'
            df[spalte] = df[spalte].str.replace(r"[,;]+$", "", regex=True)
    return df


def regel_3_umlaute(df, stamm):
    """Wenn: ein Text 'Ã' oder 'â€' enthält (UTF-8-Text, der als Windows-Text gelesen wurde, z. B. 'GÃ¶ttingen').
    Dann: Text zurückübersetzen ('Göttingen').   Außer: geht die Rückübersetzung nicht, Text lassen
    und markieren."""
    for spalte in TEXTSPALTEN:
        for i in df.index[df[spalte].str.contains("Ã|â€|Â", regex=True)]:
            try:
                df.at[i, spalte] = df.at[i, spalte].encode("cp1252").decode("utf-8")
            except (UnicodeEncodeError, UnicodeDecodeError):
                df = markiere_zeile(df, i, f"{spalte}: kaputte Zeichen, nicht reparierbar")
    return df


def regel_4_datum(df, stamm):
    """Wenn: bestelldatum nicht JJJJ-MM-TT ist.
    Dann: in JJJJ-MM-TT umschreiben. Punkt = Tag.Monat.Jahr, zweistelliges Jahr = 20xx. Bei Schrägstrich
    entscheidet eine Zahl über 12 (kann kein Monat sein), sonst die Reihenfolge, die die Quelle
    in diesem Lauf sonst benutzt.   Außer: Reihenfolge unklar, Tag fehlt (nur Monat), Datum nicht lesbar
    oder gibt es nicht: Wert lassen und markieren."""
    modus = lerne_slash_modus(df)
    for i in df.index:
        iso, grund = datum_lesen(df.at[i, "bestelldatum"], modus.get(df.at[i, "quelle"]))
        if iso:
            df.at[i, "bestelldatum"] = iso
        else:
            df = markiere_zeile(df, i, grund)
    return df


def regel_5_betrag(df, stamm):
    """Wenn: betrag nicht 'Zahl mit Punkt und zwei Stellen' ist (z. B. '192,17 €', '406 EUR', '1.250,80').
    Dann: € und EUR entfernen, Dezimalkomma zu Punkt, Tausenderzeichen entfernen, zwei Dezimalstellen.
    Minus bleibt (Gutschrift!).   Außer: Betrag leer oder Trennzeichen nicht eindeutig: Wert lassen und markieren.
    Zusätzlich markiert (Wert bleibt): Außendienst, glatter Betrag (',00' oder ohne Cent) ab 5000: mögliches Kommafehler."""
    for i in df.index:
        roh = df.at[i, "betrag"]
        neu, grund = betrag_lesen(roh)
        if neu:
            df.at[i, "betrag"] = neu
            # Verdacht Kommafehler: '14.100,00 €' kann 141,00 sein. Nicht sicher: Wert lassen, markieren.
            if df.at[i, "quelle"].startswith("AD") and neu.endswith(".00") and abs(float(neu)) >= 5000:
                df = markiere_zeile(df, i, "Betrag evtl. Kommafehler (Außendienst, glatter Betrag, hoch)")
        else:
            df = markiere_zeile(df, i, grund)
    return df


def regel_6_plz(df, stamm):
    """Wenn: der Ort mit einer PLZ beginnt ('36043 Fulda').
    Dann: PLZ in die Spalte plz (wenn dort leer), Ort ohne PLZ.   Außer: steht in plz eine andere PLZ:
    markieren.
    Wenn: die PLZ vierstellig ist (Excel hat die führende 0 verschluckt: 4109).
    Dann: eine 0 davorsetzen (04109).   Außer: PLZ hat dann nicht 5 Ziffern: Wert lassen und markieren."""
    for i in df.index:
        m = re.fullmatch(r"(\d{4,5})\s+(.+)", df.at[i, "ort"])
        if m:
            plz_im_ort = plz_normal(m[1])[0]
            if df.at[i, "plz"] == "":
                df.at[i, "plz"] = plz_im_ort
            elif plz_normal(df.at[i, "plz"])[0] != plz_im_ort:
                df = markiere_zeile(df, i, f"PLZ im Ort ({plz_im_ort}) widerspricht der PLZ-Spalte ({df.at[i, 'plz']})")
            df.at[i, "ort"] = m[2]
        wert, ok = plz_normal(df.at[i, "plz"])
        df.at[i, "plz"] = wert
        if not ok:
            df = markiere_zeile(df, i, f"PLZ nicht fünfstellig: '{wert}'")
    return df


def regel_7_kunde(df, stamm):
    """Wenn: der Kundenname nicht genau so im Kundenstamm steht.
    Dann: Name aus dem Kundenstamm übernehmen, aber nur wenn genau EIN Kunde passt (gleich nach
    Groß/Klein, Bindestrich, Punkt, oder gleich ohne Rechtsform wie GmbH / e.K.). Bei mehreren
    Betrieben mit gleichem Namen entscheiden PLZ und Ort.
    Außer: kein oder mehrere passende Kunden: Name lassen und markieren. Ähnlich klingende Namen
    (Ott / Otto) werden NIE automatisch zusammengelegt, nur als Vorschlag in den Hinweis geschrieben."""
    st = stamm_vorbereiten(stamm)
    df["_kundennr"] = ""
    for i in df.index:
        name = df.at[i, "kunde"]
        if name == "":
            df = markiere_zeile(df, i, "Kunde fehlt")
            continue
        zeile, grund = finde_kunde(name, df.at[i, "plz"], df.at[i, "ort"], st)
        if zeile is None:
            df = markiere_zeile(df, i, grund)
        else:
            df.at[i, "kunde"] = zeile["kunde"]
            df.at[i, "_kundennr"] = zeile["kundennr"]
    return df


def regel_8_plz_ort_stamm(df, stamm):
    """Wenn: der Kunde eindeutig im Kundenstamm gefunden wurde (Regel 7) und plz oder ort leer sind.
    Dann: aus dem Kundenstamm einsetzen. Ist der Ort nur anders geschrieben (GÖTTINGEN), Schreibweise
    des Kundenstamms nehmen.   Außer: steht ein anderer Wert drin (PLZ oder Ort weicht vom Stamm ab, zum
    Beispiel eine andere Lieferadresse), Wert lassen und markieren. Auch markieren, wenn der Kunde nicht
    im Stamm ist oder der Stamm selbst leer ist: dann bleibt plz oder ort leer."""
    st = stamm_vorbereiten(stamm).set_index("kundennr")
    for i in df.index:
        nr = df.at[i, "_kundennr"]
        plz, ort = df.at[i, "plz"], df.at[i, "ort"]
        if nr == "":                                              # Kunde unbekannt: nichts einsetzbar
            if plz == "":
                df = markiere_zeile(df, i, "PLZ fehlt (Kunde nicht im Stamm)")
            if ort == "":
                df = markiere_zeile(df, i, "Ort fehlt (Kunde nicht im Stamm)")
            continue
        s = st.loc[nr]
        if plz == "":
            if s["plz5"]:
                df.at[i, "plz"] = s["plz5"]
            else:
                df = markiere_zeile(df, i, "PLZ fehlt (auch im Kundenstamm leer)")
        elif s["plz5"] and plz != s["plz5"]:
            df = markiere_zeile(df, i, f"PLZ weicht vom Kundenstamm ab ({plz} statt {s['plz5']})")
        if ort == "":
            if s["ort"]:
                df.at[i, "ort"] = s["ort"]
            else:
                df = markiere_zeile(df, i, "Ort fehlt (auch im Kundenstamm leer)")
        elif s["ort"] and ort != s["ort"]:
            if schluessel(ort) == schluessel(s["ort"]):
                df.at[i, "ort"] = s["ort"]
            else:
                df = markiere_zeile(df, i, f"Ort weicht vom Kundenstamm ab ({ort} statt {s['ort']})")
    return df


def regel_9_dubletten(df, stamm):
    """Wenn: zwei Zeilen denselben Kunden, dasselbe Datum und denselben Betrag haben (erst nach den
    Regeln 4 bis 8 erkennbar, vorher sehen sie verschieden aus).
    Dann: ist genau EINE davon aus dem Webshop, die anderen (Außendienst) löschen. Der Webshop ist die
    Quelle, der Außendienst hat die Bestellung nur zusätzlich eingetragen.
    Außer: sonst (zweimal Webshop, zwei Außendienstler) nichts löschen, die späteren Zeilen markieren.
    Nicht betroffen: gleicher Betrag, aber anderes Datum (zum Beispiel jeden Monat dieselben Schleifmittel)."""
    ok = df["bestelldatum"].str.fullmatch(r"\d{4}-\d{2}-\d{2}") & df["betrag"].str.fullmatch(r"-?\d+\.\d{2}") \
        & (df["kunde"] != "")
    schl = df["kunde"].map(schluessel)
    gruppen = df[ok].groupby([schl[ok], df.loc[ok, "bestelldatum"], df.loc[ok, "betrag"]])
    loeschen = []
    for _, g in gruppen:
        if len(g) < 2:
            continue
        webshop = g[g["quelle"].str.casefold() == "webshop"]
        if len(webshop) == 1:
            loeschen += list(g.index.difference(webshop.index))
        else:
            for i in g.index[1:]:
                df = markiere_zeile(df, i, f"mögliche Dublette von {g['zeile'].iloc[0]}")
    # Dubletten mit Lücken: Außendienst-Zeile ohne Betrag oder nur mit Monat, aber genau ein passender Webshop-Auftrag
    rest = df.drop(index=loeschen)
    web = rest[rest["quelle"].str.casefold() == "webshop"]
    webk = web["kunde"].map(schluessel)
    for i in rest.index:
        if not rest.at[i, "quelle"].startswith("AD") or rest.at[i, "kunde"] == "":
            continue
        d, b = rest.at[i, "bestelldatum"], rest.at[i, "betrag"]
        voll = bool(re.fullmatch(r"\d{4}-\d{2}-\d{2}", d))
        m = re.fullmatch(r"(\w+)\.?\s+(\d{4})", d)
        if voll:
            monat = d[:7]
        elif m and m[1].casefold() in MONATE:
            monat = f"{m[2]}-{MONATE[m[1].casefold()]:02d}"
        else:
            continue
        if b != "" and voll:               # nichts fehlt: das hat die Hauptprüfung schon erledigt
            continue
        kand = web[(webk == schluessel(rest.at[i, "kunde"])) & (web["bestelldatum"].str[:7] == monat)]
        if voll:
            kand = kand[kand["bestelldatum"] == d]
        if b != "":
            kand = kand[kand["betrag"] == b]
        if len(kand) == 1:
            loeschen.append(i)
    return df.drop(index=loeschen)


def regel_10_aufraeumen(df, stamm):
    """Entfernt die Hilfsspalte _kundennr, die Regel 7 und 8 benutzt haben. Zielformat: keine Extra-Spalten."""
    return df.drop(columns=["_kundennr"])


REGELN = [regel_1_leerzeilen, regel_2_leerzeichen, regel_3_umlaute, regel_4_datum, regel_5_betrag,
          regel_6_plz, regel_7_kunde, regel_8_plz_ort_stamm, regel_9_dubletten, regel_10_aufraeumen]


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
