# How to handle cookies

from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
driver.implicitly_wait(10)
cookie=driver.get_cookies()
#print(len(cookie))
#driver.close()

# Print details of all cookies

#for cookies in cookie:
#    print(cookies)


for cookies in cookie:
    print(cookies.get('name'))
#driver.delete_all_cookies()
#driver.get_cookies()
driver.close()
