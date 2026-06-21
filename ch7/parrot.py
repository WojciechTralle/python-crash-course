prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

#create a flag and call it 'active' to indicate the active state of the program
active = True
while active:
	message = input(prompt)

	if message == 'quit':
		active = False
	else:
		print(message)






















