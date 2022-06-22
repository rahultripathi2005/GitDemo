

from selenium import webdriver

import time  
from selenium.webdriver.common.keys import Keys

class launch:

    def test_setup(self):
        global driver
        driver=webdriver.Chrome("D:/BACK UP D/SElenium/chromedriver_win32/chromedriver.exe")

        driver.maximize_window();
    def openbrower(self):
        
        print("sample test case started")  
         
        #driver=webdriver.firefox()  
        #driver=webdriver.ie()  
            #maximize the window size  
        driver.maximize_window()  
        #navigate to the url  
        driver.get("https://www.google.com")  
        #identify the Google search text box and enter the value  
        driver.find_element_by_name("q").send_keys("javatpoint")  
        time.sleep(3)  
#click on the Google search button  
        driver.find_element_by_name("btnK").send_keys(Keys.ENTER)
        time.sleep(3)  
#close the browser  
    def close(self):
        driver.close()  
        print("sample test case successfully completed")  

o=launch()
o.test_setup()
o.openbrower()
o.close()






















































