# using exceptions

try:
	print(5/0)
except ZeroDivisionError:
	print("You can't divide by zero!")

try:
	print(5/1)
except ZeroDivisionError:
	print("You can't divide by zero!")
