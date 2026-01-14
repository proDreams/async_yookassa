# Async YooKassa (unofficial)

[![Latest Stable Version](https://img.shields.io/pypi/v/async_yookassa.svg)](https://pypi.org/project/async_yookassa/)
[![Downloads](https://img.shields.io/pypi/dm/async_yookassa.svg)](https://pypi.org/project/async_yookassa/)
[![Код на салфетке](https://img.shields.io/badge/Telegram-Код_на_салфетке-blue)](https://t.me/press_any_button)
[![Заметки на салфетке](https://img.shields.io/badge/Telegram-Заметки_на_салфетке-blue)](https://t.me/writeanynotes)

Неофициальный, полностью асинхронный клиент для работы с платежным сервисом [ЮKassa](https://yookassa.ru/) (YooKassa).

Библиотека разработана с использованием современных возможностей Python, опираясь на официальную документацию API и
структуру официального SDK, но переписана с нуля для обеспечения максимальной производительности и удобства
использования в асинхронных приложениях.

## Особенности

- **Полная асинхронность**: Использует `httpx` для неблокирующих HTTP-запросов.
- **Type-Safe**: Строгая типизация с использованием Pydantic v2. Весь код покрыт тайп-хинтами.
- **Современный API**: Удобный интерфейс через контекстный менеджер `async with`.
- **Модульность**: Структурированная архитектура, отдельные сервисы для каждой сущности API (Платежи, Возвраты, Чеки и
  т.д.).
- **Надежность**: Автоматическая обработка ошибок и повтор запросов (idempotency support).

## Установка

Библиотека доступна в PyPI и может быть установлена с помощью любого пакетного менеджера.

### pip

```bash
pip install async_yookassa
```

### poetry

```bash
poetry add async_yookassa
```

### uv (рекомендуется)

```bash
uv add async_yookassa
```

## Быстрый старт

Для начала работы вам понадобятся `Shop ID` и `Secret Key` из [личного кабинета ЮКассы](https://yookassa.ru/my).

### Создание первого платежа

```python
import asyncio
from async_yookassa import YooKassaClient
from async_yookassa.models.payment import PaymentRequest, Amount, RedirectConfirmationRequest


async def main():
    async with YooKassaClient(account_id="<SHOP_ID>", secret_key="<SECRET_KEY>") as client:
        # Создаем объект запроса
        request = PaymentRequest(
            amount=Amount(value="100.00", currency="RUB"),
            confirmation=RedirectConfirmationRequest(
                type="redirect",
                return_url="https://example.com/return"
            ),
            description="Заказ №1",
            capture=True
        )

        # Отправляем запрос
        payment = await client.payment.create(request)

        print(f"Платеж создан: {payment.id}")
        print(f"Ссылка на оплату: {payment.confirmation.confirmation_url}")


if __name__ == "__main__":
    asyncio.run(main())
```

## Аутентификация

Библиотека поддерживает два способа аутентификации.

### Basic Auth (Стандартный)

Используется `shopId` и `secretKey`.

```python
client = YooKassaClient(account_id="123456", secret_key="live_...")
```

### OAuth (Для платформ)

Используется OAuth-токен.

```python
client = YooKassaClient(auth_token="<OAUTH_TOKEN>")
```

## Конфигурация клиента

При инициализации `YooKassaClient` можно передать дополнительные параметры:

```python
from async_yookassa import YooKassaClient
from httpx import AsyncClient

custom_httpx_client = AsyncClient()

client = YooKassaClient(
    account_id="...",
    secret_key="...",
    timeout=60,  # Таймаут запроса в секундах (по умолчанию 30)
    api_url="https://api.yookassa.ru/v3",  # URL API (по умолчанию продакшн)
    http_client=custom_httpx_client  # Свой экземпляр AsyncClient (опционально)
)
```

**Обратите внимание:** Если вы передаете свой `http_client`, вы сами несете ответственность за его закрытие. При
использовании `async with` клиент `async_yookassa` закроет переданный `http_client` только если он был создан внутри (
т.е. `http_client=None`).

## Сервисы API

Все взаимодействие с API происходит через соответствующие сервисы внутри клиента.

### 💳 Платежи (`client.payment`)

Управление платежами: создание, подтверждение, отмена, получение информации.

```python
# Получение списка платежей
payments = await client.payment.list(limit=10)

# Получение информации о платеже
payment = await client.payment.find_one("2be00000-00000-00000000")

# Подтверждение платежа (холдирование)
await client.payment.capture("2be00000-00000-00000000")

# Отмена платежа
await client.payment.cancel("2be00000-00000-00000000")
```

### Возвраты (`client.refund`)

Осуществление возвратов средств пользователям.

```python
from async_yookassa.models.refund import RefundRequest, Amount

refund = await client.refund.create(
    RefundRequest(
        payment_id="2be00000-00000-00000000",
        amount=Amount(value="50.00", currency="RUB"),
        description="Возврат части средств"
    )
)
```

### Чеки (`client.receipt`)

Работа с чеками для 54-ФЗ.

```python
from async_yookassa.models.receipt import ReceiptRequest, ReceiptType, Customer, ReceiptItem, SettlementReceipt

receipt = await client.receipt.create(
    ReceiptRequest(
        customer=Customer(email="user@example.com"),
        type=ReceiptType.payment,
        send=True,
        items=[
            ReceiptItem(description="Товар 1", quantity="1", amount=Amount(value="100.00", currency="RUB"), vat_code=1)
        ],
        settlements=[SettlementReceipt(...)]
    )
)
```

### Вебхуки (`client.webhook`)

Управление подписками на уведомления о событиях.

```python
from async_yookassa.models.webhook import WebhookRequest, WebhookEvent

# Подписка на уведомление о успешной оплате
webhook = await client.webhook.create(
    WebhookRequest(
        event=WebhookEvent.PAYMENT_SUCCEEDED,
        url="https://example.com/webhook"
    )
)

# Список активных вебхуков
webhooks = await client.webhook.list()
```

### Другие сервисы

| Сервис             | Описание              | Доступ через             |
|--------------------|-----------------------|--------------------------|
| **Сделки**         | Безопасная сделка     | `client.deal`            |
| **Счета**          | Выставление счетов    | `client.invoice`         |
| **Выплаты**        | Выплаты на карты      | `client.payout`          |
| **Способы оплаты** | Сохраненные карты     | `client.payment_methods` |
| **Настройки**      | Информация о магазине | `client.me`              |
| **СБП**            | Банки участники       | `client.sbp_bank`        |

## Продвинутое использование

### Интеграция с Dependency Injection (Dishka)

Если вы используете DI-фреймворк, например `dishka`, вы можете зарегистрировать клиент как провайдер.

```python
from dishka import Provider, Scope, provide
from async_yookassa import YooKassaClient


class PaymentsProvider(Provider):
    @provide(scope=Scope.APP)
    async def get_client(self) -> YooKassaClient:
        return YooKassaClient(
            account_id="<ID>",
            secret_key="<KEY>"
        )
```

### Структура проекта

Библиотека разделена на модули для удобства:

- `async_yookassa.client` — Основной клиент `YooKassaClient`.
- `async_yookassa.models` — Pydantic модели запросов и ответов.
- `async_yookassa.services` — Реализация логики работы с API (методы `create`, `list` и т.д.).
- `async_yookassa.exceptions` — Типизированные исключения.

## Вклад в развитие

Если вы нашли баг или хотите добавить новую фичу:

1. Создайте Issue с описанием.
2. Форкните репозиторий.
3. Внесите изменения и отправьте Pull Request.

## Автор

- [Иван Ашихмин](https://t.me/proDreams)

Библиотека написана в рамках проекта "Код на салфетке":

- Сайт: https://pressanybutton.ru/
- Telegram-канал: https://t.me/press_any_button

## Поддержка

Если вам нравится этот проект и вы хотите поддержать его дальнейшее развитие, рассмотрите возможность доната:

- [Поддержать через YooMoney](https://yoomoney.ru/to/41001431694461)
- [Поддержать через Tribute в Telegram](https://t.me/tribute/app?startapp=dyds)
- [Поддержать через наш Telegram-бот](https://t.me/press_any_button_bot?start=donate)

## Лицензия

Проект распространяется под лицензией **MIT**. Подробнее см. файл `LICENSE`.
