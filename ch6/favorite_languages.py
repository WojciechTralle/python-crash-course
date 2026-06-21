favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
}

print(favorite_languages)

print(favorite_languages['sarah'])

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

# looping through entire key-value pairs:
for name, language in favorite_languages.items():
	print(f"{name.title()}'s favorite language is {language.title()}.")

# looping through keys only
for name in favorite_languages.keys():
	print(name.title())

# shorter way to loop through keys only
for name in favorite_languages:
	print(name.title())

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
	print(name.title())

	if name in friends:
		language = favorite_languages[name].title()
		print(f"\t{name.title()}, I see you love {language}!")

if 'erin' not in favorite_languages.keys():
	print("Erin, please take our poll!")

print(favorite_languages.items())
print(favorite_languages.keys())
print(favorite_languages.values())

# print the dictionary with favorite languages
print(favorite_languages)

for name in sorted(favorite_languages.keys()):
	print(f"{name.title()}, thank you for taking the poll.")

# looping through all values in a dictionary
print("The following languages have been mentioned:")
for language in favorite_languages.values():
	print(language.title())

# now without any repetitions
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
	print(language.title())

# create a set with languages
languages = {'python', 'ruby', 'python', 'c'}
print(languages)


favorite_languages = {
	'jen': ['python', 'ruby'],
	'sarah': ['c'],
	'edward': ['ruby', 'go'],
	'phil': ['python','haskell'],
}

for name, languages in favorite_languages.items():
	print(f"\n{name.title()}'s favorite languages are:")
	for language in languages:
		print(f"\t{language.title()}")



















