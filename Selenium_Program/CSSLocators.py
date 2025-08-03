from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()

driver.get("https://www.facebook.com/")
driver.maximize_window()

# driver.find_element(By.CSS_SELECTOR,"input#email").send_keys("Annabond@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input[data-testid=royal-email]").send_keys("royal@gmail.com")
driver.find_element(By.CSS_SELECTOR,"input#pass").send_keys("bond007")
driver.find_element(By.CSS_SELECTOR,"button._42ft").click()

time.sleep(5)




print("/********************************** # Happy Coding, All the Best Keep going!!! # *******************************/")
time.sleep(10)
driver.close()
