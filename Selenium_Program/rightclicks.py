

from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.refresh()

driver.implicitly_wait(10)
driver.get("https://www.tutorialspoint.com/selenium/practice/buttons.php")
# driver.find_element(By.XPATH,"//button[@class='btn btn-secondary']").click()
# time.sleep(5)

gg=driver.find_element(By.XPATH,"//button[@class='btn btn-secondary']")

act=ActionChains(driver)
act.context_click(gg).perform()

time.sleep(10)


print("Good To Go,All the Best")
driver.quit()