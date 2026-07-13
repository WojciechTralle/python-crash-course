# exercise 9-1
class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Simulate restaurant description including name and cuisine type."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    
    def open_restaurant(self):
        """Indicate that the restaurant is open"""
        print(f"The restaurant {self.restaurant_name} is now open.")


restaurant = Restaurant("Mitr Thai", "Thai")

print(f"Restaurant: {restaurant.restaurant_name}")
print(f"Cuisine: {restaurant.cuisine_type}")

restaurant.describe_restaurant()
restaurant.open_restaurant()





