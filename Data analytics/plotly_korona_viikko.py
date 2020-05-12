# Plotly HTML Bar. Koronatapaukset viikoittain
# JJM 1.5.2020
# Päivitetty 5.5.2020

from plotly.offline import plot   # Tämä tarvitaan offline näyttöön plot(fig)
import plotly.graph_objects as go
import pandas as pd

headers = ["c1", "c2", "c3"]
df = pd.read_csv("fact_epirapo_covid19case_viikko_ud.csv", encoding='utf-8', skiprows=1 , names=headers, skipfooter=22, delimiter= ";", engine='python')  # Helsinki

df = df.query('(c1 == "Kaikki Alueet") & (c3 > 0)')

bar_plots = [
    go.Bar(x=df['c2'], y=df['c3'], name='2014', marker=go.bar.Marker(color='magenta'))  
    ]

layout = go.Layout(
    title=go.layout.Title(text="Koronatapaukset viikoittain ", x=0.5),
    yaxis_title="Henkilöä"
    )

fig = go.Figure(data=bar_plots, layout=layout) 

plot(fig)
#fig.show()


