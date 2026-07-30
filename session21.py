#1. Create a Python class called Product with attributes name and price, 
#and a method get_discounted_price() that returns the price after applying a 10% discount.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90   # 10% discount


# Create an object
product1 = Product("Laptop", 50000)

# Display details
print("Product Name:", product1.name)
print("Original Price:", product1.price)
print("Discounted Price:", product1.get_discounted_price())


#2. Now create a subclass called Electronics that inherits from Product and overrides 
#the get_discounted_price() method to apply a 20% discount instead of 10%.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90   # 10% discount


class Electronics(Product):
    def get_discounted_price(self):
        return self.price * 0.80   # 20% discount


# Create objects
product1 = Product("Book", 1000)
electronic1 = Electronics("Laptop", 50000)

# Display details
print("Product:", product1.name)
print("Original Price:", product1.price)
print("Discounted Price (10%):", product1.get_discounted_price())

print()

print("Electronics:", electronic1.name)
print("Original Price:", electronic1.price)
print("Discounted Price (20%):", electronic1.get_discounted_price())


#3. Write a function show_final_price(item) that takes any Product or Electronics 
#object and prints its name and the discounted price by calling get_discounted_price(). 
#Demonstrate polymorphism by passing both a Product and an Electronics object to this function.

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def get_discounted_price(self):
        return self.price * 0.90   # 10% discount


class Electronics(Product):
    def get_discounted_price(self):
        return self.price * 0.80   # 20% discount


# Function to demonstrate polymorphism
def show_final_price(item):
    print("Product Name:", item.name)
    print("Discounted Price:", item.get_discounted_price())
    print()


# Create objects
product1 = Product("Book", 1000)
electronic1 = Electronics("Laptop", 50000)

# Pass both objects to the same function
show_final_price(product1)
show_final_price(electronic1)


#4. Build a simple Ticket class for a movie booking app with a method get_final_price().
#Then, create a subclass PremiumTicket that overrides get_final_price() to add a 50 rupee convenience fee.
#Show both in action by creating objects and printing their final prices.
#<br><br><em><strong>Hint:</strong> Use super() in PremiumTicket to reuse the parent method and add the extra fee.</em>

class Ticket:
    def __init__(self, movie_name, price):
        self.movie_name = movie_name
        self.price = price

    def get_final_price(self):
        return self.price


class PremiumTicket(Ticket):
    def get_final_price(self):
        # Reuse the parent method and add ₹50 convenience fee
        return super().get_final_price() + 50


# Create objects
ticket1 = Ticket("Avengers: Endgame", 250)
premium_ticket1 = PremiumTicket("Avengers: Endgame", 250)

# Print final prices
print("Movie:", ticket1.movie_name)
print("Regular Ticket Price: ₹", ticket1.get_final_price())

print()

print("Movie:", premium_ticket1.movie_name)
print("Premium Ticket Price: ₹", premium_ticket1.get_final_price())