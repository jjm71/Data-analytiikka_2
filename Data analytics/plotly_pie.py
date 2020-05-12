# Plotly HTML Pie 
# JJM 2.5.2020

from plotly.offline import plot   # Tämä tarvitaan offline näyttöön plot(fig)
import pandas as pd
import plotly.express as px

headers = ["c1", "c2"]

df = pd.read_csv("fact_epirapo_covid19case_19.csv", encoding="utf-8", skiprows=1, skipfooter=1, names=headers, delimiter= ";", engine='python')

fig = px.pie(df, values='c2', names='c1', title='Koronatartunnat ikäryhmittäin Vk 19',
             hover_data=['c1','c2'], labels={'c1':'Ikäryhmä','c2':'Henkilöä'})

fig.update_traces(textposition='inside', textinfo='percent+label') # Lisä infoa 
fig.update_layout(uniformtext_minsize=12)   # Muuttaa fontin kokoa

fig.show()
plot(fig)
#fig.show()


