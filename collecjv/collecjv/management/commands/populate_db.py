from igdb.wrapper import IGDBWrapper
import requests
import json


client_id = 'mn03z6fvnt221t7uo6gby9ltfhwbqq'
client_secret = '4y3rm04ml420jc1b2mijzvcun4cscx'


body = {
    'client_id': client_id,
    'client_secret': client_secret,
    "grant_type": 'client_credentials'
}
r = requests.post('https://id.twitch.tv/oauth2/token', body)

# data output
keys = r.json()

print(keys)

headers = {
    'Client-ID': client_id,
    'Authorization': 'Bearer ' + keys['access_token']
}

print(headers)

stream = requests.post('https://api.igdb.com/v4/games', headers=headers, data="fields *;")

stream_data = stream.json()

print(stream_data)
