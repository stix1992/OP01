import requests

def get_exchange_rates(api_key):
          url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
          response = requests.get(url)
          data = response.json()
          if data['result'] == 'success':
              return data['conversion_rates']
          else:
              raise Exception("Failed to fetch exchange rates")

def convert_currency(amount, from_currency, to_currency, rates):
          if from_currency != "USD":
              amount = amount / rates[from_currency]
          return amount * rates[to_currency]

def main():
          api_key = '692b47f76a2571e0453e6440'  # Замените YOUR_API_KEY_HERE на ваш ключ API
          rates = get_exchange_rates(api_key)

          print("Доступные валюты:")
          for i, currency in enumerate(rates.keys()):
            print(currency,end=' ')
            if (i + 1) % 10 == 0:
              print()

          from_currency = input("\nВведите исходную валюту: ").upper()
          to_currency = input("Введите целевую валюту: ").upper()
          amount = float(input("Введите сумму для конвертации: "))

          result = convert_currency(amount, from_currency, to_currency, rates)
          print(f"{amount} {from_currency} равно {result:.2f} {to_currency}")

if __name__ == "__main__":
          main()
