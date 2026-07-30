#1. Fetch the current temperature and weather description for your city using a weather API and print 
#the results in a readable format.
# Note: Using wttr.in — a free weather API that requires NO API key (OpenWeatherMap requires a paid/registered key)

import requests

# API endpoint — wttr.in returns free JSON weather data
url = "https://wttr.in/Ahmedabad"

# Request parameters
params = {
    "format": "j1"   # JSON format
}

try:
    # Send GET request
    response = requests.get(url, params=params)

    # Raise an error for bad responses
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Extract weather information
    city = "Ahmedabad"
    temperature = data["current_condition"][0]["temp_C"]
    feels_like = data["current_condition"][0]["FeelsLikeC"]
    description = data["current_condition"][0]["weatherDesc"][0]["value"]

    # Print results
    print(f"Weather Report for {city}")
    print("-" * 30)
    print(f"Temperature : {temperature}°C")
    print(f"Feels Like  : {feels_like}°C")
    print(f"Condition   : {description}")

except requests.exceptions.RequestException as e:
    print("Error:", e)


#2. Build a small Python script that fetches the latest price of Bitcoin and Ethereum from the CoinGecko API 
#and displays them with the current date and time.

import requests
from datetime import datetime

# CoinGecko API endpoint
url = "https://api.coingecko.com/api/v3/simple/price"

# Parameters
params = {
    "ids": "bitcoin,ethereum",
    "vs_currencies": "usd"
}

try:
    # Send GET request
    response = requests.get(url, params=params)
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Get current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Extract prices
    bitcoin_price = data["bitcoin"]["usd"]
    ethereum_price = data["ethereum"]["usd"]

    # Display results
    print("=" * 40)
    print(" Cryptocurrency Prices")
    print("=" * 40)
    print(f"Date & Time : {current_time}")
    print(f"Bitcoin     : ${bitcoin_price}")
    print(f"Ethereum    : ${ethereum_price}")
    print("=" * 40)

except requests.exceptions.RequestException as e:
    print("Error fetching data:", e)



#3. import requests
import os

# NASA API Key
API_KEY = "DEMO_KEY"      # Replace with your own API key if available

# NASA APOD API URL
url = "https://api.nasa.gov/planetary/apod"

# Request parameters
params = {
    "api_key": API_KEY
}

try:
    # Fetch APOD data
    response = requests.get(url, params=params)
    response.raise_for_status()

    data = response.json()

    # Print title and explanation
    print("Title:")
    print(data["title"])

    print("\nExplanation:")
    print(data["explanation"])

    # Download image only if media type is image
    if data["media_type"] == "image":
        image_url = data["url"]

        # Get image data
        image_response = requests.get(image_url)
        image_response.raise_for_status()

        # Get filename from URL
        filename = os.path.basename(image_url)

        # Save image
        with open(filename, "wb") as file:
            file.write(image_response.content)

        print(f"\nImage saved successfully as: {filename}")
    else:
        print("\nToday's APOD is not an image.")
        print("Media URL:", data["url"])

except requests.exceptions.RequestException as e:
    print("Error:", e)



#4. Create a Python program that fetches the latest COVID-19 case numbers for India from a public COVID API and displays total cases,
# recovered, and deaths in a table format.

import requests

# Public COVID-19 API
url = "https://disease.sh/v3/covid-19/countries/India"

try:
    # Send GET request
    response = requests.get(url)
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Extract required information
    country = data["country"]
    total_cases = data["cases"]
    recovered = data["recovered"]
    deaths = data["deaths"]

    # Display data in table format
    print("=" * 45)
    print(f"{'COVID-19 Statistics':^45}")
    print("=" * 45)
    print(f"{'Country':<20} | {country}")
    print(f"{'Total Cases':<20} | {total_cases:,}")
    print(f"{'Recovered':<20} | {recovered:,}")
    print(f"{'Deaths':<20} | {deaths:,}")
    print("=" * 45)

except requests.exceptions.RequestException as e:
    print("Error fetching COVID-19 data:", e)



#5. Combine data from two APIs: fetch the current temperature in Mumbai from OpenWeatherMap and the latest Bitcoin price from CoinGecko, 
#then display both results together in a single output.<br><br><em><strong>Constraint:</strong> Handle errors gracefully if either API 
#call fails and show an appropriate message.</em>
 
import requests

# -------------------------------
# OpenWeatherMap Configuration
# -------------------------------
WEATHER_API_KEY = "YOUR_API_KEY"
WEATHER_URL = "https://api.openweathermap.org/data/2.5/weather"

weather_params = {
    "q": "Mumbai",
    "appid": WEATHER_API_KEY,
    "units": "metric"
}

# -------------------------------
# CoinGecko Configuration
# -------------------------------
CRYPTO_URL = "https://api.coingecko.com/api/v3/simple/price"

crypto_params = {
    "ids": "bitcoin",
    "vs_currencies": "usd"
}

# Variables to store results
temperature = None
bitcoin_price = None

# -------------------------------
# Fetch Weather Data
# -------------------------------
try:
    weather_response = requests.get(WEATHER_URL, params=weather_params, timeout=10)
    weather_response.raise_for_status()

    weather_data = weather_response.json()
    temperature = weather_data["main"]["temp"]

except requests.exceptions.RequestException as e:
    print("Could not fetch weather data.")
    print("Reason:", e)

# -------------------------------
# Fetch Bitcoin Price
# -------------------------------
try:
    crypto_response = requests.get(CRYPTO_URL, params=crypto_params, timeout=10)
    crypto_response.raise_for_status()

    crypto_data = crypto_response.json()
    bitcoin_price = crypto_data["bitcoin"]["usd"]

except requests.exceptions.RequestException as e:
    print("Could not fetch Bitcoin price.")
    print("Reason:", e)

# -------------------------------
# Display Final Results
# -------------------------------
print("\n========== Live Data ==========")

if temperature is not None:
    print(f"🌤️ Mumbai Temperature : {temperature}°C")
else:
    print("🌤️ Mumbai Temperature : Not Available")

if bitcoin_price is not None:
    print(f"₿ Bitcoin Price      : ${bitcoin_price}")
else:
    print("₿ Bitcoin Price      : Not Available")

print("==============================")