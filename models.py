from peewee import *

db = SqliteDatabase('artwork.db')

class Artist(Model):
    name = CharField(unique=True)
    email = CharField()

class Artwork(Model):
    artistID = ForeignKeyField(Artist)
    name = CharField(unique=True)
    price = DecimalField()
    sold = BooleanField(default=False)
    
class ModelError(Exception):
    pass