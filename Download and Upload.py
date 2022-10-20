# Download

'''from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.eclipse.org/downloads/')
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="openjdk-runtimes"]/div/div/div[1]/div/p[2]/a').click()'''

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

# How to capture Screen Shot

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.save_screenshot("D:\Selenium.png")
driver.quit()