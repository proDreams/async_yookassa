# Async YooKassa (unofficial)

[![Latest Stable Version](https://img.shields.io/pypi/v/async_yookassa.svg)](https://pypi.org/project/async_yookassa/) [![Downloads](https://img.shields.io/pypi/dm/async_yookassa.svg)](https://pypi.org/project/async_yookassa/) [![Код на салфетке](https://img.shields.io/badge/Telegram-Код_на_салфетке-blue)](https://t.me/press_any_button) [![Заметки на салфетке](https://img.shields.io/badge/Telegram-Заметки_на_салфетке-blue)](https://t.me/writeanynotes)

Неофициальный асинхронный клиент для работы с платежами по [API ЮKassa](https://yookassa.ru/developers/api)

За основу
взята [официальная библиотека от ЮМани](https://git.yoomoney.ru/projects/SDK/repos/yookassa-sdk-python/browse).

## Установка

```bash
# pip
pip install --upgrade async_yookassa

# poetry
poetry add async_yookassa

# uv
uv add async_yookassa
```

## Быстрый старт (v0.6+)

```python
from async_yookassa import YooKassaClient
from async_yookassa.models.payment_request import PaymentRequest
from async_yookassa.models.payment_submodels.amount import Amount
from async_yookassa.models.payment_submodels.confirmation import Confirmation

async with YooKassaClient(account_id="<Идентификатор магазина>", secret_key="<Секретный ключ>") as client:
    # Создание платежа
    payment = await client.payment.create(
        PaymentRequest(
            amount=Amount(value="100.00", currency="RUB"),
            confirmation=Confirmation(type="redirect", return_url="https://example.com/return"),
            description="Тестовый платёж",
        )
    )
    print(payment.confirmation.confirmation_url)

    # Получение информации о платеже
    payment = await client.payment.find_one("payment_id")

    # Список платежей
    payments = await client.payment.list()
```

### OAuth авторизация

```python
async with YooKassaClient(auth_token="<OAuth Token>") as client:
    payment = await client.payment.find_one("payment_id")
```

### Интеграция с DI (пример для Dishka)

```python
from dishka import Provider, Scope, provide, FromDishka


class YooKassaProvider(Provider):
    @provide(scope=Scope.APP)
    def get_client(self) -> YooKassaClient:
        return YooKassaClient(account_id="...", secret_key="...")


# Применение
async def create_payment(client: FromDishka[YooKassaClient]):
    async with client:
        payment = await client.payment.create(...)
```

## Доступные сервисы

| Сервис           | Описание | Методы                                            |
|------------------|----------|---------------------------------------------------|
| `client.payment` | Платежи  | `create`, `find_one`, `capture`, `cancel`, `list` |
| `client.refund`  | Возвраты | `create`, `find_one`, `list`                      |
| `client.receipt` | Чеки     | `create`, `find_one`, `list`                      |
| `client.payout`  | Выплаты  | `create`, `find_one`                              |
| `client.invoice` | Счета    | `create`, `find_one`, `cancel`, `list`            |
| `client.deal`    | Сделки   | `create`, `find_one`, `list`                      |
| `client.webhook` | Вебхуки  | `create`, `find_one`, `delete`, `list`            |

## Миграция с v0.x

<details>
<summary>📖 Инструкция по миграции</summary>

### Было (v0.x):

```python
from async_yookassa import Configuration, Payment

Configuration.configure(account_id="...", secret_key="...")
payment = await Payment.create({"amount": {"value": "100.00", "currency": "RUB"}})
```

### Стало (v0.6+):

```python
from async_yookassa import YooKassaClient
from async_yookassa.models.payment_request import PaymentRequest
from async_yookassa.models.payment_submodels.amount import Amount

async with YooKassaClient(account_id="...", secret_key="...") as client:
    payment = await client.payment.create(
        PaymentRequest(amount=Amount(value="100.00", currency="RUB"))
    )
```

### Основные изменения:

1. **Контекстный менеджер** — клиент теперь используется через `async with`
2. **Instance-based** — больше нет глобального состояния в `Configuration`
3. **Сервисы** — методы доступны через `client.payment`, `client.refund`, и т.д.

> **Старый API продолжает работать**, но выдаёт `DeprecationWarning` и будет удалён в v2.0.

</details>

## Требования

- Python >=3.11

## Лицензия

MIT
