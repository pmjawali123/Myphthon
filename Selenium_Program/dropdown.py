import time
from selenium.webdriver.common.by import By
from selenium import webdriver

import requests as requests
from selenium.webdriver.support.select import Select
from urllib3.util import url

driver=webdriver.Chrome()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
time.sleep(10)
kk=Select(driver.find_element(By.XPATH,"//input[@id='dropdown']"))
time.sleep(10)
select.select_by_index(3)

time.sleep(10)
