import requests

api_key = '9728da3c182fb80949121e2a'


def get_currencies_list():
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/USD'
    response = requests.get(url)
    data = response.json()
    currencies_list = list(data['conversion_rates'].keys())
    return currencies_list


def get_exchange_rates(base_currency):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}'
    response = requests.get(url)
    data = response.json()
    return data['conversion_rates']


def convert_currency(amount, from_currency, to_currency):
    rates = get_exchange_rates(from_currency)
    rate = rates[to_currency]
    convert_amount = amount * rate
    return convert_amount
