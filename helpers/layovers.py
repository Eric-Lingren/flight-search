
def get_layover_first_cities(data, target_departure_iata_code):
    unique_first_layover_iata_code = set()

    for item in data:
        segments = item['itineraries'][0]['segments']
        
        for i in range(len(segments) - 1):
            departure_code = segments[i]['departure']['iataCode']

            if departure_code == target_departure_iata_code:
                arrival_code = segments[i]['arrival']['iataCode']
                unique_first_layover_iata_code.add(arrival_code)
                break

    return unique_first_layover_iata_code
