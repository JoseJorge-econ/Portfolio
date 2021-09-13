from time import sleep
from datetime import date
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from calendar import monthrange


def extract_real(value):
    return value.text.split('\n')[1].split(': ')[1].replace(',', '.')

driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.get("https://www.bcb.gov.br/conversao")
driver.maximize_window()
date_input = driver.find_element_by_id("dataMask")
date_input.send_keys(Keys.RETURN)
sleep(1)
year = 2021
month = 7
values = ['date', 'price']

for day in range(1, monthrange(year, month)[1] + 1):
    dt = date(year, month, day)

    if dt.weekday() >= 5:
        continue

    date_str = dt.strftime("%d/%m/%Y")
    date_input.clear()
    date_input.send_keys(date_str)
    sleep(2)
    date_input.send_keys(Keys.RETURN)
    sleep(2)
    date_input.send_keys(Keys.RETURN)
    value = driver.find_element_by_css_selector('.resultado > div > div:nth-child(2) > div')
    value = extract_real(value)
    values.append((date_str, value))
    print('Price:', date_str, value)

csv_data = '\n'.join([','.join(data) for data in values])
f = open("data.csv", "w")
f.write(csv_data)
f.close()

driver.close()
