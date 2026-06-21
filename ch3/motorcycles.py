motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#Modifying elements of a list
#change the first item 'honda' to 'ducati'
motorcycles[0] = 'ducati'
print(motorcycles)

#Adding elements to the end of a list
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#add an element at the end of a list
motorcycles.append('ducati')
print(motorcycles)

#append several items to an empty list
#start with empty list
motorcycles = []
print(motorcycles)

#add several items
motorcycles.append('honda')
motorcycles.append('yamaha')
motorcycles.append('suzuki')
print(motorcycles)

#Inserting elements into a list
motorcycles = ['honda','yamaha','suzuki']
#insert 'ducati' at position (index) 0
motorcycles.insert(0, 'ducati')
print(motorcycles)

#Removing elements from a list
#removing an item using 'del' statement
motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#we delete the first motorcycle. 
del motorcycles[0]
#let's see this removal is permanent
print(motorcycles)

#now let's delete the second motorcycle instead:
motorcycles = ['honda','yamaha','suzuki']
del motorcycles[1]
print(motorcycles)

motorcycles = ['honda','yamaha','suzuki']
print(motorcycles)

#removing an item from the end of the list using 'pop()' method
#let us store the popped motorcycle in a variable:
popped_motorcycle = motorcycles.pop()
print(motorcycles)
#we print the popped motorcycle to show we still have access to it
print(popped_motorcycle)

motorcycles = ['honda','yamaha','suzuki']

last_owned = motorcycles.pop()
print(f"The last motorcycle I owned was a {last_owned.title()}.")

#popping items from any position in a list
motorcycles = ['honda','yamaha','suzuki']

#first pop the first motorcycle and store it in variable first_owned
first_owned = motorcycles.pop(0)
print(f"The first motorcycle I owned was a {first_owned.title()}.")

#removing an item using 'remove()' method
#this method allows one to remove an item, whose position is not known, but its value is known

motorcycles = ['honda','yamaha','suzuki','ducati']
#let's remove the value 'ducati' from the list of motorcycles
print(motorcycles)

motorcycles.remove('ducati')
print(motorcycles)

#now let's look at a list that contains more than one 'ducati'
motorcycles = ['honda','ducati','yamaha','suzuki','ducati']
print(motorcycles)
#in this situation using remove() will only delete once occurence of item
#and we'd need to use a loop to remove all instances of that item
#in fact:
motorcycles.remove('ducati')
print(motorcycles)



motorcycles = ['honda','yamaha','suzuki','ducati']
print(motorcycles)

too_expensive = 'ducati'
motorcycles.remove(too_expensive)
print(motorcycles)
print(f"\nA {too_expensive.title()} is too expensive for me.")

#avoiding index errors when working with lists
motorcycles = ['honda','yamaha','suzuki']
#print(motorcycles[3])

#last item in the list:
print(motorcycles[-1])

#try requesting last item from an empty list:
#motorcycles = []
#print(motorcycles[-1])










