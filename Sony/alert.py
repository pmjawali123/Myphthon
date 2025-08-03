from selenium import webdriver
from selenium.webdriver.common.by import  By
import time

driver=webdriver.Chrome()
time.sleep(2)
driver.get("https://www.hyrtutorials.com/p/alertsdemo.html/")
driver.maximize_window()
time.sleep(2)