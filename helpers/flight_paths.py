# def get_flight_path(data):

#   for item in data:
#         print('\n-------------------')
#         segments = item['itineraries'][0]['segments']
        
#         for i in range(len(segments)):
#             print('\n#######')
#             departure_code = segments[i]['departure']['iataCode']
#             arrival_code = segments[i]['arrival']['iataCode']
#             print('departure_code ', departure_code)
#             print('arrival_code ', arrival_code)
import json


def print_pretty(data):
    formatted_response = json.dumps(data, indent=2)
    print(formatted_response)
    
def get_flight_path(data):
    for item in data:
        print('\n' + '-'*50)
        print(f"Total Cost: {item['price']['total']} USD")
        print(f"Total Duration: {item['itineraries'][0]['duration']}")

        segments = item['itineraries'][0]['segments']

        path_segments = []
        for segment in segments:
            departure_code = segment['departure']['iataCode']
            arrival_code = segment['arrival']['iataCode']
            carrier_code = segment['carrierCode']
            operator_code = carrier_code
            flight_number = segment['number']

            if segment.get('operating') is not None:
              operator_code = segment['operating']['carrierCode']

            segment_info = f"{departure_code} --> {arrival_code} (Carrier: {carrier_code}; Operator: {operator_code}; Flight #: {flight_number})"
            path_segments.append(segment_info)

        print('\n'.join(path_segments))

