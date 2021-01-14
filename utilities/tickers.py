# sript to parse SEC company ticker JSON file 
# Adam Young © 2021 (youngcadam@ucla.edu)

import json
import requests
import os

# get updates list of stock tickers from sec.gov
url = 'https://www.sec.gov/files/company_tickers.json'
r = requests.get(url, allow_redirects=True)
open('../data/company_tickers.json', 'wb').write(r.content)

# store tickers in list
symbols = []
with open('../data/company_tickers.json') as json_file:
    data = json.load(json_file)
    
    for i in range(11227):
    	symbols.append(data[f'{i}']['ticker'])

# store formatted tickerfs in txt file
f = open('../data/tickers.txt', 'w')
for x in symbols:
	f.write("%s\n" %x)
f.close()


# remove JSON file after we finish formatting
if os.path.exists('../data/company_tickers.json'):
  os.remove('../data/company_tickers.json')


