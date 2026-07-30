#1. Create a Python class called Playlist with a private attribute _songs (a list) 
#and a public method add_song(song) to add a song title to the playlist.
# Print the playlist after adding 3 songs.

# Define the Playlist class
class Playlist:
    def __init__(self):
        # Private attribute
        self._songs = []

    # Public method to add a song
    def add_song(self, song):
        self._songs.append(song)

    # Public method to display the playlist
    def display_playlist(self):
        print("Playlist:")
        for i, song in enumerate(self._songs, start=1):
            print(f"{i}. {song}")


# Create a Playlist object
my_playlist = Playlist()

# Add 3 songs
my_playlist.add_song("Kesariya")
my_playlist.add_song("Apna Bana Le")
my_playlist.add_song("Tum Hi Ho")

# Print the playlist
my_playlist.display_playlist()


#2. Build a Product class for a Flipkart-style app with a private attribute _price. Implement get_price()
# and set_price() methods to access and update the price. Demonstrate setting and getting the price for a product object.

# Define the Product class
class Product:
    def __init__(self, name, price):
        self.name = name
        self._price = price   # Private attribute

    # Getter method
    def get_price(self):
        return self._price

    # Setter method
    def set_price(self, new_price):
        if new_price > 0:
            self._price = new_price
            print("Price updated successfully!")
        else:
            print("Invalid price! Price must be greater than ₹0.")


# Create a Product object
product = Product("Samsung Galaxy M35", 18999)

# Get the initial price
print("Product Name :", product.name)
print("Current Price: ₹", product.get_price())

# Update the price
product.set_price(17999)

# Get the updated price
print("Updated Price: ₹", product.get_price())


#3. Create a Movie class with a private attribute _rating (float between 0 and 10).
#Write getter and setter methods for _rating. The setter should only allow values
#between 0 and 10; if an invalid value is given, print an error message.
#<br><br><em><strong>Constraint:</strong> Do not allow direct access to _rating outside the class.</em>


# Define the Movie class
class Movie:
    def __init__(self, title, rating):
        self.title = title
        self._rating = 0.0   # Private attribute
        self.set_rating(rating)  # Use setter for validation

    # Getter method
    def get_rating(self):
        return self._rating

    # Setter method
    def set_rating(self, rating):
        if 0 <= rating <= 10:
            self._rating = rating
            print("Rating updated successfully!")
        else:
            print("Error: Rating must be between 0 and 10.")


# Create a Movie object
movie = Movie("3 Idiots", 9.2)

# Get the movie rating
print("Movie Title :", movie.title)
print("Rating      :", movie.get_rating())

# Update with a valid rating
movie.set_rating(8.8)
print("Updated Rating :", movie.get_rating())

# Try to update with an invalid rating
movie.set_rating(11)


#4. Design a simple abstract class PaymentMethod with an abstract method pay(amount).
#Then, create two subclasses: Paytm and PhonePe, each implementing pay(amount) 
#to print a different message. Instantiate both and call their pay methods with any amount.

from abc import ABC, abstractmethod

# Abstract class
class PaymentMethod(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Subclass: Paytm
class Paytm(PaymentMethod):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made successfully using Paytm.")


# Subclass: PhonePe
class PhonePe(PaymentMethod):
    def pay(self, amount):
        print(f"Payment of ₹{amount} made successfully using PhonePe.")


# Create objects
paytm = Paytm()
phonepe = PhonePe()

# Call pay() method
paytm.pay(500)
phonepe.pay(750)