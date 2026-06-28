# exercise 8-8
def make_album(artist_name, album_title, songs_number=None):
    """Return a dictionary describing an album."""
    album = {
    'artist': artist_name.title(), 
    'title': album_title.title(),
    }
    
    if songs_number is not None:
        album['songs_number'] = songs_number
    
    return album

while True:
    print("\nEnter an album's artist and title:")
    print("Enter 'q' to quit.")

    a_name = input("Enter artist's name: ")
    if a_name == 'q':
        break
    a_title = input("Enter album's title: ")
    if a_title == 'q':
        break

    songs_n = input("Enter the number of songs (or press Enter to skip): ")
    
    if songs_n:
        album_info = make_album(a_name, a_title, int(songs_n))
    else:
        album_info = make_album(a_name, a_title)

    print("Here's the album's info: ")
    print(album_info)
