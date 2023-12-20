from datetime import time, timedelta


class CustomTime:
    def __init__(self, hours, minutes):
        self.hours = hours
        self.minutes = minutes

    def __lt__(self, other):
        # Custom comparison method for sorting
        if self.hours < other.hours or (self.hours == other.hours and self.minutes < other.minutes):
            return True
        return False

    def __repr__(self):
        return f"{self.hours} hours, {self.minutes} minutes"




def convert_duration_to_time(duration_str):
    # Extract hours and minutes from the duration string
    hours_index = duration_str.find('H')
    minutes_index = duration_str.find('M')

    if hours_index != -1:
        hours = int(duration_str[2:hours_index])
    else:
        hours = 0

    if minutes_index != -1:
        minutes = int(duration_str[hours_index + 1:minutes_index])
    else:
        minutes = 0

    # Create a CustomTime object
    result_time = CustomTime(hours, minutes)

    return result_time
