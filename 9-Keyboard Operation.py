import time
from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://text-compare.com/')
driver.maximize_window()
F=driver.find_element(By.XPATH,'//*[@id="inputText1"]')
S=driver.find_element(By.XPATH,'//*[@id="inputText2"]')
F.send_keys("WELCOME")
act=ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys("a")
act.key_up(Keys.CONTROL).perform()
act.key_down(Keys.CONTROL).send_keys("c")
act.key_up(Keys.CONTROL).perform()
act.send_keys(Keys.TAB).perform()
act.key_down(Keys.CONTROL).send_keys("v")
act.key_up(Keys.CONTROL).perform()
time.sleep(5)
driver.close()