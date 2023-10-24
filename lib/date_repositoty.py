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