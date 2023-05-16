'''
--> Selenium contain multiple components like Selenium RC, Selenium IDE, Selenium webdriver and selenium webdriver is most
popular
it supports to automate web based application. Selenium contain number of functions and classes and classes have number
of methods and we can access all those methods by creating objects.
Actually selenium webdriver is an API because our automation script can not directly interact with browser.
Selenium web driver contain number classes and functions and classes contain number of methods by using this our
automation script can interact with browser.


--> Selenium Webdriver (4.8) used W3C(World Wide Web Consortium) protocol to interact with browser driver and browser driver
again used W3C protocol to interact with browser.
Selenium classes and methods are available in multiple languages.

------------------------------------------------------------------------------------------------------------------------

--> Selenium webdriver methods are, Find element(), Find elements(), window.handle(), window.handles(), get(), close(),
quite(),

------------------------------------------------------------------------------------------------------------------------

--> Locators- We use locators to identify the web elements from web page. We need to understand and perform the action
on web elements. In selenium webdriver there are multiple locators are available like, ID, NAME, LINK_TEXT, CLASS_NAME,
TAG_NAME, CSS_SELECTOR, XPATH.

--> ID-

from selenium import webdriver()
driver=webdriver.Chrome()
driver.get("URL")
driver.maximize_window()
driver.find_element(By.ID,"Search_BOX").send_keys("Shirts").click()
------------------------------------------------------------------------------------------------------------------------

--> NAME-

from selenium import webdriver()
driver=webdriver.Chrome()
driver.get("URL")
driver.maximize_window()
driver.find_element(By.NAME,"Submit_search").click()
------------------------------------------------------------------------------------------------------------------------

--> LINK_TEXT-

from selenium import webdriver
driver= webdriver.Chrome()
driver.get("URL")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Download").click()
------------------------------------------------------------------------------------------------------------------------

--> CLASS_NAME-

from selenium import webdriver()
driver=webdriver.Chrome()
driver.get("URL")
driver.maximize_window()
slides= driver.find_elements(By.CLASS_NAME,"Slides")
------------------------------------------------------------------------------------------------------------------------

--> TAG_NAME-

from selenium import webdriver()
driver=webdriver.Chrome()
driver.get("URL")
driver.maximize_window()
link=driver.find_elements(By.TAG_NAME,"a")
------------------------------------------------------------------------------------------------------------------------

--> Actually CLASS_NAME and TAG_NAME are used for identify number of elements from webpage,but the condition is that
these elements have same class.
--> In CLASS_NAME and TAG_NAME we have to use "Find.elements" methods to find out multiple elements.
--> TAG_NAME is used for find out the "multiple links" from webpage.
------------------------------------------------------------------------------------------------------------------------

--> CSS_SELECTOR- We can write CSS_SELECTOR with different combination like, TAG and ID, TAG and CLASS, TAG and attribute
TAG,CLASS and attribute
------------------------------------------------------------------------------------------------------------------------

--> XPATH- It is XML path which is used to find out the web elements from web page using HTML DOM(Document Object Model)
XPATH is an address of an elements

--> There are two types of XPATH-

1) Absolute XPATH - Absolute XPATH is start from the beginning, It starts from '/' , Absolute XPATH use tag and nodes and
Absolute XPATH is not stable.

2) Relative XPATH - Relative XPATH is not start from beginning it directly jump to the element on DOM, It starts with '//'
Relative XPATH use attribute. Relative XPATH is more stable.

------------------------------------------------------------------------------------------------------------------------

--> Relative XPATH is more stable than Absolute XPATH because, when developers introduce new element, change the location
of element, that time Absolute XPATH will break, in Absolute XPATH use tag and nodes but, in Relative XPATH use attribute
and attribute will never change that's why Relative XPATH is more stable than Absolute XPATH.

------------------------------------------------------------------------------------------------------------------------

--> Syntax of Relative XPATH- "//tag_name[@attribute='value']" OR "//*[@attribute='value']"
OR "//input[@id='search']"

------------------------------------------------------------------------------------------------------------------------

--> We can use XPATH options along with XPATH- AND, OR, contains(), start_with(), text()
--> When we want to find out dynamic element from web page we use contains() and start_with()
--> We can use OR operator instead of contains()  and  start_with().

------------------------------------------------------------------------------------------------------------------------


--> XPATH access- In XPATH access by making one element as a base element we can find out bottom element and top element
by using XPATH access we can traverse through DOM structure top to bottom and bottom to up.

--> Suppose, we can't able to find out element from the web page that time make one element as base element(SELF) and try
to find out Ancestor, Parent, Child, Descendant.

--> Keywords- Ancestor-Parent-"SELF"-Descendant-Child, Following, Following Sibling, Preceding, Preceding Sibling.

------------------------------------------------------------------------------------------------------------------------

--> Web driver Commands- There are multiple web driver commands are available.

1) Application Command- tittle, page_source, current_url
2) Conditional Command- is_displayed(), is_enable(), is_selectable()
3) Browser Command- close(), quit()
4) Navigational Command- forward(), back(), refresh()
5) Wait_Command- implicit_wait(), Explicit_wait()

--> tittle- To capture the tittle of the current web page
--> current_url- To capture the URL of current web page
--> page_source- To capture the source code of the web page


--> is_displayed()- It is used to identify the element is present or not on web page
--> is_enabled()- It is used to check element is enabled or not. Suppose search box is there buts we can't able to type
inside the search box
--> is_selected()- It is used to validate check box and redio buttons


--> close()- By using this method we can close single window of the browser but process is still running
--> quite()- By using this method we can close all windows of the browser along with the process

--> implicit_wait()
--> When we use "implicit wait" at the beginning of the automation script it will be applicable for all the statements
--> It work based on time
--> If the element is not found implicit wait through the exception
--> It will wait for given time period and if the element is find within time, it will go and execute next statement

--> explicit_wait()
--> It use multiple times in the script.
--> It work based on condition
--> It can handle the exception.
--> It is more efficiently

--> wait commands is used to solve the synchronization problem. All statements in the script will execute on browser
and sometimes script execution is very faster than application response in this situation script will not wait and there
is synchronization will occur.

-->
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("Amazon")
driver.maximize_window()
print(driver.tittle)
print(driver.page_source)
print(driver.current_url)
------------------------------------------------------------------------------------------------------------------------
search=driver.find_element(By.XPATH,"//input[@search-box='value']")
search.is_displayed()--True/False
search.is_enabled()--True/False
button=driver.find_element(By.XPATH,"//input[@id='button']")
button.is_selected()--False
button.click()
button.is_selected()--True
------------------------------------------------------------------------------------------------------------------------
driver.get("Facebook")
driver.back()
driver.forward()
driver.reload()
------------------------------------------------------------------------------------------------------------------------
driver.close()
driver.quit()
------------------------------------------------------------------------------------------------------------------------
driver.implicitly_wait(10)
wait=driver.wait(driver,10,ignored_exceptions[1,2,3],poll_frequency(2))
search=wait.until(Expected_condition((By.XPATH,""//*[@id='city'])
------------------------------------------------------------------------------------------------------------------------

--> find_element- It is method which return single web element.
--> If the element is not found it will thorough the exception.


--> find_elements- It is the method which return multiple web elements in the form list
--> It will not through the exception if the element is not found.

------------------------------------------------------------------------------------------------------------------------

--> text()- When want to capture inner text of the element we use text()
--> get_attribute()- When we want to capture value of any attribute of web element we use get_attribute('value')

-->driver.find_element(By.XPATH,"//a[text()='women']").click()
-->a=xyz
a.get_attribute('value')

------------------------------------------------------------------------------------------------------------------------

--> Different types of web elements and perform the action

1) Checkbox-

from selenium import webdriver
driver=webdriver.Chrome()
driver.get(Amazon")
driver.maximize_window()

--> Click on specific checkbox

driver.find_element(By.XPATH,"//input[@id='Monday']").click()

--> Select all checkboxes

checkbox=driver.find_element(By.XPATH,"//*[@id='checkbox']")
1-for checkboxes in checkbox:
checkboxes.click()
2-for i in range(len(checkbox))
checkbox[i].click()

--> Select multiple checkboxes based on choice

for checkboxes in checkbox:
w=checkboxes.get_attribute('id')
if w=='Monday' or w=='Sunday'
checkboxes.click()

--> Select last two checkboxes

for i in range(len(checkbox)-2,len(checkbox))
checkbox[i].click()

--> Select first two checkboxes

for i in range(len(checkbox))
if i<2:
checkbox.click()

--> How to unselect all checkboxes

for checkboxes in checkbox:
if checkboxes.is_selected():
checkboxes.click()
------------------------------------------------------------------------------------------------------------------------

2) Links-

Internal link- click on the link it will navigate on the same page
External Link- click on the link it will navigate some other page
Broken Link- It also available on web page but it doesn't have target page

--> Actually developers placed the broken link for the future implementation

--> How to click on the link-
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("Facebook")
driver.maximize_window()
driver.find_element(By.LINK_TEXT,"Download").click()

--> Count of links
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("Facebook")
driver.maximize_window()
link=driver.find_elements(By.TAG_NAME,"a")
print(len(link))

--> Print all links

for links in link
print(link.text)

--> How to handle broken links- Firstly we have to capture all href values of the link after that send the request to
server and server will give the response. If the response or status code is <= 400 then we confirm about the link is
broken

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("Facebook")
driver.maximize_window()
link=driver.find_elements(By.TAG_NAME,"a")
count=0
for links in link
url=links.get_attribute('href')
res=requests.head(url)
if res.status_code>=400
print(url,"It is broken link")
count+=1
else:
print(url,"It is not broken link")
------------------------------------------------------------------------------------------------------------------------

3) Dropdown- Is not a single element, it contain number of options and every option is a web element.To perform the
action on dropdown we have "select class" to use we have to import it.

--> Dropdown & it's different methods-
1) select_by_index()
2) select_by_value()
3) select_by_visible_text() -----> Preferred

from selenium import webdriver
driver=webdriver.Chrome()
driver.get("Facebook")
driver.maximize_window()
country=select(driver.find_element(By.XPATH,"//select[@id='countries']")
country.select_by_visible_text("India")

--> Total number of options in dropdown-

all = country.option
print("Total Options=",len(all))










'''