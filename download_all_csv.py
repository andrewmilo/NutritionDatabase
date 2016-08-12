'''
    Downloads all CSV files from the USDA GOV Nutrition Database.
'''
import urllib
from bs4 import BeautifulSoup
import urllib2
import httplib
import ThreadPool
from ThreadPool import ThreadPool

n = 9315 # food count
URL_ROOT = 'https://ndb.nal.usda.gov/ndb/foods/show/'

def try_link( linkpair ):

    try:
        urllib.URLopener().retrieve( linkpair[0] , 'csv/' + linkpair[1] )
    except urllib2.HTTPError, e:
        print "HTTP Error"
    except urllib2.URLError, e:
        print "URL Error"
    except httplib.HTTPException, e:
        print "HTTP Exception"
    except Exception:
        print "Unknown Error"

links = []
idx = 1
while idx <= n:
    links.append( ( URL_ROOT + str(idx) + '?format=Full&reportfmt=csv', str(idx) + '.csv' ) )
    idx += 1

pool = ThreadPool(20)

pool.map( try_link, links )
pool.wait_completion()