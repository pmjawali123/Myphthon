from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

time.sleep(2)
rows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
time.sleep(5)
col=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']//tr[1]/th"))
#
# print(rows)
# print(col)

#Print table data
#
# data=driver=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[5]/td[2]").text


for r in range(2,rows+1):
    for c in range(1,col+1):
        data1 = driver = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text


# for c in range(2,rows+1):
#     for r in range(1,col+1):
#         data = driver = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr[" + str(r) + "]/td[" + str(
#             c) + "]").text

print(data1)








