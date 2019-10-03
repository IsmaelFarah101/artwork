from models import *
import sqlite3

def create_artwork_tables():
    db.create_tables([Artwork])

def create_artwork(artist,name,price,sold):
    try:
        artistID = Artist.get(Artist.name == artist).id
        value = False
        if sold == 1:
            value = True
        elif sold == 2:
            value = False
        artwork = Artwork(artistID=artistID, name=name, price=price, sold=value)
        artwork.save()
        print('\nArtwork Created\n')
        return True
    except Exception as e:
        print('Database Error Couldnt Create Artwork')

def update_artwork(name, sold):
    try:
        value = False
        if sold == 1:
            value = True
        elif sold == 2:
            value = False
        Artwork.update(sold = value).where(Artwork.name == name).execute()
        print('\nArtist Updated\n')
        return True
    except Exception as e:
        print(f'Database Error Couldnt Update Artwork {e}')

def delete_artwork(name):    
    try:
        Artwork.delete().where(Artwork.name == name).execute()
        print('\nArtwork Deleted\n')
        return True
    except Exception as e:
        print('Database Error Couldnt Delete Artwork')

def search_all_artwork(artist):
    try:
        artistID = Artist.get(Artist.name == artist).id
        artwork = Artwork.select().where(Artwork.artistID == artistID)
        return artwork
    except Exception as e:
        print('Database Error Couldnt Fetch All Artwork')

def search_available_artwork(artist):
    try:
        artistID = Artist.get(Artist.name == artist).id
        artwork = Artwork.select().where((Artwork.artistID == artistID)&(Artwork.sold == False))
        return artwork
    except Exception as e:
        print('Database Error Couldnt Fetch Available Artwork')

