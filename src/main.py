import ConfigParser
from company import company
import importlib

sp = importlib.import_module("getStockPrice")

config = ConfigParser.ConfigParser()
config.read("../apiKeys.properties")

apiKey=config.get("financialmodelingprep", "notifyStocksApiKey")

apple = company("GOOGL")

url = apple.getUrl(apiKey)

print(sp.getStockPrice(url))
