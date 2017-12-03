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

import pprint
import praw
import pandas as pd

# from IPython.display import display, HTML

reddit = praw.Reddit(client_id='rNGwNS4hRPJDfw', client_secret="WAe0pEENwYhWu6tErofV7T7QOR4",
                     password='Sagehen47!', user_agent='python:rNGwNS4hRPJDfw:v1.0 (by /u/compstats17)',
                     username='compstatsf17')

#print(reddit.user.me())

#for submission in reddit.front.hot(limit=10):

## Convert to epoch timestamp via https://www.epochconverter.com/
# The 2 month interval here gives ~1900 rows of data
# Sept 20, 2017
start_time = 1511149287 - 1000000
# Nov 20, 2017
end_time = 1511149287

#this is the list of dictionary names that we can use to pull data from vars(submission)

#domain
#link_flair_text = categorization of the article (sub science field)
#author - Reddit object
#author_flair_css_class
#ups: total upvotes(?)
#created_utc (time of creation)
#num_comments
#author_flair_text
#gilded (somebody thought it was worth spending money on this)
#preview

# Columns
id_list = []
url_list = []
title_list = []
title_len_list = []
score_list = []
domain_list = []
subfield_list = []
author_list = []
link_karma_list = []
comment_karma_list = []
author_created_list = []
author_flair_list = []
total_upvotes_list = []
created_utc_list = []
num_comments_list = []
gilded_list = []
image_list = []
journal_h_index_list = []

## Searching posts from a given period of time in the SCIENCE subreddit
for submission in reddit.subreddit('science').submissions(
        start=start_time, end=end_time, extra_query=None):

    # Print dictionary prettier
    #pprint.pprint(vars(submission), width=1)

    # Turns out that the images in the preview-images subdictionary are copies of the same image
    # with different sizes. Thus, making preview-images a binary variable makes more sense
    try:
        preview = vars(submission)['preview']['images'][0]
        image_list.append('YES')
    except:
        print ('No images for this post')
        image_list.append('NO')

    # Populate lists. I had to encode these to make the .to_csv work.
    id_list.append(submission.id.encode('utf-8'))
    url_list.append(submission.url.encode('utf-8'))
    # Gives funny characters in csv file
    title_list.append(submission.title.encode('utf-8'))
    title_len = len((submission.title.encode('utf-8')).replace(' ',''))
    title_len_list.append(title_len)
    score_list.append(submission.score)

    domain = vars(submission)['domain']
    domain_list.append(domain)
    print (domain)
    # Binary variable for high impact journals and low impact journal/mere websites
    # Journal impact determined by its h-index. See here for a ranking:
    # http://www.scimagojr.com/journalrank.php?order=h&ord=desc

    # List of substrings that the high impact journals (h-index > 500) would contain
    h_index_500 = ['nature.com', 'sciencemag.org', 'nejm.org', 'cell.com', 'pnas.org',
                   'thelancet.com', 'jamanetwork.com', 'aps.org', 'acs.org', 'circ.ahajournals.org']

    if any(substring in domain for substring in h_index_500):
        print ('high')
        #pprint.pprint(vars(submission), width=1)
        journal_h_index_list.append('high')
    else:
        journal_h_index_list.append('low')

    subfield_list.append(vars(submission)['link_flair_text'])

    author = str(vars(submission)['author'])
    author_list.append(author)

    # Variables associated with the author of the post
    user = reddit.redditor(author)
    #print (user)

    # Apparantly some authors are no longer on reddit,
    # so they return errors for the author info queries below.
    # We could ignore these authors by assigining NA to the following 3 fields.
    try:
        link_karma_list.append(user.link_karma)
    except:
        print ('error in link karma')
        link_karma_list.append(0)
    try:
        comment_karma_list.append(user.comment_karma)
    except:
        comment_karma_list.append(0)
        print ('error in comment karma')
    try:
        author_created_list.append(user.created_utc)
    except:
        author_created_list.append(0)
        print ('error in author created')

    author_flair_list.append(vars(submission)['author_flair_css_class'])
    total_upvotes_list.append(vars(submission)['ups'])
    created_utc_list.append(vars(submission)['created_utc'])
    num_comments_list.append(vars(submission)['num_comments'])
    gilded_list.append(vars(submission)['gilded'])


# Consolidate lists into one pandas data frame
reddit_df = pd.DataFrame(
    {'id': id_list,
     'url': url_list,
     'title': title_list,
     'title_len': title_len_list,
     'score': score_list,
     'domain': domain_list,
     'journal_h_index': journal_h_index_list,
     'subfield': subfield_list,
     'author': author_list,
     'link_karma': link_karma_list,
     'comment_karma': comment_karma_list,
     'author_created_date': author_created_list,
     'author_flair': author_flair_list,
     'upvotes': total_upvotes_list,
     'created_utc': created_utc_list,
     'num_comments': num_comments_list,
     'gilded': gilded_list,
     'image': image_list,
    })

# Check out the dimensions of the df
print (reddit_df.shape)

# Save the dataframe as a csv file for us to use in R
# We could just save it in the git repo directory (aka current dir)

csv_path = './reddit_df.csv'
reddit_df.to_csv(csv_path)

# {u'enabled': False,
#              u'images': [{u'id': u'uVgy8zxh8sx6w2qHXlIFftDyGEmqanxhX7qvnUfOzkE',
#                           u'resolutions': [{u'height': 139,
#                                             u'url': u'https://i.redditmedia.com/PTgOHqPxcNhco7Eccr7lKUThY_ITUe3rjBtGNQ1xx9A.jpg?fit=crop&crop=faces%2Centropy&arh=2&w=108&s=110a93aff008f292ef7e7015121b11e3',
#                                             u'width': 108},
#                                            {u'height': 279,
#                                             u'url': u'https://i.redditmedia.com/PTgOHqPxcNhco7Eccr7lKUThY_ITUe3rjBtGNQ1xx9A.jpg?fit=crop&crop=faces%2Centropy&arh=2&w=216&s=ce3fb933cd2b59cbdbc14afac2cf547d',
#                                             u'width': 216},
#                                            {u'height': 413,
#                                             u'url': u'https://i.redditmedia.com/PTgOHqPxcNhco7Eccr7lKUThY_ITUe3rjBtGNQ1xx9A.jpg?fit=crop&crop=faces%2Centropy&arh=2&w=320&s=d966489685b4db20e4fd732f734423db',
#                                             u'width': 320}],
#                           u'source': {u'height': 672,
#                                       u'url': u'https://i.redditmedia.com/PTgOHqPxcNhco7Eccr7lKUThY_ITUe3rjBtGNQ1xx9A.jpg?s=5fbab60746d098fee6cfc714e2392485',
#                                       u'width': 520},
#                           u'variants': {}}]},
