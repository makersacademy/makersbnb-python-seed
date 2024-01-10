from lib.space import Space

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
        self._connection.execute('''
                                INSERT INTO spaces
                                    (user_id, name, description, price_per_night)
                                    VALUES
                                    (%s, %s, %s, %s)
                                    ''',
                                [new_space.user_id,
                                    new_space.name,
                                    new_space.description,
                                    new_space.price_per_night
                                    ])
        return None
    
# ---------------------------------------------------------------
# Commented out, as availability classes required before it can be used

    # def find_space_with_availabilities(self, space_id):
    #     rows = self._connection.execute(
    #         """
    #         SELECT spaces.id as space_id, spaces.user_id, spaces.description, spaces.price_per_night, availability.id as availability_id, availability.date, availability.status
    #         FROM spaces JOIN availability ON spaces.id = availability.space_id
    #         WHERE spaces.id = %s AND availability.status = %s
    #         """, 
    #         [space_id, 'TRUE']
    #     )
    #     availability = [Availability(row['availability_id'], row['date'], row['status']) for row in rows]
    #     return Space(rows[0]['space_id'], rows[0]['user_id'],rows[0]['name'], rows[0]['description'], rows[0]['price_per_night'], availability)
