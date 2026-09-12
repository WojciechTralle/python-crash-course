from user import User

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
