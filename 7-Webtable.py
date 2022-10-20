# Count of Rows and Columns

'''from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
Rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr"))
print("No of Rows",Rows)
Column=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//th"))
print("No of Column",Column)
driver.close()'''


# Read the Specific Data

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
data=driver.find_element(By.XPATH,"//table[@name='BookTable']//tr[7]/td[3]").text
print(data)
driver.close()



