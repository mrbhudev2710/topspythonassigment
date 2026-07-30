#1. Define a Python class called Song with attributes title, artist, and duration (in seconds).
# Create an object for your favorite song and print its details.

# Define the Song class
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # Duration in seconds

    def display_details(self):
        print("Song Details")
        print("------------")
        print("Title    :", self.title)
        print("Artist   :", self.artist)
        print("Duration :", self.duration, "seconds")


# Create an object for a favorite song
favorite_song = Song("Kesariya", "Arijit Singh", 268)

# Print the song details
favorite_song.display_details()


#2. Add a method play_preview(self) to the Song class that prints 'Playing 30-second preview of [title] by [artist]'.
# Call this method using the object you created.

# Define the Song class
class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration  # Duration in seconds

    def display_details(self):
        print("Song Details")
        print("------------")
        print("Title    :", self.title)
        print("Artist   :", self.artist)
        print("Duration :", self.duration, "seconds")

    # Method to play a 30-second preview
    def play_preview(self):
        print(f"Playing 30-second preview of {self.title} by {self.artist}")


# Create an object for a favorite song
favorite_song = Song("Kesariya", "Arijit Singh", 268)

# Print song details
favorite_song.display_details()

# Call the play_preview() method
favorite_song.play_preview()


#3. Create a class called FoodOrder with attributes: restaurant_name, items (list), 
#and total_price. Write an __init__() constructor to initialize these,
#then create an object representing your last Zomato or Swiggy order and print its details.

# Define the FoodOrder class
class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

# Create an object representing a Zomato/Swiggy order
my_order = FoodOrder(
    "Domino's Pizza",
    ["Margherita Pizza", "Garlic Bread", "Coke"],
    699
)

# Print the order details
print("Food Order Details")
print("-------------------")
print("Restaurant Name :", my_order.restaurant_name)
print("Items Ordered   :", ", ".join(my_order.items))
print("Total Price     : ₹", my_order.total_price)


#4. Extend the FoodOrder class by adding a method add_item(self, item_name, item_price) that adds the item
#to the items list and updates total_price. Demonstrate by adding two items to your order and printing the updated total.

# Define the FoodOrder class
class FoodOrder:
    def __init__(self, restaurant_name, items, total_price):
        self.restaurant_name = restaurant_name
        self.items = items
        self.total_price = total_price

    # Method to add a new item and update the total price
    def add_item(self, item_name, item_price):
        self.items.append(item_name)
        self.total_price += item_price
        print(f"{item_name} added successfully! (₹{item_price})")

# Create an object representing a food order
my_order = FoodOrder(
    "Domino's Pizza",
    ["Margherita Pizza", "Garlic Bread"],
    550
)

# Add two new items
my_order.add_item("Coke", 50)
my_order.add_item("Chocolate Lava Cake", 120)

# Print the updated order details
print("\nUpdated Food Order Details")
print("--------------------------")
print("Restaurant Name :", my_order.restaurant_name)
print("Items Ordered   :", ", ".join(my_order.items))
print("Total Price     : ₹", my_order.total_price)



#5.  Refactor your Song class so that the duration attribute is optional
#in the constructor (default to 0 if not provided).<br><br><em><strong>Hint:</strong>
#Use a default argument for duration in the __init__() method.</em>

# Define the Song class
class Song:
    def __init__(self, title, artist, duration=0):
        self.title = title
        self.artist = artist
        self.duration = duration  # Defaults to 0 if not provided

    def display_details(self):
        print("Song Details")
        print("------------")
        print("Title    :", self.title)
        print("Artist   :", self.artist)
        print("Duration :", self.duration, "seconds")


# Create an object with duration
song1 = Song("Kesariya", "Arijit Singh", 268)

# Create an object without providing duration
song2 = Song("Apna Bana Le", "Arijit Singh")

# Print details
song1.display_details()
print()

song2.display_details()