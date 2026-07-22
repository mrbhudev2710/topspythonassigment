1.#Create a Python script that uses a for loop to print the names of 5 favorite food delivery apps
# (e.g., Zomato, Swiggy, etc.), one per line.

# List of 5 favorite food delivery apps
food_delivery_apps = ["Zomato", "Swiggy", "Uber Eats", "Foodpanda", "Domino's"]

# Use a for loop to print each app name
for app in food_delivery_apps:
    print(app)


2.#Given a list of daily step counts for a week, use a while loop to find and print the first day
# when you crossed 10,000 steps.<br><br><em><strong>Hint:</strong> Loop through the list and stop as soon as you find a value greater than 10,000.</em>

# List of daily step counts for a week
steps = [7500, 8200, 9800, 10500, 9200, 12000, 11000]

# List of corresponding days
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Use a while loop to find the first day with more than 10,000 steps
i = 0

while i < len(steps):
    if steps[i] > 10000:
        print("First day you crossed 10,000 steps:", days[i])
        print("Steps:", steps[i])
        break
    i += 1


3.#Write a Python function that takes a list of IPL team names and prints only those teams whose names are longer than 6 characters, 
#skipping the rest using the continue statement.

# Function to print IPL team names longer than 6 characters
def print_long_team_names(teams):
    for team in teams:
        if len(team) <= 6:
            continue   # Skip team names with 6 or fewer characters
        print(team)

# List of IPL teams
ipl_teams = [
    "Mumbai Indians",
    "CSK",
    "RCB",
    "Sunrisers Hyderabad",
    "Punjab Kings",
    "Gujarat Titans",
    "Lucknow Super Giants"
]

# Call the function
print_long_team_names(ipl_teams)



4.#You have a list of song durations (in seconds) from your Spotify playlist. Use a for loop with enumerate to print each song's position 
#(starting from 1) and its duration in the format: 'Song 1: 210 seconds'

# List of song durations (in seconds)
song_durations = [210, 185, 240, 195, 220]

# Use enumerate to print the song number and duration
for position, duration in enumerate(song_durations, start=1):
    print(f"Song {position}: {duration} seconds")



5.#Build a simple shopping cart total calculator: Given a list of item prices from a Flipkart cart, 
#use a loop to sum the prices. If an item price is 0 (out of stock), skip it. Stop adding items if the running total crosses ₹2000 using break,
#and print the final total.<br><br><em><strong>Constraint:</strong> Use both break and continue in your solution.</em>

# List of item prices in the Flipkart cart
item_prices = [450, 700, 0, 600, 500, 300, 250]

# Variable to store the total price
total = 0

# Loop through each item price
for price in item_prices:
    # Skip out-of-stock items
    if price == 0:
        continue

    # Add the item price to the total
    total += price

    # Stop if the total crosses ₹2000
    if total > 2000:
        break

# Print the final total
print("Final Total: ₹", total)