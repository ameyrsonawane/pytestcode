# Mouse Operation
# By using driver.ActionChains() we can perform mouse operations


# Mouse over

'''import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://www.orangehrm.com/')
driver.maximize_window()

platform=driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[1]/a')
peoplemgnt=driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[1]/div/div/div/div/ul/li[1]')
reporting=driver.find_element(By.XPATH,'//*[@id="navbarSupportedContent"]/ul/li[1]/div/div/div/div/ul/li[1]/div/div/h6[3]/a')

act=ActionChains(driver)
act.move_to_element(platform).move_to_element(peoplemgnt).move_to_element(reporting).click().perform()
time.sleep(2)
driver.close()'''
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

# Right click()

'''import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.get('https://swisnl.github.io/jQuery-contextMenu/demo.html')
driver.maximize_window()
rclick=driver.find_element(By.XPATH,'/html/body/div/section/div/div/div/p/span')
act=ActionChains(driver)
act.context_click(rclick).perform()
time.sleep(3)
driver.close()'''


# Double click()

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://testautomationpractice.blogspot.com/')
driver.maximize_window()
dclick=driver.find_element(By.XPATH,'//*[@id="HTML10"]/div[1]/button')
act=ActionChains(driver)
act.double_click(dclick).perform()
time.sleep(3)
driver.close()'''


# Drag and Drop


'''from selenium import webdriver
driver=webdriver.Chrome()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
driver.maximize_window()
drag=driver.find_element(By.XPATH,'//*[@id="box3"]')
drop=driver.find_element(By.XPATH,'//*[@id="box103"]')
act= ActionChains(driver)
act.drag_and_drop(drag,drop).perform()'''


# Slider Element

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.jqueryscript.net/demo/Price-Range-Slider-jQuery-UI/')
driver.maximize_window()
min=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[1]')
max=driver.find_element(By.XPATH,'//*[@id="slider-range"]/span[2]')
#print(min.location)      #{'x': 59, 'y': 251}
#print(max.location)      #{'x': 613, 'y': 251}



act=ActionChains(driver)
act.drag_and_drop_by_offset(min,100,0).perform()
act.drag_and_drop_by_offset(max,-39,0).perform()
print(min.location)     #{'x': 159, 'y': 251}
print(max.location)     #{'x': 574, 'y': 251}
time.sleep(3)
driver.close()'''




# Scrolling

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()
#driver.execute_script("window.scrollBy(0,1500)","")
#time.sleep(5)
#driver.close()
flag=(driver.find_element(By.XPATH,'//*[@id="content"]/div[2]/div[2]/table[1]/tbody/tr[86]/td[1]/img'))
driver.execute_script("arguments[0].scrollIntoView();",flag)
time.sleep(5)
driver.close()'''


# Scroll down page till end

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.get('https://www.countries-ofthe-world.com/flags-of-the-world.html')
driver.maximize_window()
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")
time.sleep(5)

# Scroll up to starting point

driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)")
time.sleep(5)
driver.close()