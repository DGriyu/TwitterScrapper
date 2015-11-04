import tweepy
import time
import os
from tweepy import OAuthHandler

start_time = time.time()
keyword_list = [''] #track list
key = 'consumerkey'
secret = 'consumersecret'

access_key = 'accesskey'
access_secret = 'access_secret'

class listener(tweepy.StreamListener):
 
	def __init__(self, start_time, time_limit=60):
 
		self.time = start_time
		self.limit = time_limit
 
	def on_data(self, data):
 
		while (time.time() - self.time) < self.limit:
 
			try:
 
				saveFile = open('raw_tweets.json', 'a')
				saveFile.write(data)
				saveFile.close()
 
				return True
 
 
			except BaseException, e:
				print 'failed ondata,', str(e)
				time.sleep(5)
				pass
 
		exit()
 
	def on_error(self, status):
 
		print statuses

auth = OAuthHandler(key, secret)
auth.set_access_token(access_key, access_secret)
api = tweepy.API(auth)

twitterStream = tweepy.Stream(auth, listener(start_time, time_limit=10)) #initialize Stream object with a time out limit
twitterStream.sample(languages=['en'])
