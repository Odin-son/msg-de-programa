import tweepy

api_key_ = ''
api_key_secret_ = ''
token_ = ''
token_secret_ = ''

auth = tweepy.OAuthHandler(api_key_, api_key_secret_)
auth.set_access_token(token_, token_secret_)
api = tweepy.API(auth)

def msg(str):
    api.update_status(status=str)

