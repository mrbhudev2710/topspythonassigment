#1. Use the requests.Session() object to fetch your Flipkart order history page twice in a row (without logging in), 
#and print the response status codes for both requests.<br><br><em><strong>Hint:</strong> Observe if cookies or
# session headers change between requests.</em>

import requests

# Create a session object
session = requests.Session()

# Set browser-like headers to avoid bot detection (without this, Flipkart returns 403)
session.headers.update({
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br",
    "Connection": "keep-alive",
})

# Flipkart order history URL
url = "https://www.flipkart.com/account/orders"

# First request
response1 = session.get(url)
print("First Request Status Code:", response1.status_code)

# Second request
response2 = session.get(url)
print("Second Request Status Code:", response2.status_code)

# Display cookies stored in the session
print("\nSession Cookies:")
print(session.cookies)

# Display request headers
print("\nSession Headers:")
print(session.headers)


#2. Write a Python script using requests to call a weather API
#for the city 'Ahmedabad' and print the current temperature.
# Using wttr.in — a free weather API that requires NO API key

import requests

# API endpoint — wttr.in returns JSON weather data for free
url = "https://wttr.in/Ahmedabad"

# Request JSON format
params = {
    "format": "j1"  # JSON format
}

try:
    # Send GET request
    response = requests.get(url, params=params)

    # Raise an exception for HTTP errors
    response.raise_for_status()

    # Convert response to JSON
    data = response.json()

    # Extract current temperature in Celsius
    temperature = data["current_condition"][0]["temp_C"]
    feels_like = data["current_condition"][0]["FeelsLikeC"]
    description = data["current_condition"][0]["weatherDesc"][0]["value"]

    print(f"Current temperature in Ahmedabad: {temperature}°C")
    print(f"Feels like: {feels_like}°C")
    print(f"Condition: {description}")

except requests.exceptions.HTTPError as err:
    print("HTTP Error:", err)

except requests.exceptions.RequestException as err:
    print("Request Error:", err)

except KeyError:
    print("Could not find temperature data.")



#3. Simulate an async data fetch from two different APIs (for example, fetch trending songs from Spotify 
#and trending movies from BookMyShow) using Python's asyncio and httpx library, and print both results when done.
#<br><br><em><strong>Hint:</strong> Use asyncio.gather() to run both requests concurrently.</em>


import asyncio
# pyrefly: ignore [missing-import]
import httpx

# Simulate fetching trending songs
async def fetch_trending_songs(client):
    url = "https://jsonplaceholder.typicode.com/posts/1"
    response = await client.get(url)
    data = response.json()
    return f"Trending Song: {data['title']}"

# Simulate fetching trending movies
async def fetch_trending_movies(client):
    url = "https://jsonplaceholder.typicode.com/posts/2"
    response = await client.get(url)
    data = response.json()
    return f"Trending Movie: {data['title']}"

async def main():
    async with httpx.AsyncClient() as client:
        # Run both API requests concurrently
        songs, movies = await asyncio.gather(
            fetch_trending_songs(client),
            fetch_trending_movies(client)
        )

        print(songs)
        print(movies)

# Run the async program
asyncio.run(main())



#4. Many APIs require Bearer tokens for authentication. Write a function get_user_profile() that calls a mock API endpoint 
#(e.g., https://jsonplaceholder.typicode.com/users/1) using a fake Bearer token in the Authorization header, and prints the user's name.
#<br><br><em><strong>Constraint:</strong> Use the 'Authorization: Bearer <token>' header format.</em>


import requests

def get_user_profile():
    url = "https://jsonplaceholder.typicode.com/users/1"

    # Fake Bearer token
    token = "fake_bearer_token_12345"

    # Authorization header
    headers = {
        "Authorization": f"Bearer {token}"
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()

        # Parse JSON response
        user = response.json()

        # Print user's name
        print("User Name:", user["name"])

    except requests.exceptions.RequestException as e:
        print("Error:", e)

# Call the function
get_user_profile()



#5, Use ChatGPT or Copilot to generate Python code that demonstrates the first step of an OAuth 2.0 login flow 
#(for example, generating the URL to redirect a user to Spotify's OAuth login page). Paste the generated code 
#and briefly explain what it does.


import urllib.parse

# Spotify OAuth credentials
CLIENT_ID = "YOUR_SPOTIFY_CLIENT_ID"
REDIRECT_URI = "http://localhost:8000/callback"

# Permissions your app is requesting
SCOPE = "user-read-email user-read-private"

# Spotify OAuth authorization endpoint
AUTH_URL = "https://accounts.spotify.com/authorize"

# Query parametersA
params = {
    "client_id": CLIENT_ID,
    "response_type": "code",
    "redirect_uri": REDIRECT_URI,
    "scope": SCOPE,
}

# Generate the authorization URL
authorization_url = AUTH_URL + "?" + urllib.parse.urlencode(params)

print("Open this URL in your browser:")
print(authorization_url)