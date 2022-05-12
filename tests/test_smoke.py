import time

import pytest
from pages.locators_stroy import MainPage


def test_main_search(web_browser):
    """Тест основного меню поиска"""

    page = MainPage(web_browser)

    page.main_search = 'плитка'
    page.results.click()

    assert page.label_products.count() >= 1

    for title in page.label_products.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'плитка' in title.lower(), msg


# negative
def test_symbols_in_main_search(web_browser):
    """Тест ввода в основное меню поиска спец. символов"""

    page = MainPage(web_browser)

    page.main_search.enter('!@#$%^&*()_+')

    assert page.change_query.get_text() == 'Изменить запрос'

# negative
def test_chaines_in_main_search(web_browser):
    """Тест ввода в основное меню поиска китайских символов"""

    page = MainPage(web_browser)

    page.main_search.enter('只是一些沒有意義的詞')

    assert page.change_query.get_text() == 'Изменить запрос'


# negative
def test_latin_in_main_search(web_browser):
    """Тест ввода в основное меню поиска большого символов"""

    page = MainPage(web_browser)

    page.main_search.enter('sssssssss')

    assert page.change_query.get_text() == 'Изменить запрос'

# negative
def test_search_eng(web_browser):
    """Тест ввода товара на английской раскладке"""

    page = MainPage(web_browser)

    page.main_search = 'gkbnrf'
    page.results.click()

    assert page.label_products.count() >= 1

    for title in page.label_products.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert 'плитка' in title.lower(), msg


def test_history_search(web_browser):
    """Тест истории поиска"""

    page = MainPage(web_browser)

    page.main_search = 'плитка'
    page.results.click()
    page.main_search = 'дверь'
    page.results.click()
    page.main_search = 'кран'
    page.results.click()
    page.main_search = ''
    page.header_logo.click()
    page.main_search.click()

    assert page.history_search.get_text() == ['кран', 'дверь', 'плитка']


def test_often_search(web_browser):
    """Тест предложенных товаров"""

    page = MainPage(web_browser)

    page.main_search.click()
    product = page.often_search.get_text()
    page.often_search.click()
    results_title = page.title_product.get_text()

    assert results_title.lower() == product.lower()


def test_filter_price_min(web_browser):
    """Тест фильтра по минимальной цене"""

    page = MainPage(web_browser)

    page.main_search = 'дверь'
    page.results.click()
    max_filter = page.max_filter_value.get_text()
    page.filter_price_from.enter(f'{max_filter}')
    page.click_on_coordinates(-700, 0)

    number = page.price_products.count()
    number = [max_filter] * number

    assert number == page.price_products.get_text()


def test_filter_price_max(web_browser):
    """Тест фильтра по максимальной цене"""

    page = MainPage(web_browser)

    page.main_search = 'лампочка'
    page.results.click()
    min_filter = page.min_filter_value.get_text()
    page.filter_price_up_to.enter(f'{min_filter}')
    page.click_on_coordinates(-700, 0)

    number = page.price_products.count()
    number = [min_filter] * number

    assert number == page.price_products.get_text()


# negative
def test_more_than_max_number(web_browser):
    """Тест ввода в фильтр по цене значения больше максимального"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    max_filter = page.max_filter_value.get_text()
    max_number = int(max_filter) + 1
    page.filter_price_from.enter(f'{max_number}')
    page.click_on_coordinates(-700, 0)

    number = page.price_products.count()
    number = [max_filter] * number

    assert number == page.price_products.get_text()


# negative
def test_less_than_min_number(web_browser):
    """Тест ввода в фильтр по цене значения меньше минимального"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    max_filter = page.min_filter_value.get_text()
    min_number = int(max_filter) - 1
    page.filter_price_up_to.enter(f'{min_number}')
    page.click_on_coordinates(-700, 0)

    number = page.price_products.count()
    number = [max_filter] * number

    assert number == page.price_products.get_text()


