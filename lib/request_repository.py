from lib.request import Request
from lib.space import Space
from lib.space_repository import SpaceRepository

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
        # Get the current space's availability
        space_repository = SpaceRepository(self._connection)
        space = space_repository.find(request.space_id)[0]
        current_availability = space.availability
        # Remove the confirmed date from the availability string
        confirmed_date = request.date_to_book
        new_availability = ", ".join([date.strip() for date in current_availability.split(",") if date.strip() != confirmed_date.strip()])
        # Update the space's availability in the database
        space_repository.update_availability(space.id, new_availability)

    def decline_a_request(self, request):
        request.request_status = "False"
        space_repository = SpaceRepository(self._connection)
        space = space_repository.find(request.space_id)[0]
        current_availability = space.availability
        # Add the canceled date back to the availability string
        canceled_date = request.date_to_book
        new_availability = ", ".join([current_availability.strip(), canceled_date.strip()])
        # Update the space's availability in the database
        space_repository.update_availability(space.id, new_availability)

    def find_spaces_by_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM spaces JOIN requests ON spaces.id = requests.space_id WHERE request_status = \'TBC\' AND spaces.user_id = %s',[user_id])
        spaces_by_user_id = []
        for row in rows:
            item = Request(row["id"], 
                        row["user_id"], 
                        row["space_id"], 
                        row["date_to_book"], 
                        row["request_status"],)
            spaces_by_user_id.append(item)
        return spaces_by_user_id
    
    def find_requests_sent_by_user_id(self, user_id):
        rows = self._connection.execute(
            'SELECT * FROM requests WHERE requests.user_id = %s', [user_id])
        users_requests_made = []
        for row in rows:
            item= Request(row["id"], 
                        row["user_id"], 
                        row["space_id"], 
                        row["date_to_book"], 
                        row["request_status"],)
            users_requests_made.append(item)
        return users_requests_made

"""
user_id in requests
and match all the      
"""