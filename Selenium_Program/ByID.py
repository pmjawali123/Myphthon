from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://demo.nopcommerce.com/")
time.sleep(6)
#driver.find_element(By.ID,"small-searchterms").send_keys("Lenovo Thinkpad Carbon Laptop")

driver.find_element(By.NAME,"q").send_keys("Lenovo Thinkpad Carbon Laptop")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
time.sleep(6)
