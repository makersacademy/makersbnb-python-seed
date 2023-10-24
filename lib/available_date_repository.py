from lib.available_date import AvailableDate

class AvailableDateRepository: # a single available date for a particular space
    def __init__(s, connection):
        s._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT * FROM AvailableDates')
        items = []
        for row in rows:
            items.append(AvailableDate(row['id'], row['date_name'], row['space_id']))
        return items