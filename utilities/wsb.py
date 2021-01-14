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


reddit = praw.Reddit(
    client_id="NRVdeWmyQlW4Pg",
    client_secret="Zs9Mmci2ABVzVXXy2ZvJpjgJDKWlWg",
    user_agent="d_ark"
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
    if i%25 == 0:
        sleep(1)

#

