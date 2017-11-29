import twitter
import os
import urllib.request

# Constants
ACCESS_TOKEN_KEY = 'ACCESS_TOKEN_KEY'
ACCESS_TOKEN_SECRET = 'ACCESS_TOKEN_SECRET'
CONSUMER_KEY = 'CONSUMER_KEY'
CONSUMER_SECRET = 'CONSUMER_SECRET'

def get_api_credentials():
    return {
        'consumer_key': os.getenv('CONSUMER_KEY'),
        'consumer_secret': os.getenv('CONSUMER_SECRET'),
        'access_token_key': os.getenv('ACCESS_TOKEN_KEY'),
        'access_token_secret': os.getenv('ACCESS_TOKEN_SECRET')
}

twitter_api = twitter.Api(**get_api_credentials())

def lambda_handler(event, context):

    result = twitter_api.GetUser(screen_name="rory_jacob")

    print(str(result))

    return 'It is working'
