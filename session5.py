1. #Create a list called playlist_ids with 5 song IDs (as integers) that you might see in a Spotify playlist, 
# and print the list.

# Create a list of Spotify song IDs
playlist_ids = [101, 205, 309, 412, 578]

# Print the list
print(playlist_ids)

2. #Add two more song IDs to your playlist_ids list using both append() and extend(), 
# then print the updated list.<br><br><em><strong>Hint:</strong> Use append() for a single ID and extend() for adding multiple IDs at once.</em>

# Create a list of Spotify song IDs
playlist_ids = [101, 205, 309, 412, 578]

# Add one song ID using append()
playlist_ids.append(650)

# Add multiple song IDs using extend()
playlist_ids.extend([721, 845])

# Print the updated list
print(playlist_ids)

3. #Simulate removing the last played song from your playlist_ids list using pop(),
#  and display the removed ID along with the remaining playlist.

# Create a list of Spotify song IDs
playlist_ids = [101, 205, 309, 412, 578, 650, 721, 845]

# Remove the last played song using pop()
removed_song = playlist_ids.pop()

# Display the removed song ID
print("Removed Song ID:", removed_song)

# Display the remaining playlist
print("Remaining Playlist:", playlist_ids)

4. #Create a tuple called insta_filters with 4 Instagram filter names (as strings). Try to change the first filter name and observe what error you get.
# <br><br><em><strong>Hint:</strong> Tuples are immutable. Note down the error message.</em>

# Create a tuple of Instagram filter names
insta_filters = ("Clarendon", "Juno", "Lark", "Gingham")

# Print the tuple
print(insta_filters)

# Try to change the first filter name
insta_filters = "Valencia"

5. #Write a short Python script that takes a scenario (like a list of recent Zomato orders vs a tuple of fixed IPL team names) 
# and prints which one should use a list and which should use a tuple, explaining your choice in a comment


# List: Used for data that can change (items can be added or removed)
zomato_orders = ["Pizza", "Burger", "Biryani"]

# Tuple: Used for fixed data that should not change
ipl_team_names = (
    "Mumbai Indians",
    "Chennai Super Kings",
    "Royal Challengers Bengaluru",
    "Kolkata Knight Riders"
)

print("Recent Zomato Orders (List):", zomato_orders)
print("IPL Team Names (Tuple):", ipl_team_names)