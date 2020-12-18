#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install python-decouple')
get_ipython().system('pip install tweepy')


# In[2]:


import os
import time
from decouple import config
import tweepy
import pandas as pd


# In[ ]:


consumer_key = config('API-KEY')
consumer_secret = config('API-SECRET-KEY')
access_token = config('ACCESS-TOKEN')
access_token_secret = config('ACCESS-TOKEN-SECRET')


# In[ ]:


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

if(not api):
    sys.exit(-1)


# In[ ]:


def scrape_tweets(query, tweets_request, max_requests):
    tweet_df = pd.DataFrame(columns=['tweet', 'id', 'source', 'coordinates', 'retweetCount', 'likeCount', 'username', 'screenName', 'location', 'friendsCount', 'verificationStatus', 'description', 'followersCount'])
    
    tweet_list = []

    for i in range(0, max_requests):
        response = tweepy.Cursor(api.search, q=query, lang='en', tweet_mode='extended').items(tweets_request)
        
        tweet_list = tweet_list + [tweet for tweet in response]

    for tweet in tweet_list:
        if not hasattr(tweet, 'retweeted_status'):
            text = tweet.full_text
            id = tweet.id_str
            source = tweet.source
            coordinates = tweet.coordinates
            retweetCount = tweet.retweet_count
            likeCount = tweet.user.favourites_count
            username = tweet.user.name
            screenName = tweet.user.screen_name
            location = tweet.user.location
            friends = tweet.user.friends_count
            verification = tweet.user.verified
            description = tweet.user.description
            followers = tweet.user.followers_count

            ith_tweet = [text, id, source, coordinates, retweetCount, likeCount, username, screenName, location, friends, verification, description, followers]

            tweet_df.loc[len(tweet_df)] = ith_tweet

    return tweet_df


# In[ ]:


def save_results_as_csv(df):
    path = os.getcwd() + '\data\\'
    current_timestamp = time.strftime("%y%m%d_%H%M%S")
    
    if not os.path.exists(path):
        os.mkdir(path)
        
    filename = 'tweets_downloaded' + current_timestamp + '.csv'
    
    fullname = os.path.join(path, filename)
    
    df.to_csv(fullname, index=False)


# In[ ]:


from pymongo import MongoClient


# In[ ]:


client = MongoClient('localhost', 27017)
db = client['test']


# In[ ]:


class MongoDB(object):
    
    def __init__(self, dBName=None, collectionName=None ):
        self.dBName = dBName
        self.collectionName = collectionName
        
        self.client = client
        self.DB = self.client[self.dBName]
        self.collection = self.DB[self.collectionName]
        
    def InsertData(self, path=None):
        
        f = open(path, encoding='utf8')
        tweet_df = pd.read_csv(f)
        data = tweet_df.to_dict('records')
        
        self.collection.insert_many(data)
        print("The collection has been uploded to server...")
        
if __name__ =='__main__':
    
    mongodb = MongoDB(dBName = 'tweet_db', collectionName = 'raw_tweets')
    mongodb.InsertData(path = 'data\\tweets_downloaded201209_234308.csv')
        

