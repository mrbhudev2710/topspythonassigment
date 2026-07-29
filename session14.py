#1. Create a text file named playlist.txt and write the names of 5 songs you listened to this week, 
#each on a new line using Python's open() function in write mode.

# Create and write to playlist.txt

with open("playlist.txt", "w") as file:
    file.write("Kesariya\n")
    file.write("Apna Bana Le\n")
    file.write("Tum Hi Ho\n")
    file.write("Raataan Lambiyan\n")
    file.write("Heeriye\n")

print("playlist.txt has been created successfully!")


#2. Read the playlist.txt file you created and display each song name in uppercase letters using Python.


# Open the file in read mode
with open("playlist.txt", "r") as file:
    # Read each line and print it in uppercase
    for song in file:
        print(song.strip().upper())


#3. Download a sample CSV file of IPL match scores (you can create your own with columns: match_id, team1, team2, winner)
# and write a Python script to read the file and print the winner of each match using the csv module.

# ipl_matches.csv contents:
# match_id,team1,team2,winner
# 1,CSK,MI,CSK
# 2,RCB,KKR,KKR
# 3,GT,RR,GT
# 4,SRH,DC,SRH
# 5,PBKS,LSG,LSG

import csv

# Open and read the CSV file
with open("ipl_matches.csv", "r") as file:
    reader = csv.DictReader(file)

    print("Winners of IPL Matches:")
    for row in reader:
        print(f"Match {row['match_id']}: {row['winner']}")


#4. Find a public JSON file of trending movies (or create your own movies.json with at least 3 movie objects containing title, year, and rating), 
#then use the json module in Python to load the file and print the title and rating of each movie.

import json

# Open and load the JSON file
with open("movies.json", "r") as file:
    movies = json.load(file)

# Print the title and rating of each movie
print("Trending Movies:")
for movie in movies:
    print(f"Title: {movie['title']}, Rating: {movie['rating']}")


#5. Use the pathlib module to check if a file called 'my_fav_apps.json' exists in your current directory, and if not,
# create it and write a JSON array of your top 3 mobile apps (e.g., Instagram, Zomato, Paytm) with their names and categories.
#<br><br><em><strong>Hint:</strong> Use Path('my_fav_apps.json').exists() to check for the file, and json.dump() to write the data.</em>

from pathlib import Path
import json

# Create a Path object for the file
file_path = Path("my_fav_apps.json")

# Check if the file exists
if file_path.exists():
    print("my_fav_apps.json already exists.")
else:
    # List of favorite mobile apps
    apps = [
        {
            "name": "Instagram",
            "category": "Social Media"
        },
        {
            "name": "Zomato",
            "category": "Food Delivery"
        },
        {
            "name": "Paytm",
            "category": "Digital Payments"
        }
    ]

    # Create the file and write JSON data
    with open(file_path, "w") as file:
        json.dump(apps, file, indent=4)

    print("my_fav_apps.json has been created successfully!")
