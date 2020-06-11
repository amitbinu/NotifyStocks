import ConfigParser
from company import company
from person import person
import importlib
sp = importlib.import_module("getStockPrice")

config = ConfigParser.ConfigParser()
config.read("../apiKeys.properties")
apiKey=config.get("financialmodelingprep", "notifyStocksApiKey")

companies=["GOOGL","DGLY","SNE"]

stockPrices={}

#testStockPrices={'DGLY': "5.37", 'SNE': "70.51", 'GOOGL': "1464.7"}

for comp in companies:
    companyObj = company(comp)
    url = companyObj.getUrl(apiKey)
    stockPrice = sp.getStockPrice(url)
    stockPrices[comp] = str(stockPrice)

binu = person("binua@mcmaster.ca","Stock Notifications",stockPrices)
binu.sendEmail()

#print(sp.getStockPrice(url))



