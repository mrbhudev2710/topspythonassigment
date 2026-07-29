#1. Create a Python script that imports the math module and uses math.sqrt() 
#to calculate and print the square root of 225.

# Import the math module
import posixpath
import math

# Calculate the square root of 225
result = math.sqrt(225)

# Print the result
print("The square root of 225 is:", result)


#2. Write a script that uses the os module to create a new folder named 'MyDownloads' in your current working directory,
# then print the absolute path of the new folder.

import os

# Folder name
folder_name = "MyDownloads"

# Create the folder in the current working directory if it doesn't exist
if not os.path.exists(folder_name):
    os.mkdir(folder_name)

# Get the absolute path of the new folder
folder_path = os.path.abspath(folder_name)

# Print the absolute path
print("Folder created successfully!")
print("Absolute Path:", folder_path)



#3. Use the datetime module to get the current date and time, then format and print it as 'DD-MM-YYYY HH:MM:SS', similar to how WhatsApp shows message timestamps.<br><br><em><strong>
#Hint:</strong> Use strftime() to format the output.</em>

from datetime import datetime

# Get the current date and time
current_datetime = datetime.now()

# Format as DD-MM-YYYY HH:MM:SS
formatted_datetime = current_datetime.strftime("%d-%m-%Y %H:%M:%S")

# Print the formatted date and time
print("Current Date and Time:", formatted_datetime)


#4. Create a custom Python module called playlist_utils.py with a function add_song(playlist, song)
# that adds a song to a list. Import this module in another script and use it to add three songs to a playlist, then print the final playlist.

# Import the custom module
import playlist_utils

# Create an empty playlist
playlist = []

# Add three songs
playlist_utils.add_song(playlist, "Kesariya")
playlist_utils.add_song(playlist, "Shape of You")
playlist_utils.add_song(playlist, "Tum Hi Ho")

# Print the final playlist
print("Final Playlist:", playlist)


#5. Set up a new virtual environment using venv, activate it, and install the 'requests' package using pip. Write a short script that imports requests and prints the version installed.
# <br><br><em><strong>Hint:</strong> Use 'python -m venv venv_folder', then 'pip install requests'.</em> 

# Run these commands in your terminal (PowerShell), not in Python:
# python -m venv venv_folder
# .\venv_folder\Scripts\Activate.ps1
# pip install requests

import requests

print("Requests version:", requests.__version__)