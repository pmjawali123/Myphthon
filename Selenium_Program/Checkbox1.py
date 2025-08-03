from selenium import webdriver
import time
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.refresh()
driver.get("https://testautomationpractice.blogspot.com/")
#driver.find_element(By.XPATH,"//input[@id='monday']").click()

checkboxs=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(checkboxs))

# for i in range(len(checkboxs)):
#     checkboxs[i].click() # this Ragne func clicks all the checkboxes.

# for checkbox in checkboxs:
#     checkbox.click()
#

# for checkbox in checkboxs:
#     weekname=checkbox.get_attribute('id')
#     if weekname=="Sunday" or weekname=="Monday":
#         checkbox.click()


for i in range(len(checkboxs)-4,(len(checkboxs))):
    checkboxs[i].click()
time.sleep(10)

  #  driver.quit()


















