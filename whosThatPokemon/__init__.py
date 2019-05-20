"""
Who's That Pokemon package initializer.

Anika Stephen 
"""
import flask

# app is a single object used by all the code modules in this package
app = flask.Flask(__name__)  # pylint: disable=invalid-name

# Read settings from config module (insta485/config.py)
app.config.from_object('whosThatPokemon.config')

# Overlay settings read from file specified by environment variable. This is
# useful for using different on development and production machines.
# Reference: http://flask.pocoo.org/docs/config/
app.config.from_envvar('POKEMON_SETTINGS', silent=True)

from whosThatPokemon.index import show_index
import whosThatPokemon.model
import whosThatPokemon.api
