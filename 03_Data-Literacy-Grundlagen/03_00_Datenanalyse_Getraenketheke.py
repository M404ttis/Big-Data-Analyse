# %% [markdown]
# # Tag 3 · Zusatz: Brauchen die MoveWerk-Studios eine zweite Getränketheke?
#
# **Vermutung der Regionalleiterin:** „An vollen Tagen verkauft die Theke weniger.“
# **Ihr Vorschlag:** eine zweite Theke je Studio, damit sich keine Schlange bildet.
# **Kosten:** 38.000 € einmalig plus eine Aushilfe für 1.900 € im Monat, je Studio.
#
# Dieses Skript ist im „Percent-Format“ geschrieben (`# %%` trennt Zellen). Es läuft als
# normales Python-Skript (`python3 03_00_Datenanalyse_Getraenketheke.py`), lässt sich in
# Jupyter oder VS Code zellenweise ausführen und mit `jupytext --to notebook` in ein
# Notebook für ein Jupyter Book umwandeln.
#
# Benötigt: `pandas`, `numpy`, `matplotlib`.
#
# **Gang der Analyse**
# 1. Datenqualität prüfen und bereinigen
# 2. Den behaupteten Zusammenhang sichtbar machen
# 3. Einen dritten Faktor (Konfundierer) suchen und herausrechnen
# 4. Prüfen, ob die Theke an vollen Tagen wirklich an ihre Grenze kommt
# 5. Wirtschaftlichkeit rechnen und Empfehlung ableiten

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

try:
    ordner = Path(__file__).parent
except NameError:  # in Jupyter gibt es __file__ nicht
    ordner = Path.cwd()

plt.rcParams.update({"figure.dpi": 110, "axes.grid": True, "grid.alpha": 0.3,
                     "axes.spines.top": False, "axes.spines.right": False})
FARBE = {"check_ins": "#1f77b4", "getraenke": "#d95f02", "temp": "#7570b3"}


def zeige(name):
    """Grafik anzeigen (der Name dient nur der Orientierung im Skript)."""
    plt.show()


# %% [markdown]
# ## 1. Daten laden und Datenqualität prüfen
#
# Die Datei kommt aus drei Systemen (Kasse, Zugangskontrolle, Haustechnik) und wurde
# „nie geprüft“. Erst die Fehler suchen, dann auswerten.

# %%
roh = pd.read_csv(ordner / "movewerk_tagesdaten_2025.csv", encoding="utf-8-sig")  # BOM am Dateianfang
print(roh.shape)
roh.info()

# %% [markdown]
# **Fehlerjagd.** Jede Prüfung zählt die Fälle, die Behandlung folgt danach.

# %%
fehler = []

# leere Zeile
leer = roh.isna().all(axis=1)
fehler.append(("Komplett leere Zeile", int(leer.sum()), "entfernen"))
d = roh[~leer].copy()

# Datumsformat: Hanau liefert TT.MM.JJJJ, alle anderen JJJJ-MM-TT
iso = d["datum"].str.match(r"\d{4}-\d{2}-\d{2}$")
fehler.append(("Datum im Format TT.MM.JJJJ (nur Hanau)", int((~iso).sum()), "getrennt einlesen"))
datum = pd.Series(pd.NaT, index=d.index, dtype="datetime64[ns]")
datum[iso] = pd.to_datetime(d.loc[iso, "datum"], format="%Y-%m-%d")
datum[~iso] = pd.to_datetime(d.loc[~iso, "datum"], format="%d.%m.%Y")
d["datum"] = datum

# Studio-Schreibweisen
sachs = {"Ffm-Sachsenhausen", "Frankfurt Sachsenhausen", "frankfurt-sachsenhausen"}
fehler.append(("Studio Sachsenhausen in 4 Schreibweisen", int(d["studio"].isin(sachs).sum()),
               "auf „Frankfurt-Sachsenhausen“ vereinheitlichen"))
d["studio"] = d["studio"].replace({s: "Frankfurt-Sachsenhausen" for s in sachs})

