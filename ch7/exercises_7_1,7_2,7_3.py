# exercise 7-1
car = input("What kind of rental car would you like? ")

print(f"Let me see if I can find you a {car}.")

# exercise 7-2
dinner_group = input("How many people are in your dinner group? ")
dinner_group = int(dinner_group)

if dinner_group > 8:
	print("You'll have to wait for a table.")
else:
	print("Your table is ready.")

# exercise 7-3
number = input("Give me a number and I'll tell you if it is a multiple of 10 or not. ")
number = int(number)

if number % 10 == 0:
	print(f"The number {number} is a multiple of 10.")
else:
	print(f"The number {number} is not a multiple of 10.")















