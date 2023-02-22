import requests

def get_currencies():
    url = "https://api.exchangerate-api.com/v4/latest/USD"
    response = requests.get(url)
    data = response.json()
    currencies = list(data["rates"].keys())
    currencies.insert(0, "USD")
    return currencies

def convert_currency(amount, currency_from, currency_to):
    url = f"https://api.exchangerate-api.com/v4/latest/{currency_from}"
    response = requests.get(url)
    data = response.json()
    rate = data["rates"][currency_to]
    result = float(amount) * rate
    return round(result, 2)