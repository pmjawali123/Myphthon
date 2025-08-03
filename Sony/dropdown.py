import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.clear()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

drpdown=Select(driver.find_element(By.ID,"country"))
#drpdown.select_by_index(5)
# drpdown.select_by_visible_text("India")
#drpdown.select_by_value("germany")


all=drpdown.options
print(len(all))

for opt in all:
    if opt.text == "India":
        opt.click()
        break








time.sleep(10)
driver.quit()

print("******************Program Executed successfully, Happy Coding******************")
