from google_search import search
from datetime import datetime
import json
#from pprint import pprint

now = datetime.now()
todayTime = '%02d %02d' % (datetime.time(now).hour,datetime.time(now).minute)
todayDate = '%04d %02d %02d' % (datetime.date(now).year,datetime.date(now).month,datetime.date(now).day)

productName = 'archetype'
searchTerm = 'archetype vfx pipeline nederhorst torrent'

urlList = []

for url in search (searchTerm,stop=100):
    urlList.append(url)

accetableSites = [
    'amazon.com',
    'thegnomonworkshop.com',
    'cgchannel.com',
    'vray.info',
    'thefoundry.co.uk',
    'youtube.com',
    'vimeo.com',
    'pixologic.com',
    'twitter.com',
    'facebook.com',
    '3dtotal.com',
    'tutsplus.com'
    ]

outData = {
    'product':
    {
        'name':productName,
        'searchterm':searchTerm,
        'date':todayDate,
        'time':todayTime        
    }
    }

illegalURLs = []
for url in urlList:
    foundIllegalSite = False
    for goodSite in accetableSites:
        if goodSite.lower() in url.lower():
            break
    else:
        illegalURLs.append(url)

outData['product']['sites']= illegalURLs

#with open ('results.json','w') as outfile:
#    json.dump(outData, outfile)
fh = open ('%s_%s_%s.json' % (productName, todayDate.replace(' ','_'), todayTime.replace(' ','_')), 'w')
fh.write(json.dumps(outData, indent=4))
fh.close()
    