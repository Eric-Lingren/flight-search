
from enum import Enum
import json
import time

from enums.api_params import TravelClass


CACHE_FILE_PATH = 'amadeus_cache.json'
CACHE_EXPIRATION_TIME_SECONDS = 3600  # 1 hour


def load_request_data_cache():
    try:
        with open(CACHE_FILE_PATH, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return None


def save_request_data_cache(data):
    timestamp = time.time()
    cached_data = {'timestamp': timestamp, 'data': data}
    with open(CACHE_FILE_PATH, 'w') as file:
        json.dump(cached_data, file)


def is_request_data_cache_expired(timestamp):
    current_time = time.time()
    return current_time - timestamp > CACHE_EXPIRATION_TIME_SECONDS



ARGUMENT_DATA_CACHE_FILE_PATH = 'argument_data_cache.json'
ARGUMENT_DATA_CACHE_EXPIRATION_TIME_SECONDS = 3600  # 1 hour


def load_argument_data_cache():
    try:
        with open(ARGUMENT_DATA_CACHE_FILE_PATH, 'r') as file:
            args = json.load(file)
            # Convert string representation of TravelClass to Enum
            if 'travel_class' in args and isinstance(args['travel_class'], str):
                args['travel_class'] = TravelClass(args['travel_class'])
            return args
    except (FileNotFoundError, json.JSONDecodeError):
        return None


class EnumEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Enum):
            return obj.value
        return super(EnumEncoder, self).default(obj)


def save_argument_data_cache(args):
    with open(ARGUMENT_DATA_CACHE_FILE_PATH, 'w') as file:
        json.dump(args, file, cls=EnumEncoder)


def is_argument_data_cache_expired(timestamp):
    current_time = time.time()
    return current_time - timestamp > ARGUMENT_DATA_CACHE_EXPIRATION_TIME_SECONDS
