from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"
browser.get(URL)
browser.maximize_window()

# bevitt adatok értékei
user_name = "Kiss Róbert Ferenc"
travel_date_year = '2019'
travel_date_month = '03'
travel_date_day = '25'
travel_time_hour = '07'
travel_time_minute = '26'

# input fields
passenger = browser.find_element_by_id('passenger')
departure_date = browser.find_element_by_id('departure-date')
departure_time = browser.find_element_by_id('departure-time')
issue_ticket = browser.find_element_by_id('issue-ticket')

# bevitt adatok kitöltése
passenger.clear()
passenger.send_keys(user_name)


time.sleep(2)
browser.quit()
