from lib.listing import Listing
class ListingRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * from listings')
        return [Listing(row["id"], row["name"], row["description"], row["price_per_night"], row["available_from"], row["available_to"]) for row in rows]
    
    def find_by_id(self, id):
        rows = self._connection.execute('SELECT * from listings WHERE id = %s', [id])
        row = rows[0]
        return Listing(row["id"], row["name"], row["description"], row["price_per_night"], row["available_from"], row["available_to"])
    
    def create(self, listing):
        rows = self._connection.execute('INSERT INTO listings (name, description, price_per_night, available_from, available_to) VALUES (%s, %s, %s, %s, %s) RETURNING id', [listing.name, listing.description, listing.price_per_night, listing.available_from, listing.available_to])
        row = rows[0]
        listing.id = row["id"]
        return listing
    
    
    def delete(self, id):
        self._connection.execute('DELETE FROM listings WHERE id = %s', [id])
        return None