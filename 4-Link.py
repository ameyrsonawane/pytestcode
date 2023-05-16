# Link (Internal, External and Broken link)
import time

import requests as requests
from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# Select single link

driver.find_element(By.LINK_TEXT,'Digital downloads').click()

# Total no. of links

#Link=driver.find_elements(By.TAG_NAME,'a')
#print(len(Link))
#for Links in Link:
 #   print(Links.text)
'''import requests
# Broken Links

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://www.deadlinkcity.com/')
driver.maximize_window()
alllinks= driver.find_elements(By.TAG_NAME,'a')
                                                                             #count=0
for link in alllinks:
    URL=link.get_attribute('href')
    try:
     Res=requests.head(URL)
    except:
       None
    if Res.status_code>=400:
     print(URL,"Broken Link")
                                                                              #count+=1
    else:
     print(URL,"Valid Link")'''
                                                                              #print("Total no of broken links:",count)
