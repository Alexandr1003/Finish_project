import os

from pages.base import WebPage
from pages.elements import WebElement
from pages.elements import ManyWebElements


class MainPage(WebPage):

    def __init__(self, web_driver, url=''):
        if not url:
            url = os.getenv("MAIN_URL") or 'https://stroylandiya.ru/'

        super().__init__(web_driver, url)

    # Основное поле поиска
    main_search = WebElement(id='title-search-input_fixed')

    # Кнопка показать все результаты
    results = WebElement(class_name='digi-ac-find__button')

    # Кнопка изменить запрос при не найденных результатах
    change_query = WebElement(class_name='digi-empty__button')

    # Название продуктов
    label_products = ManyWebElements(class_name='digi-product__meta')

    # Название первого продукта
    label_one_products = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/'
                                          'div[1]/a')

    # Название продукта в карточке товара
    label_product_in_card = WebElement(css_selector='h1.dcol-8.h1.p_product--title.p_product--order.-two')

    # Цена продуктов
    price_products = ManyWebElements(css_selector='span.digi-product-price-variant.digi-product-price-variant_actual')

    # Цена первого продукта в таблице
    price_one_product = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[2]/div[3]/div/div[1]/div[2]/'
                                         'div[2]/span')

    # Цкеа продукта в карточке
    price_product_card = WebElement(xpath='/html/body/div[6]/main/div[3]/div/div[6]/div[1]/div[1]/div/div/div')

    # История поиска
    history_search = ManyWebElements(class_name='digi-ac-history__text')

    # Логотп в хедере
    header_logo = WebElement(class_name='header-v2-logo')

    # Первый предложенный товар (История поискадолжна быть пустой)
    often_search = WebElement(xpath='//*[@id="digi-shield"]/div[3]/div/div/div[1]/div/ul/li[1]/button')

    # Название первого продукта
    title_product = WebElement(class_name='digi-title')

    # Фильтр по цене ОТ
    filter_price_from = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[2]/div[2]'
                                         '/div[1]/input')

    # Фильтр по цене ДО
    filter_price_up_to = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[2]/'
                                          'div[2]/div[3]/input')

    # Значение максимального фильтра по цене
    max_filter_value = WebElement(class_name='digi-slider__max')

    # Значение Минимального фильтра по цене
    min_filter_value = WebElement(class_name='digi-slider__min')

    # Инпут для поиска по бренду
    search_brand = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[3]/div[2]/div/input')

    # 1 бренд в фильтре по бренду
    brand_one = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[3]/ul/'
                                 'li[1]/label/span[2]')
    # 2 бренд в фильтре по бренду
    brand_three = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[3]/ul/'
                                   'li[3]/label/span[2]')

    # Инпут для второго фильтра
    search_for_second_filter = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[4]/'
                                                'div[2]/div/input')

    # Первое значение второго фильтра
    second_filter_1_value = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[4]/ul/li[1]'
                                             '/label/span[2]')

    # 2 значение второго фильтра
    second_filter_2_value = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[1]/div/div/div[4]/ul/li[1]'
                                             '/label/span[2]')

    # Бренд в карточке товара
    brand_card = WebElement(xpath='/html/body/div[6]/main/div[3]/div/div[5]/div/div[2]/ul/li[2]/span[2]')

    # Первая карточка товара
    one_products = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[2]/div[3]/div/div[1]')

    # Кнопка выбора сортировки продуктов
    sort_products = WebElement(class_name='multiselect__select')

    # Кнопка сортировки продутов "По популярности"
    sort_products_popular = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[2]/div[2]/div[2]/'
                                             'div[2]/div[3]/ul/li[1]/span/span')

    # Кнопка сортировки продутов "сначла дешевле"
    sort_products_min = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/'
                                         'div[3]/ul/li[2]/span/span')

    # Кнопка сортировки продутов "сначла дороже"
    sort_products_max = WebElement(xpath='//*[@id="digi-shield"]/div[2]/div/div/div/div[2]/div[2]/div[2]/div[2]/'
                                         'div[3]/ul/li[3]/span/span')

    price_product_card = WebElement(xpath='/html/body/div[6]/main/div[3]/div/div[6]/div[1]/div[2]/div/div/div')

    # Кнопка добавления товара в корзину
    input_add_basket = WebElement(xpath='/html/body/div[6]/main/div[3]/div/div[6]/div[1]/div[3]/div/div[1]/'
                                        'div/div[2]/input')

    # Кнопка добавления в корзину из карточки товара
    add_basket = WebElement(css_selector='button.dc-btn.-primary.-hover.p_product_shoping--btn.js_to_cart.'
                                         'js_to_cart--detail')

    # Кнопка корзины
    basket = WebElement(class_name='header-v2-basket')

    # Итоговая цена в корзине
    total_price = WebElement(xpath='//*[@id="bx-delement-basket"]/div/div[2]/div/div[2]/div[2]/div/div[1]/div[3]/'
                                   'div[2]')

    # Название продукта в корзине
    title_product_basket = WebElement(xpath='//*[@id="bx-delement-basket"]/div/div[2]/div/div[2]/div[1]/div/div[2]/'
                                            'div/div/div[1]/a')

