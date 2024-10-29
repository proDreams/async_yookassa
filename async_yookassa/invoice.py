from async_yookassa.apiclient import APIClient
from async_yookassa.enums.request_methods_enum import HTTPMethodEnum
from async_yookassa.models.invoice_response_model import InvoiceResponse


class Invoice:
    """
    Класс, представляющий модель Invoice.
    """

    base_path = "/invoices"

    def __init__(self):
        self.client = APIClient()

    @classmethod
    async def find_one(cls, invoice_id: str):
        """
        Возвращает информацию о счёте

        :param invoice_id: Уникальный идентификатор счёта
        :return: Объект ответа InvoiceResponse, возвращаемого API при запросе счёта
        """
        instance = cls()

        if not isinstance(invoice_id, str):
            raise ValueError("Invalid invoice_id value")

        path = instance.base_path + "/" + invoice_id

        response = await instance.client.request(method=HTTPMethodEnum.GET, path=path)
        return InvoiceResponse(**response)
