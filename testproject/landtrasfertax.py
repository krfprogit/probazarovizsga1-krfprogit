from selenium import webdriver
import time
import csv
import datetime  # Py10

from selenium.webdriver.common.keys import Keys
import selenium.common.exceptions

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/landtransfertax.html"
browser.get(URL)
browser.maximize_window()

# input értékek
price_input = browser.find_element_by_id('price')
tax_output = browser.find_element_by_id('tax')
go_btn = browser.find_element_by_xpath('/html/body/main/div/div/p[1]/button')

# TC01
# "Land Transfer Fee" feliratú mező pontosan üres marad-e?
go_btn.click()
time.sleep(1)
assert tax_output.text == ''

# megjelenik-e a következő felirat: "Enter the property value before clicking Go button."?
disclaimer_output = browser.find_element_by_id('disclaimer')
assert disclaimer_output.is_displayed()

# time.sleep(2)
# browser.quit()
