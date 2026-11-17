# %% [markdown]
# # Tag 5 · Fallstudie RetailX: Kundensegmentierung mit k-Means
#
# **Lage:** RetailX (Wohnaccessoires, 85 Filialen und Webshop) schickt allen Kunden denselben
# Newsletter und dieselben Rabatte. Die Öffnungsrate sinkt, das Marketingbudget von 9 Mio. €
# wirkt kaum messbar. Eine Datenanalystin hat 600 aktive Kunden mit k-Means in fünf Cluster
# eingeteilt (vier Merkmale, standardisiert, k = 5).
#
# **Aufgabe hier:** die Rechnung der Analystin nachvollziehen und **kritisch prüfen**:
# Stimmt die Merkmalswahl? Ist k = 5 richtig? Ist jeder Cluster ein Segment?
#
# Dieses Skript ist im „Percent-Format“ geschrieben (`# %%` trennt Zellen). Es läuft als
# normales Python-Skript (`python3 05_UE5_6_Datenanalyse_RetailX.py`) und lässt sich in
# Jupyter zellenweise ausführen.
#
# Benötigt: `pandas`, `numpy`, `matplotlib`, `scikit-learn`.
#
# **Gang der Analyse**
# 1. Daten laden und prüfen
# 2. Merkmale ansehen (Verteilung, Zusammenhänge)
# 3. Wie viele Cluster? Ellbogen und Silhouette
# 4. k-Means mit k = 5 und das Clusterprofil der Analystin nachrechnen
# 5. Was prägt jeden Cluster? Abstand zum Durchschnitt
# 6. Sind Cluster 2 und 5 wirklich verschieden?
# 7. Wie stabil ist das Ergebnis? Andere Merkmale, anderer Start
# 8. Segmente und Maßnahmen

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, silhouette_score

try:
    ordner = Path(__file__).parent
except NameError:  # in Jupyter gibt es __file__ nicht
    ordner = Path.cwd()

plt.rcParams.update({"figure.dpi": 110, "axes.grid": True, "grid.alpha": 0.3,
                     "axes.spines.top": False, "axes.spines.right": False})
FARBEN = {"C1": "#d95f02", "C2": "#7f7f7f", "C3": "#1b9e77", "C4": "#7570b3", "C5": "#1f77b4"}

# %% [markdown]
# ## 1. Daten laden und prüfen
#
# Semikolon als Trenner, BOM am Dateianfang. Die Datei hat 601 Zeilen, davon eine leere am
# Ende.

# %%
roh = pd.read_csv(ordner / "05_retailx_kunden_stichprobe.csv", sep=";", encoding="utf-8-sig")
print("Zeilen in der Datei:", len(roh))
d = roh.dropna(subset=["kunde"]).copy()          # leere Endzeile verwerfen
print("Kunden:", len(d), " | doppelte Kundennummern:", d.kunde.duplicated().sum())

fehlend = d.isna().sum().to_frame("fehlend")
fehlend["Anteil"] = (fehlend.fehlend / len(d)).round(3)
fehlend

# %%
d.describe().round(1).T

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Bis auf das Alter ist die Datei vollständig.**
# 600 Kunden, keine Dubletten. Das Alter fehlt bei 229 Kunden (38 %), so wie in der
# Aufgabe beschrieben. Es ist auch nicht im Modell, und das ist gut so (siehe Abschnitt 7).
#
# </div>

# %% [markdown]
# ## 2. Merkmale ansehen
#
# Die Analystin nimmt vier Merkmale: Käufe pro Jahr, Ø Bon, Rabattanteil, Tage seit dem
# letzten Kauf.

# %%
MERKMALE = ["kaeufe_pro_jahr", "durchschnittsbon_eur", "rabattanteil_prozent",
            "tage_seit_letztem_kauf"]
TITEL = {"kaeufe_pro_jahr": "Käufe pro Jahr", "durchschnittsbon_eur": "Ø Bon (€)",
         "rabattanteil_prozent": "Rabattanteil (%)", "tage_seit_letztem_kauf": "Tage seit Kauf"}

