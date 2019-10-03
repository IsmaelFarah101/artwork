from peewee import *

db = SqliteDatabase('artwork.db')

class Artist(Model):
    name = CharField(null=False,unique=True)
    email = CharField(null=False)
    class Meta:
        database = db

class Artwork(Model):
    artistID = ForeignKeyField(Artist)
    name = CharField(null=False,unique=True)
    price = DecimalField(null=False)
    sold = BooleanField(default=False)
    class Meta:
        database = db