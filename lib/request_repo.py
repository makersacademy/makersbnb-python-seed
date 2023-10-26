from lib.request import *

class RequestRepo():

    def __init__(self, connection):
        self._connection = connection

    def get_all_requests_by_listing_id(self, listing_id):
        rows = self._connection.execute("SELECT * FROM requests WHERE listing_id = %i" % (int(listing_id)))
        requests = []
        for row in rows:
            request = Request(row['date'], row['listing_id'], row['requested_by'], row['requested_from'])
            requests.append(request)
        return requests

    def get_all_incoming_requests(self, user_id):
        rows = self._connection.execute("SELECT * FROM requests WHERE requested_from = %i" % (int(user_id)))
        requests = []
        for row in rows:
            request = Request(row['date'], row['listing_id'], row['requested_by'], row['requested_from'])
            requests.append(request)
        return requests
    
    def get_all_outgoing_requests(self, user_id):
        rows = self._connection.execute("SELECT * FROM requests WHERE requested_by = %i" % (int(user_id)))
        requests = []
        for row in rows:
            request = Request(row['date'], row['listing_id'], row['requested_by'], row['requested_from'])
            requests.append(request)
        return requests