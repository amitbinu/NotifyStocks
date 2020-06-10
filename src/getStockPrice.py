try:
    from urllib.request import urlopen
except ImportError:
    from urllib2 import urlopen

import json

def getStockPrice(url):
    response = urlopen(url)
    data = response.read().decode("utf-8")
    jsonObj = json.loads(data)
    return jsonObj["Stock Price"]



