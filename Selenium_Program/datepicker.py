import time

from selenium import webdriver
from selenium.webdriver.common import by
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

driver=webdriver.Chrome()
driver.delete_all_cookies()
driver.get("https://jqueryui.com/datepicker/")
driver.maximize_window()

driver.implicitly_wait(10)
driver.switch_to.frame(0)
#driver.find_element(By.XPATH,"//input[@id='datepicker']").send_keys("06/27/2025")
time.sleep(5)

year="2026"
month="July"
date="19"
driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
while True:
    mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
    yr=driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    if mon==month and yr==year:
        break;
    else:
        driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-e']").click()

dates=driver.find_elements(By.XPATH,"//div[@id='ui-datepicker-div']//table/tbody/tr/td/a")

for ele in dates:
    if ele.text==date:
        ele.click()
        break

time.sleep(3)



driver.quit()


print("So far code looks good, Thank you!")



