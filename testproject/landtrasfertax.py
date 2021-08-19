from selenium import webdriver
import time
import csv
import datetime #Py10

from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"
browser.get(URL)
browser.maximize_window()

time.sleep(2)
browser.quit()