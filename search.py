from google_search import search
from datetime import datetime
import json
import logging
import getopt
import sys
import re

###################################################################

# create logger
logger = logging.getLogger("executeScript")
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)

# create formatter
#formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
formatter = logging.Formatter('%(levelname)s : %(message)s')

# add formatter to ch
ch.setFormatter(formatter)

# add ch to logger
logger.addHandler(ch)

###################################################################

def usage (opts=''):
    if opts != '':
        for opt in opts:
            print 'Option missing: %s\n' % opt
    print '=' * 20, 'Usage','=' * 20, '\n'
    print '''
	--term 'your,search,terms,here'[REQUIRED]\n
	--product productname [REQUIRED]\n
	--usetxt (pushes out a clean text files with urls) [OPTIONAL]\n
	'''
    print '\n'
    sys.exit(1)	

def main():
    options = 'h'
    longOptions = [
        'term=',
        'product=',
        'usetxt'
    ]
    try :
	opts, pargs = getopt.getopt(sys.argv[1:], options, longOptions)
    except getopt.GetoptError, err:
	print '\nERROR: %s\n\n' % err
	usage()
	sys.exit(2)
    
    ### DEFAULT
    exportTXTURL = False
    results = 100
    
    for opt in opts:
	
	if opt[0] == '--term':
	    searchTerm = opt[1]
	elif opt[0] == '--product':
	    productName = opt[1]
	elif opt[0] == '--usetxt':
	    exportTXTURL = True
	elif opt[0] == '--results':
	    results = opt[1]

    ###### CHECK FOR OPTIONS
    missingOpts = []
    
    try:
	searchTerm
    except NameError:
	missingOpts.append('term')    
    try:
	productName
    except NameError:
	missingOpts.append('product')    

    if len(missingOpts) > 0 :
	usage(missingOpts)
	sys.exit(1)
    
    jsonData = searchGoogle(productName, searchTerm, results)
    writeJSON(jsonData)
    if exportTXTURL == True:
	writeTXT(jsonData)
	
def searchGoogle (productName, searchTerm, resultAmount):
	
    now = datetime.now()
    todayTime = '%02d %02d' % (datetime.time(now).hour,datetime.time(now).minute)
    todayDate = '%04d %02d %02d' % (datetime.date(now).year,datetime.date(now).month,datetime.date(now).day)
    
    #productName = 'archetype'
    #searchTerm = 'archetype vfx pipeline nederhorst torrent'
    
    urlList = []
    
    for url in search (searchTerm,stop=resultAmount):
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
	'tutsplus.com',
        'gnomonschool.com',
        'chillingeffects.org',
        'deviantart.com'
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
	    logger.info('Found : %s' % url)

    #illegalURLs = [targ for targ in urlList if any(re.search(r'(?!\b{})'.format(goodSite), targ, re.I) for goodSite in accetableSites)]
    #print matches	    
    
    outData['product']['sites']= illegalURLs
    return outData

def writeJSON (outData): 
    fh = open ('%s_%s_%s.json' % (outData['product']['name'], outData['product']['date'].replace(' ','_'), outData['product']['time'].replace(' ','_')), 'w')
    fh.write(json.dumps(outData, indent=4))
    fh.close()
    
def writeTXT (outData):
    fh = open ('%s_%s_%s_url.txt' % (outData['product']['name'], outData['product']['date'].replace(' ','_'), outData['product']['time'].replace(' ','_')), 'w')
    for site in outData['product']['sites']:
	fh.write ('%s\n' % site)
    fh.close()

if __name__ == '__main__':
    main()    