# %% [markdown]
# # Tag 5 · Arbeitsauftrag 1: Kundengruppen beim Garten- und Heimwerkerfachhändler
#
# **Frage:** Welche Gruppen ähnlicher Kunden gibt es im Auszug aus dem Kundenkartensystem
# (12 Kunden, Alter, Käufe pro Jahr, Umsatz pro Jahr)?
#
# Dieses Skript ist im „Percent-Format“ geschrieben (`# %%` trennt Zellen). Es läuft als
# normales Python-Skript (`python3 05_UE2_Datenanalyse_Kundengruppen.py`) und lässt sich in
# Jupyter zellenweise ausführen.
#
# Benötigt: `pandas`, `numpy`, `matplotlib`, `scikit-learn`.
#
# **Gang der Analyse**
# 1. Daten laden und eine abgeleitete Größe bilden (Umsatz je Kauf)
# 2. Die Kunden ansehen und von Hand Gruppen bilden
# 3. Gegenprobe mit k-Means (mit und ohne Standardisierung)
# 4. Wie viele Gruppen sind sinnvoll?
# 5. Welche Merkmale trennen die Gruppen?

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

try:
    ordner = Path(__file__).parent
except NameError:  # in Jupyter gibt es __file__ nicht
    ordner = Path.cwd()

plt.rcParams.update({"figure.dpi": 110, "axes.grid": True, "grid.alpha": 0.3,
                     "axes.spines.top": False, "axes.spines.right": False})
FARBEN = {1: "#1f77b4", 2: "#d95f02", 3: "#1b9e77", 4: "#7570b3"}

# %% [markdown]
# ## 1. Daten laden
#
# Die Datei hat Semikolon als Trenner und ein BOM am Anfang. Eine leere Zeile am Ende
# wird verworfen.

# %%
d = pd.read_csv(ordner / "05_kundenkarte_auszug.csv", sep=";", encoding="utf-8-sig").dropna()
d["je_kauf"] = d["umsatz_pro_jahr_eur"] / d["kaeufe_pro_jahr"]
d

# %%
print(f"Kunden:              {len(d)}")
print(f"Umsatz gesamt:       {d.umsatz_pro_jahr_eur.sum():,.0f} €")
print(f"Käufe gesamt:        {d.kaeufe_pro_jahr.sum():,.0f}")
print(f"Ø Umsatz je Kauf:    {d.umsatz_pro_jahr_eur.sum() / d.kaeufe_pro_jahr.sum():.0f} € "
      "(laut Händler: Ø Bon 68 € über alle Kunden)")
print(f"Anteil am Kartenbestand: {len(d) / 8400:.2%} von 8.400 Kunden")

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Der Auszug ist klein und nicht repräsentativ.**
# 12 von 8.400 Kunden (0,14 %). Der Ø Umsatz je Kauf liegt bei 106 € gegen 68 € Ø Bon laut
# Händler. Alles Folgende sind Hypothesen, die die ganze Kundenkartendatei prüfen muss.
#
# </div>

# %% [markdown]
# ## 2. Von Hand Gruppen bilden
#
# **Was hier tatsächlich passiert ist (ehrlich beschrieben).** Die Gruppen sind *nicht* aus
# einem Streudiagramm abgelesen. Der Autor dieser Lösung (eine KI) sieht keine Grafik,
# sondern liest die Zahlen der Tabelle. Das Streudiagramm weiter unten entsteht erst *nach*
# der Gruppenbildung und zeigt nur das Ergebnis. Vorgegangen wurde mit drei Heuristiken:
#
# 1. **Lücken suchen.** Die Werte einer Spalte der Größe nach sortieren und schauen, wo
#    ein großer Sprung liegt. Käufe: 2, 2, 3, 3, 4, 4 | 16, 18, 20, 22, 26, 30. Umsatz:
#    180 bis 710 € | 1.950 bis 2.650 €. Zwischen den Blöcken liegt jeweils niemand.
# 2. **Zwei Merkmale kreuzen.** Zwei Blöcke je Merkmal ergeben vier Felder. Alle vier sind
#    besetzt, mit je drei Kunden. Das ist das Muster „vier Gruppen“.
# 3. **Gegenprüfen und benennen.** Passen die übrigen Spalten dazu (Umsatz je Kauf,
#    Zahlart, Kunde seit)? Daraus ergeben sich die Namen.
#
# Die erste Zelle setzt Heuristik 1 und 2 in Code um. Das ist keine Magie: Der Rechner sucht
# die größte Lücke, so wie ein Mensch den Sprung im sortierten Zahlenstrahl sieht.

