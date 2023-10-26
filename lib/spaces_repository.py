from lib.space import Space
import datetime

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

    def filtered_listing(self, date_from, date_to):
        rows_list = self.all_listings()
        available_spaces = []
        # date_from_datetime_obj = datetime.datetime.strptime(date_from, "%Y/%m/%d").date()
        # date_to_datetime_obj = datetime.datetime.strptime(date_to, "%Y/%m/%d").date()
        print(date_from)
        print(type(date_from))
        print("this is a test")
        for space in rows_list:
            if (date_from and date_to > space.date_from) and (date_from and date_to <= space.date_to):
                available_spaces.append(space)
        return available_spaces

        
