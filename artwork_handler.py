from models import *
import sqlite3

def create_tables():
    db.connect()
    db.create_tables([Artwork])

def create_artwork(artist,name,price,sold):
    try:
        artistID = Artist.get(Artist.name == artist).id
        if artistID is not None:
            artwork = Artwork(artistID=artistID, name=name, price=price, sold=sold).execute()
            artwork.save()
            return True
        else:
            return False
            raise ModelError('Artist Doesnt Exist')

    except sqlite3.Error as e:
        print(f'Error occured: {e}')

def update_artwork(artist, sold):
    try:
        artistID = Artist.get(Artist.name == artist).id
        if artistID is not None:
            Artwork.update(Artwork.sold == sold).where(Artwork.artistID == artistID).execute()
            return True
        else:
            return False
            raise ModelError('Artist Doesnt Exist')
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

def search(artist):
    try:
        artistID = Artist.get(Artist.name == artist).id
        if artistID is not None:
            art_list = []
            artwork = Artwork.select().where(Artwork.name == artist).execute()
            for art in artwork:
                art_list.append(art.name)
            return art_list
    except sqlite3.Error as e:
        print(f'Error Occured: {e}')

def search_available(artist):
    try:
        artistID = Artist.get(Artist.name == artist).id
        if artistID is not None:
            art_list = []
            artwork = Artwork.select().where((Artwork.name == artist)&(Artwork.sold == False)).execute()
            for art in artwork:
                art_list.append(art)
            return art_list
        else:
            raise ModelError('Artist Doesnt Exist')
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

