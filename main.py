#!/usr/bin/python/
import tweepy,time 

ACCESS_KEY = 'xxxxxxxxxxxxxxxxx' #make sure perms are at least read and write just in case
ACCESS_SECRET = 'xxxxxxxxxxxxxxxxx' #get your keys at dev.twitter.com
CONSUMER_KEY = 'xxxxxxxxxxxxxxxxx'
CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxx'
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth) 

def login(): 
	user = api.me()
	print ("[bot] @" + user.screen_name + " successfully logged into twitter.")

def tracker(): 
	print("[bot] Script will start tracking \"" + track + "\". Tweets should start to appear below.")
	print
	time.sleep(3)

def stream():
	sapi = tweepy.streaming.Stream(auth, CustomStreamListener())
	sapi.filter(track=[track])

login()
track = raw_input('[bot] Enter @username, #hashtag or word to track: ')
tracker()
	
class CustomStreamListener(tweepy.StreamListener): 
    def on_status(self, status):
		tweet = status.text
		replyusr = status.user.screen_name
		reply = tweet.encode('ascii', 'ignore').strip()
		now = time.strftime("[%I:%M:%S %p] ")
		print(now + "@" + replyusr + ": " + reply)
		print(" ")

stream() 
