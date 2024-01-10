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
            item = Availability(row["id"], row["space_id"], row["date"], row["status"])
            availablespaces.append(item)
        return availablespaces
    
    def create(self, space):
        self._connection.execute('INSERT INTO availability (space_id, date, status) VALUES (%s, %s, %s)', 
                                [space.space_id, space.date, space.status])
        return None
