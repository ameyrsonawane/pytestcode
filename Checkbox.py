# Checkboxes

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get('https://itera-qa.azurewebsites.net/home/automation')
driver.maximize_window()
# select single checkbox

#driver.find_element(By.XPATH,'//*[@id="monday"]').click()

#driver.find_element(By.XPATH,'//*[@id="thursday"]').click()

# Print length of checkboxes

checkbox=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
print(len(checkbox))

# select all checkboxes

for checkboxes in checkbox:
    checkboxes.click()
    time.sleep(1)
# select checkboxes by choice

   # weekname=checkboxes.get_attribute('id')
    #if weekname=='monday' or weekname=='sunday':
     #   checkboxes.click()

# select last 2 checkboxes

#for i in range(len(checkbox)-2,len(checkbox)):
 #   checkbox[i].click()'''

# select first 2 checkboxes

#for i in range(len(checkbox)):
 #   if i<2:
  #      checkbox[i].click()

# unselect checkboxes
'''for checkboxes in checkbox:
    if checkboxes.is_selected():
      checkboxes.click()
time.sleep(3)
driver.quit()'''
