### via https://gist.github.com/szolotykh/e4924159d79ddbaa12c6


import tweepy
import os

# Consumer keys and access tokens, used for OAuth
consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

# OAuth process, using the keys and tokens
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Creation of the actual interface, using authentication
api = tweepy.API(auth)

# Sample method, used to update a status
# api.update_status('Hello Form RBI Lab!')

# load image
imagePath = "img.jpg"
status = "Hi! From Python script=)"

# Send the tweet.
api.update_with_media(imagePath, status)
