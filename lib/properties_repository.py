from lib.properties import Properties

class PropertiesRepository():

    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        propertiess_dictionary = self._connection.execute("SELECT * FROM properties")
        propertiess = []
        for properties in propertiess_dictionary:
            properties_object = Properties(properties["id"], properties["property_type"], properties["description"], properties["price"], properties["location"], properties["start_date"], properties["end_date"], properties["available"], properties["user_id"])
            propertiess.append(properties_object)
        return propertiess
    
    def find(self, id):
        propertiess_dictionary = self._connection.execute("SELECT * FROM propertiess WHERE id = %s", [id])
        properties = propertiess_dictionary[0]
        return Properties(properties["id"], properties["property_type"], properties["description"], properties["price"], properties["location"], properties["start_date"], properties["end_date"], properties["available"])
        
    def create(self, properties):
        self._connection.execute("INSERT INTO propertiess(property_type, description, price, location, start_date, end_date, available) VALUES (%s, %s, %s, %s, %s, %s, %s)", [properties.property_type, properties.description, properties.price, properties.location, properties.start_date, properties.end_date, properties.available])
        return None 
        
    def update(self, properties):
        self._connection.execute("UPDATE propertiess SET property_type = %s , description = %s, price = %s, location = %s, start_date = %s, end_date = %s, available = %s WHERE id = %s", [properties.property_type, properties.description, properties.price, properties.location, properties.start_date, properties.end_date, properties.available, properties.id])
        return None   
    
    def delete(self, id):
        self._connection.execute("DELETE FROM propertiess WHERE id = %s", [id])
        return None 