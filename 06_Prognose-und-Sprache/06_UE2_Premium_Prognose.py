# %% [markdown]
# # Tag 6, Arbeitsauftrag 1: Premium-Prognose beim Outdoor-Händler
#
# Zu `06_UE2_Loesung_Arbeitsauftrag1_Premium-Prognose.md`. Das Notebook zeigt die Rechnung als Grafiken.
#
# **Die zwei Fragen:**
# 1. Kauft ein neuer Kunde Premium, ja oder nein? (eine **Klasse**, also Klassifikation)
# 2. Wie viel Umsatz bringt er im nächsten Jahr? (eine **Zahl**, also Regression)
#
# Datenbasis sind nur **8 bisherige Kunden**. Alles hier ist deshalb grob.

# %%
from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams.update({"figure.dpi": 110, "axes.grid": True, "grid.alpha": 0.3})
JA, NEIN, NEU = "#1f7a8c", "#d1495b", "#555555"

# %% [markdown]
# ## 1 Daten laden
#
# Die CSV hat bisherige Kunden (A bis H) mit bekanntem Ergebnis und neue Kunden (N1 bis N4) ohne.

# %%
csv = Path("06_UE2_Arbeitsauftrag1_Daten.csv")
roh = pd.read_csv(csv, sep=";", encoding="utf-8-sig")
roh.columns = ["kunde", "gruppe", "alter", "eink", "kaeufe", "kanal", "newsletter", "seit", "premium", "umsatz"]

d = roh[roh.gruppe == "bisherig"].copy()      # 8 Kunden mit bekanntem Ergebnis
n = roh[roh.gruppe == "neu"].copy()           # 4 Kunden, gesucht
d["premium"] = d.premium.eq("ja").astype(int)  # ja = 1, nein = 0
d["umsatz"] = d.umsatz.astype(float)
d[["kunde", "alter", "eink", "kaeufe", "kanal", "premium", "umsatz"]]

# %% [markdown]
# ## 2 Frage 1: Wer kauft Premium?
#
# Jeder Punkt ist ein bisheriger Kunde, aufgetragen nach **Käufen in 12 Monaten**. Oben Premium-Käufer, unten die anderen.
# Die grauen Linien zeigen die vier neuen Kunden.

# %%
fig, ax = plt.subplots(figsize=(9, 3.6))
rng = np.random.default_rng(0)
for wert, farbe, name in [(1, JA, "kauft Premium"), (0, NEIN, "kauft kein Premium")]:
    x = d[d.premium == wert]
    ax.scatter(x.kaeufe, np.full(len(x), wert), s=110, color=farbe, label=name, zorder=3)
    for _, r in x.iterrows():
        ax.annotate(r.kunde, (r.kaeufe, wert), textcoords="offset points", xytext=(0, 11), ha="center")
ax.axvline(6.5, color="black", ls="--", lw=1.2)
ax.text(6.6, 0.5, "Grenze zwischen 6 und 7 Käufen", va="center", fontsize=9)
for _, r in n.iterrows():
    ax.axvline(r.kaeufe, color=NEU, lw=1, ls=":")
    ax.text(r.kaeufe, 1.28, r.kunde, ha="center", color=NEU, fontweight="bold")
ax.set_yticks([0, 1]); ax.set_yticklabels(["nein", "ja"]); ax.set_ylim(-0.35, 1.45)
ax.set_xlabel("Käufe in 12 Monaten"); ax.set_ylabel("Premium gekauft?")
ax.set_title("Alle Premium-Käufer haben 7 oder mehr Käufe, alle anderen 6 oder weniger")
ax.legend(loc="center left", bbox_to_anchor=(0.0, 0.62)); plt.tight_layout(); plt.show()

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage:** Die Regel "ab 7 Käufen Premium" sortiert alle 8 bekannten Kunden richtig. N1 (8) und N4 (12) liegen klar darüber,
# N2 (3) klar darunter. **N3 steht mit 6 Käufen direkt an der Grenze** und ist ein Münzwurf mit leichter Tendenz zu nein.
#
# </div>

# %%
# >>> HIER PASSIERT DIE VORHERSAGE: eine feste Schwelle auf einem Merkmal, mehr ist die Regel nicht
n["premium_regel"] = np.where(n.kaeufe >= 7, "ja", "nein")
n[["kunde", "kaeufe", "premium_regel"]]

