'''  For collegeboard Bigfuture website
Get the links of all colleges on my-college list for scraping later
Stores file on D:\collegelists.txt  '''

import time
from selenium import webdriver

#   open browser and navigate to the url
browser = webdriver.Chrome()
browser.get("https://bigfuture.collegeboard.org")

time.sleep(5)

#   type username
userSelect = browser.find_element_by_id("view7__username_pro")
userSelect.send_keys("username_here")

#   type password
pswdSelect = browser.find_element_by_id("view7__password_pro")
pswdSelect.send_keys("password_here")

#   submit form / click sign in
pswdSelect.submit()

time.sleep(3)

#   click on my colleges
browser.find_element_by_id("waistband_MyColleges").click()

time.sleep(5)

#   store a list of college in variable
collegeUrl = browser.find_elements_by_css_selector("div h4 a")

#   get the nth link and store that link in the nth place itself.
#   change webelements list to string list ao that it can be joined with join().
for link in range(0, len(collegeUrl)):
    collegeUrl[link] = collegeUrl[link].get_attribute("href")

#   join the list with CR+LF
collegeUrl = "\r\n".join(collegeUrl)

#   write contents of variable to txt file
file = open("D:\\collegelist.txt", "w")
file.write(collegeUrl)
file.close()

browser.quit()
