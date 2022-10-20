# Flipkart Application
'''
import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(20)
driver.get('https://www.flipkart.com/')
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[1]/input').send_keys("8550985895")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[2]/input').send_keys("Flipkart#01")
time.sleep(2)
driver.find_element(By.XPATH,'/html/body/div[2]/div/div/div/div/div[2]/div/form/div[4]/button').click()
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys("livpure water filter")
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[4]/div/div/div/a/div[1]/div[1]/div/div/img').click()
wid=driver.window_handles
PW=wid[0]
CW=wid[1]

driver.switch_to.window(CW)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button').click()
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys("Dell Laptop")
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[2]/div/div/div/a/div[2]/div[1]/div[1]').click()
G=driver.window_handles
GD=G[2]
driver.switch_to.window(GD)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/div/input').send_keys("T Shirt for girls")
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[1]/div[1]/div[2]/div[2]/form/div/button').click()
time.sleep(5)
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[2]/div[9]/div/div[2]/div/a/div[1]/div/div/div/img').click()
D=driver.window_handles
DD=D[3]
driver.switch_to.window(DD)
driver.find_element(By.XPATH,'//*[@id="swatch-2-size"]/a').click()
driver.find_element(By.XPATH,'//*[@id="container"]/div/div[3]/div[1]/div[1]/div[2]/div/ul/li[1]/button').click()
#driver.close(PW[0])
time.sleep(3)
hold=driver.find_element(By.XPATH,'/html/body/div[1]/div/div[2]/div/div[1]/div[1]/div/div[6]/div/form/button').click()'''


# Naukri.com Application

import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.naukri.com/')
driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="login_Layer"]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[2]/input').send_keys("amey.sonawane1@gmail.com")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[3]/input').send_keys("Nishtha@sonawane#01")
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div[4]/div[2]/div/div/div[2]/div/form/div[6]/button').click()
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/span/div/div/div/div[2]/div/div[2]/div[1]/div/a[1]/div[2]/div[1]').click()
time.sleep(3)
driver.find_element(By.XPATH,'//*[@id="root"]/div/div/span/div/div/div/div/div/div[2]/div[2]/div/div/ul/li[2]/a').click()








