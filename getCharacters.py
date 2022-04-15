import urllib.request as request
import json
import os

with open('characters.json') as units:
    items = json.load(units)

folder_name = 'characters'
urlCard = 'https://upload-os-bbs.mihoyo.com/game_record/genshin/character_card_icon/'
urlPortrait = 'https://upload-os-bbs.mihoyo.com/game_record/genshin/character_icon/'

if not os.path.exists(os.getcwd() + '/' + folder_name):
    os.makedirs(os.getcwd() + '/' + folder_name)

for portrait in items:
    if portrait['code_name']:
        segmentPortrait = 'UI_AvatarIcon_' + portrait['code_name'] + '.png'
        filename = portrait['code_name'].replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = urlPortrait + segmentPortrait
        dest = './' + folder_name + '/portrait_' + filename + '.png'
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue

for card in items:
    if card['code_name']:
        segmentCard = 'UI_AvatarIcon_' + card['code_name'] + '_Card.png'
        filename = card['code_name'].replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = urlCard + segmentCard
        dest = './' + folder_name + '/card_' + filename + '.png'
        request.urlretrieve(full, dest)
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue