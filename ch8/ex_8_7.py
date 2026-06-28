# exercise 8-7
def make_album(artist_name, album_title, songs_number=None):
	"""Return a dictionary describing an album."""
	album = {
	'artist': artist_name.title(), 
	'title': album_title.title(),
	}
	
	if songs_number is not None:
		album['songs_number'] = songs_number
	
	return album

print(make_album('red hot chili peppers', 'blood sugar sex magik', 17))
print(make_album('santana', 'all that i am'))
print(make_album('lady pank', 'lowcy glow'))

