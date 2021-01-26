# Adam Young (youngcadam@ucla.edu) © 2021                                        
# exec(open("test.py").read())                                                   
# EngInvestor/investing/                                                         
import praw
import atexit
from pprint import pprint
from time import sleep

f = open("../data/wsb.txt", "w")
subreddit_scores = {}

def savecounter():
    f.close()
    pprint(subreddit_scores)

atexit.register(savecounter)


# ADD YOUR OWN INFO HERE!

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

i = 1

for comment in reddit.multireddit("EngInvestor", "investing").stream.comments():
    f.write("%s\n" %comment.body)
    print(f"[comment: {i}  /r/{comment.subreddit}]")
    if comment.subreddit.display_name in subreddit_scores:
    	subreddit_scores[comment.subreddit.display_name] += 1
    else:
    	subreddit_scores[comment.subreddit.display_name] = 1
    i += 1
    if i%50 == 0:
        sleep(1)
        pprint(subreddit_scores)

