from flask import jsonify
from flask_restful import Resource
from twitter_handler import get_tweets
from google_vision import detect_objects

from webargs import fields
from webargs.flaskparser import use_args

import requests


def download_image(url):
    response = requests.get(url, stream=True)
    image_content = response.content
    return image_content


class TwitterSummarizer(Resource):
    @use_args({"user": fields.Str(required=True)})
    def get(self, args):
        tweets = get_tweets(args['user'])
        for tweet in tweets:
            for image in tweet.images:
                image_content = download_image(image['url'])
                objects = detect_objects(image_content)
                image.update({"objects": objects})
                print(image)
        tweets = [tweet.to_json() for tweet in tweets]
        return jsonify(tweets)
