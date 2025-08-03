from argparse import Action

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver=webdriver.Chrome()
driver.maximize_window()
driver.refresh()

driver.implicitly_wait(10)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.find_element(By.XPATH,"//input[@placeholder='Username']").send_keys("Admin")
driver.find_element(By.XPATH,"//input[@placeholder='Password']").send_keys("admin123")
driver.find_element(By.XPATH,"//button[@type='submit']").click()


admin=driver.find_element(By.XPATH,"//a[@class='oxd-main-menu-item active']")
usermanage=driver.find_element(By.XPATH,"//span[normalize-space()='User Management']")
user=driver.find_element(By.XPATH,"//ul[@class='oxd-dropdown-menu']//li")


act=ActionChains(driver)
act.move_to_element(admin).move_to_element(usermanage).move_to_element(user).click().perform()


time.sleep(5)




print("Good To Go,All the Best")
driver.quit()