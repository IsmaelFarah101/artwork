from models import *
import sqlite3

def create_tables():
    db.connect()
    db.create_tables([Artwork])

def create_artwork(artist,name,price,sold):
    try:
        artistID = Artist.get(Artist.name == artist).id
        artwork = Artwork(artistID=artistID, name=name, price=price, sold=sold).execute()
        artwork.save()
        print('Artwork Created')
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

def update_artwork(artist, sold):
    try:
        artistID = Artist.get(Artist.name == artist).id
        Artwork.update(Artwork.sold == sold).where(Artwork.artistID == artistID).execute()
        print('Artist Updated')
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

def delete_artwork(name):
    try:
        Artwork.delete().where(Artwork.name == name)
        print('Artwork Deleted')
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

def search_all(artist):
    try:
        artistID = Artist.get(Artist.name == artist).id
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
        art_list = []
        artwork = Artwork.select().where((Artwork.name == artist)&(Artwork.sold == False)).execute()
        for art in artwork:
            art_list.append(art) 
        return art_list
    except sqlite3.Error as e:
        print(f'Error occured: {e}')

