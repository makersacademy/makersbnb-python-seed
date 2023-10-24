from lib.space import Space

class SpacesRepository:
    def __init__(self, connection):
        self._connection = connection

    def all_listings(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        rows_list = []
        for row in rows:
            item = Space(row['id'], row['name'], row['description'], row['price'], row['date_from'], row['date_to'])
            rows_list.append(item)
        return rows_list
