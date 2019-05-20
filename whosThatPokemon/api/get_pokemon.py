import flask
import whosThatPokemon
from whosThatPokemon.api.exceptions import InvalidUsage
import os

@whosThatPokemon.app.route('/api/', methods=['GET'])
def get_options():
	cursor = whosThatPokemon.model.get_db().cursor()

	region = flask.request.args.get('region', default='')
	if region == "":
		raise InvalidUsage('Bad Request', status_code=400)
	
	results = cursor.execute("SELECT Name FROM pokemon \
									WHERE Region=? ORDER BY RANDOM() LIMIT 4", (region,))
	context = results.fetchall()
	for item in context:
		filename = item["Name"] + ".png"
		item['color_url'] = flask.url_for('download_color',
                                              filename=filename, region=region)
		item['silhouette'] = flask.url_for('download_silhouette',
                                              filename=filename, region=region)

	return flask.jsonify(context)


@whosThatPokemon.app.route('/color_pokemon/<path:region>/<path:filename>')
def download_color(filename, region):
    """To download image files."""
    return flask.send_from_directory(os.path.join(whosThatPokemon.app.config['COLOR_FOLDER'],region),
                                     filename, as_attachment=False)

@whosThatPokemon.app.route('/silhouette_pokemon/<path:region>/<path:filename>')
def download_silhouette(filename, region):
    """To download image files."""
    return flask.send_from_directory(os.path.join(whosThatPokemon.app.config['SILHOUETTE_FOLDER'],region),
                                     filename, as_attachment=False)


