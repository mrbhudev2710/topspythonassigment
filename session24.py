#1. Use the requests library to fetch the top 10 cryptocurrencies and their current prices in USD from the CoinGecko API 
#(https://api.coingecko.com/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc&per_page=10&page=1). Print the name and price of each coin.

import requests

# CoinGecko API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Query parameters
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

try:
    # Send GET request
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Convert response to JSON
    coins = response.json()

    # Print heading
    print("=" * 45)
    print(f"{'Top 10 Cryptocurrencies':^45}")
    print("=" * 45)

    # Print name and price of each coin
    for i, coin in enumerate(coins, start=1):
        print(f"{i}. {coin['name']:<20} : ${coin['current_price']}")

except requests.exceptions.RequestException as e:
    print("Error fetching cryptocurrency data:", e)



#2. Extend your script to also fetch and display the 24-hour price change percentage, 24-hour high, 
#and 24-hour low for each of the top 10 cryptocurrencies.

import requests

# CoinGecko API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Query parameters
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

try:
    # Send GET request
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Convert response to JSON
    coins = response.json()

    # Print table header
    print("=" * 95)
    print(f"{'Top 10 Cryptocurrencies':^95}")
    print("=" * 95)
    print(f"{'Name':<15} {'Price (USD)':>15} {'24h Change':>15} {'24h High':>15} {'24h Low':>15}")
    print("-" * 95)

    # Print details for each coin
    for coin in coins:
        name = coin["name"]
        price = coin["current_price"]
        change = coin["price_change_percentage_24h"]
        high = coin["high_24h"]
        low = coin["low_24h"]

        print(f"{name:<15} ${price:>14,.2f} {change:>14.2f}% ${high:>14,.2f} ${low:>14,.2f}")

except requests.exceptions.RequestException as e:
    print("Error fetching cryptocurrency data:", e)



#3. Save the fetched data (name, current price, price change %, 24h high, 24h low) for the top 10 
#cryptocurrencies into a CSV file named crypto_prices.csv using the csv module.

import requests
import csv

# CoinGecko API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Query parameters
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

try:
    # Fetch data from API
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Convert response to JSON
    coins = response.json()

    # Open CSV file for writing
    with open("crypto_prices.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write header row
        writer.writerow([
            "Name",
            "Current Price (USD)",
            "24h Price Change (%)",
            "24h High",
            "24h Low"
        ])

        # Write cryptocurrency data
        for coin in coins:
            writer.writerow([
                coin["name"],
                coin["current_price"],
                coin["price_change_percentage_24h"],
                coin["high_24h"],
                coin["low_24h"]
            ])

    print("Data successfully saved to 'crypto_prices.csv'.")

except requests.exceptions.RequestException as e:
    print("Error fetching cryptocurrency data:", e)
except IOError as e:
    print("Error writing to CSV file:", e)


#4. Add error handling to your code so that if the API request fails or returns an error, your script prints a user-friendly message 
#instead of crashing.<br><br><em><strong>Hint:</strong> Check the response status code and handle exceptions from the requests library.</em>

import requests
import csv

# CoinGecko API URL
url = "https://api.coingecko.com/api/v3/coins/markets"

# Query parameters
params = {
    "vs_currency": "usd",
    "order": "market_cap_desc",
    "per_page": 10,
    "page": 1
}

try:
    # Send GET request
    response = requests.get(url, params=params, timeout=10)

    # Check if request was successful
    if response.status_code == 200:
        coins = response.json()

        # Save data to CSV
        with open("crypto_prices.csv", "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)

            # Write header
            writer.writerow([
                "Name",
                "Current Price (USD)",
                "24h Price Change (%)",
                "24h High",
                "24h Low"
            ])

            # Write data
            for coin in coins:
                writer.writerow([
                    coin["name"],
                    coin["current_price"],
                    coin["price_change_percentage_24h"],
                    coin["high_24h"],
                    coin["low_24h"]
                ])

        print("Data successfully saved to 'crypto_prices.csv'.")

    else:
        print(f"API Error: Received status code {response.status_code}. Please try again later.")

except requests.exceptions.Timeout:
    print("Error: The request timed out. Please check your internet connection and try again.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the API. Please check your internet connection.")

except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)

except requests.exceptions.RequestException as err:
    print("An unexpected error occurred while fetching data:", err)

except IOError as err:
    print("Error writing to CSV file:", err)