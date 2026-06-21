#Exercise 3-1 
#Names: Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.
names = ['ken', 'chloe','christine','ale']
print(f"The first person is {names[0].title()}")
print(f"The second person is {names[1].title()}")
print(f"The third person is {names[2].title()}")
print(f"The fourth person is {names[3].title()}")

#Using loops:#Exercise 3-1 
#Names: Store the names of a few of your friends in a list called names. Print
#each person’s name by accessing each element in the list, one at a time.
names = ['ken', 'chloe','christine','ale']
print(f"The first person is {names[0].title()}")
print(f"The second person is {names[1].title()}")
print(f"The third person is {names[2].title()}")
print(f"The fourth person is {names[3].title()}")

#Exercise 3-2
#Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message
#should be the same, but each message should be personalized with the
#person’s name.
print(f"Greetings {names[0].title()}!")
print(f"Greetings {names[1].title()}!")
print(f"Greetings {names[2].title()}!")
print(f"Greetings {names[3].title()}!")

#Using loops:
for name in names:
	print(f"Greetings {name.title()}!")

#Exercise 3-3
#Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”
cars = ['honda', 'bmw','volvo','ferrari','volkswagen']
print(f"I would like to own a {cars[1].upper()}")
print(f"I wouldn't mind driving a {cars[0].title()}!")

#Using loops:
for name in names:
	print(name.title())

#Exercise 3-2
#Greetings: Start with the list you used in Exercise 3-1, but instead of just
#printing each person’s name, print a message to them. The text of each message
#should be the same, but each message should be personalized with the
#person’s name.
print(f"Greetings {names[0].title()}!")
print(f"Greetings {names[1].title()}!")
print(f"Greetings {names[2].title()}!")
print(f"Greetings {names[3].title()}!")



#Exercise 3-3
#Your Own List: Think of your favorite mode of transportation, such as a
#motorcycle or a car, and make a list that stores several examples. Use your list
#to print a series of statements about these items, such as “I would like to own a
#Honda motorcycle.”
cars = ['honda', 'bmw','volvo','ferrari','volkswagen']
print(f"I would like to own a {cars[1].upper()}")
print(f"I wouldn't mind driving a {cars[0].title()}!")

for car in cars:
	print(f"I would like to own a {car.title()}!")


