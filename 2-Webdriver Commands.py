# Application Commands
import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://opensource-demo.orangehrmlive.com')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
print(driver.page_source)
time.sleep(3)
driver.close()

# Conditional Commands(True/False/Validation purpose at element level)

'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/register')
driver.maximize_window()
searchbox=driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
print("Display_Status:",searchbox.is_displayed())

search=driver.find_element(By.XPATH,'//*[@id="small-searchterms"]')
print("Enabled_Status:",search.is_enabled())

Mrb=driver.find_element(By.XPATH,'//*[@id="gender-male"]')
print("Selected_Status:",Mrb.is_selected())
Mrb.click()
print("Selected_Status:",Mrb.is_selected())
time.sleep(3)
driver.close()'''

# Browse Commands
# Driver.close() - Close single browser window
# Driver.quit() - Close multiple browser window along with process.

# Navigational Commands

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://demo.nopcommerce.com/')
driver.maximize_window()
driver.get('https://accounts.google.com/')
driver.maximize_window()
driver.back()
time.sleep(5)
driver.forward()
driver.refresh()
time.sleep(3)
driver.close()'''

# Wait Commands(To solve the synchronization problem)
# Implicit_wait()
# Explicit_wait()
'''import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.google.com/')
driver.maximize_window()
search=driver.find_element(By.NAME,'q')
search.send_keys("Selenium")
search.submit()
driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/a/h3').click()
time.sleep(3)
driver.close()'''



# Find_element(Return single web_element)
# Find_elements(Return multiple web_elements in term of list)


# Text and Get_attribute('value')

# Text can captured inner text of any element
# Get_attribute('value') captured value of any attribute.