# %%
# Heuristik 1: größte Lücke in den sortierten Werten suchen
schwellen = {}
for spalte in ["kaeufe_pro_jahr", "umsatz_pro_jahr_eur"]:
    werte = np.sort(d[spalte].to_numpy())
    # >>> HIER PASSIERT DIE LÜCKENSUCHE: np.diff = Abstand zu den Nachbarn, argmax = größter Sprung
    i = np.diff(werte).argmax()
    schwellen[spalte] = (werte[i] + werte[i + 1]) / 2
    print(f"{spalte}: {werte.astype(int).tolist()}")
    print(f"   größte Lücke zwischen {werte[i]:.0f} und {werte[i + 1]:.0f}, "
          f"Schwelle bei {schwellen[spalte]:.0f}\n")

# Heuristik 2: beide Merkmale kreuzen
d["viele_kaeufe"] = d["kaeufe_pro_jahr"] > schwellen["kaeufe_pro_jahr"]
d["hoher_umsatz"] = d["umsatz_pro_jahr_eur"] > schwellen["umsatz_pro_jahr_eur"]
print(pd.crosstab(d["viele_kaeufe"], d["hoher_umsatz"]))
aus_luecken = {frozenset(x.kunde) for _, x in d.groupby(["viele_kaeufe", "hoher_umsatz"])}

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: „Nach Augenmaß“ heißt hier: Lücken in sortierten Zahlen finden.**
# Zwei Merkmale mit je einer klaren Lücke ergeben vier besetzte Felder. Das funktioniert nur,
# weil die Lücken in diesen 12 Kunden sehr deutlich sind. Bei vielen Kunden und fließenden
# Übergängen (ohne Lücken) trägt dieser Weg nicht mehr. Dafür gibt es Clustering-Modelle.
#
# </div>

# %% [markdown]
# **Wie macht das ein Modell?** k-Means (Abschnitt 3) sucht ebenfalls Gruppen, aber ohne
# Lücke von Hand: Es setzt k Mittelpunkte, ordnet jeden Kunden dem nächsten zu und
# verschiebt die Mittelpunkte, bis sich nichts mehr ändert. Der Vorteil: Es arbeitet mit
# **allen Merkmalen gleichzeitig** (hier Alter, Käufe, Umsatz) und braucht keine sichtbare
# Lücke. Der Nachteil: Man muss k vorgeben und die Merkmale vorher auf gleiche Skala
# bringen. Außerdem gilt auch hier: Die Gruppen deutet der Mensch.

# %%
gruppen = {1: ["K01", "K04", "K08"], 2: ["K03", "K07", "K11"],
           3: ["K02", "K05", "K10"], 4: ["K06", "K09", "K12"]}
namen = {1: "Laufkundschaft jung", 2: "Profis / Gewerbe",
         3: "Anschaffer", 4: "Gelegenheitskäufer"}
d["gruppe"] = d["kunde"].map({k: g for g, ks in gruppen.items() for k in ks})
print("Handgruppen = Gruppen aus den Lücken:", {frozenset(v) for v in gruppen.values()} == aus_luecken)

fig, ax = plt.subplots(figsize=(8, 5.5))
for g, x in d.groupby("gruppe"):
    ax.scatter(x.kaeufe_pro_jahr, x.umsatz_pro_jahr_eur, s=90, color=FARBEN[g],
               label=f"{g} {namen[g]}")
for _, z in d.iterrows():
    ax.annotate(z.kunde, (z.kaeufe_pro_jahr, z.umsatz_pro_jahr_eur),
                textcoords="offset points", xytext=(6, 5), fontsize=8)
