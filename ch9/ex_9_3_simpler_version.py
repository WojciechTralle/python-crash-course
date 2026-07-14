# Exercise 9-3

class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, age, profession, hobbies):
        """Initialize attributes describing a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.profession = profession
        self.hobbies = hobbies

    def describe_user(self):
        """Display information about the user."""
        print(f"First name: {self.first_name.title()}")
        print(f"Last name: {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Profession: {self.profession.title()}")
        print(f"Hobbies: {', '.join(self.hobbies)}")

    def greet_user(self):
        """Display a personalized greeting."""
        print(f"Hello, {self.first_name.title()} {self.last_name.title()}!")


users = [
    User(
        "wojciech",
        "tralle",
        32,
        "mathematics professor",
        ["running", "swimming", "cooking"],
    ),
    User(
        "parboni",
        "dey",
        24,
        "phd student",
        ["shopping", "instagram"],
    ),
    User(
        "alex",
        "jones",
        52,
        "radio host",
        ["broadcasting", "politics", "fitness"],
    ),
]

for user in users:
    user.describe_user()
    user.greet_user()
    print()