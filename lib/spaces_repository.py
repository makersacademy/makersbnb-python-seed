from lib.spaces import *
class SpaceRepository:
    def __init__(self,connection):
        self._connection = connection

    def add_space(self, new_space):
        self._connection.execute(
            "INSERT INTO spaces (id, name, description, price, host_ID) VALUES (%s, %s, %s, %s, %s)",
            [new_space.id, new_space.name, new_space.description, new_space.price, new_space.host_ID]
            )
        return "ADDED SPACE TO REPOSITORY"

    def get_space_by_id(self, space_id):
        rows = self._connection.execute(
            'SELECT * from spaces WHERE id = %s', [space_id]
        )
        row = rows[0]
        return Space(row['id'], row['name'], row['description'], row['price'], row['host_ID'])

    def list_all_spaces(self):
        all_spaces = self._connection.execute("SELECT * from spaces")
        spaces = []
        for s in all_spaces:
            new_space = Space(s["id"], s["name"], s["description"], s["price"], s["host_ID"])
            spaces.append(new_space)

        return spaces

    def update_space():
        pass