# exercise 7-8
sandwich_orders = ['chicken sandwich', 'doner', 'cheeseburger', 'turkey sandwich', 'burrito']
finished_sandwiches = []

# loop through sandwich_orders and remove items from it
# as long as the list is nonempty
while sandwich_orders:
	# Remove the first sandwich order and preserve the original order.
	sandwich = sandwich_orders.pop(0)
	print(f"I made your {sandwich.title()}.")
	finished_sandwiches.append(sandwich)

print("The following sandwiches have been made: ")
for sandwich in finished_sandwiches:
	print(sandwich.title())

























