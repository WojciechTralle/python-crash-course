# Exercise 10-6

print("Give me two numbers and I'll return their sum.")

n1 = input("Number one: ")
n2 = input("Number two: ")

try:
    result = int(n1) + int(n2)
except ValueError:
    print("Sorry, you didn't enter two valid numbers!")
else:
    print(f"The sum of your numbers is: {result}")