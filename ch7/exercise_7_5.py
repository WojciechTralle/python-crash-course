# exercise 7-5
# prompt user for their age
prompt = "\nTell me your age and I'll tell you the price of your movie ticket. "
prompt += "\nEnter 'quit' to stop. "

# start with the flag
active = True
while active:
	age = input(prompt)
	
	# add an if statement to end the program
	if age == 'quit':
		active = False
	# otherwise they entered their age and I can give the price	
	else:
		age = int(age)
		
		if age < 3:
			print("The ticket is free for you!")
		elif age <= 12:
			print("The ticket costs 10 dollars.")
		else:
		    print("The ticket costs 15 dollars.")


