# doppelte Zeilen
fehler.append(("Doppelte Zeilen (gleiches Studio, gleicher Tag)", int(d.duplicated().sum()), "eine behalten"))
d = d.drop_duplicates().copy()

# fehlende Werte
for spalte in ["temperatur_c", "check_ins", "getraenke_stueck"]:
    fehler.append((f"Fehlender Wert in {spalte}", int(d[spalte].isna().sum()), "Wert bleibt leer, Zeile fällt aus der Auswertung"))

# unmögliche Werte
temp_falsch = (d["temperatur_c"] > 45) | (d["temperatur_c"] < -25)
fehler.append(("Unmögliche Temperatur (85, 91,5 und −99 °C)", int(temp_falsch.sum()), "auf leer setzen"))
d.loc[temp_falsch, "temperatur_c"] = np.nan

check_falsch = (d["check_ins"] > 3000) | (d["check_ins"] <= 0)
fehler.append(("Unmögliche Check-ins (12.480, 9.999 und 0)", int(check_falsch.sum()), "auf leer setzen"))
d.loc[check_falsch, "check_ins"] = np.nan

negativ = d["getraenke_stueck"] < 0
fehler.append(("Negative Getränkezahl", int(negativ.sum()), "auf leer setzen"))
d.loc[negativ, "getraenke_stueck"] = np.nan

# fehlende Tage (14 Studios x 365 Tage = 5.110 erwartete Zeilen)
erwartet = 14 * 365
fehler.append(("Fehlende Studio-Tage", erwartet - len(d), "nicht ergänzen"))

pd.DataFrame(fehler, columns=["Fehlerart", "Anzahl", "Behandlung"])

# %% [markdown]
# **Die Falle im Seminarskript:** `pd.to_datetime(..., format="mixed", dayfirst=True)` liest
# auch das ISO-Datum `2025-02-01` mit „Tag zuerst“, also als 2. Januar. Prüfprobe: stimmt der
# berechnete Wochentag mit der Spalte `wochentag` überein?

# %%
tage = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
falsch_gelesen = pd.to_datetime(roh.loc[~leer, "datum"], format="mixed", dayfirst=True)
abweichung_falsch = (falsch_gelesen.dt.day_of_week.map(dict(enumerate(tage))) != roh.loc[~leer, "wochentag"]).sum()
abweichung_richtig = (d["datum"].dt.day_of_week.map(dict(enumerate(tage))) != d["wochentag"]).sum()
print(f"Wochentag passt nicht zum Datum: {abweichung_falsch} Zeilen (dayfirst=True), "
      f"{abweichung_richtig} Zeilen (getrennt eingelesen)")

# %%
auswertung = d.dropna(subset=["check_ins", "getraenke_stueck", "temperatur_c"]).copy()
auswertung["monat"] = auswertung["datum"].dt.month
print(f"Für die Auswertung bleiben {len(auswertung)} von {len(d)} Zeilen "
      f"({len(auswertung) / len(d):.1%}).")
auswertung[["check_ins", "getraenke_stueck", "temperatur_c"]].describe().round(1)

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Datenqualität**
#
# Elf Fehlerarten in der Datei, von Datumsformaten über doppelte Zeilen bis zu unmöglichen Werten (85 °C, 12.480 Check-ins).
# Das Seminarskript liest ISO-Daten mit `dayfirst=True` falsch (Tag und Monat vertauscht). Nach der Bereinigung bleiben 99,4 % der Zeilen.
#
# </div>

# %% [markdown]
# ## 2. Der Jahresverlauf
#
# Mittel aller Studios, Wochenmittel. Erste Frage: Was passiert wann?

