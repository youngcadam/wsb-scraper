# Reddit Comment Scraper
Extract comments from reddit posts see the most discussed stock tickers. Included example from [/r/wallstreetbets](https://reddit.com/r/wallstreetbets)

### Scrape comments on a reddit post
```python
python reddit.py -n sample.txt -p kw0lin
	       # -n (--name) - name of output file 
	       # -p (--post) - reddit post id
	       # -l (--limit) - time limit for loading more comments (recommended=100)
```

### Visualize mentioned tickers
```python
python counter.py -g bar -f GME_scrape.txt
		# -g (--graph) - type of graph to plot (bar, cloud)
		# -n (--name) - name of file in wsb-scraper/data/
		# -f (--filter) - filter listed tickers from plot tickers 
```

### Utilities
Before using these, be sure to 
```bash
cd utilities/
```

##### `ticker.py` 

download and format a list of stock tickers from [sec.gov](https://www.sec.gov/file/company-tickers)

Usage: 
```bash 
python ticker.py # creates ../data/tickers.txt
```

##### `wsb.py` 

download stream of incoming comments from popular investing subreddits

Usage: 
```bash 
python wsb.py # creates ../data/wsb.txt
```

To run in background on a VPS (tested on AWS Lightsail)
```bash
nohup python wsb.py &
```