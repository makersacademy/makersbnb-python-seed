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

    def create(self, space):
        self.connection.execute("INSERT INTO spaces (address, name, price, image_path, description, date_added, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", 
                                        [space.address, space.name, space.price, space.image_path, space.description, space.date_added, space.user_id])
        return None
    
    def find(self, id):
        rows = self.connection.execute("SELECT * FROM spaces WHERE id = %s", [id])
        row = rows[0]
        return Space(row["id"], row["address"], row["name"], row["price"], row["image_path"], row["description"], row['date_added'], row["user_id"])
    
    def delete(self, id):
        self.connection.execute("DELETE FROM spaces WHERE id = %s", [id])
        return None
    





