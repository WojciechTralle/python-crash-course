# exercise 9-8
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


class Privileges:
    """A simple attempt to model privileges of an admin."""

    def __init__(self, privileges=[
        'can add post',
        'can delete post',
        'can ban user'
        ]):
        """Initialize privileges' attributes."""
        self.privileges = privileges

    def show_privileges(self):
        """Display admin's available privileges."""
        for privilege in self.privileges:
            print(f"- {privilege.title()}")


class Admin(User):
    """Represent aspects of a user specific to admin."""
    
    def __init__(self, first_name, last_name, user_profile):
        """Initialize attributes of the parent class User.
        Then initialize attributes specific to admin.
        """
        super().__init__(first_name, last_name, user_profile)
        self.privileges = Privileges()


admin = Admin(
    "wojciech",
    "tralle", 
    {
    'age': 32, 
    'profession': "mathematics professor", 
    'hobbies': ["running", "swimming", 'cooking'],
    }
)

admin.privileges.show_privileges()
admin.describe_user()
admin.greet_user()