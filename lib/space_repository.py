from lib.space import Space
from lib.database_connection import DatabaseConnection


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection
