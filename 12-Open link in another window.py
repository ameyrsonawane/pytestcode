# Open link in another window

'''import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
rlink=Keys.CONTROL+Keys.RETURN
driver.find_element(By.XPATH,'/html/body/div[6]/div[1]/div[1]/div[2]/div[1]/ul/li[1]/a').send_keys(rlink)
time.sleep(15)
driver.quit()'''


# Switch to New Tab

'''from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.eclipse.org/downloads/')
driver.switch_to.new_window('tab')
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()'''