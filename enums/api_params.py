from enum import Enum
import argparse

class TravelClass(Enum):
    ECONOMY = "ECONOMY"
    PREMIUM_ECONOMY = "PREMIUM_ECONOMY"
    BUSINESS = "BUSINESS"
    FIRST = "FIRST"

def valid_travel_class(value):
    try:
        return TravelClass(value)
    except ValueError:
        raise argparse.ArgumentTypeError(f"Invalid travel class: {value}. Valid options are: {', '.join(tc.value for tc in TravelClass)}")



def nonstop_enum_bool(value):
    return 'true' if str(value).lower() == 'true' else 'false'