ax.set(xlabel="Käufe pro Jahr", ylabel="Umsatz pro Jahr (€)",
       title="Käufe und Umsatz: vier erkennbare Gruppen")
ax.legend()
plt.show()

# %%
tab = d.groupby("gruppe").agg(kunden=("kunde", "count"), alter=("alter", "mean"),
                              kaeufe=("kaeufe_pro_jahr", "mean"),
                              umsatz=("umsatz_pro_jahr_eur", "sum"),
                              kaeufe_summe=("kaeufe_pro_jahr", "sum"))
tab["umsatz_je_kunde"] = tab.umsatz / tab.kunden
tab["anteil_umsatz"] = tab.umsatz / tab.umsatz.sum()
tab["anteil_kaeufe"] = tab.kaeufe_summe / tab.kaeufe_summe.sum()
tab["umsatz_je_kauf"] = tab.umsatz / tab.kaeufe_summe
tab.index = [f"{g} {namen[g]}" for g in tab.index]
tab.round(2)

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Vier Gruppen, und zwei davon tragen 84 % des Umsatzes.**
# Gruppe 2 (Profis, 43,5 %) und Gruppe 3 (Anschaffer, 40,4 %) bringen den Umsatz.
# Gruppe 1 hat 52 % der Käufe, aber nur 12 % des Umsatzes. Gruppe 4 bringt 4 %.
#
# </div>

# %% [markdown]
# ## 3. Gegenprobe mit k-Means
#
# Der Algorithmus bekommt Alter, Käufe und Umsatz und soll vier Gruppen bilden. Einmal
# **standardisiert** (jedes Merkmal auf Mittelwert 0 und Streuung 1), einmal **roh**.

# %% [markdown]
# ### 3a. k-Means zum Anfassen (von Hand programmiert)
#
# Bevor die Bibliothek den Algorithmus übernimmt: so sieht k-Means im Kern aus. Zwei Schritte
# im Wechsel, bis sich nichts mehr ändert. Die Merkmale werden vorher standardisiert.

# %%
merkmale = ["alter", "kaeufe_pro_jahr", "umsatz_pro_jahr_eur"]
M = d[merkmale].astype(float)
# >>> HIER PASSIERT DIE STANDARDISIERUNG: jedes Merkmal bekommt Mittelwert 0 und Streuung 1,
# >>> damit der Umsatz (Euro, Tausende) den Abstand nicht gegenüber Alter und Käufen erdrückt
Z = (M - M.mean()) / M.std(ddof=0)


def kmeans_von_hand(Z, start, titel, schritte=15):
    """Einfaches k-Means. `start` = Zeilen, die als erste Mittelpunkte dienen.
    Zeichnet nach jedem Schritt Kunden, alte Mittelpunkte (Ring) und neue (Kreuz)."""
    z = Z.to_numpy()
    mitte = z[start].copy()
    alt = None
    verlauf = []                       # je Schritt: Zuordnung, Mittelpunkte vorher und nachher
    for schritt in range(1, schritte + 1):
        # >>> HIER PASSIERT DIE ZUORDNUNG: jeder Kunde kommt zum nächsten Mittelpunkt
        # >>> (kleinster quadrierter Abstand im standardisierten Merkmalsraum)
        abstand = ((z[:, None, :] - mitte[None, :, :]) ** 2).sum(axis=2)
        label = abstand.argmin(axis=1)
        print(f"Schritt {schritt}: {label.tolist()}")
        if alt is not None and (label == alt).all():
            print("   nichts hat sich geändert: fertig")
            verlauf.append((label, mitte, mitte))
            break
        alt = label
        # >>> HIER PASSIERT DAS LERNEN: jeder Mittelpunkt wandert in den Schwerpunkt seiner Kunden
        neu = np.array([z[label == j].mean(axis=0) if (label == j).any() else mitte[j]
                        for j in range(len(start))])
        verlauf.append((label, mitte, neu))
        mitte = neu

    # Zeichnen: Mittelpunkte zurück in Käufe und Euro umrechnen (Alter wird mitgerechnet,
    # aber nicht gezeichnet)
    mw, sd = M.mean().to_numpy(), M.std(ddof=0).to_numpy()
    spalten = ["kaeufe_pro_jahr", "umsatz_pro_jahr_eur"]
    n = len(verlauf)
    fig, axes = plt.subplots(1, n, figsize=(3.6 * n, 3.8), sharey=True, constrained_layout=True)
    for ax, (nr, (lab, vorher, nachher)) in zip(np.atleast_1d(axes), enumerate(verlauf, 1)):
        ax.scatter(d[spalten[0]], d[spalten[1]], c=[FARBEN[j + 1] for j in lab], s=45)
        v = (vorher * sd + mw)[:, 1:]
        h = (nachher * sd + mw)[:, 1:]
        ax.scatter(v[:, 0], v[:, 1], s=130, facecolors="none", edgecolors="black")   # alt
        ax.scatter(h[:, 0], h[:, 1], s=110, marker="X", c="black")                   # neu
        for j in range(len(v)):
            ax.annotate("", h[j], v[j], arrowprops=dict(arrowstyle="->", color="black"))
        ax.set(title=f"Schritt {nr}", xlabel="Käufe pro Jahr")
    np.atleast_1d(axes)[0].set_ylabel("Umsatz pro Jahr (€)")
    fig.suptitle(f"{titel}: Ring = Mittelpunkt vorher, Kreuz = nachher, Farbe = Zuordnung")
    plt.show()
    return label


