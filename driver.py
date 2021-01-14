import os

print("downloading tickers")
os.chdir("./utilities")
os.system("python tickers.py")
os.chdir("..")
print("Finished downloading tickers. Downloading comments...")
os.system("python reddit.py -n sample.txt -p kw0lin -l 50")
print("Finished downloading comments, displaying word cloud...")
os.system("python counter.py -g cloud")