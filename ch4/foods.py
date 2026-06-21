my_foods = ['pizza','falafel','carrot cake']
friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("My favorite foods are:")
print(my_foods)


print("\nMy friend's favorite foods are:")
print(friend_foods)



##############################################################################
##############################################################################
#here's what happens when one copies a list without using slice
#the following doesn't work! It returns two identical lists mine and my friend's, after modyfying
#so it's commented out
#my_foods = ['pizza','falafel','carrot cake']
#friend_foods = my_foods

#my_foods.append('cannoli')
#friend_foods.append('ice cream')

#print("My favorite foods are:")
#print(my_foods)


#print("\nMy friend's favorite foods are:")
#print(friend_foods)


