# exercise 7-9
sandwich_orders = [
'pastrami', 
'chicken sandwich', 
'doner', 'pastrami', 
'cheeseburger', 
'turkey sandwich', 
'pastrami', 
'burrito'
]
finished_sandwiches = []

print("The deli has run out of pastrami.")

# Remove all occurrences of pastrami.
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Process the remaining orders.
while sandwich_orders:
    sandwich = sandwich_orders.pop(0)
    print(f"I made your {sandwich.title()}.")
    finished_sandwiches.append(sandwich)

print("The following sandwiches have been made: ")
for sandwich in finished_sandwiches:
	print(sandwich.title())



























