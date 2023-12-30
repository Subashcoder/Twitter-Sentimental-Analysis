import tweepy
import pandas as pd

consumer_key = "your_consumer_key"
consumer_secret = "your_consumer_secret"
access_token = "your_access_token"
access_token_secret = "your_access_token_secret"

# Pass in our twitter API authentication key
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Instantiate the tweepy API
api = tweepy.API(auth, wait_on_rate_limit=True)

# Specify the screen name of the user whose timeline you want to retrieve
screen_name = "twitter_handle"

# Retrieve user timeline tweets
tweets = api.user_timeline(screen_name=screen_name, count=5, tweet_mode="extended")

# Pulling some attributes from the tweet
attributes_container = [
    [
        tweet.user.screen_name,
        tweet.user.name,
        tweet.user.location,
        tweet.created_at,
        tweet.favorite_count,
        tweet.retweet_count,
        tweet.source,
        tweet.full_text,
    ]
    for tweet in tweets
]

# Creation of column list to rename the columns in the dataframe
columns = [
    "User Screen Name",
    "User Name",
    "User Location",
    "Date Created",
    "Number of Likes",
    "Number of Retweets",
    "Source of Tweet",
    "Tweet",
]

# Creation of Dataframe
tweets_df = pd.DataFrame(attributes_container, columns=columns)

print(tweets_df)
