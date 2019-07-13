import os
import sys
import tweepy
import yaml
import random


def setup_api():
    auth = tweepy.OAuthHandler(os.getenv("CONSUMER_KEY"), os.getenv("CONSUMER_SECRET"))
    auth.set_access_token(os.getenv("ACCESS_TOKEN"), os.getenv("ACCESS_TOKEN_SECRET"))
    return tweepy.API(auth)


def choice_meigen():
    f = open("murano_tweets.yml", "r")
    murano_tweets = yaml.load(f, Loader=yaml.FullLoader)
    return random.choice(murano_tweets["tweet"])


# なぜか*argsで引数長を任意にしないとdeploy時に失敗する
def post_tweet(*args):
    api = setup_api()
    tweet = choice_meigen()
    status = api.update_status(status=tweet)
    return "Tweet Posted"


if __name__ == "__main__":
    post_tweet()
