'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()

# ID and NAME

driver.find_element(By.ID,'small-searchterms').send_keys("Asus N551JK-XO076H Laptop")
time.sleep(2)
driver.find_element(By.NAME,'q').send_keys("Asus N551JK-XO076H Laptop")
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="small-search-box-form"]/button').click()
time.sleep(3)


# Link_TEXT and PARTIAL_LINK_TEXT

driver.find_element(By.LINK_TEXT,'Register').click()
time.sleep(2)

driver.find_element(By.PARTIAL_LINK_TEXT,'Reg').click()
time.sleep(3)
driver.close()

#CLASS_NAME and TAG_NAME(Find Multiple Elements)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()
sliders=driver.find_elements(By.CLASS_NAME,'homeslider-container')
print(len(sliders))
time.sleep(3)
Links=driver.find_elements(By.TAG_NAME,'a')
print(len(Links))
time.sleep(3)
driver.close()

#CSS_SELECTOR and XPATH (Customized Locators)

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://www.facebook.com/login/')
driver.maximize_window()
driver.find_element(By.CSS_SELECTOR,'input#email').send_keys("Amey")
driver.find_element(By.CSS_SELECTOR,'#email').send_keys("Amey")
driver.find_element(By.CSS_SELECTOR,'input.inputtext ').send_keys("Amey")
driver.find_element(By.CSS_SELECTOR,'.inputtext').send_keys("Amey")
driver.find_element(By.CSS_SELECTOR,'input[autocomplete=username]').send_keys("Amey")
driver.find_element(By.CSS_SELECTOR,'[autocomplete=username]').send_keys("Amey")
driver.find_element(By.CSS_SELECTOR,'input.inputtext[autocomplete=username]').send_keys("Amey")
driver.find_element(By.CSS_SELECTOR,'.inputtext[autocomplete=username]').send_keys("Amey")
driver.find_element(By.XPATH,'//*[@id="email"]').send_keys("Amey")
time.sleep(3)
driver.close()

# XPATH with AND/OR Operator

import time
from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get('http://automationpractice.com/index.php')
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='search_query_top' and @name='search_query']").send_keys("T-shirts")

#TEXT()...(Capture the innertext of element)

#driver.find_element(By.XPATH,"//a[text()='Women']").click()
driver.find_element(By.XPATH,'//*[@id="block_top_menu"]/ul/li[1]/a').click()
time.sleep(3)
driver.close()'''
