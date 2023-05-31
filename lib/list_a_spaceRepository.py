from lib.list_a_space import Listing
from lib.user import User

class ListingRepository:
    def __init__(self, connection) -> None:
        self._connection = connection

    def add(self):
        self._connection.execute("INSERT INTO listings (user_id, name, description, price) VALUES (%s, %s, %s, %s)", [User.id, Listing.name, Listing.description, Listing.price])
        return None
