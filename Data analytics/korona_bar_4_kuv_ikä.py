# 4 pylväs diagrammia 4 eri tiedostosta (määrät tulostettuna) Koronatilanne ikäryhmittäin
# JJM 23.4.2020
# Päivitetty 29.4.2020
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = ["c1", "c2"]

df_old = pd.read_csv("fact_epirapo_covid19case_16.csv", encoding="utf-8", skiprows=1, names=headers, delimiter= ";")  # ennen
df_new = pd.read_csv("fact_epirapo_covid19case_17.csv", encoding="utf-8", skiprows=1, names=headers, delimiter= ";") # nyt
df_newest = pd.read_csv("fact_epirapo_covid19case_18.csv", encoding="utf-8", skiprows=1, names=headers, delimiter= ";") # nyt
df_newest_2 = pd.read_csv("fact_epirapo_covid19case_19.csv", encoding="utf-8", skiprows=1, names=headers, delimiter= ";") # nyt

#pd.set_option('display.max_columns', None)  # Printtauksen asetuksia
#pd.set_option('display.width', 200)         # Printtauksen asetuksia
print(df_newest_2)
plt.figure(figsize=(12,7))
names = df_old['c1']
x = np.arange(len(names))
w = 0.2
ax = plt.subplot()

plt.bar(x-w-w, df_old['c2'], width=w, align='edge')
plt.bar(x-w, df_new['c2'], width=w, align='edge')
plt.bar(x, df_newest['c2'], width=w, align='edge')
plt.bar(x+w, df_newest_2['c2'], width=w, align='edge')

plt.grid(axis='y', linewidth=1, linestyle='dotted')    # grid viivat
plt.xticks(x, names, rotation=10, ha='right')   # X-kuvaajan tekstin kirjoitus ja 
plt.ylabel('Henkilöä')        # Y-kuvaajan selitys
plt.xlabel('Ikäryhmät')      # X-kuvaajan selitys
#plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, ncol=5)     # Pylväiden selitykset 
plt.legend(['Vk 16', 'Vk 17', 'Vk 18', 'Vk 19'])        # Pylväiden selitykset                        
plt.title('Koronan tartuntojen kehitys ikäryhmittäin')    # Otsikkorivi
plt.tight_layout()

ax.axhline(y=500, alpha=0.3, linestyle='dotted', color='#ff0000')       # 'Target' viiva
#ax.annotate('500', xy=(-0.8,550), color='#ff0000')       # INFO teksti
ax.text(-1.1,500,'500', color='#ff0000')    # INFO teksti

for i in ax.patches:
    height = i.get_height()
    if height >= 500:                # Määrä >= 500. Tulostaa punaisella.
        ax.annotate('{}'.format(height),
        xy=(i.get_x() + i.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom', rotation=70, color='#ff0000')
    
    else:
        ax.annotate('{}'.format(height),
        xy=(i.get_x() + i.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom', rotation=70)

plt.savefig("Koronatartunnat_ikä.png", bbox_inches="tight")       # Tallentaa diagrammin kuvana
    
plt.show()



