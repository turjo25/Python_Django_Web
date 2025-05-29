class CurrencyConverter:
    #class attribute and the base values of the currencies
    exchange_rates = {
        "USD" : 1.0 , #Base value
        "BDT" : 121.75 ,
        "EUR" : 0.88 ,
        "GBP" : .75
    }

    #instace attribute
    def __init__(self,amount,from_currency,to_currency):
        self.amount = amount
        self.from_currency = from_currency.upper()
        self.to_currency = to_currency.upper()
    
    #instace method which will do conversion
    def convert(self):
        if self.from_currency not in CurrencyConverter.exchange_rates or \
        self.to_currency not in CurrencyConverter.exchange_rates:
            return "Invalid Currency!!!\nNot in our system!!!"
        
        base_amount = self.amount / CurrencyConverter.exchange_rates[self.from_currency]
        converted_amount = base_amount * CurrencyConverter.exchange_rates[self.to_currency]
        return round(converted_amount,2)
    
    #for rate update
    @classmethod
    def update_rate(cls, currency, new_rate):
        cls.exchange_rates[currency] = new_rate
    
    #helper method
    def is_valid_currency(code):
        return code.upper() in CurrencyConverter.exchange_rates

# User's conversion will show here   
class Logger:
    def log(self,user,converter):
        result = converter.convert()
        print(f"Record: {user} converted: {converter.amount} {converter.from_currency} -> {result} {converter.to_currency}")

#The if __name__ == "__main__": dewa mane er moddhe thaka property automatic run hbe na jde ami ei code k niye onno module e dei
if __name__ == "__main__":
    amount = float(input("Enter amount: "))
    from_curr = input("Enter your currency: ")
    to_curr = input("Enter your desired currency in which you want to convert: ")
    user = input("Enter your name: ")
    
    from_curr = from_curr.upper()
    to_curr = to_curr.upper()

    if from_curr == "TAKA":
        from_curr = "BDT"
    elif from_curr == "EURO":
        from_curr = "EUR"
    elif from_curr == "POUND":
        from_curr = "GBP"
    elif from_curr == "DOLLAR":
        from_curr = "USD"

    if to_curr == "TAKA":
        to_curr = "BDT"
    elif to_curr == "EURO":
        to_curr = "EUR"
    elif to_curr == "POUND":
        to_curr = "GBP"
    elif to_curr == "DOLLAR":
        to_curr = "USD"

    converter = CurrencyConverter(amount,from_curr,to_curr)

    if not CurrencyConverter.is_valid_currency(from_curr) or not CurrencyConverter.is_valid_currency(to_curr):
        print("Invalid Currency! We do not have that Currency")
    else:
        Logger = Logger()
        Logger.log(user,converter)
        

