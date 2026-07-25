# exercise 9-5

class User:
    """A simple attempt to model a user."""

    def __init__(self, first_name, last_name, user_profile):
        """Initialize a user's first name, last name, and profile."""
        self.first_name = first_name
        self.last_name = last_name
        self.user_profile = user_profile
        self.login_attempts = 0

    def describe_user(self):
        """Display information about the user."""
        print(f"User's first name: {self.first_name.title()}")
        print(f"User's last name: {self.last_name.title()}")
        print(f"Age: {self.user_profile['age']}")
        print(f"Profession: {self.user_profile['profession'].title()}")
        print(f"Hobbies: {', '.join(self.user_profile['hobbies'])}")

    def greet_user(self):
        """Display a personalized greeting."""
        print(f"Greetings, {self.first_name.title()} {self.last_name.title()}!")

    def increment_login_attempts(self):
        """Increment the number of login attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts to 0."""
        self.login_attempts = 0


user = User(
    "wojciech",
    "tralle",
    {
        "age": 32,
        "profession": "mathematics professor",
        "hobbies": ["running", "swimming", "cooking"],
    },
)

user.describe_user()
print()

user.greet_user()
print()

print(
    f"{user.first_name.title()} {user.last_name.title()} "
    f"signed in {user.login_attempts} time(s)."
)

for _ in range(3):
    user.increment_login_attempts()
    print(
        f"{user.first_name.title()} {user.last_name.title()} "
        f"signed in {user.login_attempts} time(s)."
    )
print()

user.reset_login_attempts()
print(
    f"{user.first_name.title()} {user.last_name.title()} "
    f"signed in {user.login_attempts} time(s)."
)

