import time
from api.fetch import fetch_flight_offers
from dotenv import load_dotenv
import json
from enums.api_params import TravelClass, valid_travel_class, nonstop_enum_bool
from helpers.cache import is_request_data_cache_expired, load_argument_data_cache, load_request_data_cache, save_argument_data_cache, save_request_data_cache

from helpers.dates import convert_duration_to_time
from helpers.flight_paths import get_flight_path
from helpers.layovers import get_layover_first_cities
from helpers.sort import sort_by_duration, sort_by_price
import argparse

load_dotenv()

def print_pretty_res(data):
    formatted_response = json.dumps(data, indent=2)
    print(formatted_response)
    



def main():
    parser = argparse.ArgumentParser(description='Make a request to the Amadeus API.')
    
    parser.add_argument('--origin', type=str, required=True, help='Origin location code')
    parser.add_argument('--destination', type=str, required=True, help='Destination location code')
    parser.add_argument('--departure-date', type=str, required=True, help='Departure date')
    parser.add_argument('--adults', type=int, default=1, help='Number of adults (default: 1)')
    parser.add_argument('--children', type=int, default=0, help='Number of children (default: 0)')
    parser.add_argument('--infants', type=int, default=0, help='Number of infants (default: 0)')
    parser.add_argument('--included-airline-codes', type=str, help='Comma separated string of airlines to include')
    parser.add_argument('--excluded-airline-codes', type=str, help='Comma separated string of airlines to exclude')
    parser.add_argument('--non-stop', type=nonstop_enum_bool, default='true', help='Non-Stop flights only (default: True)')
    parser.add_argument('--currency-code', type=str, default="USD", help='Currency (default: USD)')
    parser.add_argument('--travel-class', type=valid_travel_class, default=TravelClass.ECONOMY.value, help='Travel class of flight (default: ECONOMY)')

    args = parser.parse_args()

    cached_argument_data = load_argument_data_cache()

    # Check if the cached argument data exists and matches the current arguments
    if cached_argument_data != vars(args):
        print('Args dont match. Saving amd making new request')
        save_argument_data_cache(vars(args))
        res = fetch_flight_offers(args)
        save_request_data_cache(res)
    else:
        # Try to load data from request data cache
        cached_request_data = load_request_data_cache()
        if cached_request_data and not is_request_data_cache_expired(cached_request_data['timestamp']):
            print("Using cached request data.")
            res = cached_request_data['data']
        else:
            print("Request data is expired or not available. Making a new request.")
            res = fetch_flight_offers(args)
            save_request_data_cache(res)

    locations = res['dictionaries']['locations']
    print('You can have a layover in:')
    layover_list = set(locations.keys())
    print(layover_list)
    
    layover_first_cities = get_layover_first_cities(res['data'], args.origin)

    print('Layover first city: \n', layover_first_cities)


    # flight_paths = get_flight_path(res['data'])




if __name__ == "__main__":
    main()