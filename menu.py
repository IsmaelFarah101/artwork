from artist_handler import *
from artwork_handler import *

def add_artist_menu():
    try: 
        name = input('Enter the name of the artist: ')
        if name == "":
            raise ValueError
        email = input('Enter the email of the artist: ')
        if email == "":
            raise ValueError
        create_artist(name,email)
    except ValueError as e:
        print("\nCannot Leave Empty Value\n")

def search_artist_menu():
    artists = search_artist()
    print("\n")
    for artist in artists:
        print(artist.name,'\t',artist.email) 
    print("\n")
def create_artwork_menu():
    try:
        artist = input('Enter the name of the artist: ')
        if artist == "":
            raise ValueError
        name = input('Enter the name of the artwork: ')
        if name == "":
                raise ValueError
        price = float(input("Enter the price of the artwork: "))
        if price == "":
                raise ValueError
        sold = int(input('Enter 1 to Set to Available\nEnter 2 to Set to Sold Out\nEnter Choice: '))
        if sold != 1 and sold != 2:
            raise ValueError
        else:
            create_artwork(artist,name,price,sold)
    except ValueError as e:
        print("\nEnter the Correct Value\n")

def update_artwork_menu():
    try:
        artwork = input('Enter the name of the artwork: ')
        sold = int(input('\nEnter 1 to Set to Sold Out\nEnter 2 to Set to Available\nEnter Choice: '))
        if sold != 1 and sold != 2:
            raise ValueError
        update_artwork(artwork,sold)
    except ValueError as e:
        print('\nEnter the Correct Value\n')

def delete_artwork_menu():
    name = input('Enter artwork name: ')
    delete_artwork(name)

def search_artwork_menu():
    try:
        name = input("Enter artist name: ")
        if name == "":
            raise ValueError
        question = int(input("Enter 1 to return all artwork\nEnter 2 to return available artwork: "))
        if question == 1:
            artworks = search_all_artwork(name)
            print('\n')
            for artwork in artworks:
                print(f'{artwork.name}\n')
        elif question == 2:
            artworks = search_available_artwork(name)
            print('\n')
            for artwork in artworks:
                print(f'{artwork.name}\n')
        else:
            raise ValueError
    except ValueError as e:
        print('\nEnter the Correct Value\n')