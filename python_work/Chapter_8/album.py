def make_album(name, title, num_songs = None):
    album = {'name': name, 'title' : title}
    if num_songs:
        album['song_count'] = num_songs
    return album

album = make_album('michael jackson','thriller')
print(album)
album = make_album('Eminem','the eminem show')
print(album)
album = make_album('led zeppelin','led zeppelin IV', 8)
print(album)

while True:
    print("\nPlesae enter the following info about the album:")
    artist_name = input("Artist Name: ")
    album_title = input("Album Title: ")

    whole_album = make_album(artist_name,album_title)
    print(whole_album)

    responce = input("type no to quit the program: ")
    if responce == 'no':
        break
