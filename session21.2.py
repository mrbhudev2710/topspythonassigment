#1. Use the requests library to send a POST request to https://jsonplaceholder.typicode.com/posts 
#with a JSON payload containing a title, body, and userId, then print the response status code
# and JSON data.

import requests

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# JSON payload
payload = {
    "title": "Learning Python Requests",
    "body": "This post is created using Python requests library.",
    "userId": 1
}

# Send POST request
response = requests.post(url, json=payload)

# Print response status code
print("Status Code:", response.status_code)

# Print JSON response data
print("\nJSON Response:")
print(response.json())


#2. Build a Python script that lets a user enter a new playlist name and description, 
#sends this data as JSON in a POST request to a mock API endpoint 
#(such as https://jsonplaceholder.typicode.com/posts), and prints the playlist ID returned by the API.

import requests

# API endpoint
url = "https://jsonplaceholder.typicode.com/posts"

# Take input from user
playlist_name = input("Enter playlist name: ")
description = input("Enter playlist description: ")

# JSON data payload
playlist_data = {
    "title": playlist_name,
    "body": description,
    "userId": 1
}

# Send POST request
response = requests.post(url, json=playlist_data)

# Check response
if response.status_code == 201:
    result = response.json()

    # Print returned playlist ID
    print("Playlist created successfully!")
    print("Playlist ID:", result["id"])
else:
    print("Failed to create playlist. Status Code:", response.status_code)


#3. Send a POST request to https://reqres.in/api/users with a JSON object containing a username and job,
# then parse the response to extract and print the created user's ID and creation timestamp.
#<br><br><em><strong>Hint:</strong> Use response.json() to access the returned data.</em>

import requests

url = "https://jsonplaceholder.typicode.com/posts"

data = {
    "title": "Manav",       # username → title
    "body": "Python Developer", # job → body
    "userId": 1
}

response = requests.post(url, json=data)
if response.status_code == 201:
    user_data = response.json()
    print("User Created Successfully!")
    print("User ID:", user_data["id"])


#4. Write a script that fetches the latest 5 posts from https://jsonplaceholder.typicode.com/posts, 
#parses the JSON response, and saves the post titles and userIds to a CSV file called posts.csv.
#<br><br><em><strong>Hint:</strong> Use the csv module for writing to CSV.</em>

import requests
import csv

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch posts using GET request
response = requests.get(url)

# Check if request is successful
if response.status_code == 200:
    posts = response.json()

    # Get latest 5 posts
    latest_posts = posts[-5:]

    # Create and write CSV file
    with open("posts.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)

        # Write CSV header
        writer.writerow(["title", "userId"])

        # Write post data
        for post in latest_posts:
            writer.writerow([post["title"], post["userId"]])

    print("posts.csv file created successfully!")

else:
    print("Failed to fetch posts. Status Code:", response.status_code)


#5. Modify your script to save the same API data (latest 5 posts from https://jsonplaceholder.typicode.com/posts) 
#into a JSON file named posts.json instead of CSV.

import requests
import json

# API URL
url = "https://jsonplaceholder.typicode.com/posts"

# Fetch posts using GET request
response = requests.get(url)

# Check if request is successful
if response.status_code == 200:
    posts = response.json()

    # Get latest 5 posts
    latest_posts = posts[-5:]

    # Save data to JSON file
    with open("posts.json", "w", encoding="utf-8") as file:
        json.dump(latest_posts, file, indent=4)

    print("posts.json file created successfully!")

else:
    print("Failed to fetch posts. Status Code:", response.status_code)