import json

with open('c:\\Users\\throbby\\Documents\\GitHub\\DMCARequestor\\archetype_2013_09_14_18_44.json') as dataFile:
    jsonData = json.load(dataFile)

for site in jsonData['product']['sites']:
    print site