# Async YooKassa (unofficial)

[![Latest Stable Version](https://img.shields.io/pypi/v/async_yookassa.svg)](https://pypi.org/project/async_yookassa/) [![Downloads](https://img.shields.io/pypi/dm/async_yookassa.svg)](https://pypi.org/project/async_yookassa/) [![Код на салфетке](https://img.shields.io/badge/Telegram-Код_на_салфетке-blue)](https://t.me/press_any_button) [![Заметки на салфетке](https://img.shields.io/badge/Telegram-Заметки_на_салфетке-blue)](https://t.me/writeanynotes) 


Неофициальный клиент для работы с платежами по [API ЮKassa](https://yookassa.ru/developers/api)

За основу взята [официальная библиотека от ЮМани](https://git.yoomoney.ru/projects/SDK/repos/yookassa-sdk-python/browse).  

## Цель
Заменить синхронный `requests` на асинхронный `httpx`, также переложить валидацию данных на `Pydantic`.

## Реализовано на данный момент

* Класс `Configuration`.
* Класс `APIClient`.
* Класс `Payment`.
* Класс `Invoice`.
* Класс `Refund`.
* Класс `Receipt`.
* Класс `Payout`.
* Класс `SelfEmployed`.
* Класс `SbpBanks`.
* Класс `PersonalData`.
* Класс `Deal`.
* Класс `Webhook`.
* Класс `Settings`.
* Сопутствующие `Pydantic-модели` и `Enum`.


## Требования

1. Python >=3.12
2. pip/poetry

## Установка
### C помощью pip

1. Установите pip.
2. В консоли выполните команду
    ```bash
    pip install --upgrade async_yookassa
    ```
### C помощью poetry

1. Установите poetry.
2. В консоли выполните команду
    ```bash
    poetry add async_yookassa
    ```

## Начало работы

1. Импортируйте модуль
    ```python
    import async_yookassa
    ```
2. Установите данные для конфигурации
    ```python
    from async_yookassa import Configuration
    
    Configuration.configure(account_id='<Идентификатор магазина>', secret_key='<Секретный ключ>')
    ```

    или

    ```python
    from async_yookassa import Configuration
    
    Configuration.account_id = '<Идентификатор магазина>'
    Configuration.secret_key = '<Секретный ключ>'
    ```

    или через oauth

    ```python
    from async_yookassa import Configuration
    
    Configuration.configure_auth_token(token='<Oauth Token>')
    ```

    Если вы согласны участвовать в развитии SDK, вы можете передать данные о вашем фреймворке, cms или модуле:

    ```python
    from async_yookassa import Configuration
    from async_yookassa.models.configuration_submodels.version import Version
    
    Configuration.configure('<Идентификатор магазина>', '<Секретный ключ>')
    Configuration.configure_user_agent(
        framework=Version(name='Django', version='2.2.3'),
        cms=Version(name='Wagtail', version='2.6.2'),
        module=Version(name='Y.CMS', version='0.0.1')
    )
    ```

3. Вызовите нужный метод API. [Подробнее в документации к API ЮKassa](https://yookassa.ru/developers/api)
