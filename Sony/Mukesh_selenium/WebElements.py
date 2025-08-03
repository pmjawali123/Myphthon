# Deal with web elements
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.clear()
driver.refresh()
driver.maximize_window()


driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")
time.sleep(3)
driver.find_element(By.ID,"user-name").send_keys("standard_user")
time.sleep(3)
driver.find_element(By.NAME,"password").send_keys("secret_sauce")
time.sleep(3)
driver.find_element(By.NAME,"login-button").click()




time.sleep(10)

print("All Right, Please go ahead further Programming and Happy Coding")




