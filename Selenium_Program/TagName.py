#class and Tag locators

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.NAME, "username").send_keys("Admin")
driver.find_element(By.NAME, "password").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()

Links=driver.find_elements(By.TAG_NAME,"a")
time.sleep(10)
print(len("links"))




print("/********************************** # Happy Coding, All the Best Keep going!!! # *******************************/")

driver.close()