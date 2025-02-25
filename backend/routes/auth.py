from dotenv import load_dotenv #store spotify keys

import requests #talk to API
import urllib.parse

from flask import Flask, redirect, request, jsonify, Blueprint #create web server
from flask_cors import CORS #lets frontend talk to backend
from config import CLIENT_ID, CLIENT_SECRET, REDIRECT_URI, TOKEN_URL

import os #store spotify keys

auth_bp = Blueprint("auth", __name__)

load_dotenv()

app = Flask(__name__)
CORS(app) #allows react to talk to Flask
app.secret_key = os.urandom(24)  # Ensure session works securely


API_BASE_URL = 'https://api.spotify.com/v1/'

@app.route('/')
def index():
    return "Welcome to Groovyr <a href='/login'>Login with Spotify</a>"
# ============================================================
# establishes app route to spotify's authorization 
@app.route('/login')
def login():
    scope = 'user-read-private user-library-modify user-read-email user-modify-playback-state'

    auth_url = (
        "https://accounts.spotify.com/authorize?"
        f"client_id={CLIENT_ID}&response_type=code&redirect_uri={REDIRECT_URI}&scope={scope}"
    )
    return redirect(auth_url)

# ============================================================
#gets access token
# - after successful login, Spotify API gives us secret code
# - exchanges the secret code for an access token (token = ticket to user's artists)
# ============================================================
@app.route('/callback')
def callback():
    code = request.args.get("code") #get secret code
    token_url = "https://accounts.spotify.com/api/token"
    
    data = {
        'code': code,
        'grant_type': 'authorization_code',
        'redirect_uri': REDIRECT_URI,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET
    }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(TOKEN_URL, data=data, headers=headers)
    if response.status_code == 200: #checks if status code is 200 (means good)
        tokens = response.json() #send token to React

    #store refresh token along with access token
        return jsonify({
            "access_token": tokens["access_token"],
            "refresh_token": tokens["refresh_token"],
            "expires_in": tokens["expires_in"]
        })

    return jsonify({"error": "Failed to get token"}), 400

# ============================================================
#refreshes the access token so user doesn't need to log in after an 1 hour 
# ============================================================

@app.route('/refresh-token')
def refresh_token():
    refresh_token = request.json.get("refresh_token")

    if not refresh_token:
        return jsonify({"error": "No refresh token provided"}), 400

    token_url = "https://accounts.spotify.com/api/token"
    data = {
            'grant_type': 'refresh_token',
            'refresh_token': 'refresh_token',
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET
        }

    headers = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(TOKEN_URL, data=data, headers=headers)

    if response.status_code == 200:
        new_tokens = response.json()
        return jsonify({
            "access_token": new_tokens['access_token'],
            "expires_in": new_tokens.get("expires_in", 3600)
        })

    return jsonify({"error": "Failed to refresh token"}), 400
