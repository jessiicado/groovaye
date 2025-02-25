from flask import Blueprint, request, jsonify
import requests
from backend.config import SPOTIFY_API_URL

recommend_bp = Blueprint("recommendations", __name__)

#recommended artists: take top artists, get those related artists and fetch top tracks of those artists
@recommend_bp.route('/recommendations', methods=["GET"])
def get_recommendations():
    access_token = request.headers.get("Authorization")

    if not access_token:
        return jsonify({"error": "No token provided"}), 401
    
    headers = {"Authorization": f"Bearer {access_token}"}

#get top artists
    top_artists_url = f"{SPOTIFY_API_URL}/me/top/artists"
    top_artists_response = requests.get(top_artists_url, headers=headers)

    if top_artists_response.status_code != 200:
        return jsonify({"error": "Failed to fetch top artists"}), 400
    
    top_artists = top_artists_response.json()["items"]
    recommended_tracks = []

    for artist in top_artists[:5]: #limit to 5 artists to reduce API calls
        artist_id = artist["id"] 

        related_artists_url = f"{SPOTIFY_API_URL}/artists/{artist_id}/related-artists"
        related_response = requests.get(related_artists_url, headers=headers)

        if related_response.status_code != 200:
            continue

        related_artist = related_response.json()["artists"]

        for related in related_artist[:3]:
            related_id = related["id"]

            tracks_url = f"{SPOTIFY_API_URL}/artists/{related_id}/top-tracks"
            tracks_response = requests.get(tracks_url, headers=headers)

            if tracks_response.status_code != 200:
                continue
            
            tracks = tracks_response.json()["tracks"]

            for track in tracks[:2]:
                recommended_tracks.append({
                    "track_name": related["name"],
                    "artist_name": track["name"],
                    "preview_url": track["preview_url"],
                    "album_cover": track["album"]["images"][0]["url"],
                    "spotify_url": track["external_urls"]["spotify"]
            })

    return jsonify({"tracks": recommended_tracks})
        