fig, axes = plt.subplots(1, 4, figsize=(13, 3), constrained_layout=True)
for ax, m in zip(axes, MERKMALE):
    ax.hist(d[m], bins=30, color="#1f77b4")
    ax.set(title=TITEL[m], ylabel="Kunden")
plt.show()

# %%
korr = d[MERKMALE].corr()
korr.round(2)

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Käufe und Tage seit dem letzten Kauf messen teils dasselbe.**
# Der Zusammenhang ist r = −0,65: Wer oft kauft, kaufte meist erst vor Kurzem. Beide Merkmale
# zählen im Abstand doppelt „Aktivität“. Der Bon hat dagegen kaum Zusammenhang mit
# Käufen und Tagen (r ≈ −0,1) und nur mäßig mit dem Rabatt (r = −0,39), er bringt viel eigene
# Information. Die Verteilungen sind schief
# (viele Wenig-Käufer, wenige mit sehr hohem Bon).
#
# </div>

# %% [markdown]
# ## 3. Wie viele Cluster?
#
# **Standardisieren:** Käufe (1 bis 20), Bon (bis 218 €) und Tage (bis 556) haben ganz
# verschiedene Spannen. Ohne gemeinsame Skala würden die Tage den Abstand dominieren.

# %%
# >>> HIER PASSIERT DIE STANDARDISIERUNG: jedes Merkmal bekommt Mittelwert 0 und Streuung 1,
# >>> damit kein Merkmal den Abstand nur wegen seiner Zahlenspanne bestimmt
X = d[MERKMALE]
Z = (X - X.mean()) / X.std(ddof=0)

ks = range(1, 9)
inertia, sil = [], []
for k in ks:
    # >>> HIER PASSIERT DAS TRAINING für jede getestete Clusterzahl k
    km = KMeans(k, n_init=50, random_state=0).fit(Z)
    inertia.append(km.inertia_)
    # >>> HIER PASSIERT DIE BEWERTUNG: wie klar sind die Cluster getrennt (1 = ideal)?
    sil.append(silhouette_score(Z, km.labels_) if k > 1 else np.nan)

index = np.array(inertia) / inertia[0] * 100        # k = 1 entspricht 100 (wie in der Folie)
fig, (a, b) = plt.subplots(1, 2, figsize=(11, 3.8), constrained_layout=True)
a.plot(list(ks), index, "o-")
a.axvline(5, color="gray", ls="--", label="Wahl der Analystin (k = 5)")
a.set(xlabel="Anzahl Cluster k", ylabel="Streuung innerhalb der Cluster (Index)", title="Ellbogen")
a.legend()
b.plot(list(ks), sil, "o-", color="#d95f02")
b.axvline(5, color="gray", ls="--")
b.set(xlabel="Anzahl Cluster k", ylabel="Silhouette", title="Silhouette")
plt.show()
pd.DataFrame({"k": list(ks), "Index": index.round(1), "Silhouette": np.round(sil, 2)})

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Der Ellbogen liegt bei k = 4, nicht bei k = 5.**
# Die Streuung fällt von 42 (k = 3) auf 21 (k = 4) stark, danach nur noch langsam
# (16 bei k = 5). Die Silhouette ist bei k = 4 am höchsten (0,57), bei k = 5 nur 0,47.
# Die Wahl k = 5 ist also nicht die „sauberste“ Zahl. Ob sie trotzdem nützlich ist,
# klärt Abschnitt 6.
#
# </div>

# %% [markdown]
# ## 4. k-Means mit k = 5: das Clusterprofil
#
# So hat die Analystin gerechnet. Die Cluster werden nach ihren Eigenschaften C1 bis C5
# genannt, damit sie zu den Folien passen (die Nummern, die k-Means vergibt, sind zufällig).

# %%
# >>> HIER PASSIERT DIE GRUPPENBILDUNG: k-Means lernt fünf Mittelpunkte und gibt jedem
# >>> Kunden die Nummer des nächsten Mittelpunkts
km5 = KMeans(5, n_init=50, random_state=0).fit(Z)
d["roh_nr"] = km5.labels_
d["umsatz"] = d.kaeufe_pro_jahr * d.durchschnittsbon_eur


