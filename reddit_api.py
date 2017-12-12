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
## Retrieving data from the past 2 years:

##Due to errors with the reddit post characters, we had to run this in 9 chunks. The start and end times can be found here, and should be modified along with the csv_path below to recreate our data exactly:
#Number      #End        #Start
#1:       1512097409    1496302522
#2:       1496291678    1493729485
#3:       1480478654    1469185637
#4:       1464695476    1448900355
#5:       1469098822    1467287747
#6:       1491999970    1491999970
#7:       1487099881    1483710465
#8:       1467099725    1464698495
#9:       1483597268    1480509330

end_time = 1512614932
start_time = 1449400000


# Columns for dataframe
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
author_flair_binary_list = []
total_upvotes_list = []
created_utc_list = []
num_comments_list = []
gilded_list = []
image_list = []
journal_h_index_list = []

count = 0
## Searching posts from a given period of time in the SCIENCE subreddit
for submission in reddit.subreddit('science').submissions(
        start=start_time, end=end_time, extra_query=None):

    count = count + 1

    # The images in the preview-images subdictionary are copies of the same image
    # with different sizes. Thus, making preview-images a binary variable makes more sense.
    try:
        preview = vars(submission)['preview']['images'][0]
        image_list.append('yes')
    except:
        # print ('No images for this post')
        image_list.append('no')

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
    # Binary variable for high impact journals and low impact journal/mere websites
    # Journal impact determined by its h-index. See here for a ranking:
    # http://www.scimagojr.com/journalrank.php?order=h&ord=desc

    # List of substrings that the high impact journals (h-index > 500) would contain
    h_index_500 = ['nature.com', 'sciencemag.org', 'nejm.org', 'cell.com', 'pnas.org',
                   'thelancet.com', 'jamanetwork.com', 'aps.org', 'acs.org', 'circ.ahajournals.org']

    if any(substring in domain for substring in h_index_500):
        journal_h_index_list.append('high')
    else:
        journal_h_index_list.append('low')

    subfield_list.append(vars(submission)['link_flair_text'])

    author = str(vars(submission)['author'])
    author_list.append(author)

    # Variables associated with the author of the post
    user = reddit.redditor(author)
    #print (user)

    # Some authors are no longer on reddit,
    # so they return errors for the author info queries below.
    # We ignore these authors by assigining NA to the following 3 fields.
    try:
        link_karma_list.append(user.link_karma)
    except:
        link_karma_list.append('NA')
    try:
        comment_karma_list.append(user.comment_karma)
    except:
        comment_karma_list.append('NA')
    try:
        author_created_list.append(user.created_utc)
    except:
        author_created_list.append('NA')


    author_flair = vars(submission)['author_flair_css_class']
    if not author_flair == None:
        if len(author_flair) > 0:
            author_flair_binary = 'yes'
        else:
            author_flair_binary = 'no'
    else:
        author_flair_binary = 'no'

    author_flair_binary_list.append(author_flair_binary)
    author_flair_list.append(author_flair)
    total_upvotes_list.append(vars(submission)['ups'])
    created_utc = vars(submission)['created_utc']
    created_utc_list.append(created_utc)
    if count % 100 == 0:
        print ('Currently at epoch time of:')
        print (created_utc)

        print (len(author_list))
        print (len(link_karma_list))
        print (len(comment_karma_list))
        print (len(author_created_list))
        print (len(image_list))

    num_comments_list.append(vars(submission)['num_comments'])
    gilded_list.append(vars(submission)['gilded'])



# Consolidate lists into one pandas data frame
reddit_df = pd.DataFrame(
    {'id': id_list,
     'url': url_list,
     'title': title_list,
     'title_len': title_len_list,
     'domain': domain_list,
     'journal_h_index': journal_h_index_list,
     'subfield': subfield_list,
     'author': author_list,
     'link_karma': link_karma_list,
     'comment_karma': comment_karma_list,
     'author_created_date': author_created_list,
     'author_flair': author_flair_list,
     'author_flair_binary': author_flair_binary_list,
     'upvotes': total_upvotes_list,
     'created_utc': created_utc_list,
     'num_comments': num_comments_list,
     'gilded': gilded_list,
     'image': image_list,
    })

# Check out the dimensions of the dataframe
print (reddit_df.shape)

# Save the dataframe as a csv file

csv_path = './reddit_df.csv'
reddit_df.to_csv(csv_path)
