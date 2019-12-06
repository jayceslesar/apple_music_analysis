import pandas as pd
import plotly.graph_objs as go
import plotly.io as pio
import plotly.express as px
pio.renderers.default = "browser"

df = pd.read_csv(r'D:\apple_music_data\test.csv')
fig = px.bar(df, x='date_described', y='plays',
             hover_data=['name', 'artist'], color='date_described',
             labels={'date_described': 'date', 'plays': 'plays'}, height=400)

fig.show()