# negative
def test_latin_max_price(web_browser):
    """Тест ввода невалидных символов в поле максимальной цены"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    number_products = page.price_products.get_text() #Цены до ввода
    page.filter_price_up_to.enter('sssss')
    page.click_on_coordinates(-700, 0)
    time.sleep(5)
    number_after = page.price_products.get_text() #Цены после

    assert number_after == number_products


# negative
def test_latin_min_price(web_browser):
    """Тест ввода невалидных символов в поле минимальной цены"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    number_products = page.price_products.get_text() #Цены до ввода
    page.filter_price_from.enter('sssss')
    page.click_on_coordinates(-700, 0)
    time.sleep(5)
    number_after = page.price_products.get_text() #Цены после

    assert number_after == number_products


# negative
def test_chines_max_price(web_browser):
    """Тест ввода спец. символов в поле максимальной цены"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    number_products = page.price_products.get_text() #Цены до ввода
    page.filter_price_up_to.enter('拉丁')
    page.click_on_coordinates(-700, 0)
    time.sleep(5)
    number_after = page.price_products.get_text() #Цены после

    assert number_after == number_products


# negative
def test_chines_min_price(web_browser):
    """Тест ввода спец. символов в поле минимальной цены"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    number_products = page.price_products.get_text() #Цены до ввода
    page.filter_price_from.enter('拉丁')
    page.click_on_coordinates(-700, 0)
    time.sleep(5)
    number_after = page.price_products.get_text() #Цены после

    assert number_after == number_products


