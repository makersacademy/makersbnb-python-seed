from lib.space_class import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all spaces
    def all(self):
        space_list = []
        response = self._connection.execute('SELECT * FROM spaces')
        for returned_space in response:
            space = Space(returned_space['id'],returned_space['name'],returned_space['host_id'],returned_space['description'],returned_space['price_per_night'])
            space_list.append(space)
        return space_list

    # Find a specific space by its name
    def find_by_name(self, name):
        returned_space = self._connection.execute('SELECT * FROM spaces WHERE name = %s', [name])
        space = Space(returned_space[0]['id'],returned_space[0]['name'],returned_space[0]['host_id'],returned_space[0]['description'],returned_space[0]['price_per_night'])
        if returned_space != []:
            return space
        else:
            return 'No User Found'
    
    #Find by ID
    def find_by_id(self,id):
        returned_space = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [id])
        space = Space(returned_space[0]['id'],returned_space[0]['name'],returned_space[0]['host_id'],returned_space[0]['description'],returned_space[0]['price_per_night'])
        return space

    # Create a space
    def create(self, name, host_id, description, price_per_night):
        CreatedSpace=self._connection.execute('INSERT INTO spaces (name, host_id, description, price_per_night) VALUES (%s, %s, %s, %s) RETURNING id;',[name, host_id, description, price_per_night])
        return CreatedSpace[0]['id']

    # Delete a space by its name
    def delete_by_name(self, name):
        self._connection.execute('DELETE FROM spaces WHERE name = %s', [name])
        return None
    
    # Delete a space by its id
    def delete_by_id(self, id):
        self._connection.execute('DELETE FROM spaces WHERE id = %s', [id])
        return None
    
    # Request a space
    def request_a_stay(self,date,spaces_id,requested_by_user_id,approved):
        self._connection.execute('INSERT INTO availability (date_not_available,approved,requested_by_user_id,spaces_id) VALUES (%s,%s,%s,%s)',[date,approved,requested_by_user_id,spaces_id])
        return None
    
    # Return all_unavailable_dates
    def unavailable_days(self,spaces_id):
        response = self._connection.execute('''SELECT date_not_available
                                                FROM availability
                                                JOIN spaces ON spaces.id = availability.spaces_id
                                                WHERE availability.approved IN ('approved', 'unavailable')
                                                AND availability.spaces_id = %s; ''',[spaces_id])

        DaysUnavailable = [x['date_not_available'] for x in response]
        return DaysUnavailable


    def change_status (self,status,id, date):
        self._connection.execute ('UPDATE availability SET approved = (%s) WHERE id = (%s) AND date_not_available = (%s)',[status,id,date])

