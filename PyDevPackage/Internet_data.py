'''
Created on Jun 7, 2020

@author: Carciogenic!
'''
# How to get the Internet data 

import urllib.request

class internet:
    
    def internetcodes(self):
        Url=urllib.request.urlopen("https://www.google.co.in/")
    
        #This will print the codes 
        print("the result code", str(Url.getcode()))
        data=Url.read()
        print(data)
    
i=internet()
i.internetcodes()  