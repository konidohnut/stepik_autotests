from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time
import math


link = "https://suninjuly.github.io/selects1.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element(By.CSS_SELECTOR, '[id="num1"]')
    x = num1.get_attribute('innerHTML')
    num2 = browser.find_element(By.CSS_SELECTOR, '[id="num2"]')
    y = num2.get_attribute('innerHTML') #текст в элементе

    res = int(x) + int(y)

    res = str(res)
    select = Select(browser.find_element(By.ID, 'dropdown'))
    select.select_by_value(res)  # ищем элемент с текстом "Python"

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    time.sleep(10)
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
