# Adam Young (youngcadam@ucla.edu) © 2021 
# this script gets several comments from a post on wall street bets and saves them on a file "comments.txt"

import praw
import pandas as pd
import datetime as dt
import argparse
import atexit

def goodbye():
    for comment in submission.comments.list():
        f.write(comment.body)

atexit.register(goodbye)


# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="name of new txt file")
parser.add_argument("-p", "--post", help="id of post")

# Read arguments from the command line
args = parser.parse_args()

# Check for --name or -n
name, post = "", ""
if args.post:
	post = args.post
else:
	print("Post id required")
	quit()

if args.name:
    name =  f"./data/{args.name}"
else:
	name = f"./data/{post}_comments.txt"

f = open(name, "w")


reddit = praw.Reddit(
    client_id="NRVdeWmyQlW4Pg",
    client_secret="Zs9Mmci2ABVzVXXy2ZvJpjgJDKWlWg",
    user_agent="d_ark"
)

submission = reddit.submission(id=post)
print(submission.title)

# print all comments in the submission
submission.comments.replace_more(limit=None)
for comment in submission.comments.list():
    f.write(comment.body)

f.close()


'''
# looping through words in a comment
my_string = "this is a string"
for word in my_string.split():
print (word)
'''

'''
# Obtaining a Subreddit  subbreddit.(display_name, title, description)
subreddit = reddit.subreddit("wallstreetbets")


# looping through submissions (hot, top, controversial, new, rising, gilded)
for submission in subreddit.top('day', limit=3):
    print(submission.title)
    print(submission.score)
    print(submission.id)
    print(submission.url)
                             



# Comments
top_level_comments = list(submission.comments)
all_comments = submission.comments.list()
submission = subreddit.random()
submission.comment_sort = "top"
top_level_comments = list(submission.comments)
'''
