from lib.space import Space
from lib.base_repository_class import BaseModelManager


class SpaceRepository(BaseModelManager):

    """Space model repository"""

    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = Space
        self._table_name = "spaces"

    def create(self, new_space):
        query = (
            "INSERT INTO spaces"
            "(name, description, size, location, price, user_id)"
            "VALUES (%s, %s, %s, %s, %s, %s) RETURNING id;"
        )

        rows = self._connection.execute(
            query,
            [
                new_space.name,
                new_space.description,
                new_space.size,
                new_space.location,
                new_space.price,
                new_space.user_id,
            ],
        )
        new_space.id = rows[0].get("id")
        return new_space
    
    """
    A method to return all the spaces created by a certain user
    Using the foreign key related to the users table
    """
    def all_by_user_id(self, user_id):
        query = 'SELECT * FROM %s WHERE user_id = %s;' % (self._table_name, user_id)
        rows = self._connection.execute(query)
        print(rows)
        return [self._model_class(**row) for row in rows]
