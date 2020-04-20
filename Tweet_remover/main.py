import tweepy
import json
import time
import random
from tqdm import tqdm
import os

fullpath = os.path.abspath(__file__)
os.chdir(os.path.dirname(fullpath))

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
    data = {"consumer_key": "", "consumer_secret":"", "access_token":"","access_token_secret":""}
    try:
        open("config.json", "r")

    except:
        print("config file created")
        with open("config.json", "w") as f:
            json.dump(data, f)
            return data

    with open("config.json", "r") as f:
        data = json.load(f)
        return data




def get_last_tweets(user, count, api):
    tweet_list = []
    for tweet in tqdm(tweepy.Cursor(api.user_timeline, id=user).items()):
        tweet_list.append(tweet)
        if len(tweet_list) > count:
            break

    return tweet_list

def delete_tweets(tweets, api):
    for tweet in tweets:
        api.destroy_status(tweet.id)


def main():
    config = load_config()
    auth, api =connexion(config)

    try:
        api.me()
        print("succefuly connected {}".format(api.me().screen_name))
    except:
        print("Not connected")
        return

    nomber = ""
    while type(nomber) != type(3):
        try:
            nomber = int(input("How many tweet do you want to delete ?"))
        except:
            print("please enter a number")

    tweets = get_last_tweets(api.me().screen_name,nomber, api)
    delete_tweets(tweets, api)



if __name__ == "__main__":
    main()












#
