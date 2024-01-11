from lib.availability import Availability

class AvailabilityRepository():
    def __init__(self, connection):
        self._connection = connection

    def add(self, availability:Availability):
        self._connection.execute("INSERT INTO availabilities (date_from, date_to, space_id) VALUES (%s, %s, %s)", [availability.date_from, availability.date_to, availability.space_id])