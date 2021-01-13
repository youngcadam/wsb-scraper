import pandas as pd
import numpy as np

# import list of symbols
symbols = pd.read_csv('sec.txt', sep='	', header = None)
symbols = list(symbols[0])
symbols = {i : 0 for i in symbols}


f = open('comments.txt').read().split()
for word in f:
	if word in symbols:
		symbols[word] += 1

symbols = np.array([list(symbols.keys()), list(symbols.values())])
symbols = pd.DataFrame(data=symbols).T
symbols.columns = ['symbol', 'count']

print(symbols['count'])