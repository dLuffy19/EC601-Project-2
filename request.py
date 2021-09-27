from TwitterAPI import TwitterAPI
import os

# You need to export environment variables first:
# export 'consumer_key'='<your_consumer_key>'
consumer_key = os.environ.get("CONSUMER_KEY")
consumer_secret = os.environ.get("CONSUMER_SECRET")
access_token_key = os.environ.get("ACCESS_TOKEN_KEY")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

api = TwitterAPI(consumer_key=consumer_key, consumer_secret=consumer_secret, access_token_key=access_token_key, access_token_secret=access_token_secret)

r = api.request('search/tweets', {'q':'basketball'})
print (r.status_code)
