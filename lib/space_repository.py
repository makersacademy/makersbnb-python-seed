from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self.connection = connection

    def all(self):
        rows = self.connection.execute("SELECT * FROM spaces")
        spaces = []
        for row in rows:
            item = Space(row["id"], row["address"], row["name"], row["price"], row["image_path"], row["description"], row['date_added'], row["user_id"])
            spaces.append(item)
        return spaces




