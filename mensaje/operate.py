import tweepy
import os
import json

list_content = ['api key', 'api key secret', 'token', 'token secret']
file_path = './config.json'

def init():
    data = {'info': []}
    data['info'].append({
        "api key" : "",
        "api key secret" : "",
        "token" : "",
        "token secret" : ""
    })
    with open(file_path, 'w') as out:
       json.dump(data, out, indent=4)

def set(json_data):
    for content in list_content:
        #print(content, ' : ')
        tmp = input('{}{}'.format(content, ' : '))
        json_data['info'][0][content] = tmp

def validate(json_data):
    for content in list_content:
        if json_data['info'][0][content] == '':
            return False

def msg(str):
    # as if file does not exist
    if not os.path.isfile(file_path):
        init()

    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    if not validate(json_data):
        set(json_data)

    # if auth
    with open(file_path, 'w') as out:
       json.dump(json_data, out, indent=4)

    # ready for input

    # read config
    api_key_ = ''
    api_key_secret_ = ''
    token_ = ''
    token_secret_ = ''

    # set tweepy(twitter api)
    auth = tweepy.OAuthHandler(api_key_, api_key_secret_)
    auth.set_access_token(token_, token_secret_)
    api = tweepy.API(auth)

    # send message
    api.update_status(status=str)
