#https://open.er-api.com/v6/latest/USD
import requests

class RealTimeCurrencyConverter():
    def __init__(self,url) :
        self.data = requests.get(url).json()
        self.currencies = self.data["rates"]

    def convert(self,fromCurrency,toCurrency,amount):
        initial_amount = amount
        if fromCurrency!="USD":
            amount=amount/self.currencies[fromCurrency]
            amount = round(amount*self.currencies[toCurrency],4)
            return amount


url ="https://open.er-api.com/v6/latest/USD"

conveter = RealTimeCurrencyConverter(url)
print(conveter.convert("INR","USD",100))
print(conveter.data)