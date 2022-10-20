def headless_chrome():
 from selenium import webdriver
 driver = webdriver.Chrome()
 driver.implicitly_wait(10)
 driver.get('https://demo.nopcommerce.com/')
 driver.maximize_window()
 # cookie=driver.get_cookies()
 # print(len(cookie))
 print(driver.title)
 driver.close()

 #Not Completed