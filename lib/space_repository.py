from lib.space import Space

class SpaceRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all spaces
    def all(self):
        rows = self._connection.execute('SELECT * from spaces')
        spaces = []
        for row in rows:
            item = Space(row["id"], row["name"], row["description"], row["price_per_night"], row["user_id"])
            spaces.append(item)
        return spaces

    # Find a single space by its id
    def find(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id])
        row = rows[0]
        return Space(row["id"], row["name"], row["description"], row["price_per_night"], row["user_id"])

    # Create a new space
    # Do you want to get its id back? Look into RETURNING id;
    def create(self, space):
        self._connection.execute('INSERT INTO spaces (name, description, price_per_night, user_id) VALUES (%s, %s, %s, %s)', [
            space.name, space.description, space.price_per_night, space.user_id])
        return None

    # Delete a space by its id
    def delete(self, space_id):
        self._connection.execute(
            'DELETE FROM spaces WHERE id = %s', [space_id])
        return None