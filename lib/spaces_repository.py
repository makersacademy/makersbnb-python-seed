from lib.spaces import *
from datetime import datetime, timedelta

class SpaceRepository:
    def __init__(self,connection):
        self._connection = connection

    def add_date(self, date_from, date_to, space_id):
        date_from = datetime.strptime(date_from,'%Y-%m-%d')
        date_to = datetime.strptime(date_to,'%Y-%m-%d')

        date_list = []
        while date_from <= date_to:
            date_list.append(date_from)
            date_from += timedelta(days=1)

        for d in date_list:
            self._connection.execute('INSERT INTO dates (date, space_id) VALUES (%s, %s)', [d.isoformat(), space_id])

        return None

    def add_space(self, new_space):
        rows = self._connection.execute('INSERT INTO spaces (name, description, price, host_id) VALUES (%s, %s, %s, %s) RETURNING id', [
                                 new_space.name, new_space.description, new_space.price, new_space.host_id])
        row = rows[0]
        new_space.id = row["id"]
        return new_space

    def get_space_by_id(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id]
        )
        row = rows[0]
        return Space(row['id'], row['name'], row['description'], row['price'], row['host_id'])

    def get_spaces_by_host_id(self, host_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE host_id = %s', [host_id]
        )
        spaces = []
        for row in rows:
            spaces.append(Space(row['id'], row['name'], row['description'], row['price'], row['host_id']))
        return spaces

    def list_all_spaces(self):
        all_spaces = self._connection.execute("SELECT * from spaces")
        spaces = []
        for s in all_spaces:
            new_space = Space(s["id"], s["name"], s["description"], s["price"], s["host_id"])
            spaces.append(new_space)

        return spaces

    def get_available_dates(self, space_id):
        available_dates = []
        dates = self._connection.execute(
            'SELECT * from dates where space_id = %s', [space_id]
        )
        for date in dates:
            available_dates.append(date['date'])
        return available_dates
