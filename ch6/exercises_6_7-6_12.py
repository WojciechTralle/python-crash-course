# exercise 6-7
person_1 = {'first_name': 'wojciech', 
'last_name': 'tralle', 
'age': 31, 
'city': 'new york',
}

person_2 = {'first_name': 'parboni', 
'last_name': 'dey', 
'age': 24, 
'city': 'charlottesville',
} 

person_3 = {
    'first_name': 'ken',
    'last_name': 'adams',
    'age': 40,
    'city': 'boston',
}

people = [person_1, person_2, person_3]

for person in people:
	full_name = f"{person['first_name']} {person['last_name']}"
	age = person['age']
	city = person['city']
	print(f"\nFull Name: {full_name.title()}")
	print(f"Age: {age}")
	print(f"City: {city.title()}" )

# exercise 6-8
cat = {'kind': 'cat', 'owner_name': 'kael'}
hamster = {'kind': 'hamster', 'owner_name': 'alex'}

pets = [cat, hamster]
for pet in pets:
	print(f"\nThis animal is a {pet['kind']}. The name of its owner is {pet['owner_name'].title()}.")

# exercise 6-9
favorite_places = {'arthas': ['northrend','lorderon'], 
'terenas': ['lorderon'], 
'antonidas': ['kirin tor'],
'thrall': ['durotar', 'outland', 'kalimdor']
}

for person, places in favorite_places.items():
	print(f"\nCharacter's Name: {person.title()}")
	print(f"Favorite place(s) are:")
	for place in places:
		print(f"\t{place.title()}")

# exercise 6-10
favorite_numbers = {'wojciech': [7, 64, 1969], 
'kate': [13], 
'allison': [5,3], 
'adam': [1,2,3,9], 
'wallie': [8,67],
}

for person, numbers in favorite_numbers.items():
	print(f"\n{person.title()}'s favorite numbers:")
	for number in numbers:
		print(f"\t{number}")

# exercise 6-11
cities = {
'olsztyn': {
'country': 'poland', 
'population': 172000, 
'fact': 'Copernicus worked there'
},
'new york city': {
'country': 'united states', 
'population': 8500000,
'fact': 'one of the culinary capitals of the world'
},
'nancy': {
'country': 'france',
'population': 103000,
'fact': 'many strong mathematicians worked there including Hermite and Poincare'
},
}

for city, city_info in cities.items():
	print(f"\n{city.title()} is a city in {city_info['country'].title()}.")
	print(f"It has population around {city_info['population']}.")
	print(f"A fun fact about {city.title()} is that {city_info['fact']}.")


	
























