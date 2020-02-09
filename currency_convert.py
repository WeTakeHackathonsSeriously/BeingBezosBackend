from forex_python.converter import CurrencyRates

def one_dollar_is():
    return CurrencyRates().get_rate('USD', 'GBP')

