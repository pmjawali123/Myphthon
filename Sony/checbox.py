import time
from selenium import webdriver
from selenium.webdriver.common.by import By


driver=webdriver.Chrome()
driver.implicitly_wait(10)
driver.delete_all_cookies()
driver.clear()

driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.implicitly_wait(10)

#driver.find_element(By.ID,"sunday").click()

# checkboxes=driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
#print(len(checkboxes))
#
# for i in range (len(checkboxes)):
#    checkboxes[i].click()

# for checkbox in checkboxes:
#     checkbox.click()

# for checkbox in checkboxes:
#     week=checkbox.get_attribute("id")
#     if week=="monday" or week=="saturday":
#         checkbox.click()
#         time.sleep(10)



# for i in range (len(checkboxes)):
#     if i>2:
#         checkboxes[i].click()
#         time.sleep(10)


# for checkbox in checkboxes:
#     if checkbox.is_selected():
#         checkbox.click()




driver.find_elements(By.XPATH,"//input[@type='checkbox' and contains(@id,'day')]")
links=driver.find_elements(By.XPATH,"//a")
print(len(links))
for link in links:
    print(link.text)


print("******************Program Executed successfully, Happy Coding******************")
