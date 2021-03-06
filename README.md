Файлы
-----

[conftest.py](conftest.py) содержит весь необходимый код для обнаружения неудачных тестовых случаев и создания
скриншота страницы в случае, если какой-либо тестовый пример не будет выполнен.

[pages/base.py](pages/base.py) содержит реализацию PageObject для Python.

[pages/elements.py](pages/elements.py) содержит вспомогательный класс для определения веб-элементов на веб-страницах.

[tests/test_smoke.py](tests/test_smoke.py) содержит несколько тестов для интернет магазина Стройландия (https://market.yandex.ru/)


Как запускать тесты
----------------

1) Установите все требования:

    ```bash
    pip3 install -r requirements
    ```

2) Загрузите Selenium WebDriver с https://chromedriver.chromium.org/downloads (выберите версию, совместимую с вашим браузером)
3) Запустите тесты:

    ```bash
    pytest -v --driver Chrome --driver-path <Путь до драйвера браузера, загруженного на шаге 2>
    ```
    3.1) Для запуска отдельной тестовой функии используйте:

    ```bash
    pytest -v --driver Chrome --driver-path <Путь до драйвера браузера, загруженного на шаге 2> -k <'названии теста (функции)'>
    ```

Примечание: Основные методы библотеки PageObject были взяты у https://github.com/TimurNurlygayanov.
Мною были написаны некоторые необходимые дополнительные методы и тесты.