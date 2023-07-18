from flask import make_response, jsonify
from Clean_Blog import app, app_views
app.register_blueprint(app_views)
if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
