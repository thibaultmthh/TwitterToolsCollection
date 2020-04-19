import tweepy
import json
import time


liste_tweet = []
with open("tweet_list.txt") as f:
    for line in f.readlines():
        liste_tweet.append(line.strip())

with open("tweet_done.save", "a") as f:
    pass

liste_tweet_done = []
with open("tweet_done.save") as f:
    for line in f.readlines():
        liste_tweet_done.append(line.strip())


def connexion(tokens):
    consumer_key = tokens["consumer_key"]
    consumer_secret = tokens["consumer_secret"]
    access_token = tokens["access_token"]
    access_token_secret = tokens["access_token_secret"]
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    return auth, api


def load_config():
    data = {"consumer_key": "", "consumer_secret":"", "access_token":"","access_token_secret":"", "time_between_tweets_sec": 60*60*12}
    try:
        with open("config.json", "r") as f:
            data = json.load(f)
            return data
    except:
        with open("config.json", "w") as f:
            json.dump(data, f)
            return data

config = load_config()
auth, api =connexion(config)


for tweet in liste_tweet:
    if not tweet in liste_tweet_done:
        api.update_status(tweet)
        print(tweet)
        liste_tweet_done.append(tweet)
        with open("tweet_done.save", "a") as f:
            f.write(tweet+"\n")

        time.sleep(int(config["time_between_tweets_sec"]))


















#
