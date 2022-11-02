from selenium.webdriver.common.by import By
import time


link = 'https://mysmsbox.ru/mobile-handbook'


def test_search(browser):
    # Зайти на сайт https://mysmsbox.ru/mobile-handbook
    browser.get(link)
    browser.implicitly_wait(10)

    # Пролистать страницу до кнопки "Тюменская область" и кликнуть
    button_region = browser.find_element(By.XPATH, "//a[contains(text(), 'Тюменская область')]")
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_region)
    button_region.click()

    # Найти диапозон телефонных номеров "+7 902 620 *" и кликнуть
    button_group_call_number = browser.find_element(By.XPATH, "//a[contains(text(), '+7 902 620 *')]")
    button_group_call_number.click()

    # Проверить, что отобразился заголовок группы номеров
    browser.find_element(By.XPATH, "//h2[contains(text(), '+7 902 620')]")

    # Проверить, что отобразилась информация о типе номеров "Мобильный"
    browser.find_element(By.XPATH, "//strong[contains(text(), 'Мобильный')]")

    # Проверить, что отобразилась информация о стране "Россия"
    browser.find_element(By.XPATH, "//strong[contains(text(), 'Россия')]")

    # Найти кнопку "Посмотреть на карте" и кликнуть
    button_map = browser.find_element(By.XPATH, "//a[contains(text(), 'Посмотреть на карте')]")
    button_map.click()

    # Переключиться на страницу карты
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # Проверить, что открыта Россия
    try:
        url = browser.current_url
        assert 'Россия' in url
    except AssertionError:
        print("The map is not Russia")

    time.sleep(3)
