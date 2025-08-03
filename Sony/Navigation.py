import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.clear()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
#driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
time.sleep(5)
driver.forward()
time.sleep(5)
driver.get("https://facebook.com")
time.sleep(5)
driver.refresh()
time.sleep(5)
driver.back()





time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.quit()