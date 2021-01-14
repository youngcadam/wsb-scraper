import pandas as pd
import numpy as np
import re

# load list of stock tickers
symbols = open('./data/tickers.txt').read().split()
symbols = {str(i) : 0 for i in symbols}

# load comments
f = open('./data/daily_plays.txt').read()
f = re.split('[^a-zA-Z0-9]+', f)

# store occurrences of each ticker symbol into a DataFrame
for word in f:
	if word in symbols:
		symbols[word] += 1

symbols = np.array([list(symbols.keys()), list(symbols.values())])
symbols = pd.DataFrame(data=symbols).T
symbols.columns = ['symbol', 'count']
symbols['count'] = pd.to_numeric(symbols['count'])

# print nonzero symbols by value in descending order 
nonzero_index = np.nonzero(symbols['count'].to_numpy())
print(symbols.loc[nonzero_index].sort_values(by=['count'], ascending=False))
