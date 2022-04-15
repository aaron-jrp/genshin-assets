import urllib.request as request
import json
import os

with open('weapons.json') as weapons:
    items = json.load(weapons)

folder_name = 'weapons'
url = 'https://upload-os-bbs.mihoyo.com/game_record/genshin/equip/'

if not os.path.exists(os.getcwd() + '/' + folder_name):
    os.makedirs(os.getcwd() + '/' + folder_name)

for key, values in items.items():
    for value in values:
        if value['code_name']:
            segment = 'UI_EquipIcon_' + key + '_' + value['code_name'] + '.png'
            filename = value['name'].replace(" ", "_")
            filename = filename.replace( "'", "")
            filename = filename.lower()
            full = url + segment
            dest = './' + folder_name + '/' + key.lower() + '_' + filename + '.png'
            try:
                request.urlretrieve(full, dest)
            except Exception as e:
                print(full)
                continue