# %%
woche = auswertung.groupby("datum")[["check_ins", "getraenke_stueck", "temperatur_c"]].mean().rolling(7, min_periods=1).mean()
fig, achsen = plt.subplots(3, 1, figsize=(10, 7), sharex=True)
for ax, spalte, farbe, titel in zip(
        achsen, ["check_ins", "getraenke_stueck", "temperatur_c"],
        [FARBE["check_ins"], FARBE["getraenke"], FARBE["temp"]],
        ["Check-ins je Studio und Tag", "Verkaufte Getränke je Studio und Tag", "Temperatur in °C"]):
    ax.plot(woche.index, woche[spalte], color=farbe)
    ax.set_ylabel(titel, fontsize=8)
achsen[0].set_title("Jahresverlauf 2025 (Wochenmittel, alle Studios)")
zeige("01_jahresverlauf")

# %% [markdown]
# **Beobachtung:** Check-ins und Getränke laufen **gegeneinander**. Im Winter sind die Studios
# voll und die Theke verkauft wenig, im Sommer ist es umgekehrt. Die Temperatur schwingt
# mit beiden Kurven.

# %% [markdown]
# ## 3. Der behauptete Zusammenhang
#
# Jeder Punkt ist ein Studio an einem Tag.

# %%
r_roh = auswertung["check_ins"].corr(auswertung["getraenke_stueck"])
steigung_roh, achsenabschnitt_roh = np.polyfit(auswertung["check_ins"], auswertung["getraenke_stueck"], 1)

fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(auswertung["check_ins"], auswertung["getraenke_stueck"], s=6, alpha=0.3, color="grey")
x = np.linspace(auswertung["check_ins"].min(), auswertung["check_ins"].max(), 50)
ax.plot(x, steigung_roh * x + achsenabschnitt_roh, color="crimson", lw=2,
        label=f"Trend: {steigung_roh:.2f} Getränke je Check-in")
ax.set(xlabel="Check-ins", ylabel="Getränke (Stück)",
       title=f"Mehr Check-ins, weniger Getränke? Korrelation r = {r_roh:.2f}")
ax.legend()
zeige("02_naiver_zusammenhang")
print(f"Korrelation Check-ins und Getränke: r = {r_roh:.2f}")

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Die Beobachtung stimmt, die Deutung ist offen**
#
# An Tagen mit mehr Check-ins werden weniger Getränke verkauft (r ≈ −0,34). Ob volle Studios die **Ursache** sind, folgt daraus nicht.
# Das Flussdiagramm vom Vormittag fragt: *„Könnte ein dritter Faktor beides erklären?“*
#
# </div>

# %% [markdown]
# ## 4. Der dritte Faktor: die Temperatur
#
# Wenn die Temperatur beides bewegt, steckt sie hinter dem Zusammenhang (Konfundierer).

# %%
r_temp_check = auswertung["temperatur_c"].corr(auswertung["check_ins"])
r_temp_getr = auswertung["temperatur_c"].corr(auswertung["getraenke_stueck"])

fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4.3), sharex=True)
a1.scatter(auswertung["temperatur_c"], auswertung["check_ins"], s=6, alpha=0.3, color=FARBE["check_ins"])
a1.set(xlabel="Temperatur in °C", ylabel="Check-ins", title=f"Kälte bringt Mitglieder: r = {r_temp_check:.2f}")
a2.scatter(auswertung["temperatur_c"], auswertung["getraenke_stueck"], s=6, alpha=0.3, color=FARBE["getraenke"])
a2.set(xlabel="Temperatur in °C", ylabel="Getränke (Stück)", title=f"Wärme bringt Durst: r = {r_temp_getr:.2f}")
zeige("03_dritter_faktor_temperatur")
print(f"Temperatur und Check-ins: r = {r_temp_check:.2f} · Temperatur und Getränke: r = {r_temp_getr:.2f}")

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Die Temperatur ist der dritte Faktor (Konfundierer)**
#
# Kalte Tage füllen die Studios (r ≈ −0,84), warme Tage steigern den Getränkeabsatz (r ≈ +0,72). Der negative Zusammenhang von Check-ins und Getränken entsteht allein über die Jahreszeit.
#
# </div>

# Gleiche Punktwolke wie vorher, jetzt nach Temperatur eingefärbt:

