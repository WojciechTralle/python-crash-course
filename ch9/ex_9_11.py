# Exercise 9-11
# Imported Admin
from user_privileges_admin import Admin

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
