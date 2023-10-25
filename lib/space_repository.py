from lib.space import Space


class SpaceRepository:
    def __init__(self, db_connection):
        self._connection = db_connection

    def create(self, space):
        self._connection.seed('seeds/airbnb.sql')
        rows = self._connection.execute(
            "INSERT INTO spaces (name, description, size, price, owner_id) VALUES (%s, %s, %s, %s, %s) RETURNING id", 
            [space.name, space.description, int(space.size), int(space.price), space.owner_id]
        )
        space.id = rows[0]['id']
        return None
