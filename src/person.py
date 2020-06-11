from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage
import auth
import httplib2
import os
import sendEmail

try:
    import argparse
    flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
except ImportError:
    flags = None

class person():
    def __init__(self,email,subject,stockPrices):
        self.__email = email
        self.__subject = subject
        self.__stockPrices= stockPrices

    def set_email(self, email): 
         self.__email = email
  
    def get_email(self): 
        return self.__email

    def set_subject(self, subject): 
         self.__subject = subject
  
    def get_subject(self): 
        return self.__subject
    
    def set_stockPrices(self, stockPrices):
        self.__stockPrices = stockPrices
        
    def get_stockPrices(self): 
        return self.__stockPrices

    def sendEmail(self):
        SCOPES = 'https://mail.google.com/'
        CLIENT_SECRET_FILE = 'credentials.json'
        APPLICATION_NAME = 'Gmail API Python Quickstart'
        authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
        credentials = authInst.get_credentials()

        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)
        sendInst = sendEmail.sendEmail(service)
        message = sendInst.create_message('test17291729@gmail.com',self.__email, self.__subject,self.createMessage())
        
        sendInst.send_message('me',message)

    def createMessage(self):
        msg="Hey, <br> <BLOCKQUOTE> Here are the price(s) for the stock(s) you chose: </BLOCKQUOTE> <br> <ul> "
        for key in self.__stockPrices:
            msg = msg + "<li>"
            msg = msg + key + " : " + self.__stockPrices[key] 
            msg = msg + "</li> <br>"

        msg = msg + "</ul>"
        return msg
        
