import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.clear()


driver.get("https://www.facebook.com/")
driver.maximize_window()

time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'input#email').send_keys("prakashjawali@gmail.com")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'input#pass').send_keys("India@123")
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,'button[data-testid=royal-login-button]').click()
# tagname as button and attirbute values are considerd for login button






time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()
