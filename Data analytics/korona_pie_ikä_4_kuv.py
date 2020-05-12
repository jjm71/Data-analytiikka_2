# Ympyrädiagrammi 4 tiedostosta (määrät tulostettuna) Koronatilanne ikäryhmittäin
# JJM 29.4.2020
# Päivitetty 30.4.2020
import pandas as pd
import matplotlib.pyplot as plt

headers = ["c1", "c2"]

df = pd.read_csv("fact_epirapo_covid19case_16.csv", encoding="utf-8", skiprows=1, skipfooter=1, names=headers, delimiter= ";", engine='python')
df_2 = pd.read_csv("fact_epirapo_covid19case_17.csv", encoding="utf-8", skiprows=1, skipfooter=1, names=headers, delimiter= ";", engine='python')
df_3 = pd.read_csv("fact_epirapo_covid19case_18.csv", encoding="utf-8", skiprows=1, skipfooter=1, names=headers, delimiter= ";", engine='python')
df_4 = pd.read_csv("fact_epirapo_covid19case_19.csv", encoding="utf-8", skiprows=1, skipfooter=1, names=headers, delimiter= ";", engine='python')

plt.figure(figsize=(12,10))
 
ax = plt.subplot(221)

plt.title('Vk 16', bbox={'facecolor':'0.8', 'pad':1, 'boxstyle':'round'}, position=(0,1))
ax.pie(df['c2'], labels=df['c1'], autopct='%1.1f%%', shadow=True, startangle=0, radius=1.3, pctdistance=0.85)

ax = plt.subplot(222)
plt.title('Vk 17', bbox={'facecolor':'0.8', 'pad':1, 'boxstyle':'round'}, position=(0,1))
ax.pie(df_2['c2'], labels=df_2['c1'], autopct='%1.1f%%', shadow=True, radius=1.3, pctdistance=0.85)

ax = plt.subplot(223)
plt.title('Vk 18', bbox={'facecolor':'0.8', 'pad':1, 'boxstyle':'round'}, position=(0,1))
ax.pie(df_3['c2'], labels=df_3['c1'], autopct='%1.1f%%', shadow=True, startangle=355, radius=1.3, pctdistance=0.85)

ax = plt.subplot(224)
plt.title('Vk 19', bbox={'facecolor':'0.8', 'pad':1, 'boxstyle':'round'}, position=(0,1))
ax.pie(df_4['c2'], labels=df_4['c1'], autopct='%1.1f%%',  shadow=True, startangle=355, radius=1.3, pctdistance=0.85)

plt.savefig("Koronatartunnat_ikä_pie_4.png", bbox_inches="tight")       # Tallentaa diagrammin kuvana

plt.show()
