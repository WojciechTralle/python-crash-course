# Exercise 10-4
filename = 'guest_book.txt'

i = 0

print("Enter 'quit' when you're finished with adding guests.")


while True:
    guest_name = input("What is your name? ")
    
    if guest_name.lower() == 'quit':
        break

    print(f"Hello, {guest_name}! Welcome!")

    with open(filename, 'a') as file_object:
        file_object.write(f"{i+1}. {guest_name}\n")

    i += 1