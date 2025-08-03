import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import alert_is_present

driver=webdriver.Chrome()
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)
