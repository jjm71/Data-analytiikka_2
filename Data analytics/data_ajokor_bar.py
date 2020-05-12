# 4 kuvaajaa yhdestä tiedostosta (nimen perusteella)
# JJM 24.4.2020
# Päivitetty 29.4.2020
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

headers = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12"]
df = pd.read_csv("ajoktyyp.csv", encoding='latin1', skiprows=3, names=headers, delimiter= ";") 

#pd.set_option('display.max_columns', None)
#pd.set_option('display.width', 200)

plt.figure(figsize=(14,8))    # kuvaajan koko
#------------------------------------------------------
kaupunki = 'Oulu'   ###### HOX !!!!! Tähän valittu kaupunki !!!
#-----------------------------------------------------
arvot_2016 = df.loc[df.c1 == kaupunki]['c8']     # Valittu kaupunki ja vuosi
arvot_2017 = df.loc[df.c1 == kaupunki]['c9']
arvot_2018 = df.loc[df.c1 == kaupunki]['c10']
arvot_2019 = df.loc[df.c1 == kaupunki]['c11']

print(arvot_2019)
name = df['c5']        # Selitys 'sarake' valittu muuttujaan

x = np.arange(len(arvot_2016))      # valitun 'listan' pituus
w = 0.2             # Pylvään leveys
ax = plt.subplot()  # Tämä tarvitaan lukujen näyttämiseen

plt.bar(x-w-w, arvot_2016, width=w, align='edge')  # 2016
plt.bar(x-w, arvot_2017, width=w, align='edge')   # 2017
plt.bar(x, arvot_2018, width=w, align='edge')   # 2018
plt.bar(x+w, arvot_2019, width=w, align='edge')   # 2019

plt.xticks(x, name, rotation=25, ha='right')    # X-akselin selitys ja asettelu 
plt.grid(axis='y', linewidth=1, linestyle='dotted')    # grid viivat
plt.legend(['2016', '2017', '2018', '2019'])      # pylväiden selitykset
plt.ylabel('HENKILÖÄ')                          # Y-akselin selitys
plt.title('Toimitetut ajokortit koontiluokittain ' + kaupunki)    # otsikkorivi
plt.tight_layout()

for i in ax.patches:
    height = i.get_height()
    if height >= 5000:                # Määrä >= 5000. Tulostaa punaisella.
        ax.annotate('{}'.format(height),
        xy=(i.get_x() + i.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom', rotation=80, color='#ff0000')
        
    else:
        ax.annotate('{}'.format(height),
        xy=(i.get_x() + i.get_width() / 2, height),
        xytext=(0, 3),  # 3 points vertical offset
        textcoords="offset points",
        ha='center', va='bottom', rotation=80)

plt.savefig("Ajokortit koontiluokittain.png", bbox_inches="tight")       # Tallentaa diagrammin kuvana

plt.show()
