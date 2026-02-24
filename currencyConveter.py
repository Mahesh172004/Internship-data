def currency_converter():
    amount = float(input("Enter the amount to convert: "))
    from_currency = input("Enter the currency to convert from (e.g., USD, EUR, INR): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., USD, EUR, INR): ").upper()

    rates={"USD": 1.0, "EUR": 0.85, "INR": 90.61}  # Example exchange rates

    if from_currency in rates and to_currency in rates:
        converted_amount = amount * (rates[to_currency] / rates[from_currency])
        print(f"{amount} {from_currency} is equal to {converted_amount:.2f} {to_currency}.")
    else:
        print("Invalid currency. Please try again.") 

currency_converter()           