from selenium.webdriver.common.by import By
import time


link = 'https://ru.wikipedia.org/'


def test_search(browser):
    # Зайти на сайт https://ru.wikipedia.org/
    browser.get(link)
    browser.implicitly_wait(10)

    # Проверить наличие поля поиска
    search = browser.find_element(By.ID, "searchInput")

    # Проверить наличие текста "Добро_пожаловать_в_Википедию" на главной странице
    browser.find_element(By.ID, "Добро_пожаловать_в_Википедию,")

    # Ввести в строке поиска заведомо бессмысленный набор букв
    search.send_keys("slkdfwoer345uoiwjfio")

    # Нажать кнопку “Поиск”
    button = browser.find_element(By.ID, "searchButton")
    button.click()

    # Проверить наличие на странице текста “Соответствий запросу не найдено.”
    browser.find_element(By.XPATH, "//p[contains(text(), 'Соответствий запросу не найдено.')]")

    # Ввести в строке поиска слово “Кожухов”
    search = browser.find_element(By.ID, "searchInput")
    search.send_keys("Кожухов")

    # Нажать кнопку “Поиск”
    button = browser.find_element(By.ID, "searchButton")
    button.click()

    # Проверить наличие результата
    button_href = browser.find_element(By.CSS_SELECTOR, "a[title*='Кожухов, Александр Борисович']")

    # Открыть ссылку результата
    button_href.click()

    # Проверить наличие на странице "Содержания"
    browser.find_element(By.XPATH, "//h2[contains(text(), 'Содержание')]")

    time.sleep(3)
