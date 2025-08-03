import time

from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.clear()


driver.get("https://www.swiggy.com/restaurants")
driver.maximize_window()

# sliders = driver.find_elements(By.CLASS_NAME,"sc-jDfjYv jA-dVNK")
# print(len(sliders))
links=driver.find_elements(By.TAG_NAME,'a')
print(len(links))
# link = (links.__getattribute__())
# print(link)
#
visible_links = [l for l in links if l.is_displayed() and l.get_attribute("href")]

for link in visible_links:
    print(f"Text: {link.text.strip()} | URL: {link.get_attribute('href')}")











time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()


