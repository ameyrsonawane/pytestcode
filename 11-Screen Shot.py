# How to capture Screen Shot

from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.save_screenshot("D:\Selenium.png")
driver.quit()