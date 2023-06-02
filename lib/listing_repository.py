from lib.listings import Listing
from datetime import datetime

class ListingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from listings')
        listings = []
        for row in rows:
            item = Listing(row["id"], row["name"], row["description"], row["price"], row['user_id'])
            listings.append(item)
        return listings
    
    def create(self, listing):
        self._connection.execute(
        'INSERT INTO listings (name, description, price, user_id) VALUES (%s, %s, %s, %s)', 
        [listing.name, listing.description, listing.price, listing.user_id]
    )
    

    def get_single_listing(self, listing_id):
        query = """
        SELECT l.id, l.name, l.description, l.price, l.user_id, a.available_date
        FROM listings l
        LEFT JOIN availability a ON l.id = a.listing_id
        WHERE l.id = %s
        """
        data = self._connection.execute(query, [listing_id])

        if not data:
            return None

        listing_row = data[0]
        print(f" listing_row: {listing_row}")
        listing = Listing(listing_row["id"], listing_row["name"], listing_row["description"], listing_row["price"], listing_row["user_id"])
        available_dates = [datetime.strftime(row["available_date"], "%Y-%m-%d") for row in data if row["available_date"] is not None]
        # available_dates = [row["available_date"] for row in data if row["available_date"] is not None]
        print(f"listing: {listing} available_dates: {available_dates}")
        return listing, available_dates
        
        
        # Find a single listing by id
    def find(self, user_id):
        rows = self._connection.execute(
            'SELECT * from listings WHERE id = %s', [user_id])
        row = rows[0]
        return Listing(row["id"], row["name"], row["description"], row["price"], row["user_id"])