#1. Use iter() and next() to manually loop through a list of your 5 favorite food delivery apps (like Zomato, Swiggy, Domino's, etc.) 
#and print each app name one by one.

# List of 5 favorite food delivery apps
food_apps = ["Zomato", "Swiggy", "Domino's", "Uber Eats", "EatSure"]

# Create an iterator
app_iterator = iter(food_apps)

# Print each app one by one using next()
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))
print(next(app_iterator))


#2. Write a generator function called playlist_generator that takes a list of song names and yields each song one at a time,
# simulating a Spotify playlist shuffle.

import random

def playlist_generator(song_list):
    # Shuffle the playlist
    random.shuffle(song_list)

    # Yield one song at a time
    for song in song_list:
        yield song

# List of songs
songs = [
    "Kesariya",
    "Perfect",
    "Shape of You",
    "Blinding Lights",
    "Tum Hi Ho"
]

# Create the generator
playlist = playlist_generator(songs)

# Play songs one by one
for song in playlist:
    print("Now Playing:", song)


#3. Use enumerate() to print out the index and name of each item in a shopping cart list (e.g., ['Pizza', 'Burger', 'Fries', 'Coke']) 
#like Flipkart displays item numbers in your cart.

# Shopping cart list
shopping_cart = ["Pizza", "Burger", "Fries", "Coke"]

# Print item number and item name
for index, item in enumerate(shopping_cart, start=1):
    print(f"Item {index}: {item}")


#4. Given two lists — one with cricket team names and one with their IPL points — use zip() to pair each team with its points and print them in the format:
#'Team: Mumbai Indians, Points: 18'.

# List of IPL team names
teams = [
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders"
]

# Corresponding IPL points
points = [18, 16, 14, 20]

# Pair each team with its points using zip()
for team, point in zip(teams, points):
    print(f"Team: {team}, Points: {point}")


#5. Create a generator function called order_id_generator that yields a new order ID (starting from 1001) each time it's called, 
#similar to how Zomato or Swiggy generates unique order numbers.<br><br><em><strong>Hint:</strong> Use the yield statement inside a loop to generate the next ID.</em>

# Generator function to generate unique order IDs
def order_id_generator():
    order_id = 1001  # Starting order ID

    while True:
        yield order_id
        order_id += 1

# Create the generator
orders = order_id_generator()

# Generate and print 5 order IDs
print("Order ID:", next(orders))
print("Order ID:", next(orders))
print("Order ID:", next(orders))
print("Order ID:", next(orders))
print("Order ID:", next(orders))