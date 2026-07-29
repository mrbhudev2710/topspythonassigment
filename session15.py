#1. Write a Python function called get_song_duration_per_minute that divides the total duration of a Spotify playlist (in minutes)
# by the number of songs, and handles the case where the number of songs is zero using try, except, and finally blocks.

def get_song_duration_per_minute(total_duration, number_of_songs):
    try:
        average_duration = total_duration / number_of_songs
        print(f"Average song duration: {average_duration:.2f} minutes")
    except ZeroDivisionError:
        print("Error: Number of songs cannot be zero.")
    finally:
        print("Calculation completed.")

# Example 1
get_song_duration_per_minute(50, 10)

# Example 2 (Zero songs)
get_song_duration_per_minute(50, 0)


#2. Build a Flipkart-style price-per-item calculator: take total cart amount and item count as input,
# perform division, and use try-except to catch and display a user-friendly message if the item count is zero.

def calculate_price_per_item():
    try:
        # Take user input
        total_amount = float(input("Enter total cart amount (₹): "))
        item_count = int(input("Enter number of items: "))

        # Calculate price per item
        price_per_item = total_amount / item_count

        print(f"Price per item: ₹{price_per_item:.2f}")

    except ZeroDivisionError:
        print("Error: Item count cannot be zero. Please enter at least 1 item.")

# Call the function
calculate_price_per_item()


#3. Create a Paytm cashback calculator that asks for total spend and number of offers applied, then divides spend by
#offers to show average cashback per offer. If the number of offers is zero, raise a custom exception called NoOffersApplied 
#and display a custom error message.<br><br><em><strong>Hint:</strong> Define your own exception class by subclassing Exception.</em>

# Define a custom exception
class NoOffersApplied(Exception):
    pass

# Paytm Cashback Calculator
try:
    total_spend = float(input("Enter total spend (₹): "))
    offers = int(input("Enter number of offers applied: "))

    if offers == 0:
        raise NoOffersApplied("No offers applied! Cashback cannot be calculated.")

    average_cashback = total_spend / offers
    print(f"Average cashback per offer: ₹{average_cashback:.2f}")

except NoOffersApplied as e:
    print("Custom Error:", e)


#4. Refactor the following buggy code to handle exceptions correctly so it never crashes and always prints 'Thank you for using the calculator' at the end, 
# even if an exception occurs:<br><br>def calculate_average_rating(total_rating, num_reviews):<br> return total_rating / num_reviews<br>print(calculate_average_rating(500, 0))

def calculate_average_rating(total_rating, num_reviews):
    return total_rating / num_reviews

try:
    result = calculate_average_rating(500, 0)
    print("Average Rating:", result)

except ZeroDivisionError:
    print("Error: Number of reviews cannot be zero.")

finally:
    print("Thank you for using the calculator.")


#5. Write a function called safe_divide_for_zomato that takes two numbers (bill amount and number of people), 
#uses try, except, else, and finally to divide the bill and print the result, print a custom error if division by zero,
# and always print 'Split calculation done' at the end.

def safe_divide_for_zomato(bill_amount, number_of_people):
    try:
        amount_per_person = bill_amount / number_of_people
    except ZeroDivisionError:
        print("Error: Number of people cannot be zero.")
    else:
        print(f"Each person should pay: ₹{amount_per_person:.2f}")
    finally:
        print("Split calculation done")

# Example 1
safe_divide_for_zomato(1200, 4)

# Example 2 (Division by zero)
safe_divide_for_zomato(1200, 0)