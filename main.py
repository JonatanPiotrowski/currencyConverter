import requests

api_key = '9728da3c182fb80949121e2a'

supported_currencies = ['PLN', 'USD', 'EUR']


def currency_exchange(source_currency, target_currency):
    url = f'https://v6.exchangerate-api.com/v6/{api_key}/latest/{source_currency}'
    response = requests.get(url)
    exchange_rate = response.json()
    conversion_rates = exchange_rate['conversion_rates']
    return f"{conversion_rates[source_currency]} {source_currency} = {conversion_rates[target_currency]:.2f} {target_currency}"


while True:
    source_currency = input("Enter source currency: ")
    target_currency = input("Enter target currency: ")
    print(currency_exchange(source_currency, target_currency))
    break
