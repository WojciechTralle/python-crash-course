#Exercise 4-10
cubes = []
for number in range(1,11):
	cubes.append(number ** 3)

print(f"The first ten cubes are {cubes}")

print("The first three items in the list are:")
for cube in cubes[:3]:
	print(cube)
print("Three items from the middle of the list are:")
for cube in cubes[3:6]:
	print(cube)
print("The last three items in the list are:")
for cube in cubes[7:]:
	print(cube)

#Exercise 4-11
pizzas = ['bianca','parma','artochoke']
for pizza in pizzas:
	print(f"I like {pizza.title()} pizza.")

print("I really really love pizza!")
print(f"I'm not a great fan of pizzas with tomato sauce.")
print(f"Tomato has too strong of a taste for a pizza.")

friend_pizzas = pizzas[:]
pizzas.append('calzone')
friend_pizzas.append('margherita')

print("My favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("My friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)


#Exercise 4-12
my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
for food in my_foods:
	print(food)


print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)





























