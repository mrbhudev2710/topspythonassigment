#1. Use the requests.get() function to fetch the latest posts from the JSONPlaceholder API endpoint 
#https://jsonplaceholder.typicode.com/posts and print the status code and the first post's title.

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Print status code
print("Status Code:", response.status_code)

# Check if the request was successful
if response.status_code == 200:
    posts = response.json()

    # Print the title of the first post
    print("First Post Title:", posts[0]["title"])
else:
    print("Failed to fetch posts.")


#2. Send a POST request to https://jsonplaceholder.typicode.com/posts using requests.post()
#with the data: title='My First Post', body='Hello from Python!', userId=101, 
#and print the status code and the returned JSON response.

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Data to send in the POST request
data = {
    "title": "My First Post",
    "body": "Hello from Python!",
    "userId": 101
}

# Send POST request
response = requests.post(url, json=data)

# Print status code
print("Status Code:", response.status_code)

# Print JSON response
print("\nReturned JSON Response:")
print(response.json())


#3. Fetch a list of users from https://jsonplaceholder.typicode.com/users 
#using requests.get(), then use the .json() method to extract and print the 
#usernames of all users whose email ends with '.org'.

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/users"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    users = response.json()

    print("Usernames with '.org' email addresses:\n")

    for user in users:
        if user["email"].endswith(".org"):
            print(user["username"])
else:
    print("Failed to fetch users. Status Code:", response.status_code)


#4. Build a small script that fetches movies from the OMDB API (http://www.omdbapi.com/) 
#by sending a GET request with query parameters: apikey='demo', s='Avengers'. 
#Print the total number of results found.<br><br><em><strong>Hint:</strong> Pass the 
#parameters using the params={} argument in requests.get().</em>

import requests

# API URL
url = "http://www.omdbapi.com/"

# Query parameters
params = {
    "apikey": "demo",
    "s": "Avengers"
}

# Send GET request
response = requests.get(url, params=params)

# Check if the request was successful
if response.status_code == 200:
    data = response.json()

    if data.get("Response") == "True":
        print("Total Results Found:", data["totalResults"])
    else:
        print("API Error:", data.get("Error"))
else:
    print("Failed to connect. Status Code:", response.status_code)