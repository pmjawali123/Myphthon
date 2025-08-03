from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
time.sleep(5)
driver.gethttps://opensource-demo.orangehrmlive.com/web/index.php/auth/login
driver.find_element(By.XPATH,("//*[@id='container']/div/div[3]/div/div[2]/div/form/div[1]/input")).send_keys("prakashjawali@gmail.com")

time.sleep(10)

driver.close()



print("Browser is succesfull")