# negative
def test_symbols_max_price(web_browser):
    """Тест ввода спец. символов в поле максимальной цены"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    number_products = page.price_products.get_text() #Цены до ввода
    page.filter_price_up_to.enter('!@#$%^&*()_+')
    page.click_on_coordinates(-700, 0)
    time.sleep(5)
    number_after = page.price_products.get_text() #Цены после

    assert number_after == number_products


# negative
def test_symbols_min_price(web_browser):
    """Тест ввода спец. символов в поле минимальной цены"""

    page = MainPage(web_browser)

    page.main_search = 'цемент'
    page.results.click()
    number_products = page.price_products.get_text() #Цены до ввода
    page.filter_price_from.enter('!@#$%^&*()_+')
    page.click_on_coordinates(-700, 0)
    time.sleep(5)
    number_after = page.price_products.get_text() #Цены после

    assert number_after == number_products

def test_filter_by_brand(web_browser):
    """Проверка фильтра по бренду"""

    page = MainPage(web_browser)

    page.main_search = 'отвёртка'
    page.results.click()
    brand = page.brand_one.get_text()
    page.brand_one.click()
    time.sleep(1)

    for title in page.label_products.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{brand.lower()}' in title.lower(), msg

def test_search_brand(web_browser):
    """Тест поиска по фильтру 'бренд'"""

    page = MainPage(web_browser)
    page.main_search = 'окно'
    page.results.click()

    three = page.brand_one.get_text()
    page.search_brand = f"{three}"
    page.brand_one.click()
    time.sleep(1)

    for title in page.label_products.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{three.lower()}' in title.lower(), msg

def test_search_long(web_browser):
    """Тест поиска по фильтру 'длинна'"""

    page = MainPage(web_browser)
    page.main_search = 'отвёртка'
    page.results.click()

    two = page.second_filter_2_value.get_text()
    page.search_for_second_filter = f"{two}"
    page.second_filter_2_value.click()
    time.sleep(1)

    for title in page.label_products.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{two.lower()}' in title.lower(), msg

def test_filter_long(web_browser):
    """Проверка фильтра по длинне отвёртки"""

    page = MainPage(web_browser)

    page.main_search = 'отвёртка'
    page.results.click()
    long = page.second_filter_1_value.get_text()
    page.second_filter_1_value.click()
    time.sleep(1)

    for title in page.label_products.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{long.lower()}' in title.lower(), msg


def test_multiple_filter(web_browser):
    """Проверка нескольких фильтров"""

    page = MainPage(web_browser)

    page.main_search = 'отвёртка'
    page.results.click()
    long = page.second_filter_1_value.get_text()
    page.second_filter_1_value.click()
    time.sleep(1)

    max_filter = page.max_filter_value.get_text()
    page.filter_price_from.enter(f'{max_filter}')
    page.click_on_coordinates(-200, -30)

    number = page.price_products.count()
    number = [max_filter] * number

    assert number == page.price_products.get_text()

    for title in page.label_products.get_text():
        msg = 'Wrong product in search "{}"'.format(title)
        assert f'{long.lower()}' in title.lower(), msg


def test_check_sort_by_price_min(web_browser):
    """ Проверка сортировки по цене от меньшего к большему"""

    page = MainPage(web_browser)

    page.main_search = 'отвёртка'
    page.results.click()

    page.sort_products.click()
    page.sort_products_min.click()
    page.wait_page_loaded()

    all_prices = str(page.price_products.get_text())

    for x, y in (',', '.'), (' ', ''):
        all_prices = all_prices.replace(x, y)
    all_prices = all_prices.split()

    assert all_prices == sorted(all_prices), "Sort by price doesn't work!"


def test_check_sort_by_price_max(web_browser):
    """ Проверка сортировки по цене от большего к меньшему"""

    page = MainPage(web_browser)

    page.main_search = 'отвёртка'
    page.results.click()

    page.sort_products.click()
    page.sort_products_max.click()
    page.wait_page_loaded()

    all_prices = str(page.price_products.get_text())

    for x, y in (',', '.'), (' ', ''):
        all_prices = all_prices.replace(x, y)
    all_prices = all_prices.split()

    print(all_prices)
    print(sorted(all_prices))

    assert all_prices == sorted(all_prices, reverse=True), "Sort by price doesn't work!"


def test_check_sort_by_price_and_filter(web_browser):
    """ Проверка сортировки по цене вместе с фильтром"""

    page = MainPage(web_browser)

    page.main_search = 'отвёртка'
    page.results.click()

    page.filter_price_up_to.enter("800")
    page.click_on_coordinates(-700, 0)

    page.sort_products.click()
    page.sort_products_max.click()
    page.wait_page_loaded()

    one = page.price_one_product.get_text()
    one = "".join(c for c in one if c.isdecimal())

    all_prices = str(page.price_products.get_text())
    for x, y in (',', '.'), (' ', ''):
        all_prices = all_prices.replace(x, y)
    all_prices = all_prices.split()

    print(all_prices)
    print(sorted(all_prices))

    assert all_prices == sorted(all_prices, reverse=True), "Sort by price doesn't work!"
    assert one <= '800'


def test_card_product(web_browser):
    """Тест корректности отображения данных продукта в общем списке продуктов и в карточке товара"""

    page = MainPage(web_browser)
    page.main_search = 'отвёртка'
    page.results.click()

    label = page.label_one_products.get_text()
    one = page.price_one_product.get_text()
    one = "".join(c for c in one if c.isdecimal())

    page.label_one_products.click()
    label_card = page.label_product_in_card.get_text()
    price = page.price_product_card.get_text()
    price = "".join(c for c in price if c.isdecimal())

    print(label)
    print(label_card)

    assert label.lower() == label_card.lower()
    assert one == price

def test_basket(web_browser):
    """Тест добавдения товара в корзину"""

    page = MainPage(web_browser)
    page.main_search = 'чайник'
    page.results.click()
    title = page.label_one_products.get_text()
    page.label_one_products.click()

    price = page.price_product_card.get_text()
    price = "".join(c for c in price if c.isdecimal())
    page.add_basket.click()
    page.basket.click()
    summation = page.total_price.get_text()
    summation = "".join(c for c in summation if c.isdecimal())
    title_basket = page.title_product_basket.get_text()

    assert summation == str(price)
    assert title.lower() == title_basket.lower()

def test_add_basket(web_browser):
    """Тест добавдения нескольких товаров в корзину"""

    page = MainPage(web_browser)
    page.main_search = 'цемент'
    page.results.click()
    page.label_one_products.click()

    price = page.price_product_card.get_text()
    price = "".join(c for c in price if c.isdecimal())
    page.input_add_basket.enter('5')
    price = int(price) * 5
    page.add_basket.click()
    page.basket.click()
    summation = page.total_price.get_text()
    summation = "".join(c for c in summation if c.isdecimal())

    assert summation == str(price)

