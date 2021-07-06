import yfinance as yf

#-----INSERT CRYPTO SYMBOL (BTC-USD, ETH-USD, ...)
SYMB = "DOGE-USD"

#-----INSERT VALID PERIOD (1d, 5d, 1mo, 3mo, 6mo, 1y, 2y, 5y, 10y, ytd, max)
PERIOD = "max"

crypto = yf.Ticker("{}".format(SYMB))
history = crypto.history(period="{}".format(PERIOD))

print(history.to_csv())

#-----within the command line, redirect output to a csv file:
#     'python3 yahoo.py > crypto.csv'