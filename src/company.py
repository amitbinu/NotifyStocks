class company():
    def __init__(self,companyName):
        self.__company = companyName

    def set_company(self, companyName): 
         self.__company = companyName
  
    def get_company(self): 
        return self.__company 

    def getUrl(self,apiKey):
        baseUrl="https://financialmodelingprep.com/api/v3/company/discounted-cash-flow/"
        api="?apikey="
        return baseUrl + self.__company + api + apiKey
