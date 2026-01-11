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

import warnings

# === New API (recommended) ===
from async_yookassa.client import YooKassaClient

# === Legacy API (deprecated) ===
# Эти импорты сохранены для обратной совместимости
from async_yookassa.configuration import Configuration
from async_yookassa.deal import Deal
from async_yookassa.invoice import Invoice
from async_yookassa.payout import Payout
from async_yookassa.personal_data import PersonalData
from async_yookassa.receipt import Receipt
from async_yookassa.refund import Refund
from async_yookassa.sbp_banks import SbpBanks
from async_yookassa.self_employed import SelfEmployed
from async_yookassa.settings import Settings
from async_yookassa.webhooks import Webhook

__author__ = "Ivan Ashikhmin and YooMoney"
__email__ = "sushkoos@gmail.com and cms@yoomoney.ru"
__version__ = "0.6.0rc2"

__all__ = [
    # Recommended (new API)
    "YooKassaClient",
    # Legacy (deprecated, kept for backwards compatibility)
    "Configuration",
    "Invoice",
    "Refund",
    "Receipt",
    "Payout",
    "SelfEmployed",
    "SbpBanks",
    "PersonalData",
    "Deal",
    "Webhook",
    "Settings",
]


def __getattr__(name: str):
    """Выдаёт deprecation warning при использовании legacy классов."""
    legacy_classes = {
        "Configuration",
        "Invoice",
        "Refund",
        "Receipt",
        "Payout",
        "SelfEmployed",
        "SbpBanks",
        "PersonalData",
        "Deal",
        "Webhook",
        "Settings",
    }
    if name in legacy_classes:
        warnings.warn(
            f"{name} is deprecated and will be removed in v1.0. "
            f"Use YooKassaClient instead. See migration guide: "
            f"https://github.com/proDreams/async_yookassa#migration",
            DeprecationWarning,
            stacklevel=2,
        )
    raise AttributeError(f"module 'async_yookassa' has no attribute {name!r}")
