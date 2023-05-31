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
        