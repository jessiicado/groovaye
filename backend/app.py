from flask import Flask, jsonify
from routes.auth import auth_bp
from routes.recommendations import recommend_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp)
app.register_blueprint(recommend_bp)

@app.route('/get_recommendations')
def get_recommendations():
    recommendations = [
        {"artist": "Artist 1", "song": "Song 1", "album": "Album 1"},
        {"artist": "Artist 2", "song": "Song 2", "album": "Album 2"},
        {"artist": "Artist 3", "song": "Song 3", "album": "Album 3"},
    ]

    return jsonify(recommendations)
if __name__ == '__main__':
    app.run(debug=True)