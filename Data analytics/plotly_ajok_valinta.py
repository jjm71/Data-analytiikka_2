# Plotly HTML Bar valinta
# JJM 1.5.2020

from plotly.offline import plot   # Tämä tarvitaan offline näyttöön plot(fig)
import plotly.graph_objects as go
import pandas as pd

headers = ["c1", "c2", "c3", "c4", "c5", "c6", "c7", "c8", "c9", "c10", "c11", "c12"]
df = pd.read_csv("ajoktyyp.csv", encoding="latin1", skiprows=3, names=headers, delimiter= ";")  # Helsinki

##################################
kaupunki = 'Oulu'
#################################
xx = df.loc[df.c1 == kaupunki]['c5']  # teksti
y2014 = df.loc[df.c1 == kaupunki]['c6']  # määrä
y2015 = df.loc[df.c1 == kaupunki]['c7']  #
y2016 = df.loc[df.c1 == kaupunki]['c8']  #
y2017 = df.loc[df.c1 == kaupunki]['c9']  #
y2018 = df.loc[df.c1 == kaupunki]['c10']  #
y2019 = df.loc[df.c1 == kaupunki]['c11']  #

bar_plots = [
    go.Bar(x=xx, y=y2014, name='2014', marker=go.bar.Marker(color='black')),
    go.Bar(x=xx, y=y2015, name='2015', marker=go.bar.Marker(color='orange')),
    go.Bar(x=xx, y=y2016, name='2016', marker=go.bar.Marker(color='green')),
    go.Bar(x=xx, y=y2017, name='2017', marker=go.bar.Marker(color='#0343ff')),
    go.Bar(x=xx, y=y2018, name='2018', marker=go.bar.Marker(color='#e50000')),
    go.Bar(x=xx, y=y2019, name='2019', marker=go.bar.Marker(color='#929591'))
    ]

layout = go.Layout(
    title=go.layout.Title(text="Toimitetut ajokortit koontiluokittain " + kaupunki, x=0.5),
    yaxis_title="Henkilöä"
    )

fig = go.Figure(data=bar_plots, layout=layout) 

plot(fig)
#fig.show()


