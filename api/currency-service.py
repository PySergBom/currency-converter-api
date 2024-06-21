import requests


def get_exchange_rate(from_currency: str, to_currency: str) -> float:
    api_key = "16fcaa0489a23513586d42fa"
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{from_currency.upper()}"

    response = requests.get(url)

    if response.status_code != 200:
        return None

    data = response.json()
    print(data)

    try:
        return data['conversion_rates'][to_currency.upper()]
    except KeyError:
        return None
