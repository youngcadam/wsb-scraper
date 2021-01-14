# Reddit Submission Comment Scraper
Extract comments from reddit posts see the most discussed stock tickers.

### Scrape comments on a reddit post
```python
python reddit.py -n example_name.txt -p kw0lin
	      # -n --name of output file 
	      # -p --post reddit post id
```

### Visualize mentioned tickers
```python
python counter.py -g bar
			# -g --graph to plot (bar, cloud)
```

### Utilities
Before using these, be sure to 
```bash
cd utilities/
```

#### `ticker.py` 

to download and format a list of stock tickers from [sec.gov](https://www.sec.gov/file/company-tickers)

Usage: 
```bash 
python ticker.py # creates ../data/tickers.txt
```

#### `wsb.py` 

download stream of incoming comments from investing multireddit

Usage: 
```bash 
python wsb.py # creates ../data/wsb.txt
```