# %%
fig, ax = plt.subplots(figsize=(8, 5.3))
punkte = ax.scatter(auswertung["check_ins"], auswertung["getraenke_stueck"], c=auswertung["temperatur_c"],
                    cmap="coolwarm", s=7, alpha=0.6)
plt.colorbar(punkte, label="Temperatur in °C")
ax.set(xlabel="Check-ins", ylabel="Getränke (Stück)", title="Die Punktwolke ist nach Temperatur geschichtet")
zeige("04_nach_temperatur_eingefaerbt")

# %% [markdown]
# ## 5. Temperatur konstant halten
#
# Wir vergleichen nur Tage **gleicher Temperatur** miteinander. Dort kann die Temperatur den
# Zusammenhang nicht mehr erzeugen. Feiertage lassen wir weg, weil dann beides einbricht.

# %%
werktage = auswertung[auswertung["feiertag"] == 0].copy()
grenzen = [-10, 2.5, 5, 7.5, 10, 12.5, 15, 17.5, 20, 40]
werktage["klasse"] = pd.cut(werktage["temperatur_c"], grenzen)

fig, achsen = plt.subplots(3, 3, figsize=(11, 8.5), sharex=False, sharey=True, constrained_layout=True)
innen = []
for ax, (klasse, g) in zip(achsen.ravel(), werktage.groupby("klasse", observed=True)):
    r = g["check_ins"].corr(g["getraenke_stueck"])
    m, b = np.polyfit(g["check_ins"], g["getraenke_stueck"], 1)
    xs = np.linspace(g["check_ins"].min(), g["check_ins"].max(), 20)
    ax.scatter(g["check_ins"], g["getraenke_stueck"], s=5, alpha=0.35, color="grey")
    ax.plot(xs, m * xs + b, color="crimson")
    ax.set_title(f"{klasse.left:g} bis {klasse.right:g} °C · r = {r:.2f}", fontsize=9)
    innen.append((str(klasse), len(g), round(r, 2), round(m, 2)))
fig.suptitle("Bei gleicher Temperatur: mehr Check-ins, mehr Getränke")
fig.supxlabel("Check-ins")
fig.supylabel("Getränke (Stück)")
zeige("05_temperatur_konstant")
pd.DataFrame(innen, columns=["Temperaturklasse", "Tage", "r", "Steigung (Getränke je Check-in)"])

# %%
# Kennzahl in einer Zahl: Regression mit und ohne Temperatur
def ols(y, *spalten):
    X = np.column_stack([np.ones(len(y)), *spalten])
    return np.linalg.lstsq(X, y, rcond=None)[0]


y = werktage["getraenke_stueck"].to_numpy()
ohne = ols(y, werktage["check_ins"])
mit = ols(y, werktage["check_ins"], werktage["temperatur_c"])

# Teilkorrelation: Temperatur aus beiden Größen herausrechnen
def rest(v, t):
    X = np.column_stack([np.ones(len(t)), t, t ** 2])
    return v - X @ np.linalg.lstsq(X, v, rcond=None)[0]


t = werktage["temperatur_c"].to_numpy()
r_teil = np.corrcoef(rest(werktage["check_ins"].to_numpy(), t), rest(y, t))[0, 1]

print(f"Ohne Temperatur: {ohne[1]:+.2f} Getränke je zusätzlichem Check-in")
print(f"Mit Temperatur:  {mit[1]:+.2f} Getränke je zusätzlichem Check-in "
      f"und {mit[2]:+.1f} Getränke je °C")
print(f"Teilkorrelation Check-ins und Getränke bei gleicher Temperatur: r = {r_teil:+.2f}")

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Das Vorzeichen dreht sich**
#
# Ohne Temperatur: −0,26 Getränke je zusätzlichem Check-in. Mit Temperatur: **+0,50**.
# Bei gleicher Temperatur gehören mehr Check-ins zu **mehr** Getränken (Teilkorrelation r ≈ +0,71). Der negative Zusammenhang war ein **Scheinzusammenhang**.
#
# </div>