def benennen(daten):
    """Zuordnung der k-Means-Nummern zu C1 bis C5 über markante Eigenschaften."""
    m = daten.groupby("roh_nr")[MERKMALE].mean()
    c3 = m.kaeufe_pro_jahr.idxmax()                         # die meisten Käufe
    c1 = m.rabattanteil_prozent.idxmax()                    # der höchste Rabattanteil
    c4 = m.durchschnittsbon_eur.idxmax()                    # der höchste Bon
    c2 = m.tage_seit_letztem_kauf.idxmax()                  # der längste Abstand zum letzten Kauf
    c5 = (set(m.index) - {c1, c2, c3, c4}).pop()            # der Rest
    return {c1: "C1", c2: "C2", c3: "C3", c4: "C4", c5: "C5"}


d["C"] = d.roh_nr.map(benennen(d))

profil = d.groupby("C").agg(kunden=("kunde", "count"), kaeufe=("kaeufe_pro_jahr", "mean"),
                            bon=("durchschnittsbon_eur", "mean"),
                            rabatt=("rabattanteil_prozent", "mean"),
                            tage=("tage_seit_letztem_kauf", "mean"), umsatz=("umsatz", "sum"))
profil["Kunden %"] = profil.kunden / profil.kunden.sum() * 100
profil["Umsatz %"] = profil.umsatz / profil.umsatz.sum() * 100
alle = pd.DataFrame({"kunden": [len(d)], "kaeufe": [d.kaeufe_pro_jahr.mean()],
                     "bon": [d.durchschnittsbon_eur.mean()], "rabatt": [d.rabattanteil_prozent.mean()],
                     "tage": [d.tage_seit_letztem_kauf.mean()], "umsatz": [d.umsatz.sum()],
                     "Kunden %": [100.0], "Umsatz %": [100.0]}, index=["Alle"])
pd.concat([profil, alle]).drop(columns=["umsatz"]).round(1)

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Die Rechnung der Analystin ist reproduzierbar.**
# Die Tabelle stimmt mit der Folie überein (z. B. C3: 15 % der Kunden, 13,0 Käufe, 48 % des
# Umsatzes). Der Umsatzanteil ist dabei Käufe × Ø Bon, ein Hilfswert, kein Kassenumsatz.
# Wenige Kunden (C3) tragen fast die Hälfte des Umsatzes.
#
# </div>

# %%
fig, ax = plt.subplots(figsize=(8, 5.5))
for c, x in d.groupby("C"):
    ax.scatter(x.tage_seit_letztem_kauf, x.kaeufe_pro_jahr, s=22, alpha=0.7, color=FARBEN[c],
               label=f"{c} ({len(x)})")
ax.set(xlabel="Tage seit dem letzten Kauf", ylabel="Käufe pro Jahr",
       title="Die fünf Cluster in zwei der vier Merkmale")
ax.legend()
plt.show()

# %% [markdown]
# ## 5. Was prägt jeden Cluster?
#
# Leitfrage der Folie: *Ab welchem Abstand zum Durchschnitt prägt ein Merkmal einen
# Cluster?* Dafür wird der Clustermittelwert in **Standardabweichungen** vom Gesamtmittel
# gemessen. Als Faustregel (Annahme) gilt ein Abstand ab ±0,5 als merklich, ab ±1 als stark.

# %%
abstand = Z.groupby(d.C).mean()
abstand.columns = [TITEL[c] for c in abstand.columns]

fig, ax = plt.subplots(figsize=(7.5, 3.8))
bild = ax.imshow(abstand.to_numpy(), cmap="RdBu_r", vmin=-3, vmax=3, aspect="auto")
ax.set_xticks(range(4), abstand.columns)
ax.set_yticks(range(5), abstand.index)
ax.grid(False)
for i in range(5):
    for j in range(4):
        ax.text(j, i, f"{abstand.iloc[i, j]:+.1f}", ha="center", va="center", fontsize=10)
