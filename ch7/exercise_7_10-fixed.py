# exercise 7-10 - fixed
# In the previous exercise the issue was that if there
# were more than one person with the same name participating
# in the poll, then only the result of the last person person with that name would be displayed.
# Let's fix this.

responses = []

# Set a flag to indicate that the poll is active
polling_active = True

while polling_active:
	name = input("\nWhat is your name? ")
	response = input("\nIf you could visit one place in the world, where would you go? ")


	# Store the response in a dictionary.
	person = {
    'name': name,
    'response': response,
}
	# Add this person and their response to the list of responses.
	responses.append(person)

	# Find out if anyone else is going to take the poll.
	repeat = input("Would you like someone else to take the poll (yes/no)? ")
	if repeat == 'no':
		polling_active = False

# Polling is complete. Show the results.
print("\n--- Polling Results ---")
for person in responses:
	print(f"{person['name'].title()} would like to go to {person['response']}.")

