# Exercise 10-3
filename = 'guest.txt'

guest_name = input("What is your name?")

with open(filename, 'w') as file_object:
	file_object.write(f"The name is {guest_name}.")
    
