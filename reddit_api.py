# Created reddit account "compstatsf17" with password "Sagehen47!" (no quotes on either of those)
#
# registered app as compstats17_final_project
# client_secret: WAe0pEENwYhWu6tErofV7T7QOR4
# client_id: rNGwNS4hRPJDfw
#
# Connected app with the account compstatsf17, so now the app can access all functions of that user
# The "state" of the user is the pseudo-random string (no quotes) "fenwiosj"
# The code created when authorizing the user is (no quotes) "yE0L1_clkxrpp0mVpVthf-KQWlo"
#
# The python api wrapper can be found here:
# https://github.com/praw-dev/praw
#
# Try runnning the code below:

import praw
import pandas as pd
# from IPython.display import display, HTML

reddit = praw.Reddit(client_id='rNGwNS4hRPJDfw', client_secret="WAe0pEENwYhWu6tErofV7T7QOR4",
                     password='Sagehen47!', user_agent='python:rNGwNS4hRPJDfw:v1.0 (by /u/compstats17)',
                     username='compstatsf17')

#print(reddit.user.me())

# Columns
id_list = []
url_list = []
title_list = []
score_list = []

#for submission in reddit.front.hot(limit=10):

## Convert to epoch timestamp via https://www.epochconverter.com/
# The 2 month interval here gives ~1900 rows of data
# Sept 20, 2017
start_time = 1505878887
# Nov 20, 2017
end_time = 1511149287

## Searching posts from a given period of time in the SCIENCE subreddit
for submission in reddit.subreddit('science').submissions(
        start=start_time, end=end_time, extra_query=None):
    # Populate lists. I had to encode these to make the .to_csv work.
    id_list.append(submission.id.encode('utf-8'))
    url_list.append(submission.url.encode('utf-8'))
    # Gives funny characters in csv file
    title_list.append(submission.title.encode('utf-8'))
    score_list.append(submission.score)

# Consolidate lists into one pandas data frame
reddit_df = pd.DataFrame(
    {'id': id_list,
     'url': url_list,
     'title': title_list,
     'score': score_list,
    })

# Check out the dimensions of the df
print (reddit_df.shape)

# Save the dataframe as a csv file for us to use in R
# We could just save it in the git repo directory (aka current dir)
csv_path = './reddit_df.csv'
reddit_df.to_csv(csv_path)