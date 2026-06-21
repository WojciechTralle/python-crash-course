# exercise 7-10
responses = {}

# Set a flag to indicate that the poll is active
polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("\nIf you could visit one place in the world, where would you go? ")


	# Store the response in a dictionary.
	responses[name] = response

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like someone else to take the poll (yes/no)? ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Polling Results ---")
for name, response in responses.items():
	print(f"{name.title()} would like to go to {response.title()}.")

