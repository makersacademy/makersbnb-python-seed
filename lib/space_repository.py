from lib.space import *

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def add(self, space):
        rows = self._connection.execute(
            'INSERT into spaces(description, price, user_id, name, fromdate, todate, free_dates) VALUES (%s, %s, %s, %s, %s, %s, %s) RETURNING id', [space.description, space.price, space.user_id, space.name, space.fromdate, space.todate, space.free_dates]
        )
        space.id = rows[0]['id']
        return None

    def all(self):
        rows = self._connection.execute(
            'SELECT * FROM spaces'
        )
        spaces = []
        print(rows)
        for row in rows:
            item = Space(row['id'], row['description'], row['price'], row['user_id'], row['name'], row['fromdate'], row['todate'], row['free_dates'])
            spaces.append(item)
        return spaces

    def comprehend_freedates(self,id):
        # Turn "[]" into []
        freedate_list = self._connection.execute(
            'SELECT free_dates FROM spaces WHERE id = %s', [id]
        )
        # freedate_list.split('"')
        return freedate_list

# add method for find or filter based on ? user_id? availability?
    def filter(self,fromdate,todate=0):
        if todate == 0:
            todate = fromdate
        id_list = self._connection.execute(
            'SELECT id FROM spaces',
        )
        id_and_dates = {}
        for item in id_list:
            id_and_dates.update({f"{item}":f"{self.comprehend_freedates(*item.values())}"})
        # {"1:[blahaha]","2:[blahblah]"}
        space_ids = []
        print("!!!!!!!!!!!!!!!!!!!!!")
        print(id_and_dates)
        print("!!!!!!!!!!!!!!!!!!!!!!!!!")
        for key, value in id_and_dates.items():
            if fromdate and todate in id_and_dates[value]:
                space_ids.append(value)
        # for object in rows:
        #     space_ids.append(*object.values())
        return space_ids
            