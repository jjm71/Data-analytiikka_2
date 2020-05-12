# 4 pylväs diagrammia 4 eri tiedostosta (määrät tulostettuna) Koronatilanne sairaanhoitopiireittäin
# JJM 23.4.2020
# Päivitetty 6.5.2020
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = ["c1", "c2"]
headers_2 = ["c1", "c3"]
headers_3 = ["c1", "c4"]
headers_4 = ["c1", "c5"]

df_old = pd.read_csv("fact_epirapo_covid19case_2_16.csv", encoding="utf-8", skiprows=1, names=headers, delimiter= ";")  
df_new = pd.read_csv("fact_epirapo_covid19case_2_17.csv", encoding="utf-8", skiprows=1, names=headers_2, delimiter= ";") 
df_newest = pd.read_csv("fact_epirapo_covid19case_2_18.csv", encoding="utf-8", skiprows=1, names=headers_3, delimiter= ";") 
df_newest_2 = pd.read_csv("fact_epirapo_covid19case_2_19.csv", encoding="utf-8", skiprows=1, names=headers_4, delimiter= ";") 

yhd = pd.concat([df_old, df_new['c3'], df_newest['c4'], df_newest_2['c5']], axis=1) # join='inner' # Muodostaa yhden listan jossa kaikki määrät vierekkäin (sarakkeittain)

yhd = yhd.sort_values('c5', ascending = True)  # Laittaa järjestykseen sarakkeen 'c5' (määrän) perusteella # .reset_index(drop=True)

plt.figure(figsize=(14,6))
names = yhd['c1']
x = np.arange(len(names))
w = 0.2
ax = plt.subplot()

plt.bar(x-w-w, yhd['c2'], width=w, label='Vk 16', align='edge')
plt.bar(x-w, yhd['c3'], width=w, label='Vk 17', align='edge')
plt.bar(x, yhd['c4'], width=w, label='Vk 18', align='edge')
plt.bar(x+w, yhd['c5'], width=w, label='Vk 19', align='edge')

plt.grid(axis='y', linewidth=1, linestyle='dotted')    # grid viivat
plt.xticks(x, names, rotation=25, ha='right')   # X-akselin teksti ja asettelu
plt.ylabel('Henkilöä')     # Y-akselin teksti
plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.15), fancybox=True, ncol=5) # Palkkien selitys asettelu                   
plt.title('Koronan tartuntojen kehitys sairaanhoitopiireittäin')    # Otsikkorivi
plt.tight_layout()

ax.axhline(y=100, alpha=0.4, linestyle='dotted', color='#ff0000')  # 'Target' viiva
ax.text(-1.95,100,'100', color='#ff0000')    # INFO teksti

aa = 3
for i in ax.patches:
    height = i.get_height()
    if height >= 100:                # Määrä >= 100. Tulostaa punaisella.
        ax.annotate('{}'.format(height),
        xy=(i.get_x() + i.get_width() / 2, height),
        xytext=(0, aa),  # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom', rotation=80, color='#ff0000')
        aa += 0.3
    else:
        ax.annotate('{}'.format(height),
        xy=(i.get_x() + i.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom', rotation=70)

plt.savefig("Koronatartunnat.png", bbox_inches="tight")       # Tallentaa diagrammin kuvana
    
plt.show()



