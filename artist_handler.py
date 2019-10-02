from models import *
import sqlite3

def create_tables():
    db.connect()
    db.create_tables([Artist])

def create_artist(name, email):
    try:
        artist = Artist(name=name, email=email)
        artist.save()
    except sqlite3.Error as e:
        print(f'Error Occured: {e}')
