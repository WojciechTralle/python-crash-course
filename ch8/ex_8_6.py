# exercise 8-6
def city_country(city_name, country):
	"""Return formatted pair 'city, country' string"""
	return f"{city_name.title()}, {country.title()}"

print(city_country('olsztyn', 'poland'))
print(city_country('new york', 'united states'))
print(city_country('nancy', 'france'))