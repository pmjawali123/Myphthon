from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://facebook.com/")
driver.maximize_window()
time.sleep(4)
#driver.save_screenshot("C:\Screenshot\homepage.png")
driver.get_screenshot_as_png("C:/Screenshot/homepage3")



time.sleep(2)
driver.find_element(By.ID,"small-searchterms").send_keys("button-1 search-box-button")


driver.save_screenshot("C:\Screenshot\homepage.png")


time.sleep(5)




time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()
