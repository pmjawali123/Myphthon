import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.clear()
driver.refresh()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://www.amazon.in/")





driver.find_element(By.ID,"twotabsearchtextbox").send_keys("mobile")
driver.find_element(By.ID,"nav-search-submit-button").click()


# driver.find_element(By.LINK_TEXT,"Register").click()


# links = driver.find_elements(By.TAG_NAME,"a")
# print(len(links))
#
# for link in links:
#     print(link.get_property("href"))

mobiles = driver.find_elements(By.CLASS_NAME,"s-image")
print(len(mobiles))
for  mob in mobiles:
    print(mob.get_property("alt"))
time.sleep(10)
