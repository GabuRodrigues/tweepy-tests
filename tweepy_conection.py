import tweepy
import json

file_credentials = open('credentials.json')
json_credentials = json.load(file_credentials)

consumer_key = json_credentials['API_Key']
consumer_secret = json_credentials['API_Key_Secret']
access_token = json_credentials['Access_Token']
access_token_secret = json_credentials['Access_Token_Secret']

auth = tweepy.OAuth1UserHandler(
   consumer_key, consumer_secret, access_token, access_token_secret
)

api = tweepy.API(auth)

public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)
