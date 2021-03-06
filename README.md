## MATH 154 Project Proposal: Investigating the Popularity of  Scientific Phenomena on Social Media Platforms ##
### Sal Fu (Project Manager, Reporter) 
### Jerry Xuan (Task Manager, Director of Research) 
### Brian Lorenz (Facilitator, Director of Computation) ###

### Motivation

Large numbers of scientific studies are published each day, and most go unnoticed. Some results, however, are much more noticed than others. Why? Why do some scientific results (gravitational wave detection, TRAPPIST-1 exoplanets) go viral? We wish to investigate what factors might influence the popularity of links about science on a social media platform. For example, some forms of presentation (video vs. text) may make an article more viral. The research field that the article pertains to could also matter. By investigating these factors, we might be able to help people better understand how to present their work and engage the public. 

### Data Access

We will be accessing data from either Reddit, Twitter, or Facebook via APIs. We are still in the process of investigating the amount of data that we’ll have access to, but it seems that the Twitter APIs are live in the sense that we can only access data from the past 7 days. We have provided the links to the APIs below. Our analysis will only focus on one social media platform, but we will decide on that after exploring the different datasets and assessing the ease with which we can wrangle the dataset.

Reddit - https://github.com/reddit/reddit/wiki/API

This R package may help: https://cran.r-project.org/web/packages/RedditExtractoR/RedditExtractoR.pdf

Or this Python resource (we are all familiar with Python): http://t-redactyl.io/blog/2015/11/analysing-reddit-data-part-2-extracting-the-data.html

Twitter - https://www.rdocumentation.org/packages/twitteR/versions/1.1.9

Facebook - https://developers.facebook.com/docs/graph-api/using-graph-api/

### Programs

We will be using R to do most of our analysis. We will use Python to interface with the Reddit API and the Facebook API by sending HTTP requests for data, which will come in the form of JSON files. For Twitter, the package is written specifically for R, so we will be using R solely.

### Variables of Interest

Our primary response variable is popularity, measured on Reddit through upvotes, on Facebook through likes, or on Twitter through hearts/retweets. We are interested in investigating what effect each of the following variables have on the popularity of the article (as measured by number of upvotes/(dis)likes/retweets/share)s:

* Scientific field that the article is associated with (e.g. Astronomy, Chemistry, Health Science…)

* There are already categories for these on Reddit. 

* Institution that produced the study, author of paper (fame of author: e.g. whether author has a wikipedia page)

* Source of the linked article - scientific journals, websites, summary article, newspaper

* Presentation type. e.g. Video demo, pretty images, explosions, flowery use of language

* Title description - do certain keywords increase popularity? 

Below is a paper that predicts political ideology of twitter users. In this paper, there seems to be a series of packages that allow us to perform analysis on the words that social media users use, which should also be useful for gauging users’ response to given scientific articles. 

http://aclweb.org/anthology/P/P17/P17-1068.pdf

### Final Products

We hope to deliver a series of visualizations illustrating the advantages of certain types of scientific communication in popularizing the scientific topic. From these visualizations, we will make suggestions for scientific communicators hoping to make their topic reach a broader audience. Based on our findings, we will try to make a predictive model that scores new studies and see how our predictions match with the results on social media platforms. Our recent work with random forests would lend itself nicely to generating such a model - we can make our response variable popularity and allow all other variables to be explanatory, then generate a random forest that predicts that popularity of an article based on its other factors. 

### Project Update 11/20/2017

1. Yes, we have collected the majority of the data that we will need. We have accessed reddit's api through the Python Reddit API Wrapper (praw) and generated a .csv file containing our response variable (numbe of upvotes) and a variety of explanatory variables (domain, subfield, author, date/time created, etc...). The .csv file is on github if you are interested in looking at it. If we decide to add more explanatory variables, we can easily modify the python code to add more. For now, we have only collected data over a small timeframe (11 days) but plan to expand this to a few years once we know that everything is working. 

2. We need to wrangle the data to make it more readable for the functions that we are going to use. For example, we have retrieved the time that the post was created, but it would be most helpful if we can convert that time into a time of day. 

We also need to figure out how to classify different sources (e.g. scientific, not scientific). Our initial thought was that we could pair the journals with their impact factors, but the sources that the posts draw from include journal articles as well as pop science articles. This is something we’re still looking into.

3. We have accessed an api for a constantly updating website, so our model can change as new data comes in. We hope to use sentiment analysis to examine the type of language used in successful posts. Finally, we intend to use neural networks as one of our models - none of us have learned about these before. 

### Prof Hardin comments on update

Hi, team viral!  Seems like you are well on your way.  You should check out the R package `lubridate` for wrangling date stuff (it is magical :).  Also, in terms of wrangling, you should think about wrangling as PART of the project (and *not* as the stuff you need to do before the project starts).  

Seems like you have a lot of new stuff to learn.  I'd recommend doing one thing at a time.  I like the idea of group effort, but maybe all of you should investigate sentiment analysis so that you can talk to one another and bounce ideas around.  And then move to neural networks.

You are in good shape!  Let me know if/when you have any questions.  -JH

###Presentation
Pdf can be found in the repo, and the editable version is here:
https://docs.google.com/presentation/d/1XQjcbkE_-deVCwuIRn500gd3TsLtjMviDk0dEn2rH_4/edit?usp=sharing
