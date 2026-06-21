# Exercise 3-8
travel_destinations = ['Thailand','Japan','Italy','Switzerland','Vietnam']
print(travel_destinations)

print("Here is the list in alphabetical order:")
print(sorted(travel_destinations))

print("Here is the original list:")
print(travel_destinations)

print("Here is the list in reverse alphabetical order:")
print(sorted(travel_destinations, reverse=True))

print("Here is the original list:")
print(travel_destinations)

travel_destinations.reverse()
print("Here is the list in reverse order:")
print(travel_destinations)

# reverse the order again to get the original list
travel_destinations.reverse()
print("Here is the list back in its original order:")
print(travel_destinations)

travel_destinations.sort()
print("Here is the list in alphabetical order:")
print(travel_destinations)

travel_destinations = ['Thailand','Japan','Italy','Switzerland','Vietnam']
print("Here's the original list")
print(travel_destinations)

travel_destinations.sort(reverse=True)
print("Here's the list in reverse alphabetical order:")
print(travel_destinations)


# Exercise 3-9
guest_list = ['Maria C.','Arnold','LuckyLuke','A.C.Doyle']
print(f"Hello {guest_list[0]}. I wanted to invite you to dinner!")
print(f"Hello {guest_list[1]}. I don't know you, but feel free to stop by for dinner.")
print(f"Hi {guest_list[2]}. I'm just practicing coding, and for some reason this name appeared inside my head, so you're invited for dinner.")
print(f"Dear Mr. {guest_list[3]}. I really enjoyed your novel the 'Hound of Baskervilles', and even though you're deceased I'd love to invite you for dinner!")

print(f"Our party has {len(guest_list)} guests!")


# Exercise 3-10
# here are the languages that I know fluently:
my_languages = ['polish','french','english']

# add more languages
my_languages.append('spanish')
my_languages.append('italian')
my_languages.append('japanese')
my_languages.append('german')
my_languages.append('chinese')

# print updated list
print(my_languages)

# insert 'bangla' in 3rd position
my_languages.insert(2,'bangla')
print(my_languages)

# delete 'japanese'
del my_languages[6]
print(my_languages)

# remove last item and store it
popped_language = my_languages.pop()
print(f"Here's the popped language: {popped_language}")

# check list after popping
print(my_languages)

# check stored item
print(popped_language)

# remove item at 4th position (index 3)
my_languages.pop(3)
print(my_languages)

# remove 'bangla'
my_languages.remove('bangla')
print(my_languages)

# sort alphabetically
my_languages.sort()
print(my_languages)

# reverse alphabetical order
my_languages.sort(reverse=True)
print(my_languages)

# temporary alphabetical sort
print(sorted(my_languages))
print(my_languages)

# reset list
my_languages = ['polish', 'french', 'english', 'spanish', 'italian', 'japanese', 'german', 'chinese']
print(f"Now start with the following list of my_languages:\n\t{my_languages}")

# temporary reverse sort
print(sorted(my_languages, reverse=True))
print(my_languages)

# reverse current order
my_languages.reverse()
print(my_languages)

# length of list
print(f"The length of the list is:\t{len(my_languages)}.")