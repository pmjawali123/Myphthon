import warnings

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from urllib3 import disable_warnings

warnings.filterwarnings("ignore")

driver=webdriver.Chrome()
driver.get("https://google.com/")
driver.maximize_window()

time.sleep(10)


