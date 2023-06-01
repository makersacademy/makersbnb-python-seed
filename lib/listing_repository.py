from lib.listings import Listing

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
        listing = Listing(listing_row["id"], listing_row["name"], listing_row["description"], listing_row["price"], listing_row['user_id'])
        available_dates = [row["available_date"] for row in data if row["available_date"] is not None]
        

        return listing, available_dates