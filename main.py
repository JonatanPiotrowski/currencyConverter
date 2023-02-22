import requests

api_key = '9728da3c182fb80949121e2a'

supported_currencies = ['PLN', 'USD', 'EUR']


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


while True:
    amount = float(input("Amount of money: "))
    source_currency = input("Enter base currency: ")
    target_currency = input("Enter base currency: ")
    print(round(convert_currency(amount, source_currency, target_currency), 2))
    break
