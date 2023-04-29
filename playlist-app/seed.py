from models import db, Song, Playlist, PlaylistSong
from app import app

db.drop_all()

db.create_all()

"""Songs"""

song1 = Song(title='Beat It', artist='Michael Jackson')

song2 = Song(title='Who Hurt You?', artist='Daniel Ceasar')

song3 = Song(title='Smooth Criminal', artist='Michael Jackson')

song4 = Song(title='Monster', artist='Nicki Minaj')

song5 = Song(title='SAFARI', artist='Tyler, The Creator')

song6 = Song(title='CORSO', artist='Tyler, The Creator')


"""Playlist"""

playlist1 = Playlist(name='Hip-Hop', description='The best songs in Hip-Hop')


playlist2 = Playlist(name='Pop', description='The best songs of Pop')


"""song commits"""
db.session.add(song1)
db.session.add(song2)
db.session.add(song3)
db.session.add(song4)
db.session.commit()
db.session.add(song5)
db.session.add(song6)


"""playlist commit"""

db.session.add(playlist1)
db.session.add(playlist2)

db.session.commit()
