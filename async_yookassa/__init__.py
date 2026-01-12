"""
Async YooKassa - неофициальный асинхронный клиент для YooKassa API.

Рекомендуемый способ использования (v0.6+):

```python
from async_yookassa import YooKassaClient

async with YooKassaClient(account_id="...", secret_key="...") as client:
    payment = await client.payment.create(PaymentRequest(...))
```

Legacy API (deprecated, будет удален в v1.0):

```python
from async_yookassa import Configuration, Payment

Configuration.configure(account_id="...", secret_key="...")
payment = await Payment.create({...})
```
"""

from async_yookassa.client import YooKassaClient

__author__ = "Ivan Ashikhmin and YooMoney"
__email__ = "sushkoos@gmail.com and cms@yoomoney.ru"
__version__ = "0.6.0rc2"

__all__ = [
    "YooKassaClient",
]
