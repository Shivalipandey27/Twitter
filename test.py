import twitter

consumer_key = 'IANS8HHqvYxZidEuJ3k42eM8M'
consumer_secret = 'muzPXcxqSaUgOwFVGxbxyKgqgxzTj2tRid7wnuSd87TBln3oYh'
access_token = '1663969912891555845-npqNVkz7w3jNHGGgLHiAq7K1Z49anD'
access_token_secret = 'Sby5HlAXoOvpsZD5lkj2kT4TWS2EokpcR9FiaWTT4V5vJ'

api = twitter.Api(consumer_key=consumer_key,
                  consumer_secret=consumer_secret,
                  access_token_key=access_token,
                  access_token_secret=access_token_secret)

f_count=api.GetFollowerIDs()
print(len(f_count))