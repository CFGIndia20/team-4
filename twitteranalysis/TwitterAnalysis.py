#!/usr/bin/env python
# coding: utf-8

# In[27]:


import GetOldTweets3 as got
import csv
import pandas as pd
import re
import string 
from textblob import TextBlob


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
df.to_csv('tweets.csv')
df


# In[ ]:




