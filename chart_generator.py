import yfinance as yf
import plotly.graph_objects as go
import pandas


#-----USER INPUT:

print("- - - - - - - - - - - - - - - - - - - - - - - - - \n")
print("\n *  *  Welcome to the Candlestick Chart Generator!  *  *  \n") 
print("Please input a cryptocurrency symbol of your choice to generate a candlestick chart:")
crypto = input("Type only the symbol in full here: ")
print("\n - - - - - - - - - - - - - - - - - - - - - - - - - \n")


#-----DATA AQUISITION (from Yahoo Finance)
SYMB = "{}-USD".format(crypto)
PERIOD = "max"

file = open("crypto.csv", 'w')
crypto_ticker = yf.Ticker(SYMB)
history = crypto_ticker.history(period="max")
file.write(history.to_csv())
file.close()


#-----CHART GENERATOR (from Yahoo Finance)
df = pandas.read_csv('crypto.csv')

fig = go.Figure(data=[go.Candlestick(x=df['Date'],
                open=df['Open'], 
                high=df['High'], 
                low=df['Low'],
                close=df['Close'])])

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
)

fig.show()