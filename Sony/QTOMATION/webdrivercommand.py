import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.clear()
driver.refresh()
driver.maximize_window()


driver.implicitly_wait(5)
driver.get("https://www.saucedemo.com/")

page_title=driver.title
print("Title of the Page:   ",page_title)
print(driver.current_url)
print(driver.title)

