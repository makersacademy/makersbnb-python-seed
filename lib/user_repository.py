from lib.user import User
from lib.base_repository_class import BaseModelManager


class UserRepository(BaseModelManager):
    def __init__(self, connection) -> None:
        super().__init__(connection)
        self._model_class = User
        self._table_name = 'users'

    def create(self, user):
        self._connection.execute(
            'INSERT INTO users (email, username, password) VALUES (%s, %s, %s)',
            [user.email, user.username, user.password]
        )
        return None

    #TODO: Move it to BASE CLASS
    def update(self, user):
        self._connection.execute(
            'UPDATE users SET email = %s, username = %s, password = %s WHERE id = %s',
            [user.email, user.username, user.password, user.id])
        return None
    
