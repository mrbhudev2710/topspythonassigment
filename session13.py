#1.Write a recursive function in Python called print_playlist_songs(songs) that takes a list of song names (like a Spotify playlist) 
# and prints each song name one by one using recursion.

# Recursive function to print playlist songs
import numbers
def print_playlist_songs(songs):
    # Base case: if the list is empty, stop recursion
    if not songs:
        return

    # Print the first song
    print(songs[0])

    # Recursive call with the remaining songs
    print_playlist_songs(songs[1:])


# Example Spotify playlist
playlist = [
    "Aarzu",
    "Kehna Lagaa",
    "Yeh Fitoor Mera",
    "Perfect",
    "Believer"
]

# Call the function
print_playlist_songs(playlist)


#2. Create a recursive function count_unread_messages(messages) that takes a nested dictionary representing WhatsApp chat groups and subgroups,
# and returns the total number of unread messages across all groups.<br><br><em><strong>Hint:</strong> Each group can have a 'count'
# key for unread messages and a 'subgroups' key with a list of more groups.</em>

# Recursive function to count total unread messages
def count_unread_messages(messages):
    total = messages.get("count", 0)

    # Recursively count unread messages in subgroups
    for subgroup in messages.get("subgroups", []):
        total += count_unread_messages(subgroup)

    return total


# Example nested WhatsApp groups
whatsapp_groups = {
    "name": "Family",
    "count": 5,
    "subgroups": [
        {
            "name": "Cousins",
            "count": 3,
            "subgroups": [
                {
                    "name": "College Friends",
                    "count": 2,
                    "subgroups": []
                }
            ]
        },
        {
            "name": "Office",
            "count": 4,
            "subgroups": [
                {
                    "name": "Project Team",
                    "count": 6,
                    "subgroups": []
                }
            ]
        }
    ]
}

# Call the function
total_unread = count_unread_messages(whatsapp_groups)

print("Total unread messages:", total_unread)



#3. Given the following code, identify which variables are local and which are global, and explain what will be printed when you call outer()
# and then print(x) at the end:<br><br>```python

x = 'global'

def outer():
    x = 'outer'

    def inner():
        nonlocal x
        x = 'inner'

    inner()
    print("Inside outer:", x)

outer()
print("Outside:", x)


#4. Build a recursive function format_number_short(n) that takes a number (like a follower count on Instagram or YouTube) 
#and returns it as a string in short format: 1500 as '1.5K', 1200000 as '1.2M', 500 as '500'.

def format_number_short(n):
    suffixes = ["", "K", "M", "B", "T"]

    def helper(num, index):
        if num < 1000 or index == len(suffixes) - 1:
            if index == 0:
                return str(int(num))
            else:
                return f"{num:.1f}{suffixes[index]}"
        return helper(num / 1000, index + 1)

    return helper(n, 0)


# Example usage
print(format_number_short(500))        # 500
print(format_number_short(1500))       # 1.5K
print(format_number_short(1200000))    # 1.2M
print(format_number_short(2500000000)) # 2.5B