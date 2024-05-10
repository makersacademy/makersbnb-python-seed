from lib.date import *

class DateRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute("SELECT * FROM dates")
        dates = []
        for row in rows:
            item = Date(row['id'], str(row['date']), row['confirmed'], row['space_id'])
            dates.append(item)
            # print(type(item.id))
            # print(type(item.date))
            # print(type(item.confirmed))
            # print(type(item.space_id))
        return dates
    
    def find(self, id):
        row = self._connection.execute("SELECT * FROM dates WHERE id = %s", (id,))
        row = row[0]
        return Date(row['id'], str(row['date']), row['confirmed'], row['space_id'])

    def create(self, date):
        self._connection.execute("INSERT INTO dates (date, confirmed, space_id) VALUES (%s, %s, %s)", (date.date, date.confirmed, date.space_id))
        return None
    
    def delete(self, id):
        self._connection.execute("DELETE FROM dates WHERE id = %s", (id,))
        return None
    