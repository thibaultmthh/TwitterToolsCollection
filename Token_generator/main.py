from flask import Flask, session, redirect, request
import json
import tweepy
import os

fullpath = os.path.abspath(__file__)
os.chdir(os.path.dirname(fullpath))

app = Flask(__name__)
data = {"request_token": "", "token": "", "api": ""}

def load_config():
    data = {"consumer_key": "", "consumer_secret":"", "host":"127.0.0.1","port":"5000", "path_callback":"callback"}
    try:
        with open("config.json", "r") as f:
            data = json.load(f)
            return data
    except:
        with open("config.json", "w") as f:
            json.dump(data, f)
            return data

config = load_config()
consumer_key = config["consumer_key"]
consumer_secret = config["consumer_secret"]
host = config["host"]
port = config["port"]
path_callback = config["path_callback"]
callback = 'http://{}:{}/{}'.format(host,port, path_callback)



@app.route('/')
def auth():
    try:
        auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
        url = auth.get_authorization_url()
        data['request_token'] = auth.request_token
        return redirect(url)
    except Exception as e:
        return "Erreur, maybe bad consumer_key or consumer_secret"


@app.route('/{}'.format(path_callback))
def twitter_callback():
    request_token = data['request_token']
    del data['request_token']

    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    auth.request_token = request_token
    verifier = request.args.get('oauth_verifier')
    auth.get_access_token(verifier)
    data['token'] = (auth.access_token, auth.access_token_secret)
    message = 'Copy this config in any config file  : <br/><br/>{{"consumer_key" : "{ck}",<br/>  "consumer_secret" : "{cs}",<br/>  "access_token" : "{at}",<br/>  "access_token_secret" : "{ats}"}}'.format(ck = consumer_key, cs = consumer_secret, at = auth.access_token,ats =auth.access_token_secret)
    return message


print("\n\n\n\n")
print("Go to http://{}:{}".format(host,port))
print("and follow instruction ")
print("\n\n\n\n")




if len(consumer_key) > 5 and len(consumer_secret) > 5:
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret, callback)
    url = auth.get_authorization_url()


    app.run(host=host, port = port)

else:
    print("Fill the config file (config.json) before start the server")
