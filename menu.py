from artist_handler import *
from artwork_handler import *

##this function interfaces with the database handler to create the artist
def add_artist_menu():
    try: 
        name = input('Enter the name of the artist: ')
        ##this raises a value error if they are empty
        if name == "":
            raise ValueError
        email = input('Enter the email of the artist: ')
        if email == "":
            raise ValueError
        ##calls the function and passes the arguement
        create_artist(name,email)
    except ValueError as e:
        print("\nCannot Leave Empty Value\n")

##this function interface with the database handler that fetches the user list
def search_artist_menu():
    ##this returns a list of the artists
    artists = search_artist()
    print("\n")
    ##this prints out each artists name and email
    for artist in artists:
        print(artist.name,'\t',artist.email) 
    print("\n")

##this function interfces with the database handler that creates the artwork
def create_artwork_menu():
    try:
        ##this gets the input and raises a exception if the user leaves anything empty
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
            ##calls the function and passes the arguements
            create_artwork(artist,name,price,sold)
    except ValueError as e:
        print("\nEnter the Correct Value\n")

##this function interfaces with the database handlaer that updates the artwork
def update_artwork_menu():
    try:
        artwork = input('Enter the name of the artwork: ')
        ##this raises exceptions if the user inputs wrong things
        if artwork == "":
            raise ValueError
        sold = int(input('\nEnter 1 to Set to Sold Out\nEnter 2 to Set to Available\nEnter Choice: '))
        if sold != 1 and sold != 2:
            raise ValueError
        ##calls the update function
        update_artwork(artwork,sold)
    except ValueError as e:
        print('\nEnter the Correct Value\n')

##this function interfaces with the database handler that deletes the artwork
def delete_artwork_menu():
    try:
        name = input('Enter artwork name: ')
        ##gets user input and raise exception if its empty
        if name == "":
            raise ValueError
        ##calls the delete function
        delete_artwork(name)
    except ValueError as e:
        print('\nDont leave anything empty\n')
def search_artwork_menu():
    try:
        ##gets the artists name and then asks the user if he wants to see all the artwork or only the available artwork
        name = input("Enter artist name: ")
        if name == "":
            raise ValueError
        ##gets either 1 or 2 to get either the available to all the artwork
        question = int(input("Enter 1 to return all artwork\nEnter 2 to return available artwork: "))
        ##calls the appropriate function for the users response or raises error if the user chooses a different number
        if question == 1:
            artworks = search_all_artwork(name)
            print('\n')
            for artwork in artworks:
                print(f"{artwork.name}\t${artwork.price}\t")
            print('\n')
        elif question == 2:
            artworks = search_available_artwork(name)
            print('\n')
            for artwork in artworks:
                print(artwork.name)
            print('\n')
        else:
            raise ValueError
    except ValueError as e:
        print('\nEnter the Correct Value\n')