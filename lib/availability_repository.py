from lib.availability import Availability
from datetime import date

class AvailabilityRepository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all artists
    def all(self):
        rows = self._connection.execute('SELECT * from availability')
        availablespaces = []
        for row in rows:
            item = Availability(row["space_id"], row["date"], row["status"])
            availablespaces.append(item)
        return availablespaces
    
