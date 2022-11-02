from selenium.webdriver.common.by import By
import time
import os
from dotenv import load_dotenv, find_dotenv

link = 'https://mail.yandex.ru/'


def test_search(browser):
    load_dotenv(find_dotenv())
    # Зайти на сайт https://mail.yandex.ru/
    browser.get(link)
    browser.implicitly_wait(10)

    # Кликнуть по кнопке "Войти в Почту"
    button_sign_in = browser.find_element(By.CSS_SELECTOR, "button[type='button']")
    button_sign_in.click()

    # Кликнуть по кнопке "Почта", т.е. войти по почте
    button_mail = browser.find_element(By.CSS_SELECTOR, "[data-type='login']")
    button_mail.click()

    # Ввести в поле "Логин или email" почту
    input_mail = browser.find_element(By.CSS_SELECTOR, "[placeholder='Логин или email']")
    input_mail.send_keys(os.environ.get("email"))

    # Кликнуть по кнопке "Войти"
    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    # Ввести в поле "Введите пароль" пароль
    input_mail = browser.find_element(By.CSS_SELECTOR, "[placeholder='Введите пароль']")
    input_mail.send_keys(os.environ.get("password"))

    # Кликнуть по кнопке "Войти"
    button_enter = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    button_enter.click()

    # Кликнуть по кнопке "Пропустить"
    try:
        button_enter = browser.find_element(By.CSS_SELECTOR, "span a[class*='Button2']")
        button_enter.click()
    except:
        pass

    time.sleep(3)
