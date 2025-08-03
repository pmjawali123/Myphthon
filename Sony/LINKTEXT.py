from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver=webdriver.Chrome()
time.sleep(2)

driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)

#driver.find_element(By.LINK_TEXT,"Register").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()



time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()