fig.colorbar(bild, label="Abstand in Standardabweichungen")
ax.set_title("Abstand des Clustermittels zum Gesamtmittel")
plt.show()
abstand.round(2)

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: C1 bis C4 haben ein klares Gesicht, C5 nicht.**
# C1 = hoher Rabattanteil (+1,4), C2 = lange her (+1,3), C3 = viele Käufe (+2,0) bei
# wenig Rabatt (−1,0), C4 = sehr hoher Bon (+2,9). C5 liegt bei allen vier Merkmalen
# zwischen −0,5 und 0 (leicht unter dem Durchschnitt) und fällt nirgends auf.
#
# </div>

# %% [markdown]
# **Merkmale, die nicht im Modell stehen**, nur zur Beschreibung (Warengruppe, Online-Anteil,
# Kunde seit, Alter):

# %%
beschr = d.groupby("C").agg(online=("anteil_online_prozent", "mean"), seit=("kunde_seit", "mean"),
                            alter=("alter", "mean"), alter_fehlt=("alter", lambda s: s.isna().mean()))
beschr["Warengruppe"] = d.groupby("C").haupt_warengruppe.agg(
    lambda s: f"{s.value_counts().index[0]} ({s.value_counts(normalize=True).iloc[0]:.0%})")
beschr.round(2)

# %% [markdown]
# ## 6. Sind C2 und C5 wirklich verschieden?
#
# Beide haben wenige Käufe (1,5 und 2,5), einen kleinen Bon (43 € und 45 €) und denselben
# Rabattanteil (30 % und 31 %). Es bleibt ein Unterschied: Tage seit dem letzten Kauf.

# %%
vergleich = d[d.C.isin(["C2", "C5"])].groupby("C").tage_seit_letztem_kauf.agg(["min", "median", "max"])
print(vergleich)

fig, ax = plt.subplots(figsize=(8, 3.5))
for c in ("C2", "C5"):
    ax.hist(d.loc[d.C == c, "tage_seit_letztem_kauf"], bins=30, alpha=0.7, color=FARBEN[c], label=c)
ax.axvline(d.loc[d.C == "C5", "tage_seit_letztem_kauf"].max(), color="black", ls="--")
ax.set(xlabel="Tage seit dem letzten Kauf", ylabel="Kunden",
       title="C2 und C5 trennt eine Linie bei der Tageszahl")
ax.legend()
plt.show()

# %%
# k = 4 zum Vergleich: wohin gehen die Kunden von C5?
km4 = KMeans(4, n_init=50, random_state=0).fit(Z)
pd.crosstab(d.C, km4.labels_, rownames=["k = 5"], colnames=["k = 4 (Nummer)"])

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: C2 und C5 sind ein Cluster, den eine Grenze bei 234 Tagen teilt.**
# Kein Kunde von C5 liegt über 234 Tagen, keiner von C2 darunter. Sonst sind sie fast
# gleich. Bei k = 4 landen 91 von 114 C5-Kunden in einem gemeinsamen Cluster mit C2.
# „Tage seit dem letzten Kauf“ ist zudem ein **Zustand**, kein Charakterzug: Ein Kunde aus
# C5 rutscht nach C2, wenn er nicht kauft. Ein eigenes Segment ist das wohl nicht.
#
# </div>

# %% [markdown]
# ## 7. Wie stabil ist das Ergebnis?
#
# **Stabilität:** Wir vergleichen Clusterungen mit dem Adjusted Rand Index (ARI, 1 = gleiche
# Einteilung, 0 = wie Zufall). Drei Fragen: anderer Startwert, ohne Standardisierung, andere
# Merkmale.

# %%
def ari(a, b):
    return round(adjusted_rand_score(a, b), 2)


# a) anderer Startwert: ein einziger Startversuch gegen 50 Versuche
einzeln = [ari(km5.labels_, KMeans(5, n_init=1, random_state=s).fit(Z).labels_) for s in range(10)]
mehrfach = [ari(km5.labels_, KMeans(5, n_init=50, random_state=s).fit(Z).labels_) for s in range(1, 6)]
print("1 Startversuch, 10 Läufe:  ", einzeln)
print("50 Startversuche, 5 Läufe: ", mehrfach)

# %%
# b) ohne Standardisierung, c) andere Merkmale
def clustere(spalten, standardisieren=True):
    daten = d[spalten]
    if standardisieren:
        daten = (daten - daten.mean()) / daten.std(ddof=0)
    return KMeans(5, n_init=50, random_state=0).fit(daten).labels_


