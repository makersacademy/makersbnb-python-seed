from lib.space import Space
from lib.database_connection import DatabaseConnection 

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        return [Space(row["id"],
                    row["space_name"],
                    row["location"],
                    row["description"],
                    row["price"],
                    row["user_id"],
                    str(row["start_date"]),
                    str(row["end_date"])
                    )for row in rows]


    def create(self, space):
        self._connection.execute('INSERT INTO spaces (id, space_name, location, description, price, user_id, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s, %s)', [space.id, space.space_name, space.description, space.price, space.user_id, space.start_date, space.end_date])

    
