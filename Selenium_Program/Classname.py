#class and Tag locators

from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.amazon.in/alm/storefront?almBrandId=ctnow&ref_=nav_cs_fresh")
#driver.find_elements(By.CLASS_NAME,"")

tag=driver.find_elements(By.CLASS_NAME,"yAlKeh")
print(len(tag))

print("/********************************** # Happy Coding, All the Best Keep going!!! # *******************************/")
time.sleep(10)
driver.close()