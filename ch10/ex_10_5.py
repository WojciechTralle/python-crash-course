# Exercise 10-5

filename = 'poll_responses.txt'

i = 0

print("Enter 'quit' when you're finished with the poll.")

while True:
    response = input("Why do you like programming? ")

    if response.lower() == 'quit':
        break

    print("Thank you! Your response was added to the poll.")

    with open(filename, 'a') as file_object:
        file_object.write(f"{i+1}. {response}\n")

    i += 1