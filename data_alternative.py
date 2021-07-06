import requests, json, csv

#-----INSERT SANDBOX TOKEN (eg: Tpk... , Tsk...)
TOKEN = 'Tpk_5c4481a7985d4e2da0702757175f0fcf'

#-----INSERT STOCK SYMBOL (TSLA, MSFT, APPL, etc)
SYMB = 'TWTR'

URL = 'https://sandbox.iexapis.com/stable/stock/{}/chart/ytd?token={}'.format(SYMB, TOKEN)
req = requests.get(URL)
json_data = json.loads(req.content)

file = open('twtr.csv', 'w')
write = csv.writer(file)
write.writerow(['date', 'open', 'high', 'low', 'close'])

for item in json_data:
    print(item)
    write.writerow([item['date'], item['open'], item['high'], item['low'], item['close']])

file.close()

#note: SANDBOX use only