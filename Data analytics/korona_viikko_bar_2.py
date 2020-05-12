# Pylväs diagrammi 1 tiedostosta. Koronatapaukset viikoittain.
# JJM 5.5.2020
# Päivitetty 6.5.2020
import pandas as pd
import matplotlib.pyplot as plt

headers = ["c1", "c2", "c3"]
#df = pd.read_csv("fact_epirapo_covid19case_viikko.csv", encoding='utf-8', skiprows=1, names=headers, skipfooter=22, delimiter= ";", engine='python')  # Helsinki
df = pd.read_csv("fact_epirapo_covid19case_viikko_ud.csv", encoding='utf-8', skiprows=1, names=headers, delimiter= ";")  # Helsinki

df = df.query('(c1 == "Kaikki Alueet") & (c3 > 0) & (c3 < 2000)')   # Valitaan tekstistä vain nämä rivit jotka täyttää tämän ehdon

plt.figure(figsize=(15,5))      # Kuvan koko

plt.bar(df.c2, df.c3, color='red', alpha=0.5)         # Pylväiden piirto

plt.grid(axis='y', linewidth=1, linestyle='dotted')   # Grid viiva
plt.xticks(rotation=25, ha='right')               # X-akselin tekstin asettelu
plt.legend(['2020'])                 # Pylväiden selitykset
plt.ylabel('HENKILÖÄ')               # Y-akselin selitys
plt.title('Koronatartunnat viikoittain')          # Otsikko
plt.axhline(y=500, alpha=0.3, linestyle='dotted', color='#ff0000')       # 'Target' viiva 
plt.tight_layout()               # 'Suppeampi tulostus'

posx = 0
indrow = 0
for i in range(0, len(df)):
    luku = df.iloc[indrow,2]   # laittaa tiedostosta sarakkeen 'c3' luvun muuttujaan rivi kerrallaan
    plt.text(posx,luku + 15, int(luku), ha='center')    # Tulostaa määrän palkin yläpuolelle kokonaislukuna
    posx += 1
    indrow += 1

plt.show()