def gruppen_aus(label):
    return sorted(sorted(d.kunde[label == j]) for j in set(label))


# Start 1: die ersten vier Kunden (K01 bis K04) als Mittelpunkte
label1 = kmeans_von_hand(Z, start=[0, 1, 2, 3], titel="Start K01 bis K04")
print(gruppen_aus(label1))

# %%
# Start 2: ungünstige Startpunkte (K01, K03, K05, K07)
label2 = kmeans_von_hand(Z, start=[0, 2, 4, 6], titel="Ungünstiger Start")
print(gruppen_aus(label2))

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: k-Means besteht aus zwei Schritten, und der Start zählt.**
# Zuordnen (nächster Mittelpunkt) und Verschieben (Schwerpunkt der Gruppe), im Wechsel, bis
# sich nichts mehr ändert. Mit den Startpunkten K01 bis K04 entstehen die vier Dreiergruppen.
# Mit ungünstigen Startpunkten bleibt der Algorithmus in einer schlechten Lösung hängen.
# Deshalb startet die Bibliothek mehrfach (`n_init=50`) und nimmt das beste Ergebnis.
#
# </div>

# %% [markdown]
# ### 3b. Dasselbe mit der Bibliothek (scikit-learn)

# %%
# >>> HIER PASSIERT DIE GRUPPENBILDUNG: fit_predict lernt die Mittelpunkte aus den Daten
# >>> und gibt für jeden Kunden die Gruppennummer zurück (mit 50 Startversuchen, bester gewinnt)
d["km_standard"] = KMeans(4, n_init=50, random_state=0).fit_predict(Z)
# gleiche Rechnung ohne Standardisierung, zum Vergleich
d["km_roh"] = KMeans(4, n_init=50, random_state=0).fit_predict(M)

print("Standardisiert:")
print(d.groupby("km_standard").kunde.apply(list).to_string())
print("\nRoh (ohne Standardisierung):")
print(d.groupby("km_roh").kunde.apply(list).to_string())

# %%
hand = {frozenset(ks) for ks in gruppen.values()}
for spalte in ("km_standard", "km_roh"):
    cl = {frozenset(x.kunde) for _, x in d.groupby(spalte)}
    print(f"{spalte}: stimmt mit der Handarbeit überein: {cl == hand}")

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Merkmale vor dem Clustern auf gleiche Skala bringen.**
# Standardisiert findet k-Means genau die vier Dreiergruppen der Handarbeit. Ohne
# Standardisierung dominiert der Umsatz (Eurospanne bis 2.650, Alter nur 22 bis 63), und die
# Gruppen K02/K10/K11 sowie K03/K05/K07 werden vermischt.
#
# </div>

