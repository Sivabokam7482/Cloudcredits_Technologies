# Python program for Currency Converter

import requests

# Function to get exchange rates
def get_exchange_rate(api_key, base_currency):
    # url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/{base_currency}"
    url=f"https://v6.exchangerate-api.com/v6/ab3047fba1788b759f5483f4/latest/INR"

    response = requests.get(url)
    data = response.json()
    
    if data["result"] == "success":
        return data["conversion_rates"]
    else:
        print("Error fetching exchange rates:", data["error-type"])
        return None

# Function to convert currency
def convert_currency(amount, from_currency, to_currency, rates):
    if from_currency not in rates or to_currency not in rates:
        print("Invalid currency code.")
        return None
    
    converted_amount = amount * (rates[to_currency] / rates[from_currency])
    return round(converted_amount, 2)

# Main function
def main():
    API_KEY = "ab3047fba1788b759f5483f4"  # Replace with your API key
    base_currency = "INR"  # Default base currency

    rates = get_exchange_rate(API_KEY, base_currency)
    if not rates:
        return
    
    print("Available currencies:", ", ".join(rates.keys()))
    
    amount = float(input("Enter amount: "))
    from_currency = input("Enter source currency (e.g., USD, EUR): ").upper()
    to_currency = input("Enter target currency (e.g., INR, GBP): ").upper()
    
    result = convert_currency(amount, from_currency, to_currency, rates)

    print(f"\n\033[1m1 {from_currency} is equal to {round((result/amount),2)} {to_currency}\033[0m")
    
    if result is not None:
        print(f"\n\033[1m{amount} {from_currency} is equal to {result} {to_currency}\033[0m")

if __name__ == "__main__":
    main()
