from flask import make_response, jsonify
from Clean_Blog import app, app_views
# from Clean_Blog import storage
app.register_blueprint(app_views)
# app.register_blueprint(app_views)
# @app.teardown_appcontext
# def close_db_connection(exception):
#     """
#     calls storage.close() to close the database connection
#     """
#
#     storage.close()
#
#
# @app.errorhandler(404)
# def error(error):
#     """
#     Handles 404 error
#     """
#     return make_response(jsonify({"error": "Not found"}), 404)


if __name__ == '__main__':
    app.run(debug=True)
