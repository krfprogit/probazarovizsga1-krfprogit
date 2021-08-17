from selenium import webdriver
import time

PATH = "C:\\Windows\\chromedriver.exe"
browser = webdriver.Chrome(PATH)

URL = "https://witty-hill-0acfceb03.azurestaticapps.net/salestax.html"
browser.get(URL)
browser.maximize_window()

# ellenőrző értékek
salestax_value_tc01 = '0.00'
total_value_tc01 = '4.95'
salestax_value_tc02 = '4.95'
total_value_tc02 = '9.90'

# input mezők
subtotal_btn = browser.find_element_by_id('subtotalBtn')
calculate_order_btn = browser.find_element_by_id('gtotalBtn')

################################################################### TC01
salestax_output = browser.find_element_by_id('salestax')
total_output = browser.find_element_by_id('gtotal')
subtotal_btn.click()
calculate_order_btn.click()
time.sleep(2)

# ellenőrzések
# assert salestax_output.text == salestax_value_tc01
# assert total_output.text == total_value_tc01

############################################################ TC02
salestax_output.clear()
total_output.clear()

# input mezők
product_item_6x6_btn = browser.find_element_by_xpath('//*[@id="Proditem"]/option[2]').click()

quantity_input = browser.find_element_by_id('quantity')
quantity_value = '1'
quantity_input.clear()
quantity_input.send_keys(quantity_value)

subtotal_btn.click()
calculate_order_btn.click()
time.sleep(2)

print(type(salestax_output.text))
print(salestax_output.text)
# assert salestax_output.text == salestax_value_tc02

print(type(total_output.text))
print(total_output.text)
# assert total_output.text == total_value_tc02

# ellenőrzések, TC02

# time.sleep(2)
# browser.quit()
