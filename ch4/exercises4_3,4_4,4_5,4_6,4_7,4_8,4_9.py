#Exercise 4-3. Counting to twenty
numbers = range(1, 1000001)

#Exercise 4-4. One million.
numbers = range(1, 1000001)
#the print below commented out because of 
#long execution time
#print(numbers)


#Exercise 4-5. Summing a million
print(f"The minimum value in the list is {min(numbers)}.")
print(f"The maximum value in the list is {max(numbers)}.")
print(f"The sum of all natural numbers from 1 to one million equals {sum(numbers)}.")

#Exercise 4-6. Odd numbers
odd_numbers = []
for number in range(1,21,2):
	odd_numbers.append(number)
print(odd_numbers)

#alternatively:
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)


#Exercise 4-7. Threes
threes = []
for number in range(3,31,3):
	threes.append(number)
print(threes)

#alternatively:
threes = list(range(3, 31, 3))
print(threes)

#Exercise 4-8. Cubes
cubes = []
for number in range(1,11):
	cubes.append(number ** 3)

print(cubes)

#Exercise 4-9. Cube Comprehension
cubes = [value ** 3 for value in range(1,11)]
print(cubes)














