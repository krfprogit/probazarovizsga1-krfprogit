from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/hogwards.html"
browser.get(URL)
browser.maximize_window()


def input_kitoltes(input, adat):
    input.clear()
    input.send_keys(adat)


# bevitt adatok értékei
user_name = "KISS RÓBERT FERENC"
travel_date = '0020192504'
travel_time = '0715'

# input mezők
passenger = browser.find_element_by_id('passenger')
departure_date = browser.find_element_by_id('departure-date')
departure_time = browser.find_element_by_id('departure-time')
issue_ticket = browser.find_element_by_id('issue-ticket')

# bevitt adatok kitöltése
input_kitoltes(passenger, user_name)
input_kitoltes(departure_date, travel_date)
input_kitoltes(departure_time, travel_time)
time.sleep(2)

issue_ticket.click()


# time.sleep(2)
# browser.quit()
