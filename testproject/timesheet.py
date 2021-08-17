from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/timesheet.html"
browser.get(URL)
browser.maximize_window()

# TC01_1
email_input = browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[1]')
email_input.clear()
next_btn = browser.find_element_by_xpath('//*[@id="buttons"]/input')
# assert next_btn.click() == False

# TC01_2

# TC02_1
# bemenő adatok
email_value_tc02 = 'test@bela.hu'
hours_value_tc02 = '2'
minutes_value_tc02 = '0'
message_value_tc02 = 'working hard'
types_of_work_value_tc02 = 'Time working on visual effects for movie'

# bemenő mezők
email_input.clear()
email_input.send_keys(email_value_tc02)
hours_input = browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[2]')
hours_input.send_keys(hours_value_tc02)
minutes_input = browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/input[3]')
minutes_input.send_keys(minutes_value_tc02)
message_input = browser.find_element_by_xpath('//*[@id="section-timesheet"]/div[1]/form/textarea')
message_input.send_keys(message_value_tc02)
types_of_work_input = browser.find_element_by_xpath('//*[@id="dropDown"]/option').click()
next_btn = browser.find_element_by_xpath('//*[@id="buttons"]/input').click()




time.sleep(2)
browser.quit()
