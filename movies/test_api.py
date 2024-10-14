import requests

# Registration URL
register_url = 'http://localhost:8000/register/'
registration_data = {
    'username': 'new_user',
    'password': 'secure_password'
}
register_response = requests.post(register_url, json=registration_data)

if register_response.status_code == 201:
    print("User registered successfully!")
else:
    print("Error registering user:", register_response.json())

# Token URL
token_url = 'http://localhost:8000/api/token/'
token_data = {
    'username': 'new_user',
    'password': 'secure_password'
}
token_response = requests.post(token_url, json=token_data)

if token_response.status_code == 200:
    tokens = token_response.json()
    access_token = tokens['access']
    print("Access token obtained:", access_token)
else:
    print("Error obtaining token:", token_response.json())

# Use the token to access protected resources
movies_url = 'http://localhost:8000/movies/'
headers = {
    'Authorization': f'Bearer {access_token}',  # Include the token here
    'Content-Type': 'application/json'
}
movies_response = requests.get(movies_url, headers=headers)

if movies_response.status_code == 200:
    print("Movies fetched successfully:", movies_response.json())
else:
    print("Error fetching movies:", movies_response.json())
