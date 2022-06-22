
'''
Created on Feb 14, 2020

@author: Carciogenic!

'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest,HtmlTestRunner
import time

# How to run unittest  in cmd - D:\workspace\PyDev\PyDevPackage>python -m unittest PyDevModule.py

class GoogleSerch(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
               
        cls.driver=webdriver.Chrome("D:/BACK UP D/SElenium/chromedriver_win32/chromedriver.exe")
    
        cls.driver.maximize_window();
        cls.driver.implicitly_wait(10)
    #driver = webdriver.Firefox()
    def test_login(self):
        print('test started')
        self.driver.get("https://www.google.com/")  
        #identify the Google search text box and enter the value  
        self.driver.find_element_by_name("q").send_keys("javatpoint")  
        time.sleep(3)  
#click on the Google search button  
        self.driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
        time.sleep(3)  

    @classmethod
    
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()
        print("test successful")
    '''Below methods used to access the above functions'''   
if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='D:/workspace/PyDev/PyDevPackage/HTMreports'))