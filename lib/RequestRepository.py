from lib.Request import Request

class RequestRepository:
    def __init__(self, connection):
        self._connection = connection
        
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM requests")
        
        return [
            Request(row['req_id'], row['space_id'], row['date_req'], row['stat'])
            for row in rows
        ]
        
# Create booking request     
    def create(self, request):
        self._connection.execute(
        'INSERT INTO requests (req_id, space_id, date_req, stat) VALUES (%s, %s, %s, %s)', 
        [request.req_id, request.space_id, request.date_req, request.stat]
        )