"""
Who's That Pokemon (main) view.

URLs include:
/
"""
import flask
import whosThatPokemon


@whosThatPokemon.app.route('/', methods=['GET'])
def show_index():
    """Display / route."""
    
    return flask.render_template("index.html")
