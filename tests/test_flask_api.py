import sys

sys.path.append('./src')

APP_URL = "http://localhost:5000/summary?user=elonmusk"


def test_twitter_api():
    from twitter_handler import get_tweets
    tweets = get_tweets('elonmusk')
    assert tweets is not None


def test_download_image():
    from resources import download_image
    image = download_image('http://placehold.it/120x120&text=image1')
    with open('./tests/test_image.png', 'rb') as f:
        control_image = f.read()
    assert image == control_image


def test_server():
    from api import app  # noqa: E402
    client = app.test_client()
    data = client.get('/summary?user=elonmusk')
    assert data._status_code == 200


def test_server_missing_parameter():
    from api import app  # noqa: E402
    client = app.test_client()
    data = client.get('/summary')
    assert data._status_code != 200
