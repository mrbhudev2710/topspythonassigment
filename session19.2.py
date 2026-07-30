#1. Use the requests library in Python to send a GET request to the public API https://jsonplaceholder.typicode.com/posts
#and print the titles of the first 5 posts.

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Check if request was successful
if response.status_code == 200:
    posts = response.json()

    print("Titles of the first 5 posts:\n")
    for post in posts[:5]:
        print(post["title"])
else:
    print("Failed to fetch data. Status code:", response.status_code)



#2. Create a Python dictionary that represents a Zomato-style restaurant object with fields like name, 
#location, cuisines, and ratings. Convert this dictionary to a JSON string using the json module and print the result.

import json

# Create a restaurant dictionary
restaurant = {
    "name": "Spice Villa",
    "location": "Ahmedabad, Gujarat",
    "cuisines": ["North Indian", "Chinese", "Fast Food"],
    "ratings": 4.5
}

# Convert dictionary to JSON string
restaurant_json = json.dumps(restaurant, indent=4)

# Print JSON string
print(restaurant_json)


#3. Send a POST request to https://jsonplaceholder.typicode.com/posts to add a new
# playlist with fields: title, userId, and body. Print the status code and the JSON response.
#<br><br><em><strong>Hint:</strong> Use requests.post() and pass your data as a JSON payload.</em>

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send in the POST request
playlist = {
    "title": "My Favorite Songs",
    "userId": 1,
    "body": "This is my new playlist containing my favorite songs."
}

# Send POST request
response = requests.post(url, json=playlist)

# Print status code
print("Status Code:", response.status_code)

# Print JSON response
print("\nResponse JSON:")
print(response.json())


#4. Modify your GET request to https://jsonplaceholder.typicode.com/posts so it only fetches
#posts by userId=2 by passing the correct query parameter. Print the IDs of the returned posts.
#<br><br><em><strong>Hint:</strong> Use the 'params' argument in requests.get().</em>

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Query parameter
params = {
    "userId": 2
}

# Send GET request with query parameter
response = requests.get(url, params=params)

# Check if request was successful
if response.status_code == 200:
    posts = response.json()

    print("Post IDs for userId = 2:\n")
    for post in posts:
        print(post["id"])
else:
    print("Failed to fetch data. Status Code:", response.status_code)


#5. Research using ChatGPT or Copilot to find out how to set custom HTTP headers (like 
#'Authorization') in a Python requests call. Write a short code snippet that sends a 
#GET request to any API endpoint with a custom header and print the response status code.

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Custom HTTP headers
headers = {
    "Authorization": "Bearer my_sample_token_12345",
    "User-Agent": "PythonRequests/1.0"
}

# Send GET request with custom headers
response = requests.get(url, headers=headers)

# Print the response status code
print("Status Code:", response.status_code)