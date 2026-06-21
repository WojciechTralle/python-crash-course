#Chapter 4
#sorting lists
cars = ['bmw','audi','toyota','subaru']
#use sort() method to sort the list alphabetically
cars.sort()
print(cars)
#note: the order is permanently changed

#one can also sort the list in reverse alphabetical order
cars = ['bmw','audi','toyota','subaru']
cars.sort(reverse = True)
print(cars)

#sorting lists temporarily with sorted() function
cars = ['bmw','audi','toyota','subaru']

print("Here is the original list:")
print(cars)

print("Here is the sorted list:")
print(sorted(cars))

print("Here is the original list again:")
print(cars)

#sorted() function also supports reverse = True argument:
print("Here is the list in reverse alphabetical order:")
print(sorted(cars, reverse = True))

#printing a list in reverse order with reverse() method
cars = ['bmw','audi','toyota','subaru']
print(cars)

cars.reverse()
print(cars)

#find length of list using len()
print(f"The length of the list with cars is {len(cars)}.")


#Chapter 5
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
	if car == 'bmw':
		print(car.upper())
	else:
		print(car.title())






















