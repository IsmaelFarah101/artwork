from peewee import *
##this is the database
db = SqliteDatabase('artwork.db')

##this is the database that stores the user name and email
class Artist(Model):
    name = CharField(null=False,unique=True)
    email = CharField(null=False)
    class Meta:
        database = db

##this is stores the artwork for the artist with a foriegn key relationship
class Artwork(Model):
    artistID = ForeignKeyField(Artist)
    name = CharField(null=False,unique=True)
    price = DecimalField(null=False)
    sold = BooleanField(default=False)
    class Meta:
        database = db