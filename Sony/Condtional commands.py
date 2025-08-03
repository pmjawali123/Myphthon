import driver
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
searchbox=(driver.find_element(By.ID,"small-searchterms"))
searchbox.is_enabled()
print("Enabled",searchbox.is_enabled())
print("Displayed",searchbox.is_displayed())
print("selected",searchbox.is_selected())