# %% [markdown]
# ## 6. Gegenprobe: Stößt die Theke an volle Tagen an ihre Grenze?
#
# Die Regionalleiterin könnte trotzdem etwas Richtiges sehen: Wenn sich Schlangen bilden,
# müsste der Absatz **je Check-in** an den vollsten Tagen sinken, und zwar **bei gleicher Temperatur**.
# Wir teilen dazu jede Temperaturklasse in vier gleich große Auslastungsviertel.

# %%
werktage["quote"] = werktage["getraenke_stueck"] / werktage["check_ins"]
werktage["viertel"] = werktage.groupby("klasse", observed=True)["check_ins"].transform(
    lambda s: pd.qcut(s, 4, labels=[1, 2, 3, 4]))
tab = werktage.pivot_table(index="klasse", columns="viertel", values="quote", observed=True)

fig, ax = plt.subplots(figsize=(10, 4.3))
breite = 0.2
for i, v in enumerate(tab.columns):
    ax.bar(np.arange(len(tab)) + (i - 1.5) * breite, tab[v], breite, label=f"Viertel {v}" + (" (ruhigste Tage)" if v == 1 else " (vollste Tage)" if v == 4 else ""),
           color=plt.cm.Blues(0.35 + 0.17 * i))
ax.set_xticks(np.arange(len(tab)), [f"{k.left:g}–{k.right:g}" for k in tab.index], fontsize=8)
ax.set(xlabel="Temperaturklasse in °C", ylabel="Getränke je Check-in",
       title="Getränke je Check-in nach Auslastung (gleiche Temperatur)")
ax.legend(fontsize=8)
zeige("06_getraenke_je_checkin_nach_auslastung")

rueckgang = (tab[4] / tab[1] - 1).mean()
print(f"Vollste gegen ruhigste Tage, gleiche Temperatur: {rueckgang:+.1%} Getränke je Check-in")

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Keine Anzeichen für eine überforderte Theke**
#
# An den vollsten Tagen ist der Absatz je Check-in nur ca. 2 % niedriger als an den ruhigsten, bei gleicher Temperatur. Das ist kein Einbruch.
#
# **Grenze der Daten:** Wir haben nur Tageswerte. Schlangen entstehen in Stoßzeiten (z. B. 18 bis 20 Uhr), das messen Tagessummen nicht.
#
# </div>

# %% [markdown]
# ## 7. Weitere Spalten: erklären sie etwas oder verändern sie den Zusammenhang?

# %%
fig, (a1, a2) = plt.subplots(1, 2, figsize=(11, 4))

wochentag = werktage.groupby("wochentag")["quote"].mean().reindex(tage)
a1.bar(wochentag.index, wochentag.values, color="steelblue")
a1.set(title="Getränke je Check-in nach Wochentag (ohne Feiertage)", ylabel="Getränke je Check-in")

feiertag = auswertung.groupby("feiertag")[["check_ins", "getraenke_stueck"]].mean()
feiertag.index = ["kein Feiertag", "Feiertag"]
feiertag.plot.bar(ax=a2, rot=0, color=[FARBE["check_ins"], FARBE["getraenke"]])
a2.set(title="Feiertage: beides bricht ein")
zeige("07_wochentag_feiertag")

studio = auswertung.assign(quote=auswertung["getraenke_stueck"] / auswertung["check_ins"]) \
    .groupby("studio")[["check_ins", "getraenke_stueck", "quote"]].mean().round(2)
studio.sort_values("check_ins", ascending=False)

# %% [markdown]
# **Wochentag, Feiertag, Studio:**
# - Wochentag: Montag und Dienstag sind etwas voller, die Quote je Check-in bleibt gleich.
# - Feiertage: Check-ins und Getränke fallen **gemeinsam** um rund 40 %. Das ist der Gegenbeweis
#   zur These: ein leeres Studio verkauft proportional weniger.
# - Studios: Die Quote liegt in allen 14 Studios bei 0,52 bis 0,58 Getränken je Check-in.
#   Hanau (altes Kassensystem) fällt nicht auf. Der Datumsfehler dort ist nur ein
#   Formatproblem des Exports.
# - **Irrelevant** für die Frage: das Jubiläum 2026 und die neuen Umkleiden in Mainz.

