# Exercise 9-12
from privileges_admin import Admin

my_admin = Admin(
    "wojciech",
    "tralle", 
    {
    'age': 32, 
    'profession': "mathematics professor", 
    'hobbies': ["running", "swimming", 'cooking'],
    }
)


my_admin.privileges.show_privileges()

