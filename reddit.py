# Adam Young (youngcadam@ucla.edu) © 2021 
# this script gets several comments from a post on wall street bets and saves them on a file "comments.txt"

import praw
import pandas as pd
import datetime as dt
import argparse
import atexit


# Initiate the parser
parser = argparse.ArgumentParser()
parser.add_argument("-n", "--name", help="name of new txt file")
parser.add_argument("-p", "--post", help="id of post")
parser.add_argument("-l", "--limit", help="limit of wait time (default = None)")

# parse arguments
args = parser.parse_args()
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

if args.limit:
    limit =  int(args.limit)
else:
    print("Using default limit: 50")
    limit = 50


# open file and initialize praw
f = open(name, "w")

reddit = praw.Reddit(
    client_id="",
    client_secret="",
    user_agent=""
)

submission = reddit.submission(id=post)
# submission.comment_sort = "new"
print(f"Post Title: {submission.title}")
print(f"# of comments: {submission.num_comments}")

# print all comments in the submission
submission.comments.replace_more(limit=limit, threshold=5)
commentlist = []
i = 0
for comment in submission.comments.list():
    commentlist.append(comment.body)
    #print(f"Success! Recorded comment {i} to from /r/{comment.subreddit}")
    i += 1
print(f"Comments Recorded: {i}")

for comment in commentlist:
    f.write(comment)
f.close()

