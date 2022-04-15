import urllib.request as request
import json
import os

with open('materials.json') as materials:
    items = json.load(materials)

folder_name = 'materials'
folder_common = 'common'
folder_characters = 'characters'
folder_weapons = 'weapons'
url = 'https://uploadstatic-sea.hoyoverse.com/hk4e/e20200928calculate/item_icon_ud09dc/'

if not os.path.exists(os.getcwd() + '/' + folder_name):
    os.makedirs(os.getcwd() + '/' + folder_name)
if not os.path.exists(os.getcwd() + '/' + folder_name + '/' + folder_common):
    os.makedirs(os.getcwd() + '/' + folder_name + '/' + folder_common)
if not os.path.exists(os.getcwd() + '/' + folder_name + '/' + folder_characters):
    os.makedirs(os.getcwd() + '/' + folder_name + '/' + folder_characters)
if not os.path.exists(os.getcwd() + '/' + folder_name + '/' + folder_weapons):
    os.makedirs(os.getcwd() + '/' + folder_name + '/' + folder_weapons)

commonItems = items['Common']
characterExp = items['Character']['Experience']
characterAsc = items['Character']['Ascension']
characterTalent = items['Character']['Talent']
weaponExp = items['Weapon']['Enhancement']
weaponAsc = items['Weapon']['Ascension']

for common in commonItems:
    if common['name']:
        filename = common['name'].replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = url + common['file'] + '.png'
        dest = './' + folder_name + '/' + folder_common + '/ascension_' + filename + '.png'
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue

for key, value in characterExp.items():
    if value:
        filename = key.replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = url + value + '.png'
        dest = './' + folder_name + '/' + folder_characters + '/exp_' + filename + '.png'
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue

for key, value in characterAsc.items():
    if value:
        filename = key.replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = url + value + '.png'
        dest = './' + folder_name + '/' + folder_characters + '/ascension_' + filename + '.png'
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue

for key, value in characterTalent.items():
    if value:
        filename = key.replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = url + value + '.png'
        dest = './' + folder_name + '/' + folder_characters + '/talent_' + filename + '.png'
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue

for key, value in weaponExp.items():
    if value:
        filename = key.replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = url + value + '.png'
        dest = './' + folder_name + '/' + folder_weapons + '/exp_' + filename + '.png'
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue

for key, value in weaponAsc.items():
    if value:
        filename = key.replace(" ", "_")
        filename = filename.replace( "'", "")
        filename = filename.lower()
        full = url + value + '.png'
        dest = './' + folder_name + '/' + folder_weapons + '/ascension_' + filename + '.png'
        try:
            request.urlretrieve(full, dest)
        except Exception as e:
            print(full)
            continue