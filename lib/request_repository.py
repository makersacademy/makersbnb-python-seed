from lib.request import Request

class RequestRepository():
    def __init__(self, connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT * FROM requests')
        requests = []
        for row in rows:
            item = Request(row["id"], row["user_id"], row["space_id"], row["date_to_book"], row["request_status"])
            requests.append(item)
        return requests
    def create(self, request):
        rows = self._connection.execute(
            'INSERT INTO requests (user_id, space_id, date_to_book, request_status) VALUES (%s, %s, %s, %s) RETURNING id', [
                request.user_id, request.space_id, request.date_to_book, request.request_status])
        request.id = rows[0]['id']

    def find(self, id):
        rows = self._connection.execute(
            'SELECT * from requests WHERE id = %s', [id])
        row = rows[0]
        return Request(row["id"], row["user_id"], row["space_id"], row["date_to_book"], row["request_status"])
    
    def send_request(self, request):
        self._connection.execute('UPDATE requests SET request_status = \'True\' WHERE id = %s', [request.id])
        request.request_status = "TB"
        return None

    def confirm(self, request):
        self._connection.execute('UPDATE requests SET request_status = \'True\' WHERE id = %s', [request.id])
        request.request_status = "True"
        return None
    
    def decline_a_request(self, request):
        request.request_status = "False"
        return None
    
    def find_spaces_by_user_id(self, user_id):
            rows = self._connection.execute(
                     'SELECT * FROM spaces JOIN requests ON spaces.id = requests.space_id WHERE request_status =  ')
            return rows