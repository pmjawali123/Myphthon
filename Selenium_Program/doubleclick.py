

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.common.devtools.v135.dom import scroll_into_view_if_needed

driver=webdriver.Chrome()
driver.maximize_window()
driver.refresh()

driver.implicitly_wait(10)
driver.get("https://testautomationpractice.blogspot.com/#")
button=driver.find_element(By.XPATH,"//button[@ondblclick='myFunction1()']")


act=ActionChains(driver)
act.double_click(button).perform()

driver.execute_script("window.scrollBy(0,2000",'')
time.sleep(10)

print("Good To Go,All the Best")
driver.quit()
