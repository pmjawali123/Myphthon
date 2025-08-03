from selenium import webdriver
import time
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.tutorialspoint.com/selenium/practice/links.php")
driver.find_element(By.LINK_TEXT,'Home').click()
links=driver.find_elements(By.TAG_NAME,"a")

print(len(links))


for link in links:
    print(link.text)


time.sleep(10)


