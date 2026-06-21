#Exercise 5-8
user_names = ['wojciech','adam','admin','voy5trll','esp']

for user in user_names:
	if user == 'admin':
		print("\nHello admin, would you like to see a status report?")
	else:
		print(f"\nHello {user}, thank you for logging in again.")


#Exercise 5-9
#user_names = ['wojciech','adam','admin','voy5trll','esp']
user_names = []

if user_names:
	for user in user_names:
		if user == 'admin':
			print("\nHello admin, would you like to see a status report?")
		else:
			print(f"\nHello {user}, thank you for logging in again.")
else:
	print("\nWe need to find some users!")

#Exercise 5-10
current_users = ['Wojciech','adam','Admin','voY5trll','esp']

new_users = ['admin','wojciech','Patrick','holley']

current_users_lower = []
for user in current_users:
	current_users_lower.append(user.lower())

print(f"Here are current users in lowercase: {current_users_lower}")

for user in new_users:
	if user.lower() in current_users_lower:
		print(f"\nThe username {user} is not available. Please enter a new user name.")
	else:
		print(f"\nThe username {user} is available.")

#Exercise 5-11
ordinals = [number for number in range(1,10)]

for ordinal in ordinals:
	if ordinal == 1:
		print(f"{ordinal}st")
	elif ordinal == 2:
		print(f"{ordinal}nd")
	elif ordinal == 3:
		print(f"{ordinal}rd")
	else:
		print(f"{ordinal}th")































