from lib.availability import Availability

class AvailabilityRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM availabilities')
        availabilities = []
        for row in rows:
            item = Availability(row['id'], row['availability_from'], row['availability_to'], row['space_id'])
            availabilities.append(item)
        return availabilities
    
    def find(self, id):
        rows = self._connection.execute('SELECT * FROM availabilities WHERE id = %s', [id])
        row = rows[0]
        availability_from = row['availability_from']
        availability_to = row['availability_to']
        return Availability(row['id'], availability_from, availability_to, row['space_id'])
    
    def create(self, availability_from, availability_to, space_id):
        self._connection.execute('INSERT INTO availabilities (availability_from, availability_to, space_id) VALUES (%s, %s, %s)', [availability_from, availability_to, space_id])

    def update(self, availability):
        self._connection.execute('UPDATE availabilities SET availability_from = %s, availability_to = %s, space_id = %s WHERE id = %s', [availability.availability_from, availability.availability_to, availability.space_id, availability.id])
        
    def delete(self, id):
        self._connection.execute('DELETE FROM availabilities WHERE id = %s', [id])