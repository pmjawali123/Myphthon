import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.clear()


driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

rd_male_btn=(driver.find_element(By.ID,"gender-male"))
print("radio button is selected",rd_male_btn.is_selected())

rd_male_btn.click()


time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()