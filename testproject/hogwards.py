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
travel_date = '2019-02-04'
travel_time = '07:15AM'

# bevitt mezők
passenger_input = browser.find_element_by_id('passenger')
departure_date_input = browser.find_element_by_id('departure-date')
departure_time_input = browser.find_element_by_id('departure-time')
issue_ticket_input = browser.find_element_by_id('issue-ticket')

# bevitt adatok kitöltése
input_kitoltes(passenger_input, user_name)
input_kitoltes(departure_date_input, travel_date)
input_kitoltes(departure_time_input, travel_time)
time.sleep(2)

issue_ticket_input.click()

#kitöltött adatok
passenger_output = browser.find_element_by_id('passenger-name')
departure_date_output1 = browser.find_element_by_id('departure-date-text')
departure_date_output2 = browser.find_element_by_id('side-detparture-date')
departure_time_output1 = browser.find_element_by_id('departure-time-text')
departure_time_output2 = browser.find_element_by_id('side-departure-time')

print(passenger_output.text)
print(departure_date_output1.text)
print(departure_date_output2.text)
print(departure_time_output1.text)
print(departure_time_output2.text)




# time.sleep(2)
# browser.quit()
