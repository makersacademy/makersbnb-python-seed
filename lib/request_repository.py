from lib.request import Request
from datetime import date

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection

    def add(self, request):
        rows = self._connection.execute(
            'INSERT into requests(spaceid, date, guestid, hostid) VALUES (%s, %s, %s, %s) RETURNING id', [
                request.spaceid, request.date, request.guestid, request.hostid
                ]
        )
        request.id = rows[0]['id']
        return None

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM requests'
        )
        request = []
        for row in rows:
            item = Request(row['id'], row['spaceid'], row['date'], row['guestid'], row['hostid'])
            request.append(item)
        return request