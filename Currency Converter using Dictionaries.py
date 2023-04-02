# Define the exchange rates dictionary
# Identifications
# PKR = Pakistani Rupee
# USD = United States Dollar
# SAR = Saudi Arabian Rayal
# EUR = European Pound
# TRY = Turkish Lera
exchange_rates = {  # Main Dictionary
    "PKR": {  # Currency Rates w.r.t PKR
        "USD": 0.0063,
        "SAR": 0.0236,
        "EUR": 0.0054,
        "TRY": 0.0516
    },
    "USD": {  # Currency Rates w.r.t USD
        "PKR": 158.13,
        "SAR": 3.75,
        "EUR": 0.91,
        "TRY": 8.67
    },
    "SAR": {  # Currency Rates w.r.t SAR
        "PKR": 42.28,
        "USD": 0.27,
        "EUR": 0.22,
        "TRY": 2.08
    },
    "EUR": {  # Currency Rates w.r.t EUR
        "PKR": 184.97,
        "USD": 1.10,
        "SAR": 4.45,
        "TRY": 9.51
    },
    "TRY": {  # Currency Rates w.r.t TRY
        "PKR": 19.38,
        "USD": 0.12,
        "SAR": 0.48,
        "EUR": 0.11
    }
}

# Get input from user
# Enter the Currency name, user wants to convert from
from_currency = input("Enter the currency you want to convert from: \n")

# Enter the curreny name, user wants to convert in
to_currency = input("Enter the currency you want to convert in: \n")

# Enter the amount which needs to be converted
# using float to convert amount in float because in python, input value bulit has
# string data type and we have to apply operations to convert curreny
# and we cannot apply operations with a string and a float
# so, we converted input string into float value
amount = float(input("Enter the amount you want to convert: \n"))

# Convert the amount
# get the value from nested dictionary of exchange rates dictionary from which
# amount is needs to be converted, of currency in which we have to convert in
# and then multiply it with actual amount and stored a variable
converted_amount = amount * exchange_rates[from_currency][to_currency]

# Print the result
# used foramatted strings
print(f"{amount} {from_currency} = {converted_amount} {to_currency}")
