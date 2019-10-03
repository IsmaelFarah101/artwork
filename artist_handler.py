from models import *

def create_artist_tables():
    db.create_tables([Artist])

def create_artist(name, email):
    try:
        artist = Artist(name=name, email=email)
        artist.save()
        print("\nArtist Created\n")
        return True
    except Exception as e:
        print('Database Error Couldnt Create Artist')

def search_artist():
    try:
        artists = Artist.select()
        return artists
    except Exception as e:
        print('Database Error Couldnt Fetch Artist')