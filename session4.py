1. #Take the string 'Flipkart-Sale2024' and use string methods to convert it to lowercase,
#  replace the dash with a space, and print the result.

# Original string
text = "Flipkart-Sale2024"

# Convert to lowercase and replace '-' with a space
result = text.lower().replace("-", " ")

# Print the result
print(result)

2. #Given the product name ' OnePlus Nord-CE 3 ', write code to clean it by removing extra spaces,
#  converting all letters to uppercase, and replacing the dash with a colon.
# <br><br><em><strong>Hint:</strong> Use strip(), upper(), and replace() methods in sequence.</em>

# Original product name
product_name = " OnePlus Nord-CE 3 "

# Clean the product name
cleaned_name = product_name.strip().upper().replace("-", ":")

# Print the cleaned product name
print(cleaned_name)

#Write a function split_product_code(product_code) that takes a string like
#  'ZOMATO-FOOD-2024' and returns a list of its parts using the split() method.

# Function to split the product code
def split_product_code(product_code):
    return product_code.split("-")

# Sample product code
code = "ZOMATO-FOOD-2024"

# Call the function and print the result
result = split_product_code(code)
print(result)

4. #Given the string 'Spotify_Premium_Offer', use string slicing to extract and print only the word 'Premium'.

# Original string
text = "Spotify_Premium_Offer"

# Extract the word "Premium" using string slicing
premium = text[8:15]

# Print the result
print(premium)

#Format and print a message using variables: product = 'Myntra Shirt', price = 799.5. The output should be: 
# 'Deal: Myntra Shirt is available at ₹799.50 only!' using string formatting.

# Variables
product = "Myntra Shirt"
price = 799.5

# Format and print the message
print(f"Deal: {product} is available at ₹{price:.2f} only!")