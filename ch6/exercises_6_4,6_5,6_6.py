# exercise 6-4
glossary = {
    'list': 'a type of object that stores a sequence of values of various types',
    'dictionary': 'an object that stores key-value pairs',
    'if-elif-else chain': 'a chain of conditional statements starting with if, then a finite number of elifs and ending with else',
    'loop': 'a structure that repeats a block of code',
    'variable': 'a name that refers to a value stored in memory',
    'string': 'a series of characters',
    'integer': 'a whole number',
    'float': 'a number with a decimal point',
    'key': 'the first item in a key-value pair',
    'value': 'the second item in a key-value pair',    
}

for word, defn in glossary.items():
	print(f"\nA {word} is {defn}.")

# exercise 6-5
rivers = {'nile': 'egypt', 'vistula': 'poland', 'danube': 'austria'}

for river, country in rivers.items():
	print(f"\nThe {river.title()} runs through {country.title()}.")

for river in rivers.keys():
	print(river.title())

for country in rivers.values():
	print(country.title())

# exercise 6-6
favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	'wojciech': 'python',
	'allison': 'pascal'
}

friends_poll = ['wojciech', 'allison', 'edward', 'kael', 'garrithos']

for person in friends_poll:
	if person in favorite_languages.keys():
		print(f"{person.title()}, thank you for responding to the poll!")
	else:
		print(f"{person.title()}, please take the poll!")


























