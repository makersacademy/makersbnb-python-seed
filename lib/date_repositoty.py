from lib.date import Date


class DateRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute(
            "SELECT * FROM dates ORDER BY id ASC;"
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
    
    # to find available spaces on a specific date, give date and True.
    # to find unavailable dates on a specific date, give date and False.
    def find_with_date(self, date, available):
        rows = self._connection.execute(
            "SELECT * FROM dates WHERE date = %s AND available = %s", [date, available]
        )
        return [
            Date(row['id'], str(row['date']), row['available'], row['space_id']) for row in rows
        ]
    
    # to find available dates give True as argument, give False to find unavailable dates.
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
    
    def delete_individual(self, id):
        self._connection.execute(
            "DELETE FROM dates WHERE id = %s", [id]
        )
        return None
    
    def delete_by_space(self, space_id):
        self._connection.execute(
            "DELETE FROM dates WHERE space_id = %s", [space_id]
        )
        return None
    
    # To update a date's availability to available, give the date_id and True.
    # To update a date's availability to unavailable, give the date_id and False.
    def update_availability(self, date_id, new_available):
        self._connection.execute(
            "UPDATE dates SET available = %s WHERE id = %s", 
            [new_available, date_id]
        )
        return None
