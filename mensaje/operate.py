import tweepy
import os
import json

list_content = ['api key', 'api key secret', 'token', 'token secret']
file_path = './config.json'

def create_file():
    data = {'info': []}
    data['info'].append({
        "api key" : "",
        "api key secret" : "",
        "token" : "",
        "token secret" : ""
    })
    with open(file_path, 'w') as out:
        json.dump(data, out, indent=4)

def write_info(json_data):
    for content in list_content:
        tmp = input('{}{}'.format(content, ' : '))
        json_data['info'][0][content] = tmp

def validate(json_data):
    for content in list_content:
        if json_data['info'][0][content] == '':
            return False

def msg(str):
    # as if file does not exist
    if not os.path.isfile(file_path):
        create_file()

    # as if empty
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    if not validate(json_data):
        write_info(json_data)

        with open(file_path, 'w') as out:
            json.dump(json_data, out, indent=4)

    # read config
    with open(file_path, 'r') as json_file:
        json_data = json.load(json_file)

    api_key_ = json_data['info'][0][list_content[0]]
    api_key_secret_ = json_data['info'][0][list_content[1]]
    token_ = json_data['info'][0][list_content[2]]
    token_secret_ = json_data['info'][0][list_content[3]]

    # set tweepy(twitter api)
    auth = tweepy.OAuthHandler(api_key_, api_key_secret_)
    auth.set_access_token(token_, token_secret_)
    api = tweepy.API(auth)

    # send message
    api.update_status(status=str)
