
import requests
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os
import json

# Load environment variables from the .env file
load_dotenv()

# Set Amadeus API credentials
AMADEUS_BASE_URL_TEST = os.getenv("AMADEUS_BASE_URL_TEST")
grant_type = os.getenv("AMADEUS_GRANT_TYPE")
client_id = os.getenv("AMADEUS_CLIENT_ID")
client_secret = os.getenv("AMADEUS_CLIENT_SECRET")

def get_access_token():
    token_file_path = os.path.join(os.path.dirname(__file__), "access_token.txt")

    # Check if the token file exists
    if os.path.exists(token_file_path):
        # Read the token and expiration time from the file
        with open(token_file_path, "r") as file:
            token_info = json.load(file)

        # Extract relevant information from the stored data
        access_token = token_info.get("access_token")
        expiration_time_str = token_info.get("expiration_time")

        # Convert the expiration time to a datetime object
        expiration_time = datetime.fromisoformat(expiration_time_str)

        # Check if the token is still valid
        if expiration_time > datetime.now():
            return access_token

    # If the token doesn't exist or has expired, request a new one
    url = f"{AMADEUS_BASE_URL_TEST}/v1/security/oauth2/token"
    params = {
        "grant_type": grant_type,
        "client_id": client_id,
        "client_secret": client_secret
    }

    response = requests.post(url, data=params)

    if response.status_code == 200:
        data = response.json()
        access_token = data.get("access_token")
        expires_in = data.get("expires_in")

        # Calculate the expiration time
        expiration_time = datetime.now() + timedelta(seconds=expires_in)

        # Save the relevant token information to the file
        token_info = {
            "access_token": access_token,
            "expiration_time": expiration_time.isoformat(),
            "username": data.get("username"),
            "application_name": data.get("application_name"),
            "client_id": data.get("client_id")
        }

        with open(token_file_path, "w") as file:
            json.dump(token_info, file)

        return access_token
    else:
        raise Exception(f"Error: {response.status_code} - {response.text}")
