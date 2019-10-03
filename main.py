from menu import *
from artist_handler import *
from artwork_handler import *
def options():
    ##this prints of the menu for the user
    options = ["1: Search for Artist: ", "2: Add Artist: ","3: Search Artwork: ","4: Add Artwork: ","5: Update Artwork: ","6: Delete Artwork: "]
    for option in options:
        print(option)
def main():
    try: 
        ##this handles the users response and fetches the appropiate function or exits if the user chooses and different number
        options()
        question = int(input("Enter Choice: "))
        while question:
            if question == 1:
                search_artist_menu()
                options()
                question = int(input("Enter Choice: "))
            elif question == 2:
                add_artist_menu()
                options()
                question = int(input("Enter Choice: "))
            elif question == 3:
                search_artwork_menu()
                options()
                question = int(input("Enter Choice: "))
            elif question == 4:
                create_artwork_menu()
                options()
                question = int(input("Enter Choice: "))
            elif question == 5:
                update_artwork_menu()
                options()
                question = int(input("Enter Choice: "))
            elif question == 6:
                delete_artwork_menu()
                options()
                question = int(input("Enter Choice: "))
            else:
                break
    except ValueError as e:
        print("Only enter numbers")

##creates the tables if they dont exists and call the main function
create_artist_tables()
create_artwork_tables()
main()
