import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.expected_conditions import alert_is_present

driver=webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/javascript_alerts")
driver.find_element(By.XPATH,"//button[normalize-space()='Click for JS Prompt']").click()
time.sleep(5)

alertwindow=driver.switch_to.alert
alertwindow.send_keys("Welcome")
print(alertwindow.text)
# alertwindow.accept()

alertwindow.dismiss()
time.sleep(5)
