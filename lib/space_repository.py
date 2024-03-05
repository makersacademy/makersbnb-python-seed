from lib.spaces import Spaces

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute("SELECT * FROM makersbnb")
        spaces = []
        for row in rows:
            space = Spaces(
                row['id'],
                row["name"], 
                row["description"], 
                row["price"],
                row["owner"])
            spaces.append(space)
        return spaces
    

    def create(self, space):
        self._connection.execute('INSERT INTO makersbnb (id, name, description, price, owner) VALUES (%s, %s, %s, %s, %s)', [
                                space.id, space.name, space.description, space.price, space.owner])
        return None
    
    #class to return available dates? Or have them pick any date, and then returns if that date is available or not?