from lib.space import *

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def add(self, space):
        rows = self._connection.execute(
            'INSERT into spaces(description, price, user_id, name, free_dates) VALUES (%s, %s, %s, %s, %s) RETURNING id', [space.description, space.price, space.user_id, space.name, space.free_dates]
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