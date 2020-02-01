from flask import Flask
from flask_restful import Api

import resources
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

api = Api(app)
api.add_resource(resources.TwitterSummarizer, '/summary')

if __name__ == '__main__':
    app.run()
