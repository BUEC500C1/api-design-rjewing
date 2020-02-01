import requests
import tweepy
from config import Config

auth = tweepy.OAuthHandler(Config.TWITTER_API_KEY, Config.TWITTER_SECRET_KEY)
auth.set_access_token(Config.TWITTER_ACCESS_TOKEN,
                      Config.TWITTER_ACCESS_SECRET)

api = tweepy.API(auth)


class Tweet():
    def __init__(self, tweet):
        self.user = tweet.user.screen_name
        self.text = tweet.text
        self.images = []

        for media in tweet.entities.get("media", [{}]):
            # checks if there is any media-entity
            if media.get("type", None) == "photo":
                # checks if the entity is of the type "photo"
                self.images.append({ "url": media["media_url"]} )

    def __repr__(self):
        return f'{{"user": {self.user}, "text": {self.text}, "media": {self.images}}}'

    def __str__(self):
        return f"@{self.user}: \"{self.text}\" -- Media: {self.images}"

    def to_json(self):
        return {"user": self.user, "text": self.text, "media": self.images}


def get_tweets(username):
    timeline_statuses = api.user_timeline(username)
    tweets = [Tweet(tweet) for tweet in timeline_statuses]
    return tweets
