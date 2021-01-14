# Adam Young (youngcadam@ucla.edu) © 2021 
# exec(open("test.py").read()) 
# EngInvestor/investing/
import praw
import atexit

f = open("../data/wsb.txt", "a")

def savecounter():
    f.close()

atexit.register(savecounter)


reddit = praw.Reddit(
    client_id="NRVdeWmyQlW4Pg",
    client_secret="Zs9Mmci2ABVzVXXy2ZvJpjgJDKWlWg",
    user_agent="d_ark"
)

i = 0
for comment in reddit.multireddit("EngInvestor", "investing").stream.comments(skip_existing=True):
    f.write("%s\n" %comment.body)
    print(f"Success! Recorded comment {i} to data/wsb.txt")
    i += 1	
