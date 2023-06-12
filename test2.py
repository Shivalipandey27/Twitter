import tweepy
import pandas as pd

consumer_key = 'IANS8HHqvYxZidEuJ3k42eM8M'
consumer_secret = 'muzPXcxqSaUgOwFVGxbxyKgqgxzTj2tRid7wnuSd87TBln3oYh'
access_token = '1663969912891555845-npqNVkz7w3jNHGGgLHiAq7K1Z49anD'
access_token_secret = 'Sby5HlAXoOvpsZD5lkj2kT4TWS2EokpcR9FiaWTT4V5vJ'

auth = tweepy.OAuthHandler(
    consumer_key, consumer_secret,access_token, access_token_secret
    )
api = tweepy.API(auth)

elonmusk_tweet=api.user_timeline(screen_name='@elonmusk', count=100)

tweet_list=[]
for etw in elonmusk_tweet:
    print(etw._json["text"])
    required_tweet={"user" :etw.user.screen_name,
                    "tweet_text":etw._json["text"] 
                    }
    tweet_list.append(required_tweet) 

df=pd.DataFrame(tweet_list)
df.to_csv("elon_tweet.csv",index=False)