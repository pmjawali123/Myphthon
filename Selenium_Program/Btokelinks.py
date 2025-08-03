import link
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

import requests as requests
from urllib3.util import url

driver=webdriver.Chrome()

driver.maximize_window()
driver.implicitly_wait(10)
driver.get("https://www.tutorialspoint.com/selenium/practice/links.php")

alllinks = driver.find_elements((By.TAG_NAME,"a"))

count = 0
for link in alllinks:
    url=link.get_attribute("href")
    try:
    res = requests.head(url)
    expect:
        var = None

    if res.status_code>=400:
        print("This is the progrm link")
        count+=1
    else:
        print(url, "Valid link")
