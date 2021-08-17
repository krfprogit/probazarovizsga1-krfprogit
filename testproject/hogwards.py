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
user_name = 'KISS RÓBERT FERENC'
travel_date = '002019-02-04'
travel_time = '07:15AM'

# bevitt mezők
passenger_input = browser.find_element_by_id('passenger')
departure_date_input = browser.find_element_by_id('departure-date')
departure_time_input = browser.find_element_by_id('departure-time')
issue_ticket_btn = browser.find_element_by_id('issue-ticket')

# bevitt adatok kitöltése
input_kitoltes(passenger_input, user_name)
input_kitoltes(departure_date_input, travel_date)
input_kitoltes(departure_time_input, travel_time)
time.sleep(2)

issue_ticket_btn.click()

# kitöltött adatok értékei
passenger_output = browser.find_element_by_id('passenger-name').text
departure_date_output1 = browser.find_element_by_id('departure-date-text').text
departure_date_output2 = browser.find_element_by_id('side-detparture-date').text
departure_time_output1 = browser.find_element_by_id('departure-time-text').text
departure_time_output2 = browser.find_element_by_id('side-departure-time').text

# ellenőrzés
assert user_name == passenger_output
# assert travel_date == departure_date_output1
# assert travel_date == departure_date_output2
assert travel_time == departure_time_output1
assert travel_time == departure_time_output2

# time.sleep(2)
# browser.quit()
