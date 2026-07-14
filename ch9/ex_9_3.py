# exercise 9-3
class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, user_profile):
        """Initialize a user: first_name, last_name and user_profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile

    def describe_user(self):
        """Simulate user's description including first_name, last_name and user_profile."""
        print(f"User's first name: {self.first_name.title()}")
        print(f"User's last name: {self.last_name.title()}")
        #print(f"User's profile: {self.user_profile}")
        print(f"Age: {self.user_profile['age']}")
        print(f"Profession: {self.user_profile['profession'].title()}")
        print(f"Hobbies: {', '.join(self.user_profile['hobbies'])}")

    def greet_user(self):
        """Simulate a personal greeting to a user."""
        print(f"Greetings, {self.first_name.title()} {self.last_name.title()}!")


users = [
    User("wojciech", 
        "tralle", 
    {
    'age': 32, 
    'profession': "mathematics professor", 
    'hobbies': ["running", "swimming", 'cooking'],
    }),
    User("parboni", 
        "dey", 
    {
    'age': 24, 
    'profession': "phd student", 
    'hobbies': ["shopping", "instagram"]
    }),
    User("alex",
        "jones",
    {
    'age': 52,
    'profession': "radio host",
    'hobbies': ["broadcasting", "politics", "fitness"]
    })
]

for user in users:
    user.describe_user()
    user.greet_user()
    print()

