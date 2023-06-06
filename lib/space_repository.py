from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            items = Space(row["id"], row["title"], row["description"], row["price"], str(row["date_range"]), row["user_id"])
            spaces.append(items)
        return spaces
    