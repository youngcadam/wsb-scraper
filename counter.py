import pandas as pd
import numpy as np

# import list of symbols
symbols = pd.read_csv('./data/sec.txt', sep='	', header = None)
symbols = list(symbols[0])
symbols = {i : 0 for i in symbols}


f = open('./data/daily_plays.txt').read().split()
for word in f:
	if word in symbols:
		symbols[word] += 1

symbols = np.array([list(symbols.keys()), list(symbols.values())])
symbols = pd.DataFrame(data=symbols).T
symbols.columns = ['symbol', 'count']
# counts = np.array(symbols['count'].to_numpy())
symbols['count'] = pd.to_numeric(symbols['count'])
print(symbols.sort_values(by=['count'], ascending=False))
nonzero_index = np.nonzero(symbols['count'].to_numpy())
nonzero_index = np.tolist(nonzero_index)
print(nonzero_index)
# print(np.nonzero(symbols['count'].to_numpy()))
print(symbols[nonzero_index])
