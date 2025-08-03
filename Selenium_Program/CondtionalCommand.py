from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver=webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
#driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
#driver.get("https://www.facebook.com/")

driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")

title=driver.title
print(title)

url =driver.current_url
print(url)

# source=driver.page_source
# print(source)
time.sleep(5)
#search=driver.find_element(By.XPATH,"//input[@id='small-searchterms']")
# driver.find_element(By.XPATH,"//a[@class='ico-register']").click()
# time.sleep(5)

gm=driver.find_element(By.ID,"gender-male")
print("Enables status",gm.is_selected())
gf=driver.find_element(By.NAME,"Gender")
print("Enables status",gm.is_selected())

gm.click()
driver.find_element(By.ID,"FirstName").send_keys("Prakash")
driver.find_element(By.ID,"LastName").send_keys("Prakash123")
driver.find_element(By.ID,"Email").send_keys("Prakash@gmail.com")
driver.find_element(By.ID,"Company").send_keys("Google")

time.sleep(5)
driver.find_element(By.NAME,"Password").send_keys("Prakash123")
driver.find_element(By.ID,"ConfirmPassword").send_keys("Prakash123")
driver.find_element(By.ID,"register-button").click()





# time.sleep(5)
# print("Enabled Status",search.is_enabled())
# print("Displayed Satus",search.is_displayed())







# #driver.find_element(By.PARTIAL_LINK_TEXT,"Reg").click()
# driver.find_element(By.PARTIAL_LINK_TEXT,"Register").click()


print("/********************************** # Happy Coding, All the Best Keep going!!! # *******************************/")
time.sleep(10)
driver.close()