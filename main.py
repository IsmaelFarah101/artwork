from menu import *
from artist_handler import *
from artwork_handler import *
def options():
    options = ["1: Search for Artist: ", "2: Add Artist: ","3: Search Artwork: ","4: Add Artwork: ","5: Update Artwork: ","6: Delete Artwork: "]
    for option in options:
        print(option)
def main():
    try:
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

create_artist_tables()
create_artwork_tables()
main()