# %% [markdown]
# **Gegenprobe: trifft die Regel die bekannten Kunden?** (Das beweist nichts über neue Kunden, es zeigt nur, dass die Regel zu den 8 Punkten passt.)

# %%
trefferquote = ((d.kaeufe >= 7).astype(int) == d.premium).mean()
print(f"Regel 'ab 7 Käufen' trifft {trefferquote:.0%} der bekannten Kunden")
print(d.groupby("premium").kaeufe.agg(["min", "mean", "max"]).rename(index={0: "nein", 1: "ja"}))

# %% [markdown]
# ## 3 Frage 2: Wie viel Umsatz?
#
# Wieder jeder Punkt ein bisheriger Kunde: nach rechts die Käufe, nach oben der Umsatz im Folgejahr.
# Farbe zeigt, ob der Kunde Premium gekauft hat. Man sieht: **mehr Käufe, mehr Umsatz**, ungefähr auf einer Geraden.

# %%
fig, ax = plt.subplots(figsize=(9, 5))
for wert, farbe, name in [(1, JA, "Premium"), (0, NEIN, "kein Premium")]:
    x = d[d.premium == wert]
    ax.scatter(x.kaeufe, x.umsatz, s=110, color=farbe, label=name, zorder=3)
for _, r in d.iterrows():
    ax.annotate(r.kunde, (r.kaeufe, r.umsatz), textcoords="offset points", xytext=(7, 6))
ax.set_xlabel("Käufe in 12 Monaten"); ax.set_ylabel("Umsatz im Folgejahr (€)")
ax.set_title("Bekannte Kunden: mehr Käufe, mehr Umsatz"); ax.legend(); plt.tight_layout(); plt.show()

# %% [markdown]
# ### Die Gerade (einfache lineare Regression)
#
# Gesucht ist die Gerade `Umsatz = a + b × Käufe`, die möglichst nah an allen acht Punkten liegt.
# "Möglichst nah" heißt: die Summe der **quadrierten senkrechten Abstände** zwischen Punkt und Gerade soll am kleinsten sein.
# Für eine Gerade gibt es dafür eine fertige Formel.

# %%
# >>> HIER PASSIERT DAS LERNEN: die Gerade wird an die 8 Punkte angepasst (kleinste Fehlerquadrate)
b, a = np.polyfit(d.kaeufe, d.umsatz, 1)
print(f"Umsatz ≈ {a:.0f} € + {b:.0f} € × Käufe")

# Gleiches von Hand nachgerechnet, damit klar ist, dass da keine Magie drinsteckt:
mx, my = d.kaeufe.mean(), d.umsatz.mean()
b_hand = ((d.kaeufe - mx) * (d.umsatz - my)).sum() / ((d.kaeufe - mx) ** 2).sum()
a_hand = my - b_hand * mx
print(f"von Hand: Steigung {b_hand:.1f}, Achsenabschnitt {a_hand:.1f}   (Mittelwerte: {mx:.2f} Käufe, {my:.1f} €)")

# %% [markdown]
# **Wie lesen?** Jeder zusätzliche Kauf geht im Schnitt mit rund 114 € mehr Umsatz einher. Wer 0 Käufe hätte, läge rechnerisch bei 102 €.
# Der zweite Wert ist eine Rechenhilfe, kein echter Kunde.

# %% [markdown]
# ### Wie weit liegen die echten Kunden von der Geraden entfernt?
#
# Diese Abstände sind der Fehler der Geraden. Ihre Streuung ist die ehrliche Spanne für die Prognose.

# %%
d["gerade"] = a + b * d.kaeufe
d["abstand"] = d.umsatz - d.gerade
streuung = d.abstand.std(ddof=2)   # ddof=2: zwei Zahlen (a, b) wurden aus den Daten geschätzt
print(f"Streuung um die Gerade: {streuung:.0f} €")

