#!/usr/bin/env python
# coding: utf-8

# In[27]:


import GetOldTweets3 as got
import csv
import pandas as pd
import re
import string
from textblob import TextBlob
from .name_add_desc_separator import BreakDown
from .textClassification import textClassifier
from .categories import category
import json
import requests
from datetime import datetime


# In[32]:


category = pd.read_csv("cd_categories.csv")
category


# In[33]:


title = category['title'].to_list()


# In[43]:


final_list = []
for i in range(0,29):
	tweetCriteria =  got.manager.TweetCriteria().setQuerySearch('janaagraha, civic').setMaxTweets(30)
	tweet = got.manager.TweetManager.getTweets(tweetCriteria)[i]
	#dicti = ({'tweetID':[tweet.id],'tweetUserName':[tweet.username],'tweetText':[tweet.text]})
	#pd = pandas.DataFrame(dicti)
	#pd = pd.append(pd)
	def clean_tweet(t1):
	  # remove old style retweet text "RT"
	  tweet = re.sub(r'^RT[\s]+', '', t1)

	  # remove hyperlinks
	  tweet = re.sub(r'https?:\/\/.*[\r\n]*', '', t1)

	  # remove hashtags
	  # only removing the hash # sign from the word
	  tweet = re.sub(r'#', '', t1)

	  # remove mentions
	  tweet = re.sub(r'@[A-Za-z0-9]+', '', t1)

	  # remove punctuations like quote, exclamation sign, etc.
	  # we replace them with a space
	  tweet = re.sub(r'['+string.punctuation+']+', ' ', t1)

	  return tweet


	categ = categorize(clean_tweet(tweet.text))
	t = get_tweet_sentiment(clean_tweet(tweet.text))
	inner_list = [tweet.username, clean_tweet(tweet.text),tweet.date,tweet.retweets, tweet.geo,tweet.permalink]
	final_list.append(inner_list)


# In[44]:


df = pd.DataFrame(final_list, columns=[ 'username', 'description', 'date','retweets','location','link'])

para = df['description'][1]

def mainExcalibur(para, timestamp=None, source="TW", phone_number=None, username=username):
    """
        Takes the input from different sources, stores it and returns the track id and url.
    """
    l = BreakDown(text=para)
    name = l[1]
    location = l[2]
    descp = l[3]
    category_id = textClassifier(descp)

    data = {
        'location' : location,
        'description' : descp,
        'category' : str(category_id),
        'timestamp' : str(datetime.now()),
        'source' : source,
    }
    url = 'http://127.0.0.1:8000/api/botapi/post/'
    x = requests.post(url, data = json.dumps(data), headers = {'Content-Type' : 'application/json'})

    x = x.json()
    # return "Thank you for posting the complain. Your complaint id is `x` {}. Your complaint id is For more details visit {}.".format(str(x["track_id"]), str(x["url"]))
    return {'id': x['track_id'], 'url': x['url']}

# In[ ]:
