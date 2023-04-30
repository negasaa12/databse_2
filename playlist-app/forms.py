"""Forms for playlist app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, BooleanField, IntegerField, SelectField, PasswordField
from wtforms.validators import InputRequired, Email, Optional, DataRequired, URL
from models import Song


class PlaylistForm(FlaskForm):
    """Form for adding playlists."""

    name = StringField('Name', validators=[InputRequired()])

    description = StringField('Description', validators=[InputRequired()])
    # Add the necessary code to use this form


class SongForm(FlaskForm):
    """Form for adding songs."""
    title = StringField('Title', validators=[InputRequired()])

    artist = StringField('Artist', validators=[InputRequired()])
    # Add the necessary code to use this form


# DO NOT MODIFY THIS FORM - EVERYTHING YOU NEED IS HERE
class NewSongForPlaylistForm(FlaskForm):
    """Form for adding a song to playlist."""

    song = SelectField('Song To Add', coerce=int)

    def __init__(self, *args, **kwargs):
        super(NewSongForPlaylistForm, self).__init__(*args, **kwargs)
        self.song.choices = [(song.id, song.title)
                             for song in Song.query.all()]
