from artist_handler import *
from artwork_handler import *

def add_artist():
    name = input('Enter the name of the artist: ')
    email = input('Enter the email of the artist: ')
    create_artist(name,email)

def search_artist():
    artists = search_artist()
    for artist in artists:
        print(artist) 
     
def create_artwork():
    artist = input('Enter the name of the artist: ')
    name = input('Enter the name of the artwork')
    price = float(input("Enter the price of the artwork: "))
    sold = bool(input('Enter True or False if the product is avaliable or sold: '))
    create_artwork(artist,name,price,sold)

def update_artwork():
    artist = input('Enter the name of the artist: ')
    sold = bool(input('Enter True or False to update trhe products availability: '))
    update_artwork(artist,sold)

def delete_artwork():
    name = input('Enter artwork name: ')
    delete_artwork(name)

def search_artwork():
    question = int(input('Enter 1 to find all artwork or 2 to find available artwork: '))
    if question == 1:
        artworks = search_all()
        for artwork in artworks:
            print(artwork)
    elif question == 2:
        artworks = search_all()
        for artwork in artworks:
            print(artwork)
    else:
        return 


