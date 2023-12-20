import os
from dotenv import load_dotenv
import requests
import argparse

from auth.get_token import get_access_token

load_dotenv()

AMADEUS_BASE_URL_TEST = os.getenv("AMADEUS_BASE_URL_TEST")

def fetch_flight_offers(args):
    query_url = f"{AMADEUS_BASE_URL_TEST}/v2/shopping/flight-offers"
    params = {
        "originLocationCode": args.origin,
        "destinationLocationCode": args.destination,
        "departureDate": args.departure_date,
        "adults": args.adults,
        "children": args.children,
        "infants": args.infants,
        "includedAirlineCodes": args.included_airline_codes,
        "excludedAirlineCodes": args.excluded_airline_codes,
        "nonStop": args.non_stop,
        "currencyCode": args.currency_code,
        "travelClass": args.travel_class.value,
    }
    
    token = get_access_token()
    headers = {"Authorization": f"Bearer {token}"}

    response = requests.get(query_url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json()
        meta = data['meta']

        if meta['count'] == 0:
            print('No results found')
        else:
            return data
    else:
        print(f"Error: {response.status_code}")
        # Handle error cases as needed