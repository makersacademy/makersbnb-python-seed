from lib.space import Space
from lib.availability import Availability
from datetime import datetime

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        return [Space(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night']) for row in rows]
    
    def find(self, space_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s',[space_id])
        row = rows[0]
        return Space(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night'])
    
    def create(self, new_space):
        rows = self._connection.execute('''
                                INSERT INTO spaces
                                    (user_id, name, description, price_per_night)
                                    VALUES
                                    (%s, %s, %s, %s) RETURNING id
                                    ''',
                                [new_space.user_id,
                                    new_space.name,
                                    new_space.description,
                                    new_space.price_per_night
                                    ])
        row = rows[0]
        new_space.id = row['id']
        return new_space
    

    def find_space_with_availabilities(self, space_id):
        rows = self._connection.execute(
            """
            SELECT spaces.id as space_id, spaces.user_id, spaces.name, spaces.description, spaces.price_per_night, availability.id as availability_id, availability.date, availability.status
            FROM spaces JOIN availability ON spaces.id = availability.space_id
            WHERE spaces.id = %s AND availability.status = %s
            """, 
            [space_id, 'TRUE']
        )
        if rows == []:
            return None
        #gets all availabilities as class objects
        availabilities = [Availability(row['availability_id'], row['space_id'], row['date'], row['status']) for row in rows]
        #gets dates from class objects in  a list
        dates = [availability.date for availability in availabilities]
        #reformats each date in the list to 'DD-MM-YYYY'
        formatted_dates = [date.strftime('%d-%m-%Y') for date in dates]
        space = Space(rows[0]['space_id'], rows[0]['user_id'],rows[0]['name'], rows[0]['description'], rows[0]['price_per_night'])
        return space, formatted_dates
    
    def find_space_with_availabilities_month(self, space_id, month):
        rows = self._connection.execute(
            """
            SELECT spaces.id as space_id, spaces.user_id, spaces.name, spaces.description, spaces.price_per_night, availability.id as availability_id, availability.date, availability.status
            FROM spaces JOIN availability ON spaces.id = availability.space_id
            WHERE spaces.id = %s AND availability.status = %s AND TO_CHAR(date::date, 'FMMonth') = %s
            """, 
            [space_id, 'TRUE', f'{month}']
        )
        if rows == []:
            return None
        #gets all availabilities as class objects
        availabilities = [Availability(row['availability_id'], row['space_id'], row['date'], row['status']) for row in rows]
        #gets dates from class objects in  a list
        dates = [availability.date for availability in availabilities]
        #reformats each date in the list to 'DD-MM-YYYY'
        formatted_dates = [date.strftime('%d-%m-%Y') for date in dates]
        space = Space(rows[0]['space_id'], rows[0]['user_id'],rows[0]['name'], rows[0]['description'], rows[0]['price_per_night'])
        return space, formatted_dates

    def find_by_user(self, user_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE user_id = %s',[user_id])
        return [Space(row['id'], row['user_id'], row['name'], row['description'], row['price_per_night']) for row in rows]
    