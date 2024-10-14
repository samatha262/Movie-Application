import os
import requests
from requests.auth import HTTPBasicAuth
from django.conf import settings

def fetch_movies(page=1):
    # Base URL for the movie listing API
    url = f'https://demo.credy.in/api/v1/maya/movies/?page={page}'

    # Fetching credentials from environment variables
    username = os.getenv('MOVIE_API_USERNAME', settings.MOVIE_API_USERNAME)
    password = os.getenv('MOVIE_API_PASSWORD', settings.MOVIE_API_PASSWORD)

    try:
        response = requests.get(url, auth=HTTPBasicAuth(username, password))
        response.raise_for_status()  # Raise an error for bad responses (4xx or 5xx)

        return response.json()  # Return the JSON response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching movies: {e}")
        return None
