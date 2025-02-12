import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("AMADEUS_FLIGHT_API_KEY")
api_secret = os.getenv("AMADEUS_FLIGHT_API_SECRET") # Replace with your Amadeus API secret

def get_access_token(api_key, api_secret):
    auth_url = 'https://test.api.amadeus.com/v1/security/oauth2/token'
    auth_response = requests.post(auth_url, data={
        'grant_type': 'client_credentials',
        'client_id': api_key,
        'client_secret': api_secret
    })
    
    if auth_response.status_code == 200:
        return auth_response.json()['access_token']
    else:
        print("Error obtaining access token:", auth_response.status_code)
        return None

def get_flight_info(origin, destination, date, access_token):
    search_url = 'https://test.api.amadeus.com/v2/shopping/flight-offers'
    headers = {
        'Authorization': f'Bearer {access_token}',
        'Content-Type': 'application/json'
    }
    params = {
        'originLocationCode': origin,
        'destinationLocationCode': destination,
        'departureDate': date,
        'adults': 1
    }

    response = requests.get(search_url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        if 'data' in data and data['data']:
            for offer in data['data']:
                print(f"Flight: {offer['id']}")
                for segment in offer['itineraries'][0]['segments']:
                    print(f"  From: {segment['departure']['iataCode']} at {segment['departure']['at']}")
                    print(f"  To: {segment['arrival']['iataCode']} at {segment['arrival']['at']}")
                    print(f"  Carrier: {segment['carrierCode']}")
                    print(f"  Flight Number: {segment['number']}")
                print()
        else:
            print("No flight information found.")
    else:
        print("Error:", response.status_code, response.text)


access_token = get_access_token(api_key, api_secret)
if access_token:
    origin = input("Enter the origin airport code: ")
    destination = input("Enter the destination airport code: ")
    date = input("Enter the departure date (YYYY-MM-DD): ")
    get_flight_info(origin, destination, date, access_token)