# %% [markdown]
# ## 4. Wie viele Gruppen?
#
# Ellbogen-Methode (Streuung innerhalb der Gruppen) und Silhouette (wie klar sind die
# Gruppen getrennt, 1 ist ideal), beides auf den standardisierten Daten.

# %%
ks = range(2, 7)
inertia, sil = [], []
for k in ks:
    # >>> HIER PASSIERT DAS TRAINING für jede getestete Gruppenzahl k
    km = KMeans(k, n_init=50, random_state=0).fit(Z)
    inertia.append(km.inertia_)
    # >>> HIER PASSIERT DIE BEWERTUNG: wie klar sind die Gruppen getrennt (1 = ideal)?
    sil.append(silhouette_score(Z, km.labels_))

fig, (a, b) = plt.subplots(1, 2, figsize=(10, 3.8), constrained_layout=True)
a.plot(ks, inertia, "o-")
a.set(xlabel="Anzahl Gruppen k", ylabel="Streuung innerhalb der Gruppen", title="Ellbogen")
b.plot(ks, sil, "o-", color="#d95f02")
b.set(xlabel="Anzahl Gruppen k", ylabel="Silhouette", title="Silhouette")
plt.show()
pd.DataFrame({"k": list(ks), "inertia": np.round(inertia, 2), "silhouette": np.round(sil, 2)})

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: k = 4 ist ein vernünftiger Punkt.**
# Die Streuung fällt bis k = 4 stark und danach kaum noch. Die Silhouette ist bei k = 4 mit
# 0,71 hoch. Bei nur 12 Kunden ist das aber ein Hinweis, kein Beweis.
#
# </div>

# %% [markdown]
# ## 5. Welche Merkmale trennen die Gruppen?
#
# Es gibt vier Gruppen, also sechs Gruppenpaare. Ein Merkmal trennt ein Paar, wenn sich
# die Wertebereiche (kleinster bis größter Wert) der beiden Gruppen nicht überlappen. Für
# Zahlart und Filiale zeigt danach die Kreuztabelle die Verteilung.

# %%
import itertools


def getrennte_paare(spalte):
    r = d.groupby("gruppe")[spalte].agg(["min", "max"])
    return [(a, b) for a, b in itertools.combinations(r.index, 2)
            if r.loc[a, "max"] < r.loc[b, "min"] or r.loc[b, "max"] < r.loc[a, "min"]]


merkmal_namen = ["kaeufe_pro_jahr", "umsatz_pro_jahr_eur", "je_kauf", "alter", "kunde_seit"]
pd.DataFrame({"getrennte Paare (von 6)": [len(getrennte_paare(s)) for s in merkmal_namen],
              "nicht getrennt": [[p for p in itertools.combinations(range(1, 5), 2)
                                  if p not in getrennte_paare(s)] for s in merkmal_namen]},
             index=merkmal_namen)

# %%
print(pd.crosstab(d["gruppe"], d["zahlart"]), "\n")
print(pd.crosstab(d["gruppe"], d["filiale"]))

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Entscheidend ist die Kombination aus Käufen und Umsatz.**
# Käufe und Umsatz trennen einzeln je 5 von 6 Gruppenpaaren, zusammen (Umsatz je Kauf)
# alle 6. Auch „Kunde seit“ trennt alle 6, ist aber eher ein Begleitmerkmal (Kundendauer).
# Die Zahlart „Rechnung“ erkennt die Profis sofort. Die Filiale trennt nichts: jede Gruppe
# enthält Nord und Süd.
#
# </div>

# %% [markdown]
# ## 6. Gesamtbild
#
# - **Vier Gruppen:** Laufkundschaft jung (K01, K04, K08), Profis (K03, K07, K11),
#   Anschaffer (K02, K05, K10), Gelegenheitskäufer (K06, K09, K12).
# - **Nicht schlussfolgern:** Das Alter läuft mit, ist aber nicht die Ursache.
# - **Vorsicht:** 12 Kunden, nicht repräsentativ. Die Deutungen (Gewerbekunden,
#   Rasenmäher-Käufer) sind Hypothesen, die der Händler bestätigen müsste.
# - **Nächster Schritt:** dieselbe Auswertung auf den 8.400 Kunden der Kundenkarte.