varianten = {
    "ohne Standardisierung": clustere(MERKMALE, standardisieren=False),
    "ohne Tage seit Kauf": clustere(["kaeufe_pro_jahr", "durchschnittsbon_eur", "rabattanteil_prozent"]),
    "plus Online-Anteil": clustere(MERKMALE + ["anteil_online_prozent"]),
    "plus Kunde seit": clustere(MERKMALE + ["kunde_seit"]),
}
pd.DataFrame({"ARI gegen die Analystin": {n: ari(km5.labels_, l) for n, l in varianten.items()}})

# %%
# Das Alter: fehlt oft und hängt mit nichts zusammen
d[["alter", "kunde_seit", "anteil_online_prozent"] + MERKMALE].corr().round(2)["alter"]

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Die Cluster sind stabil, aber nicht unabhängig von der Merkmalswahl.**
# Mit 50 Startversuchen kommt jedes Mal dieselbe Einteilung heraus (ARI = 1,0). Mit nur einem
# Startversuch gibt es schlechtere Ergebnisse. Ohne Standardisierung wird es ein anderes
# Bild (ARI ca. 0,5), und auch mit Online-Anteil oder Kunde seit ändern sich die Cluster
# merklich. Das Alter hängt mit nichts zusammen (r ≈ 0) und fehlt oft: Weglassen ist richtig.
#
# </div>

# %% [markdown]
# ## 8. Segmente und Maßnahmen
#
# **Entscheidung (Vorschlag):** vier Segmente statt fünf. C2 und C5 werden zu *einem*
# Segment „Gelegenheitskäufer“ mit einer Regel für die Zeit seit dem letzten Kauf.
# Das Marketing (6 Personen) kann realistisch drei bis vier Segmente bespielen.
#
# | Segment | Cluster | Was sie auszeichnet | Maßnahme | Risiko |
# |---|---|---|---|---|
# | **Stammkunden** | C3 (15 %, 48 % Umsatz) | 13 Käufe, kaum Rabatt, zuletzt vor 20 Tagen | Bindung statt Rabatt: Vorab-Zugang zur Eigenmarke, App-Vorteile | zu viele Aktionen, Rabatt gewöhnt sie an Preisnachlass |
# | **Rabatt-Jäger** | C1 (27 %, 23 % Umsatz) | 71 % Rabattanteil, kleiner Bon, kaufen regelmäßig | Rabatt nicht erhöhen, Mengen- oder Bonusanreize (höherer Bon), Code-Quote testen | Marge schrumpft, Abhängigkeit von Aktionen |
# | **Wenig-Käufer, großer Bon** | C4 (9 %, 11 % Umsatz) | Bon 152 €, Textil, 46 % online | Online-Newsletter mit Textil und Wohnen, Kollektionen | Gruppe klein (52 Kunden), Zufallsrisiko |
# | **Gelegenheitskäufer** | C2 + C5 (49 %, 18 % Umsatz) | 1 bis 3 Käufe, Bon 45 €, Rabatt 30 % | Zweitkauf-Anreiz bei kurzer Pause, günstige Reaktivierung bei über 234 Tagen | Werbekosten verpuffen |
#
# **Wie messen, ob es wirkt?** Mit Kontrollgruppe (A/B-Test): einem Teil der Kunden eines
# Segments gar nichts ändern. Verglichen werden Öffnungsrate, Wiederkaufrate, Ø Bon und
# Rabattquote.

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage: Nicht jeder Cluster ist ein Segment, und das Modell nennt kein k.**
# Die Daten tragen vier Gruppen sauber (Ellbogen und Silhouette bei k = 4), fünf nur mit
# einer zeitabhängigen Grenze. Entscheidend ist, was das Marketing bespielen kann und ob
# eine Gruppe eine eigene Maßnahme bekommt. Falsche Einordnung (z. B. ein treuer Kunde als
# Rabatt-Jäger) kostet Vertrauen, deshalb: Regeln regelmäßig neu rechnen und mit Kontrollgruppe
# testen.
#
# </div>
