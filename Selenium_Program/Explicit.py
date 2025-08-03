# Sync application using implicit and explcit wait
from selenium.webdriver.common.by import By
from selenium import webdriver
import time

from selenium.webdriver.support.wait import WebDriverWait

driver=webdriver.Chrome()
mywait=WebDriverWait(driver,10)

driver.get("https://www.google.com/")
driver.maximize_window()

Search=driver.find_element(By.NAME,"q")
Search.send_keys("Selenium")
Search.submit()

driver.find_element(By.XPATH,"//h3[text()='Selenium']").click()

driver.close()






