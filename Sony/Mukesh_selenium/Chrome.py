from selenium import webdriver

driver = webdriver.Chrome()
print(type(driver))
driver.get("https://www.google.com/")
myDriver = driver.title
print("My Driver is name :  ",myDriver)

#assert "google" in myDriver

