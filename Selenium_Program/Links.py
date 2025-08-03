
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
# driver.implicitly_wait(15)
driver.refresh()

driver.get("https://demo.nopcommerce.com/")
links = driver.find_element(By.XPATH,'//a')
time.sleep(5)

# actual_result=driver.title
# print(actual_result)
# expected_result=actual_result
# if actual_result=="Selenium Practice - Check Box":
#     print("Login is success, pleasd continue your coding")
# else:
#     print("Login is failed, Please verify  your code")