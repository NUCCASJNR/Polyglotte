from flask import make_response, jsonify
from Clean_Blog import app, app_views
# from Clean_Blog import storage
app.register_blueprint(app_views)
# app.config['SERVER_NAME'] = 'polyglotte.tech'


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
