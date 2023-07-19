from lib.request import Request

class RequestRepository():
    def __init__(self, connection):
        self._connection = connection
    def all(self):
        rows = self._connection.execute('SELECT * FROM requests')
        requests = []
        for row in rows:
            item = Request(row["id"], row["user_id"], row["space_id"], row["date_to_book"])
            requests.append(item)
        
        return requests