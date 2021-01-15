import pandas as pd
import numpy as np
import re
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument('-g', '--graph', help='select graph to plot')
parser.add_argument('-n', '--name', help='name of file from ./data/ to parse')
args = parser.parse_args()

# load list of stock tickers
symbols = open('./data/tickers.txt').read().split()
symbols = {str(i) : 0 for i in symbols}

# load comments
if args.name:
	name = args.name
else:
	name = 'sample.txt'

f = open(f'./data/{name}').read()
f = re.split('[^a-zA-Z0-9]+', f)

# record occurrences of each ticker symbol
for word in f:
	if word in symbols:
		symbols[word] += 1

# delete distracting patterns
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
flukes = [  'AT', 'NOW' ,'ARE', 'CEO', 'EV', 'GO', 'TV', 'DD', 'VERY', 'RH', 'EOD', 'IRS', 'RSI', 'FREE', 'PRO', 'EDIT', 'ALL', 'JACK', 'LMAO', 'COOL', 'CAN', 'RIDE', 'CASH', 'OPEN', 'LOVE', 'BIG' ,'HE', 'IT', 'FOR', 'PLAY']
for i in alph:
	flukes.append(i)

for i in flukes:
	if i in symbols:
		del symbols[i]

symbols = np.array([list(symbols.keys()), list(symbols.values())])
symbols = pd.DataFrame(data=symbols).T
symbols.columns = ['symbol', 'count']
symbols['count'] = pd.to_numeric(symbols['count'])

# print nonzero symbols by value in descending order 
nonzero_index = np.nonzero(symbols['count'].to_numpy())
x = symbols.loc[nonzero_index].sort_values(by=['count'], ascending=False)
d = {}
count = 0
for a, b in x.values:
    d[a] = b
    count += 1
    if count > 20 and args.graph == "bar":
    	break



if args.graph == 'cloud':
	wordcloud = WordCloud(width=960, height=500, relative_scaling=.2)
	wordcloud.generate_from_frequencies(frequencies=d)
	plt.figure()
	plt.imshow(wordcloud, interpolation='bilinear')
	plt.axis('off')
	plt.savefig('data/wordcloud.png', dpi=400)
	print('Saved figure: data/wordcloud.png')
	plt.show()

elif args.graph == 'bar' or args.graph == 'histogram':
	plt.bar(d.keys(), d.values())
	plt.xticks(rotation=70)
	plt.savefig('data/histogram.png', dpi=400)
	print('Saved figure: data/histogram.png')
	plt.show()


else:
	print('Invalid argument: must include graph type!')
	quit()
