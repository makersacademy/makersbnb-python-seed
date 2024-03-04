from lib.property import Property

class PropertyRepository:

    def __init__(self, connection):
        self._connection = connection

    def all(self): 
        rows = self._connection.execute("SELECT * FROM properties;")
        properties = []
        for row in rows: 
            property = Property(row['id'], row['name'], row['description'], row['price'], row['user_id'], row['booked_status'])
            properties.append(property)
        return properties
    
    def find(self, id):
        rows = self._connection.execute("SELECT * FROM properties WHERE id = %s", [id])
        row = rows[0]
        return Property(row["id"], row["name"], row["description"], row["price"], row["user_id"], row['booked_status'])