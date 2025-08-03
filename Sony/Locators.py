from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://demo.nopcommerce.com/")
driver.maximize_window()
time.sleep(2)
driver.find_element(By.ID,"small-searchterms").send_keys("button-1 search-box-button")

driver.find_element(By.XPATH,"//button[@type='submit']").click()

time.sleep(5)




time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()
