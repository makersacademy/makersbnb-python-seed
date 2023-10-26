from lib.request import *
from datetime import datetime

class RequestRepo():

    def __init__(self, connection):
        self._connection = connection

    def get_all_requests_by_listing_id(self, listing_id):
        rows = self._connection.execute("SELECT * FROM requests WHERE listing_id = %i" % (int(listing_id)))
        requests = []
        for row in rows:
            request = Request(row['date'], row['listing_id'], row['requested_by_id'], row['requested_from_id'])
            requests.append(request)
        return requests

    def get_all_outgoing_requests(self, user_id):
        rows = self._connection.execute("SELECT * FROM requests WHERE requested_by_id = %i" % (int(user_id)))
        requests = []
        for row in rows:
            request = Request(row['date'], row['listing_id'], row['requested_by_id'], row['requested_from_id'])
            requests.append(request)
        outgoing_requests = []
        for request in requests:
            dict = {}
            dict['listing_id'] = request.listing_id
            listing = self._connection.execute("SELECT listing_name FROM listings WHERE id = %i" % int((request.listing_id)))[0]['listing_name']
            dict['listing'] = listing
            dict['date'] = request.date.strftime("%d/%m/%Y")
            outgoing_requests.append(dict)
        return outgoing_requests
    
    def get_all_incoming_requests(self, user_id):
        rows = self._connection.execute("SELECT * FROM requests WHERE requested_from_id = %i" % (int(user_id)))
        requests = []
        for row in rows:
            request = Request(row['date'], row['listing_id'], row['requested_by_id'], row['requested_from_id'])
            requests.append(request)
        outgoing_requests = []
        for request in requests:
            dict = {}
            dict['listing_id'] = request.listing_id
            listing = self._connection.execute("SELECT listing_name FROM listings WHERE id = %i" % int((request.listing_id)))[0]['listing_name']
            dict['listing'] = listing
            dict['date'] = request.date.strftime("%d/%m/%Y")
            username = self._connection.execute("SELECT username FROM users WHERE id = %i" % int((request.requested_by_id)))[0]['username']
            dict['username'] = username
            outgoing_requests.append(dict)
        return outgoing_requests

