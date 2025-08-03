import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.clear()


driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()

driver.find_element(By.NAME,"username").send_keys("Admin")
time.sleep(1)
driver.find_element(By.NAME,"password").send_keys("admin123")
time.sleep(1)
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(1)








time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()


