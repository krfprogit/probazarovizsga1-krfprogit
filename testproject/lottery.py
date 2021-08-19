from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/lottery.html"
browser.get(URL)
browser.maximize_window()
time.sleep(1)

# input mezők
generate_btn = browser.find_element_by_id('draw-number')
reset_btn = browser.find_element_by_id('reset-numbers')


def find_numbers():
    numbers_drawn = browser.find_elements_by_xpath('//*[@id="container"]/div')
    numbers_quantity = len(numbers_drawn)
    return numbers_quantity


# TC01
# ures lista

assert find_numbers() == 0

# TC02
# 6x click
for i in range(6):
    generate_btn.click()
    time.sleep(1)

# számok darabszáma = 6?

assert find_numbers() == 6

# számok 1 és 59 között vannak?
# for i in range(1, 7):
#     numbers_value = browser.find_element_by_xpath(f'//*[@id="container"]/div[{i}]').text
#     print(numbers_value, ' ', end='')
# print()
# print('---------------------')

# számok 1 és 59 között vannak?
numbers_drawn = browser.find_elements_by_xpath('//*[@id="container"]/div')
for n in numbers_drawn:
    numbers_value = n.text
    print(numbers_value, ' ', end='')
    numbers_value = int(numbers_value)
    assert numbers_value >= 1 and numbers_value <= 59

# TC03
# hetedik click, csak 6 szám
generate_btn.click()
time.sleep(1)

assert find_numbers() != 7

# reset, nincs szám
reset_btn.click()
time.sleep(1)

assert find_numbers() == 0

time.sleep(2)
browser.quit()