fig, ax = plt.subplots(figsize=(9, 3.6))
farben = [JA if p else NEIN for p in d.premium]
ax.bar(d.kunde, d.abstand, color=farben)
ax.axhline(0, color="black", lw=1)
ax.axhline(streuung, color="gray", ls="--"); ax.axhline(-streuung, color="gray", ls="--")
ax.text(7.4, streuung + 25, f"± {streuung:.0f} €", ha="right", color="gray")
ax.set_ylabel("Umsatz minus Gerade (€)"); ax.set_title("Abstand der echten Kunden von der Geraden (D und C liegen weit daneben)")
plt.tight_layout(); plt.show()
d[["kunde", "kaeufe", "umsatz", "gerade", "abstand"]].round(0)

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage:** Die Gerade liegt im Schnitt rund **± 400 €** daneben. Bei einem Umsatz von 100 bis 1.600 € ist das viel.
# **D** (5.500 € Einkommen) liegt ca. 740 € über der Geraden, **C** (2.100 € Einkommen) ca. 480 € darunter.
# Das Einkommen steckt nicht in der Geraden. Genau da fehlt das, was die Streuung erklären könnte.
#
# </div>

# %% [markdown]
# ## 4 Die Prognose für die neuen Kunden
#
# Erst die reine Rechnung (die Gerade), dann meine Anpassung von Hand. Beides getrennt, damit sichtbar ist, was Rechnung und was Urteil ist.

# %%
# >>> HIER PASSIERT DIE PROGNOSE: die gelernte Gerade wird auf neue Käufe angewendet
n["gerade"] = a + b * n.kaeufe
anpassung = {"N1": 0, "N2": 0, "N3": -85, "N4": -470}   # mein Urteil, nicht berechnet (Begründung im .md)
n["schaetzung"] = n.gerade + n.kunde.map(anpassung)
n["schaetzung_gerundet"] = (n.schaetzung / 50).round() * 50
n[["kunde", "kaeufe", "gerade", "schaetzung", "schaetzung_gerundet"]].round(0)

# %%
fig, ax = plt.subplots(figsize=(9.5, 5.5))
xs = np.linspace(0, 13, 100)
ax.fill_between(xs, a + b * xs - streuung, a + b * xs + streuung, color=JA, alpha=0.12, label=f"± {streuung:.0f} € Streuung")
ax.plot(xs, a + b * xs, color=JA, lw=2, label=f"Gerade: {a:.0f} € + {b:.0f} € × Käufe")
for wert, farbe, name in [(1, JA, "bekannt, Premium"), (0, NEIN, "bekannt, kein Premium")]:
    x = d[d.premium == wert]
    ax.scatter(x.kaeufe, x.umsatz, s=90, color=farbe, label=name, zorder=3)
    for _, r in x.iterrows():
        ax.annotate(r.kunde, (r.kaeufe, r.umsatz), textcoords="offset points", xytext=(6, 5), fontsize=9)
ax.scatter(n.kaeufe, n.gerade, s=140, facecolors="none", edgecolors=NEU, linewidths=2, label="neu: Wert auf der Geraden", zorder=4)
for _, r in n.iterrows():
    ax.annotate(r.kunde, (r.kaeufe, r.gerade), textcoords="offset points", xytext=(-4, -17), color=NEU, fontweight="bold", ha="right")
    if r.kunde in ("N3", "N4"):   # Handanpassung als Pfeil
        ax.annotate("", xy=(r.kaeufe, r.schaetzung), xytext=(r.kaeufe, r.gerade),
                    arrowprops=dict(arrowstyle="->", color="black", lw=1.5), zorder=5)
ax.scatter(n.kaeufe, n.schaetzung, s=70, marker="D", color="black", label="meine Schätzung (N3, N4 von Hand angepasst)", zorder=5)
ax.set_xlim(0, 13); ax.set_ylim(-100, 2000)
ax.set_xlabel("Käufe in 12 Monaten"); ax.set_ylabel("Umsatz im Folgejahr (€)")
ax.set_title("Prognose: Gerade (Rechnung) und meine Schätzung (Rechnung plus Urteil)")
ax.legend(loc="upper left", fontsize=8.5); plt.tight_layout(); plt.show()

