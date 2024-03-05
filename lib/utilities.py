from datetime import datetime

# takes a string in the format '2024-07-13' and returns a date object
def string_to_date(string_date):
    return datetime.strptime(string_date, '%Y-%m-%d').date()