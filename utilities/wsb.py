# Adam Young (youngcadam@ucla.edu) © 2021                                        
# exec(open("test.py").read())                                                   
# EngInvestor/investing/                                                         
import praw
import atexit
from time import sleep

f = open("../data/wsb.txt", "a")

def savecounter():
    f.close()

atexit.register(savecounter)


reddit = praw.Reddit(
    client_id="NRVdeWmyQlW4Pg",
    client_secret="Zs9Mmci2ABVzVXXy2ZvJpjgJDKWlWg",
    user_agent="d_ark"
)

i = 1
for comment in reddit.multireddit("EngInvestor", "investing").stream.comments(sk\
ip_existing=True):
    f.write("%s\n" %comment.body)
    print(f"[comment: {i}   /r/{comment.subreddit}]")
    i += 1
    if i%25 == 0:
        sleep(3)
