#1. Use re.findall() to extract all valid phone numbers from a given string in the format '+91-XXXXXXXXXX' 
#(e.g., '+91-9876543210'). Print the list of found numbers.

import re

# Sample string containing phone numbers
text = """
Customer 1: +91-9876543210
Customer 2: +91-9123456789
Invalid: 9876543210
Office: +91-9988776655
"""

# Regular expression pattern
pattern = r"\+91-\d{10}"

# Find all matching phone numbers
phone_numbers = re.findall(pattern, text)

# Print the list of found numbers
print("Phone Numbers Found:")
print(phone_numbers)

#2. Write a Python function using re.search() that checks if a string contains a valid date in the format 
#'DD/MM/YYYY'. The function should return True if a date is found, otherwise False.

import re

def contains_valid_date(text):
    # Regular expression for DD/MM/YYYY format
    pattern = r"\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/\d{4}\b"

    # Search for the date in the string
    if re.search(pattern, text):
        return True
    else:
        return False


# Example usage
text1 = "My birthday is 15/08/2024."
text2 = "Today's date is 2024-08-15."

print(contains_valid_date(text1))  # True
print(contains_valid_date(text2))  # False


#3. Given a block of text containing multiple prices (like 'Rs. 299', 'Rs. 1500', etc.),
#use re.findall() to extract all the numeric price values as integers and print their sum.
#<br><br><em><strong>Hint:</strong> Look for patterns like 'Rs. ' followed by one or more digits.</em>


import re

# Sample text
text = "Laptop: Rs. 29999, Mouse: Rs. 799, Keyboard: Rs. 1500, Pen Drive: Rs. 999"

# Extract all numeric price values
prices = re.findall(r"Rs\.\s*(\d+)", text)

# Convert extracted strings to integers
prices = [int(price) for price in prices]

# Print the extracted prices
print("Prices:", prices)

# Print the sum of all prices
print("Total Sum:", sum(prices))


#4. Use re.sub() to replace all email addresses in a string with '[hidden email]'
# and print the modified string.<br><br><em><strong>Constraint:</strong> Do not use any external libraries except re.</em>


import re

# Sample text
text = """
Contact us at support@example.com or sales123@gmail.com.
You can also email admin@company.org for more details.
"""

# Replace all email addresses with '[hidden email]'
modified_text = re.sub(
    r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}",
    "[hidden email]",
    text
)

# Print the modified string
print(modified_text)


#5. Download a sample Instagram comments text file (or create your own with at least 10 lines),
# then write a Python script to extract all valid Instagram usernames (pattern: starts with '@', followed by letters,
# numbers, underscores, minimum 3 characters) using re.findall() and print the unique usernames.

import re

# Open and read the file
with open("comments.txt", "r") as file:
    comments = file.read()

# Regular expression:
# @ followed by letters, numbers, or underscores
# Minimum username length = 3 characters (after @)
pattern = r'@[A-Za-z0-9_]{3,}'

# Extract all usernames
usernames = re.findall(pattern, comments)

# Remove duplicates using a set
unique_usernames = sorted(set(usernames))

# Print unique usernames
print("Unique Instagram Usernames:")
for username in unique_usernames:
    print(username)