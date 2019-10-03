from models import *
import sqlite3
##this is the function to create the table
def create_artwork_tables():
    db.create_tables([Artwork])
##this is the function creates the artwork
def create_artwork(artist,name,price,sold):
    try:
        ##this fetches the artists id
        artistID = Artist.get(Artist.name == artist).id
        ##if sold is 1 or 2 it becomes true or false for availabilty
        value = False
        if sold == 1:
            value = True
        elif sold == 2:
            value = False
        ##create the query and save it to the database
        artwork = Artwork(artistID=artistID, name=name, price=price, sold=value)
        artwork.save()
        print('\nArtwork Created\n')
        return True
    ##raise generic exceptions if there is a issue with the database
    except Exception as e:
        print('Database Error Couldnt Create Artwork')

##this is the function updates the artwork
def update_artwork(name, sold):
    try:
        ##this updates the availibilty based on the arguement passed by the user
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
        ##deletes the artwork for the with the specified name
        Artwork.delete().where(Artwork.name == name).execute()
        print('\nArtwork Deleted\n')
        return True
    except Exception as e:
        print('Database Error Couldnt Delete Artwork')

def search_all_artwork(artist):
    try:
        ##this returns all artworks regardless of availibilty for the particular user
        artistID = Artist.get(Artist.name == artist).id
        artwork = Artwork.select().where(Artwork.artistID == artistID)
        return artwork
    except Exception as e:
        print('Database Error Couldnt Fetch All Artwork')

def search_available_artwork(artist):
    try:
        ##this function only returns the available artworks for the specified user
        artistID = Artist.get(Artist.name == artist).id
        artwork = Artwork.select().where((Artwork.artistID == artistID)&(Artwork.sold == False))
        return artwork
    except Exception as e:
        print('Database Error Couldnt Fetch Available Artwork')

