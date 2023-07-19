from lib.request import Request
from lib.space import Space

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
        self._connection.execute('UPDATE requests SET request_status = \'TBC\' WHERE id = %s', [request.id])
        request.request_status = "TBC"
        return None

    def confirm_booking(self, request):
        self._connection.execute('UPDATE requests SET request_status = \'True\' WHERE id = %s', [request.id])
        request.request_status = "True"
        return None
    
    def decline_a_request(self, request):
        request.request_status = "False"
        return None
    
    def find_spaces_by_user_id(self, user_id):
        rows1 = self._connection.execute(
            'SELECT space_id FROM requests') 
        rows2 = self._connection.execute(
            'SELECT user_id FROM spaces WHERE id = %s',[user_id] #selects all the spaces owned by the given user
        )#of these spaces owned by user check which ones have a request 
        request_list = []
        for space_id in rows1:
            if space_id in rows2:
                request_list.append(space_id)
            else:
                pass
        print(request_list)




        # rows = self._connection.execute(
        #     'SELECT * FROM spaces JOIN requests ON spaces.id = requests.space_id WHERE request_status = \'TBC\' AND spaces.user_id = %s',[user_id])
        # spaces_by_user_id = []
        # for row in rows:
        #     item = Space(row["id"], 
        #                 row["name"], 
        #                 row["description"], 
        #                 row["price"], 
        #                 row["availability"], 
        #                 row["user_id"])
        #     spaces_by_user_id.append(item)
        print('********************')
        print(rows1)
        print('********************')
        print(rows2)
        print('********************')

        # print(spaces_by_user_id)
        return None