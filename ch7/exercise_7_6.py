# exercise 7-6
# version with 'break' statement
prompt = "\nPlease enter your desired pizza toppings one at a time: "
prompt += "\nEnter 'quit' to close your order. "

# start with empty list of pizza toppings
toppings_list = []

while True:
	message = input(prompt)
	
	if message == 'quit':
		break
	else:
		toppings_list.append(message)
		print(f"I'll add {message} to your pizza.")

print(f"Here's the complete list of your chosen toppings: {toppings_list}")


# version with conditional test
prompt = "\nPlease enter your desired pizza toppings one at a time: "
prompt += "\nEnter 'quit' to close your order. "

# start with empty list of pizza toppings
toppings_list = []

message = ""

while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        toppings_list.append(message)
        print(f"I'll add {message} to your pizza.")
        
print(f"Here's the complete list of your chosen toppings: {toppings_list}")


















