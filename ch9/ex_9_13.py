# Exercise 9-13
from random import randint

class Die:
	"""A simple attempt to represent a die."""

	def __init__(self, sides=6):
		"""Initialize attributes to describe a die."""
		self.sides = sides

	def roll_die(self):
		"""
		Print a random integer between 1 and the number of sides
		of the die.
		"""
		print(randint(1,self.sides))

std_die = Die()
for roll in range(10):
	std_die.roll_die()

ten_sided_die = Die(10)
for roll in range(10):
	ten_sided_die.roll_die()

twenty_sided_die = Die(20)
for roll in range(10):
	twenty_sided_die.roll_die()


