# api-design-rjewing


## Setup
Install the requirements using:
```
pip3 install -r requirements.txt
```
To use the api, first set the following environment variables for your API keys:
```
TWITTER_API_KEY = XXXXXX
TWITTER_SECRET_KEY = XXXXXX
TWITTER_ACCESS_TOKEN = XXXXXX
TWITTER_ACCESS_SECRET = XXXXXX

GOOGLE_API_KEY = XXXXXX
GOOGLE_SECRET_KEY = XXXXXX
```

The flask server will import these environment variables and use them to access the twitter and google APIs.

Then run:
```
flask run
```

## Testing
We can test the API using curl:
```
curl http://155.41.14.49:5000/summary?user=elonmusk
```

Or by running unit tests:
```
python3 -m pytest
```