from lib.space import Space
from lib.database_connection import DatabaseConnection 

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        result = [
            Space(
                row["id"],
                row["space_name"],
                row["description"],
                row["price"],
                row["user_id"],
                str(row["start_date"]),
                str(row["end_date"]),
            )
            for row in rows
        ]
        if len(result) == 0:
            result = "No results found"
        return result
    
    def create(self, space):
        self._connection.execute(
            "INSERT INTO spaces (space_name, description, price, user_id, start_date, end_date) VALUES (%s, %s, %s, %s, %s, %s)",
            [
                space.space_name,
                space.description,
                space.price,
                space.user_id,
                space.start_date,
                space.end_date,
            ],
        )
        return None

    def delete(self, id):
        self._connection.execute("DELETE FROM spaces WHERE id = %s", [id])
        return None


    def find_by_id(self, id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE id= %s", [id])


        result = [
            Space(
                row["id"],
                row["space_name"],
                row["description"],
                row["price"],
                row["user_id"],
                str(row["start_date"]),
                str(row["end_date"]),
            )
            for row in rows
        ]
        if len(result) == 0:
            result = "No results found"
        return result

    def find_by_price(self, price):
        rows = self._connection.execute("SELECT * FROM spaces WHERE price= %s", [price])

        result = [
            Space(
                row["id"],
                row["space_name"],
                row["description"],
                row["price"],
                row["user_id"],
                str(row["start_date"]),
                str(row["end_date"]),
            )
            for row in rows
        ]
        if len(result) == 0:
            result = "No results found"
        return result

    def find_by_date(self, date):
        rows = self._connection.execute(
            "SELECT * FROM spaces WHERE %s between start_date AND end_date", [date]
        )

        result = [
            Space(
                row["id"],
                row["space_name"],
                row["description"],
                row["price"],
                row["user_id"],
                str(row["start_date"]),
                str(row["end_date"]),
            )
            for row in rows
        ]
        if len(result) == 0:
            result = "No results found"
        return result
      
      
    def find_by_space_name(self, space_name):
        rows = self._connection.execute("SELECT * FROM spaces WHERE space_name = %s", [space_name])

        result = [
            Space(
                row["id"],
                row["space_name"],
                row["description"],
                row["price"],
                row["user_id"],
                str(row["start_date"]),
                str(row["end_date"]),
            )
            for row in rows
        ]
        if len(result) == 0:
            result = "No results found"
        return result
    
    def find_spaces_by_user(self, user_id):
        rows = self._connection.execute("SELECT * FROM spaces WHERE user_id = %s", [user_id])

        result = [
            Space(
                row["id"],
                row["space_name"],
                row["description"],
                row["price"],
                row["user_id"],
                str(row["start_date"]),
                str(row["end_date"]),
            )
            for row in rows
        ]
        if len(result) == 0:
            result = "No results found"
        return result
    
