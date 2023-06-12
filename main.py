import tweepy

# API credentials
consumer_key = 'IANS8HHqvYxZidEuJ3k42eM8M'
consumer_secret = 'muzPXcxqSaUgOwFVGxbxyKgqgxzTj2tRid7wnuSd87TBln3oYh'
access_token = '1663969912891555845-npqNVkz7w3jNHGGgLHiAq7K1Z49anD'
access_token_secret = 'Sby5HlAXoOvpsZD5lkj2kT4TWS2EokpcR9FiaWTT4V5vJ'

# Authenticate with Twitter Ads API
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True, wait_on_rate_limit_notify=True)

# Account ID of your Twitter Ads account
account_id = 'shivali98993246'

# Retrieve campaign IDs
campaigns = api.get_campaigns(account_id=account_id)

for campaign in campaigns:
    campaign_id = campaign.id
    campaign_name = campaign.name

    # Retrieve campaign stats
    campaign_stats = api.get_campaign_stats(account_id=account_id, campaign_ids=[campaign_id])

    for stat in campaign_stats:
        impressions = stat.metrics.impressions
        clicks = stat.metrics.clicks
        retweets = stat.metrics.retweets
        likes = stat.metrics.likes

        print(f"Campaign: {campaign_name}")
        print(f"Impressions: {impressions}")
        print(f"Clicks: {clicks}")
        print(f"Retweets: {retweets}")
        print(f"Likes: {likes}")
        
