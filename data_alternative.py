import requests, json, csv

#NOTE: SANDBOX IEXCLOUD.IO API use only

#-----INSERT SANDBOX IEXCLOUD.IO TOKEN (eg: Tpk... , Tsk...)
TOKEN = '-'

#-----INSERT STOCK SYMBOL (TSLA, MSFT, APPL, etc)
SYMB = '-'

URL = 'https://sandbox.iexapis.com/stable/stock/{}/chart/ytd?token={}'.format(SYMB, TOKEN)
req = requests.get(URL)
json_data = json.loads(req.content)

file = open('stock.csv', 'w')
write = csv.writer(file)
write.writerow(['date', 'open', 'high', 'low', 'close'])

for item in json_data:
    print(item)
    write.writerow([item['date'], item['open'], item['high'], item['low'], item['close']])

file.close()
