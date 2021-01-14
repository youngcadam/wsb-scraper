import pandas as pd
import numpy as np
import re
import csv
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import argparse

# parse arguments
parser = argparse.ArgumentParser()
parser.add_argument("-g", "--graph", help="select graph to plot")
args = parser.parse_args()

# load list of stock tickers
symbols = open('./data/tickers.txt').read().split()
symbols = {str(i) : 0 for i in symbols}

# load comments
f = open('./data/sample.txt').read()
f = re.split('[^a-zA-Z0-9]+', f)

# record occurrences of each ticker symbol
for word in f:
	if word in symbols:
		symbols[word] += 1

# delete distracting patterns
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
flukes = ['CEO', 'EV', 'GO', 'TV', 'DD', 'VERY', 'RH', 'EOD']
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
    if count > 25 and args.graph == "bar":
    	break

if args.graph == "cloud":
	wordcloud = WordCloud(relative_scaling=.5)
	wordcloud.generate_from_frequencies(frequencies=d)
	plt.figure()
	plt.imshow(wordcloud, interpolation="bilinear")
	plt.axis("off")
	plt.savefig("wordcloud.png", dpi=200)
	print("Saved figure: wordcloud.png")
	plt.show()

elif args.graph == "bar" or args.graph == "histogram":
	plt.bar(d.keys(), d.values())
	plt.savefig("histogram.png", dpi=200)
	print("Saved figure: histogram.png")
	plt.show()


else:
	print("Invalid argument: must include graph type!")
	quit()
