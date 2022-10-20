# Dropdown (Select class(Methods-select_by_visible_text/select_by_index/select_by_value))

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
driver=webdriver.Chrome()
driver.get('https://www.opencart.com/index.php?route=account/register')
driver.maximize_window()
allcountries=Select(driver.find_element(By.XPATH,'//*[@id="input-country"]'))
#allcountries.select_by_visible_text("India")
#time.sleep(7)
#driver.quit()

# Capture and Print all options

#all=allcountries.options
#print(len(all))
#for opt in all:
 #print(opt.text)

# without using built_in function

all=allcountries.options
for opt in all:
  if opt.text=="India":
    opt.click()
    break


