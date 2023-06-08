from lib.request import Request
class RequestRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_requests_by_owner_id(self, owner_id):
        rows = self._connection.execute('SELECT * FROM requests WHERE owner_id = %s', [owner_id])
        requests = []
        for row in rows: 
            requests.append(Request(row['id'], row['owner_id'], row['visitor_id'],
                                    row['space_id'], str(row['request_date']), row['confirmed']))
        return requests

    def get_requests_by_visitor_id(self, visitor_id):
        rows = self._connection.execute('SELECT * FROM requests WHERE visitor_id = %s', [visitor_id])
        requests = []
        for row in rows: 
            requests.append(Request(row['id'], row['owner_id'], row['visitor_id'],
                                    row['space_id'], str(row['request_date']), row['confirmed']))
        return requests