from helpers.dates import convert_duration_to_time


def sort_by_price(data, high_to_low=False):
  sorted_data = sorted(data, key=lambda x: x['price']['total'], reverse=high_to_low)
  return sorted_data


def sort_by_duration(data, high_to_low=False):
    for item in data:
        duration_str = item['itineraries'][0]['duration']
        duration_time = convert_duration_to_time(duration_str)
        item['itineraries'][0]['duration_datetime'] = duration_time

    data.sort(key=lambda x: x['itineraries'][0]['duration_datetime'], reverse=high_to_low)
    return data

