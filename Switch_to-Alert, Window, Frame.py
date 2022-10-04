# Alerts

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
#driver.get('https://the-internet.herokuapp.com/javascript_alerts')
#driver.maximize_window()
driver.find_element(By.XPATH,'//*[@id="content"]/div/ul/li[3]/button').click()
time.sleep(5)
alerts=driver.switch_to.alert
print(alerts.text)
alerts.send_keys("welcome")
time.sleep(2)
#alerts.accept()
alerts.dismiss()
time.sleep(5)
driver.quit()

# Authentication Popup (Used Injection method providing username and password)

driver.get('https://the-internet.herokuapp.com/basic_auth')

#driver.get('https://admin:admin@the-internet.herokuapp.com/basic_auth')
driver.maximize_window()
time.sleep(5)
driver.quit()'''

# Frame OR Iframe(3-Frames)

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html?overview-summary.html')
driver.maximize_window()
driver.switch_to.frame('packageListFrame')
driver.find_element(By.LINK_TEXT,'org.openqa.selenium').click()
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame('packageFrame')
driver.find_element(By.LINK_TEXT,'WebDriver').click()
driver.switch_to.default_content()
time.sleep(5)
driver.switch_to.frame('classFrame')
driver.find_element(By.XPATH,'/html/body/header/nav/div[1]/div[1]/ul/li[8]/a').click()
time.sleep(5)
driver.quit()'''

# Outer frame/Inner frame(2-Frames)

'''import time
from selenium import webdriver
driver=webdriver.Chrome()
from selenium.webdriver.common.by import By
driver.get('https://demo.automationtesting.in/Frames.html')
driver.maximize_window()
driver.find_element(By.XPATH,'/html/body/section/div[1]/div/div/div/div[1]/div/ul/li[2]/a').click()
outer=driver.find_element(By.XPATH,'//*[@id="Multiple"]/iframe')
driver.switch_to.frame(outer)

inner=driver.find_element(By.XPATH,'/html/body/section/div/div/iframe')
driver.switch_to.frame(inner)
driver.find_element(By.XPATH,'/html/body/section/div/div/div/input').send_keys("WELCOME")
time.sleep(5)
driver.quit()'''

# Browser window (Need to pass window ID)

import time
from selenium import webdriver
driver=webdriver.Chrome()
driver.implicitly_wait(10)
from selenium.webdriver.common.by import By
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
driver.maximize_window()
time.sleep(3)
driver.find_element(By.XPATH,'/html/body/div/div[1]/div/div[1]/div/div[2]/div[3]/div[2]/p[2]/a').click()
wid=driver.window_handles
'''PW=wid[0]
CW=wid[1]
driver.switch_to.window(CW)
driver.find_element(By.XPATH,'//*[@id="linkadd"]').click()
#driver.quit()'''

'''for winid in wid:
    driver.switch_to.window(winid)
    print(driver.title)'''

for winid in wid:
    driver.switch_to.window(winid)
    if driver.title=="OrangeHRM":
        driver.close()

