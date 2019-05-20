"""REST API exception handling."""
import flask
import whosThatPokemon


class InvalidUsage(Exception):
    """Exception class for seach."""

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        """Construct InvalidUsage."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Create dictionary response."""
        obj = dict(self.payload or ())
        obj['message'] = self.message
        obj['status_code'] = self.status_code
        return obj


@whosThatPokemon.app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """Handle exception."""
    response = flask.jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
