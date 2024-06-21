from fastapi import APIRouter, HTTPException
from .currency_service import get_exchange_rate

router = APIRouter()


@router.get("/rates", tags=["Обмен валюты"])
async def convert_currency(from_currency: str, to_currency: str, value: float):
    """
    Конвертация валюты на основе обменного курса.

    Этот эндпоинт позволяет вам конвертировать сумму из одной валюты в другую, используя предоставленный обменный курс.
    - **from_currency**: Код валюты, из которой конвертировать.
    - **to_currency**: Код валюты, в которую конвертировать.
    - **value**: Сумма для конвертации.
    """
    rate = get_exchange_rate(from_currency, to_currency)
    if rate is None:
        raise HTTPException(status_code=404, detail="Exchange rate not found, please input correct currency code")

    result = value * rate
    return {"result": result}