# %% [markdown]
# ## 8. Wirtschaftlichkeit der zweiten Theke
#
# *Annahmen (nicht im Aufgabenblatt):* Abschreibung über 5 Jahre. Der Verkaufspreis von 2,90 €
# wird als Umsatz gerechnet. Das ist großzügig, weil die Marge niedriger ist.

# %%
PREIS = 2.90
INVEST, PERSONAL_JAHR, JAHRE = 38_000, 1_900 * 12, 5
kosten_je_jahr = INVEST / JAHRE + PERSONAL_JAHR
noetig_je_jahr = kosten_je_jahr / PREIS
absatz_je_jahr = auswertung.groupby("studio")["getraenke_stueck"].sum().mean() / auswertung.groupby("studio").size().mean() * 365

# Obergrenze: Hätten alle Tage die Quote der ruhigsten Tage gleicher Temperatur, wie viel mehr würde je Studio verkauft?
referenz = werktage.groupby("klasse", observed=True)["quote"].transform(
    lambda s: s[werktage.loc[s.index, "viertel"] == 1].mean())
obergrenze = ((referenz - werktage["quote"]).clip(lower=0) * werktage["check_ins"]).sum() / 14

print(f"Kosten je Studio und Jahr:       {kosten_je_jahr:,.0f} € ({INVEST:,} € über {JAHRE} Jahre plus {PERSONAL_JAHR:,} € Personal)")
print(f"Nötig, um das einzuspielen:      {noetig_je_jahr:,.0f} zusätzliche Getränke je Studio und Jahr "
      f"= {noetig_je_jahr / 365:.0f} je Tag = {noetig_je_jahr / absatz_je_jahr:.1%} des heutigen Absatzes")
print(f"Obergrenze aus den Daten:        {obergrenze:,.0f} zusätzliche Getränke je Studio und Jahr "
      f"({obergrenze / absatz_je_jahr:.1%}), wenn die Engstelle komplett verschwände")

fig, ax = plt.subplots(figsize=(7, 3.6))
ax.barh(["Obergrenze laut Daten", "Nötig für Kostendeckung"], [obergrenze, noetig_je_jahr],
        color=["steelblue", "crimson"])
ax.set(xlabel="zusätzlich verkaufte Getränke je Studio und Jahr", title="Reicht der mögliche Zusatzabsatz?")
zeige("08_wirtschaftlichkeit")

# %% [markdown]
# ## 9. Fazit
#
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Empfehlung**
#
# **Zweite Theke nicht flächendeckend einführen.**
#
# 1. **Datenqualität:** elf Fehlerarten, darunter ein Datumsformat, das mit dem Seminarskript falsch gelesen wird.
# 2. **Zusammenhang:** Roh gilt „mehr Check-ins, weniger Getränke“ (r ≈ −0,34), ein **Scheinzusammenhang**. Die Temperatur bewegt beides.
# 3. **Bei gleicher Temperatur:** mehr Check-ins gehören zu **mehr** Getränken (+0,50 je Check-in).
# 4. **Engstelle:** nur ca. 2 % weniger Getränke je Check-in an den vollsten Tagen. Selbst wenn eine zweite Theke diese Lücke ganz schließt, käme nur etwa die Hälfte der nötigen Zusatzmenge zusammen (ca. 4,5 % statt 8,5 % mehr Absatz).
# 5. **Wenn die Geschäftsführung der Schlangen-Vermutung nachgehen will:** ein **Pilot** in einem vollen Studio (z. B. Sachsenhausen) mit Vergleichsstudio und Stundenwerten der Kasse, bevor 14 × 38.000 € ausgegeben werden.
#
# </div>

# **Offen:** Stundenwerte (Stoßzeiten), Wartezeiten, Marge je Getränk, Kundenzufriedenheit an der Theke.
