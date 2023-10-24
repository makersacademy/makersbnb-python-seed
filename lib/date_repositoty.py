from lib.date import Date


class DateRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM dates;"
        )
        return [
            Date(row['id'], str(row['date']), row['available'], row['space_id']) for row in rows
        ]
    
    def find_with_id(self, id):
        rows = self._connection.execute(
            "SELECT * FROM dates WHERE id = %s", [id]
        )
        row = rows[0]
        return Date(row['id'], str(row['date']), row['available'], row['space_id'])
    
    def find_with_date(self, date):
        rows = self._connection.execute(
            "SELECT * FROM dates WHERE date = %s", [date]
        )
        return [
            Date(row['id'], str(row['date']), row['available'], row['space_id']) for row in rows
        ]
    
    def find_by_available(self, available):
        rows = self._connection.execute(
            "SELECT * FROM dates WHERE available = %s", [available]
        )
        return [
            Date(row['id'], str(row['date']), row['available'], row['space_id']) for row in rows
        ]
    
    def create(self, date):
        rows = self._connection.execute(
            "INSERT INTO dates (date, available, space_id) VALUES (%s, %s, %s) RETURNING id",
            [date.date, date.available, date.space_id]
        )
        row = rows[0]
        date.id = row['id']
        return None
    
    def delete(self, id):
        self._connection.execute(
            "DELETE FROM dates WHERE id = %s", [id]
        )
        return None