"""
Who's That Pokemon configuration.

Anika Stephen
"""

import os

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Database file is /var/pokemon.sqlite3
DATABASE_FILENAME = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'var', 'pokemon.sqlite3'
)

# File Upload to static/img/
COLOR_FOLDER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'static', 'img', "color_pokemon"
)

SILHOUETTE_FOLDER = os.path.join(
    os.path.dirname(os.path.realpath(__file__)),
    'static', 'img', "silhouette_pokemon"
)
