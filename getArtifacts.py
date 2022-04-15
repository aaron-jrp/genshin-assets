import urllib.request as request
import json
import os

with open('artifacts.json') as artifacts:
    items = json.load(artifacts)

folder_name = 'artifacts'
url = 'https://upload-os-bbs.mihoyo.com/game_record/genshin/equip/'

if not os.path.exists(os.getcwd() + '/' + folder_name):
    os.makedirs(os.getcwd() + '/' + folder_name)

for key, values in items.items():
    for value in values:
        if value['key']:
            for _type in value['types']:
                if _type:
                    idx = value['types'].index(_type) + 1
                    segment = 'UI_RelicIcon_' + str(value['key']) + '_' + str(idx) + '.png'
                    filename = key.replace(" ", "_")
                    filename = filename.replace( "'", "")
                    filename = filename.lower()
                    full = url + segment
                    dest = './' + folder_name + '/' + str(value['key']) + '-' + str(idx) + '_' + filename + '.png'
                    try:
                        request.urlretrieve(full, dest)
                    except Exception as e:
                        print(full)
                        continue