import plotly.graph_objects as go
from data import SYMB 
import pandas

df = pandas.read_csv('crypto.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'], 
                high=df['High'], 
                low=df['Low'],
                close=df['Close'])])


lines = [
    dict(x0='2020-12-25', x1='2020-12-25', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2021-01-28', x1='2021-01-28', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2021-02-04', x1='2021-02-04', y0=0, y1=1, xref='x', yref='paper'),
    dict(x0='2021-04-15', x1='2021-04-15', y0=0, y1=1, xref='x', yref='paper')
]

annotate = [
    dict(x='2020-12-25', y=0.15, xref='x', yref='paper', showarrow=False, xanchor='left', text='Musk Tweets (One Word: Dogecoin)'),
    dict(x='2021-01-28', y=0.25, xref='x', yref='paper', showarrow=False, xanchor='left', text='Musk Tweets Picture of Dogecoin'),
    dict(x='2021-02-04', y=0.35, xref='x', yref='paper', showarrow=False, xanchor='left', text='Musk Tweets Doge Rocket Ship'),
    dict(x='2021-04-15', y=0.10, xref='x', yref='paper', showarrow=False, xanchor='left', text='Musk Tweets Barking at the Moon')

]

#fig.update_layout(title = '{} Graph Plot'.format(SYMB), annotations=annotate, shapes=lines)


fig.update_layout(
    title = {
        'text': '{} Graph Plot'.format(SYMB),
        'font_size': 40,
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title = "Time",
    yaxis_title = 'Value in USD',
    annotations=annotate, 
    shapes=lines,
    font = dict(
        family = "Raleway, monospace",
        size = 15,
        color="Black"
    ) 
)


fig.write_html('crypto.html', auto_open=True)
fig.show()
