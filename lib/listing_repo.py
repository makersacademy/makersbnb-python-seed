from lib.listing import *

class ListingRepo():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM listings')
        listings = []
        for row in rows:
            listing = Listing(row['listing_name'], row['listing_description'], float(row['listing_price']), int(row['user_id']))
            listings.append(listing)
        return listings
    
    def find_with_listing_id(self, id):
        data = self._connection.execute('SELECT * FROM listings WHERE id = %i' % (int(id)))
        print(data)
        listing = Listing(data[0]['listing_name'], data[0]['listing_description'], data[0]['listing_price'], data[0]['user_id'])
        return listing
    
    def add(self, name, desc, price, user_id):
        self._connection.execute("INSERT INTO listings (listing_name, listing_description, listing_price, user_id) VALUES ('%s', '%s', %f, %i)" % (name, desc, float(price), int(user_id)))