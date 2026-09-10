# exercise 9-4
class Restaurant:
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant_name and cuisine_type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """Display the restaurant's name and cuisine type."""
        print(f"The restaurant is called {self.restaurant_name}.")
        print(f"{self.restaurant_name} is a {self.cuisine_type} restaurant.")

    def open_restaurant(self):
        """Display that the restaurant is open."""
        print(f"The restaurant {self.restaurant_name} is now open.")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
        # Improvement: Reject negative values.
        if number < 0:
            raise ValueError("Number of customers served cannot be negative.") 
        self.number_served = number
    
    def increment_number_served(self, number):
        """Increment the number of customers that have been served."""
        # Improvement: Reject negative values.
        if number < 0:
            raise ValueError("Number of customers served cannot be negative.")
        self.number_served += number


