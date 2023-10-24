from lib.space_class import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all spaces
    def all(self):
        space_list = []
        response = self._connection.execute('SELECT * FROM spaces')
        for returned_space in response:
            space = Space(returned_space['name'],returned_space['host_id'],returned_space['description'],returned_space['price_per_night'])
            space_list.append(space)
        return space_list

    # Find a specific space by its name
    def find_by_name(self, name):
        returned_space = self._connection.execute('SELECT * FROM spaces WHERE name = %s', [name])
        space = Space(returned_space[0]['name'],returned_space[0]['host_id'],returned_space[0]['description'],returned_space[0]['price_per_night'])
        if returned_space != []:
            return space
        else:
            return 'No User Found'


    # Create a space
    def create(self, name, host_id, description, price_per_night):
        self._connection.execute('INSERT INTO spaces (name, host_id, description, price_per_night) VALUES (%s, %s, %s, %s)',[name, host_id, description, price_per_night])
        return None

    # Delete a space by its name
    def delete_by_name(self, name):
        self._connection.execute('DELETE FROM spaces WHERE name = %s', [name])
        return None
