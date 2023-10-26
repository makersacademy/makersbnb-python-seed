from lib.space.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        return self._connection.execute('SELECT * FROM spaces')
        
