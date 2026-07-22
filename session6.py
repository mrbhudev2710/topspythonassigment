1. #Create a Python dictionary called insta_followers that stores the number of followers for 5 Instagram influencers 
# (use their usernames as keys and follower counts as values). Print the dictionary.

# Dictionary storing Instagram influencers and their follower counts
insta_followers = {
    "viratkohli": 271000000,
    "shraddhakapoor": 95000000,
    "aliaabhatt": 87000000,
    "deepikapadukone": 80000000,
    "narendramodi": 92000000
}

# Print the dictionary
print(insta_followers)

2. #Add a new influencer to your insta_followers dictionary and update the follower count for one existing influencer. 
# Then, delete one influencer from the dictionary and print the updated dictionary.

# Dictionary storing Instagram influencers and their follower counts
insta_followers = {
    "viratkohli": 271000000,
    "shraddhakapoor": 95000000,
    "aliaabhatt": 87000000,
    "deepikapadukone": 80000000,
    "narendramodi": 92000000
}

# Add a new influencer
insta_followers["kiaraaliaadvani"] = 35000000

# Update the follower count of an existing influencer
insta_followers["viratkohli"] = 272000000

# Delete one influencer
del insta_followers["deepikapadukone"]

# Print the updated dictionary
print(insta_followers)

3. #Given a dictionary called food_prices with 5 Zomato food items as keys and their prices as values, 
# write code to display all items that cost more than ₹200.

# Dictionary of Zomato food items and their prices
food_prices = {
    "Burger": 180,
    "Pizza": 350,
    "Biryani": 250,
    "Pasta": 190,
    "Paneer Tikka": 300
}

# Display items costing more than ₹200
print("Food items costing more than ₹200:")

for item, price in food_prices.items():
    if price > 200:
        print(f"{item}: ₹{price}")