from selenium import webdriver


driver=webdriver.Chrome()
driver.delete_all_cookies()
driver.get("https:\\google.com")
driver.maximize_window()