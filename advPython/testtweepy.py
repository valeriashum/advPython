import tweepy

consumer_key = 'XA5F1MmgTeqgcVTdZrfYxfvRe'
consumer_secret = '7uaYtIxCMCROxhhB5RylovdBUQnfKx5yCbjAfA5qjJuZCrt6SE'

access_token = '4913629276-UvQpvRThygNpC8MiMAhWKlGhgnFQ6253RgE7lw4'
access_token_secret = 'qLm9cJYpICpN5ZeKdyQy0IAifuoqOyEjI2538wz4cVwc7'

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

twitter_api = tweepy.API(auth)

tweets_of_user = twitter_api.user_timeline("CodeFirstGirls")
for tweet in tweets_of_user:
	print tweet.text

#user = twitter_api.get_user("CodeFirstGirls")
#print "screen name: " + user.screen_name
#print "number of followers: " + str(user.followers_count)


# tweet = raw_input("post a message in twitter: "
# tweet_api.update_status(tweet)



