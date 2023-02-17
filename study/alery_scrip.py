from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    button = browser.find_element(By.CSS_SELECTOR, 'button.btn')
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    def calc(num):
        return str(math.log(abs(12 * math.sin(int(num)))))


    x = browser.find_element(By.CSS_SELECTOR, '[id="input_value"]')
    num = x.get_attribute('innerHTML')

    res = calc(num)

    input1 = browser.find_element(By.ID, 'answer')
    input1.send_keys(res)

    button = browser.find_element(By.CSS_SELECTOR, '[type="submit"]')
    button.click()

    time.sleep(12)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(2)
    # закрываем браузер после всех манипуляций
    browser.quit()