# %% [markdown]
# <div style="border: 2px solid teal; border-radius: 8px; padding: 0.3em 1em; margin: 0.6em 0;">
#
# **Kernaussage:** Die Rauten sind meine Schätzung, die Ringe das, was die Gerade allein ergibt. Bei **N1 und N2** sind sie fast gleich.
# Bei **N3** (kleiner Pfeil) habe ich etwas abgezogen, weil ich bei Premium eher auf nein tippe. Bei **N4** (langer Pfeil) deutlich mehr:
# der nächste bekannte Kunde C (11 Käufe) machte nur 870 €. Das ist **Urteil, keine Rechnung**, und der größte Eingriff in der ganzen Aufgabe.
# Das blaue Band ist die ehrliche Unsicherheit: bei acht Kunden liegt jede Zahl rund ± 400 € daneben.
#
# </div>

# %% [markdown]
# ## 5 Warum ich N4 von Hand angepasst habe: das Einkommen
#
# Links: Einkommen gegen Käufe. Rechts: Einkommen gegen den Abstand zur Geraden. Wenn das Einkommen den Fehler erklärt, sollten die Punkte rechts auf einer Linie liegen.

# %%
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(11, 4))
for wert, farbe, name in [(1, JA, "Premium"), (0, NEIN, "kein Premium")]:
    x = d[d.premium == wert]
    ax1.scatter(x.eink, x.kaeufe, s=90, color=farbe, label=name, zorder=3)
    for _, r in x.iterrows():
        ax1.annotate(r.kunde, (r.eink, r.kaeufe), textcoords="offset points", xytext=(6, 5))
ax1.scatter(n.eink, n.kaeufe, s=120, facecolors="none", edgecolors=NEU, linewidths=2, label="neu")
for _, r in n.iterrows():
    ax1.annotate(r.kunde, (r.eink, r.kaeufe), textcoords="offset points", xytext=(6, -14), color=NEU)
ax1.set_xlabel("Einkommen pro Monat (€)"); ax1.set_ylabel("Käufe in 12 Monaten")
ax1.set_title("Einkommen trennt Premium nicht"); ax1.legend(fontsize=8)

ax2.scatter(d.eink, d.abstand, s=90, color=farben, zorder=3)
for _, r in d.iterrows():
    ax2.annotate(r.kunde, (r.eink, r.abstand), textcoords="offset points", xytext=(6, 5))
ax2.axhline(0, color="black", lw=1)
ax2.axvline(6100, color=NEU, ls=":"); ax2.text(6050, ax2.get_ylim()[0] * 0.9, "N2: 6.100 €\n(außerhalb)", ha="right", color=NEU, fontsize=9)
ax2.set_xlabel("Einkommen pro Monat (€)"); ax2.set_ylabel("Abstand zur Geraden (€)")
ax2.set_title("Höheres Einkommen, eher über der Geraden"); plt.tight_layout(); plt.show()
print("Korrelation Einkommen und Abstand:", round(d.eink.corr(d.abstand), 2))

# %% [markdown]
# **Was man sieht:** Premium ist beim Einkommen nicht getrennt (links), das Einkommen ist für ja/nein unwichtig.
# Beim Umsatz gibt es einen Zusammenhang (rechts): wer mehr verdient, liegt eher über der Geraden. Mit nur 8 Punkten bleibt das eine
# Vermutung, und N2 (6.100 €) liegt **außerhalb** des bekannten Bereichs (1.700 bis 5.500 €). Dort wäre jede Aussage Extrapolation.
#
# ## 6 Gesamtbild
#
# | Frage | Ergebnis | Methode |
# |---|---|---|
# | Premium ja/nein | N1 ja, N2 nein, N3 unsicher (Tendenz nein), N4 ja | Schwelle bei 7 Käufen |
# | Umsatz | N1 ca. 1.000 €, N2 ca. 450 €, N3 ca. 700 €, N4 ca. 1.000 € | Gerade aus Käufen, N3 und N4 von Hand angepasst |
# | Wie sicher | ± 400 € | Streuung der acht Kunden um die Gerade |
#
# **Nicht vergessen:** Der Umsatz steht *nach* dem Premium-Kauf. Dass Premium-Käufer im Schnitt 1.285 € gegen 340 € machen,
# heißt nicht, dass Premium diese 945 € bringt. Häufigkäufer kaufen vermutlich Premium *und* viel, die Mitgliedschaft selbst kann
# zusätzlich Käufe auslösen. Die acht Datenpunkte trennen das nicht.
