1. #Define a function called calculate_final_price(price, discount_rate) that returns the final price after applying 
#the discount rate to the given price.

# Function to calculate the final price after applying a discount
def calculate_final_price(price, discount_rate):
    final_price = price - (price * discount_rate / 100)
    return final_price

# Example usage
price = 1000
discount_rate = 20

result = calculate_final_price(price, discount_rate)
print("Final Price: ₹", result)



2.#Create a function called get_delivery_charge(amount, city='Ahmedabad') that returns 0 if city is 'Ahmedabad',
# otherwise returns 50 as a delivery charge.<br><br><em><strong>Hint:</strong> Use a default argument for the city parameter.</em>

# Function to calculate delivery charge
def get_delivery_charge(amount, city='Ahmedabad'):
    if city == 'Ahmedabad':
        return 0
    else:
        return 50

# Example usage
print(get_delivery_charge(500))             # Default city: Ahmedabad
print(get_delivery_charge(500, "Surat"))    # Another city



3.#Write a function called format_price(price, currency='INR') that returns a string like '₹500'
# if currency is 'INR', or '$500' if currency is 'USD'.

# Function to format the price based on the currency
def format_price(price, currency='INR'):
    if currency == 'INR':
        return f"₹{price}"
    elif currency == 'USD':
        return f"${price}"
    else:
        return f"{price}"

# Example usage
print(format_price(500))          # Default currency (INR)
print(format_price(500, 'USD'))   # USD



4.#Build a function called apply_coupon(price, coupon_code=None) that returns the price after a 10% discount if coupon_code is 'ZOMATO10',
# otherwise returns the original price.<br><br><em><strong>Constraint:</strong> Use a default argument for coupon_code.</em>

# Function to apply a coupon discount
def apply_coupon(price, coupon_code=None):
    if coupon_code == "ZOMATO10":
        return price - (price * 10 / 100)   # Apply 10% discount
    else:
        return price   # Return original price

# Example usage
print(apply_coupon(500))                  # No coupon
print(apply_coupon(500, "ZOMATO10"))      # Valid coupon
print(apply_coupon(500, "SAVE20"))        # Invalid coupon