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

search_tweets = api.search_tweets(q='#pokemon', lang='pt', result_type='mixed', count=20)

for tweet in search_tweets:
    print(f"{tweet.user.name} tweeted: ")
    print(tweet.text)
    print(f"# of likes: {tweet.favorite_count}")
    print(f'# of retweets: {tweet.retweet_count}')
    print("-------------------------------------------------------------------------------")
