1.#Write a lambda function to convert a list of song titles from Spotify to all lowercase letters and use map()
# to apply it to ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita'], printing the cleaned list.

# List of Spotify song titles
songs = ['Shape Of You', 'Blinding Lights', 'Levitating', 'Senorita']

# Lambda function to convert titles to lowercase
to_lower = lambda song: song.lower()

# Apply the lambda function using map()
cleaned_songs = list(map(to_lower, songs))

# Print the cleaned list
print(cleaned_songs)



2.#Given a list of Zomato restaurant ratings [4.2, 3.8, 4.5, 2.9, 3.5],use filter() 
#with a lambda to find and print only the restaurants with ratings above 4.0.

# List of Zomato restaurant ratings
ratings = [4.2, 3.8, 4.5, 2.9, 3.5]

# Use filter() with a lambda function
high_ratings = list(filter(lambda rating: rating > 4.0, ratings))

# Print the filtered ratings
print(high_ratings)


3.#Use reduce() from functools to calculate the total price of items in a Flipkart shopping cart: [499, 1299, 299, 799].
# Print the final total.<br><br><em><strong>Hint:</strong> Import reduce from functools and use a lambda to sum two numbers.</em>

from functools import reduce

# List of Flipkart item prices
cart_prices = [499, 1299, 299, 799]

# Use reduce() with a lambda function to calculate the total
total_price = reduce(lambda x, y: x + y, cart_prices)

# Print the final total
print("Total Price: ₹", total_price)



4.#Create a function format_followers that takes a number and returns it in 'K' or 'M' format (e.g., 1500 → '1.5K', 1200000 → '1.2M'), 
#then use map() to apply it to a list of follower counts: [950, 1500, 25000, 1200000].

# Function to format follower counts
def format_followers(count):
    if count >= 1_000_000:
        return f"{count / 1_000_000:.1f}M"
    elif count >= 1_000:
        return f"{count / 1_000:.1f}K"
    else:
        return str(count)

# List of follower counts
followers = [950, 1500, 25000, 1200000]

# Apply the function using map()
formatted_followers = list(map(format_followers, followers))

# Print the formatted list
print(formatted_followers)



5.#Use an AI tool like ChatGPT or Copilot to generate a lambda function that filters out all odd numbers from a list of IPL scores [101, 98, 120, 77, 88],
# then test the code in your Python environment and paste the working code here.


# List of IPL scores
ipl_scores = [101, 98, 120, 77, 88]

# Use filter() with a lambda function to keep only even scores
even_scores = list(filter(lambda score: score % 2 == 0, ipl_scores))

# Print the result
print(even_scores)