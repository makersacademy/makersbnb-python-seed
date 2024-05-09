from lib.request import Request

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM users_spaces_requests')
        requests = []
        for row in rows:
            item = Request(row["user_id"], row["space_id"], row["start_date"], row["end_date"])
            requests.append(item) 
        return requests
    
    def create(self, request):
        self._connection.execute('INSERT INTO users_spaces_requests (user_id, space_id, start_date, end_date) VALUES (%s, %s, %s, %s)',
                                 [request.user_id, request.space_id, request.start_date, request.end_date])
        return None 
    
    def find(self, user_id, space_id):
        rows = self._connection.execute('SELECT * FROM users_spaces_requests WHERE user_id = %s AND space_id = %s', [user_id, space_id])
        row = rows[0]
        return Request(row["user_id"], row["space_id"], row["start_date"], row["end_date"])
    
    def delete(self, user_id, space_id):
        self._connection.execute('DELETE FROM users_spaces_requests WHERE user_id = %s AND space_id = %s', [user_id, space_id])
        return None 