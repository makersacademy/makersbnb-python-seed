from lib.space import Space

class SpacesRepository:
    def __init__(self, connection):
        self._connection = connection

    def all_listings(self):
        rows = self._connection.execute("SELECT * FROM spaces")
        rows_list = []
        for row in rows:
            item = Space(row['id'], row['name'], row['description'], row['price'], row['date_from'], row['date_to'], row['user_id'])
            rows_list.append(item)
        return rows_list
    
    def create_listing(self, space):
        self._connection.execute("INSERT INTO spaces(name, description, price, date_from, date_to, user_id) VALUES(%s,%s,%s,%s,%s,%s)", [space.name, space.description, space.price, space.date_from, space.date_to, space.user_id])

        
