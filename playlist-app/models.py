"""Models for Playlist app."""

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

db = SQLAlchemy()


class Playlist(db.Model):
    """Playlist."""

    __tablename__ = 'playlists'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    name = db.Column(db.Text, nullable=False)

    description = db.Column(db.Text, nullable=True)

    # ADD THE NECESSARY CODE HERE


class Song(db.Model):
    """Song."""

    __tablename__ = 'songs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.Text, nullable=False)

    artist = db.Column(db.Text, nullable=False)

    # ADD THE NECESSARY CODE HERE


class PlaylistSong(db.Model):
    """Mapping of a playlist to a song."""

    __tablename__ = 'playlistsongs'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    playlist_id = db.Column(db.Integer, ForeignKey('playlists.id'))

    song_id = db.Column(db.Integer, ForeignKey('songs.id'))


# DO NOT MODIFY THIS FUNCTION
def connect_db(app):
    """Connect to database."""

    db.app = app
    db.init_app(app)
