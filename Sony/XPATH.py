from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support.select import Select


driver=webdriver.Chrome()
driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
driver.maximize_window()

driver.implicitly_wait(10)
time.sleep(10)
actual_result = driver.title
expected_result = "Order Food Online from India's Best Food Delivery Service | Swiggy"

if actual_result==expected_result:
    print("Title looks good")
else:
    print("Title is not matched")

# print(driver.current_url)
# print(driver.page_source)



#
# driver.find_element(By.XPATH,"//span[text()='Search']").click()
# driver.find_element(By.XPATH,"//input[contains(@class,ss)]").send_keys("Ghee Rice",Keys.ENTER)
#
# time.sleep(4)
# #driver.find_element(By.XPATH,"//span[text()='Restaurants']").click()
# driver.find_element(By.XPATH,"//*[text()='Sort by']").click()
#
#



time.sleep(10)
print("******************Program Executed successfully, Happy Coding******************")
driver.close()
