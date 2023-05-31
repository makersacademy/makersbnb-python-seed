from lib.listing import Listing

class ListingRepository:
    def __init__(self, connection):
        self._connection = connection
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM listings")
        return [Listing(row["id"], row["user_id"], row["price"], row["name"], row["description"]) for row in rows]

    def add(self, user_id, price, name, description):
        self._connection.execute("INSERT INTO listings (user_id, price, name, description) VALUES (%s, %s, %s, %s)", [user_id, price, name, description])
        return None