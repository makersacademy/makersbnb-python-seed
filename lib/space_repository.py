from lib.space import *
from datetime import datetime
class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def add(self, space):
        rows = self._connection.execute(
            'INSERT into spaces(description, price, user_id, name, fromdate, todate) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id', [space.description, space.price, space.user_id, space.name, space.fromdate, space.todate]
        )
        space.id = rows[0]['id']
        return None

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM spaces'
        )
        spaces = []
        for row in rows:
            item = Space(row['id'], row['description'], row['price'], row['user_id'], row['name'], row['fromdate'], row['todate'])
            spaces.append(item)
        return spaces

# add method for find or filter based on ? user_id? availability?