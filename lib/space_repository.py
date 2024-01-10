from lib.space import Space
from lib.database_connection import DatabaseConnection


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        return [Space(row["id"],
                    row["space_name"],
                    row["description"],
                    row["price"],
                    row["user_id"],
                    str(row["start_date"]),
                    str(row["end_date"])
                    )for row in rows]


    def create(self, space):
        self._connection.execute('INSERT INTO spaces (space_name, description, price, user_id, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)', [space.space_name, space.description, space.price, space.user_id, space.start_date, space.end_date])

    def find_user(self, user_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [user_id])
        row = rows[0]
        return Space(row["id"], row["space_name"], row["description"], row["price"], row["user_id"], row["start_date"], row["end_date"])
    
    def find_price(self, price):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE price = %s', [price])
        row = rows[0]
        return Space(row["id"], row["space_name"], row["description"], row["price"], row["user_id"], row["start_date"], row["end_date"])
    
    def find_availability(self, start_date, end_date):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE %s BETWEEN start_date AND end_date = %s', [start_date, end_date])
        row = rows[0]
        return Space(row["id"], row["space_name"], row["description"], row["price"], row["user_id"], row["start_date"], row["end_date"])
