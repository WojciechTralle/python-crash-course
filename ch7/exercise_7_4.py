# exercise 7-4
prompt = "\nPlease enter your desired pizza toppings one at a time: "
prompt += "\nEnter 'quit' to close your order. "

# start with empty list of pizza toppings
toppings_list = []
#create a flag and call it 'active' to indicate the active state of the program
active = True
while active:
	message = input(prompt)
	if message != 'quit':
		toppings_list.append(message)
		print(f"I'll add {message} to your pizza.")

	else:
		active = False

print(f"Here's the complete list of your chosen toppings: {toppings_list}")





















