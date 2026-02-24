def temperature_converter():
    temp = float(input("Enter the temperature to convert: "))
    from_unit = input("Enter the unit to convert from (C, F, K): ").upper()
    to_unit = input("Enter the unit to convert to (C, F, K): ").upper()

    if from_unit == to_unit:
        result = temp

    #censius to fahrenheit and kelvin
    elif from_unit == "C":
        if to_unit == "F":
            result = (temp * 9/5) + 32
        elif to_unit == "K":
            result = temp + 273.15
        else:
            print("Invalid unit")
            return

    #fahrenheit to celsius and kelvin
    elif from_unit == "F":
        if to_unit == "C":
            result = (temp - 32) * 5/9
        elif to_unit == "K":
            result = (temp - 32) * 5/9 + 273.15
        else:
            print("Invalid unit")
            return

    #kelvin to celsius and fahrenheit
    elif from_unit == "K":
        if to_unit == "C":
            result = temp - 273.15
        elif to_unit == "F":
            result = (temp - 273.15) * 9/5 + 32
        else:
            print("Invalid unit")
            return

    print(f"{temp} {from_unit} is equal to {result:.2f} {to_unit}")

temperature_converter()                        