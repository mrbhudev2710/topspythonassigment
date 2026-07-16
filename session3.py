1.# Declare four variables in python: your age as an int, your height in centimeters as a float,
# your name as a star, and whether you have a spotify account as a bool. Print each variable and use the type() function to display its data type.abs

# Declare variables
age = 20                    # int
height = 175.5              # float (in centimeters)
name = "Manav"              # str
has_spotify = True          # bool

# Print variables
print("Age:", age)
print("Height:", height)
print("Name:", name)
print("Has Spotify:", has_spotify)

# Print data types
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of name:", type(name))
print("Type of has_spotify:", type(has_spotify))


2. # Write a function total_cart_amount(prices) that takes a list of product price as strings (like ['199.99, '49', '350.75']) and returns the total as a float.
#Print the result for a sample Flipkart-style cart.<br><br><em><strong> Use float() to convert each string before summing.</em>

# Function to calculate total cart amount
def total_cart_amount(prices):
    total = 0
    for price in prices:
        total += float(price)   #convert string to float and add 
    return total

# Sample Flipkart-style cart
prices = ['199.99', '49', '350.75', '1200.50']
print("Total cart amount:", total_cart_amount(prices))


3. # Create a script that asks the users to input their cricket score as a string, converts it to an int,
# and prints 'Half-cenutry!' if the score is 50 or more, otherwise prints 'keep going!'.<br><br><em></strong> Use input(), int(), and if-else.</em>

#Ask the user to enter their cricket score
score = input("Enter your cricket score: ")

# Check the score 
if score >= 50:
    print("Half-century!")
else:
    print("Keep going!")



4. # Given the variables is_premium = 'True (as a string), write code to correctly convert it to a boolean value and print its type.
# <br><br><em><strong>Hint:</strong> Use the bool() function alone won't work as expected. Think about string comparsion.</em>

# String value
is_premium = 'True'

#Convert string to boolean 
is_premium = is_premium == 'True'

# Print the boolean value and its type
print(is_premium)
print(type(is_premium))
