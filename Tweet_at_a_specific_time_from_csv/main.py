# -*- coding: utf-8 -*-

import tweepy
import json
import time
import csv

already_post=[]

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
        with open("config.json", "r") as f:
            data = json.load(f)
            return data
    except:
        with open("config.json", "w") as f:
            json.dump(data, f)
            return data
def read_csv(path):
    with open(str(path)) as file:
        dialect = csv.Sniffer().sniff(file.read(1024))
        csv_file = csv.reader(file, dialect, quotechar='"')
        csv_file_list = []
        file.seek(0)
        for row in file:
            pass
        file.seek(0)
        for row in csv_file:
            csv_file_list.append(row)
    return csv_file_list

def post_shedule_post():
    a = read_csv("tweet_liste.csv")
    year = time.localtime().tm_year
    month = time.localtime().tm_mon
    day = time.localtime().tm_mday
    hour = time.localtime().tm_hour
    minute = time.localtime().tm_min
    if len(str(month)) == 1:
        month = '0{}'.format(month)
    if len(str(day)) == 1:
        day = '0{}'.format(day)
    if len(str(hour)) == 1:
        hour = '0{}'.format(hour)
    if len(str(minute)) == 1:
        minute = '0{}'.format(minute)

    date = "{}/{}/{}".format(day, month, year)
    hours = "{}h{}".format(hour, minute)
    for x in a:
        if x[0] == date and x[1] == hours and not x in already_post:
            already_post.append(x)
            a= x[2].encode("utf-8")
            print("[{}:{}] tweet sended".format(hour,minute))
            return api.update_status(a)


config = load_config()
auth, api =connexion(config)
try:
    api.me()
    print("succefuly connected to {}".format(api.me().screen_name))
except:
    print("Not connected")
while True:
    post_shedule_post()
