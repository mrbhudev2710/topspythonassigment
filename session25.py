#1. Fetch the latest 24-hour price and volume data for at least 10 popular cryptocurrencies using the Binance
# API and save the raw JSON response to a file named crypto_data.json.

import requests
import json

# Binance 24-hour ticker API
url = "https://api.binance.com/api/v3/ticker/24hr"

try:
    # Send GET request
    response = requests.get(url, timeout=10)

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Select the first 10 cryptocurrencies
    top_10 = data[:10]

    # Save raw JSON data to a file
    with open("crypto_data.json", "w", encoding="utf-8") as file:
        json.dump(top_10, file, indent=4)

    print("Top 10 cryptocurrency data has been saved to 'crypto_data.json'.")

    # Display price and volume information
    print("\nTop 10 Cryptocurrencies (24h Data)")
    print("-" * 60)

    for coin in top_10:
        print(f"Symbol       : {coin['symbol']}")
        print(f"Last Price   : {coin['lastPrice']}")
        print(f"24h Volume   : {coin['volume']}")
        print("-" * 60)

except requests.exceptions.Timeout:
    print("Error: The request timed out.")

except requests.exceptions.ConnectionError:
    print("Error: Unable to connect to the Binance API.")

except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)

except requests.exceptions.RequestException as err:
    print("Request Error:", err)

except IOError as err:
    print("File Error:", err)



#2. Write a Python function find_most_volatile_coin(data) that takes the loaded Binance coin data and 
#returns the symbol of the coin with the highest percentage price change in the last 24 hours.

import json

def find_most_volatile_coin(data):
    # Find the coin with the highest price change percentage
    most_volatile = max(data, key=lambda coin: abs(float(coin["priceChangePercent"])))
    
    return most_volatile["symbol"]

# Load JSON data from file
with open("crypto_data.json", "r", encoding="utf-8") as file:
    coin_data = json.load(file)

# Find and print the most volatile coin
symbol = find_most_volatile_coin(coin_data)
print("Most Volatile Coin:", symbol)


#3. Create a script that calculates the average price of all coins in your crypto_data.json,
# then prints a list of all coins currently trading below this average price.

import json

# Load data from JSON file
try:
    with open("crypto_data.json", "r", encoding="utf-8") as file:
        coins = json.load(file)

    # Calculate average price
    total_price = 0

    for coin in coins:
        total_price += float(coin["lastPrice"])

    average_price = total_price / len(coins)

    print(f"Average Price of All Coins: {average_price:.8f}\n")

    print("Coins Trading Below the Average Price:")
    print("-" * 40)

    found = False

    for coin in coins:
        price = float(coin["lastPrice"])

        if price < average_price:
            print(f"{coin['symbol']:<12} Price: {price}")
            found = True

    if not found:
        print("No coins are trading below the average price.")

except FileNotFoundError:
    print("Error: 'crypto_data.json' file not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'crypto_data.json'.")

except KeyError as e:
    print(f"Error: Missing key {e} in the JSON data.")

except Exception as e:
    print("An unexpected error occurred:", e)



#4. Build a function rank_coins_by_volume(data) that sorts all coins by their total traded volume in descending order
# and prints the top 5 coins with their rank and volume.

import json

def rank_coins_by_volume(data):
    # Sort coins by volume in descending order
    sorted_coins = sorted(
        data,
        key=lambda coin: float(coin["volume"]),
        reverse=True
    )

    print("Top 5 Coins by Trading Volume")
    print("-" * 40)

    # Print the top 5 coins
    for rank, coin in enumerate(sorted_coins[:5], start=1):
        print(f"{rank}. {coin['symbol']:<10} Volume: {float(coin['volume']):,.2f}")

# Load JSON data from file
try:
    with open("crypto_data.json", "r", encoding="utf-8") as file:
        coin_data = json.load(file)

    # Call the function
    rank_coins_by_volume(coin_data)

except FileNotFoundError:
    print("Error: 'crypto_data.json' file not found.")

except json.JSONDecodeError:
    print("Error: Invalid JSON format in 'crypto_data.json'.")

except KeyError as e:
    print(f"Error: Missing key {e} in the JSON data.")

except Exception as e:
    print("An unexpected error occurred:", e)



#5. Automate your data fetch and analysis by scheduling your script to run every hour using the schedule Python library,
# and add error handling to gracefully manage Binance API rate limits.<br><br><em><strong>Hint:</strong> Catch HTTP 429 
#errors and implement a retry with exponential backoff.</em>

import requests
import json
# pyrefly: ignore [missing-import]
import schedule
import time

# Binance API URL
URL = "https://api.binance.com/api/v3/ticker/24hr"

def fetch_crypto_data():
    max_retries = 5
    retry_delay = 2  # Initial delay in seconds

    for attempt in range(max_retries):
        try:
            response = requests.get(URL, timeout=10)

            # Handle rate limiting (HTTP 429)
            if response.status_code == 429:
                print(f"Rate limit exceeded. Retrying in {retry_delay} seconds...")
                time.sleep(retry_delay)
                retry_delay *= 2  # Exponential backoff
                continue

            # Raise exception for other HTTP errors
            response.raise_for_status()

            # Convert response to JSON
            data = response.json()

            # Save only the first 10 coins
            with open("crypto_data.json", "w", encoding="utf-8") as file:
                json.dump(data[:10], file, indent=4)

            print("Data fetched and saved successfully.")
            return

        except requests.exceptions.Timeout:
            print("Request timed out. Trying again...")

        except requests.exceptions.ConnectionError:
            print("Connection error. Check your internet connection.")
            return

        except requests.exceptions.HTTPError as e:
            print("HTTP Error:", e)
            return

        except requests.exceptions.RequestException as e:
            print("Request Error:", e)
            return

    print("Maximum retry attempts reached. Please try again later.")

# Schedule the task every hour
schedule.every().hour.do(fetch_crypto_data)

# Run once immediately
fetch_crypto_data()

print("Scheduler started... Press Ctrl+C to stop.")

# Keep the scheduler running
try:
    while True:
        schedule.run_pending()
        time.sleep(1)
except KeyboardInterrupt:
    print("\nScheduler stopped successfully.")