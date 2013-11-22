#This is called Craig, because it gets new MARC record IDs
#call getNewBNums() with the number of days to fetch, and it'll return a list of BNumbers of newly added items to NYPL catalog
# oh and add your bibliocommons api key mkay
import requests
import simplejson as json
import time

bibliokey = ""
bibliobase = "https://api.bibliocommons.com/v1/titles"
bibliotime = time.time()

marcurlbase = "http://catalog.nypl.org/xrecord="

def biblioget(p):
    global bibliotime
    while time.time() < bibliotime + 0.51:
        time.sleep(0.001)
    r=requests.get(bibliobase, params = p)
    bibliotime = time.time()
    return r

def getNewBNums(daysToGet=7):
    bnums = []
    pagenum = 1
    while True:
        # Turn this into a function afterwards
        
        
        query = "nw:[0 TO %d]" %daysToGet
        
        
        
        param_base= {"library":"nypl", "search_type":"custom", "q":query, "limit":"100", "page":str(pagenum), "metadata":"0", "date_format":"iso8601", "locale":"en-US", "api_key":bibliokey}
        
        r=biblioget(param_base)
        #print r.json()
        
        response = r.json()
        
        #figure out how many more calls we have
        totalItems = int(response['count'])
        pages = int(response['pages'])
        perPage = int(response['limit'])
        
        for i in response['titles']:
            biblioB = i['id']
            bNum = "b"+biblioB[0:-6]
            bnums.append(bNum)
                
        #Captured them all
        pagenum +=1
        if pagenum > pages:
            break
    
    return bnums


