from lib.properties import Properties

class PropertiesRepository():

    def __init__(self, connection) -> None:
        self._connection = connection

    def all(self):
        properties_dictionary = self._connection.execute("SELECT * FROM properties")
        properties = []
        for property in properties_dictionary:
            properties_object = Properties(property["id"], property["property_type"], property["description"], property["price"], property["location"], property["start_date"], property["end_date"], property["available"], property["user_id"])
            properties.append(properties_object)
        return properties
    
    def find(self, id):
        properties_dictionary = self._connection.execute("SELECT * FROM Properties WHERE id = %s", [id])
        property = properties_dictionary[0]
        return Properties(property["id"], property["property_type"], property["description"], property["price"], property["location"], property["start_date"], property["end_date"], property["available"])
        
    def create(self, properties):
        self._connection.execute("INSERT INTO Properties(property_type, description, price, location, start_date, end_date, available) VALUES (%s, %s, %s, %s, %s, %s, %s)", [properties.property_type, properties.description, properties.price, properties.location, properties.start_date, properties.end_date, properties.available])
        return None 
        
    def update(self, properties):
        self._connection.execute("UPDATE Properties SET property_type = %s , description = %s, price = %s, location = %s, start_date = %s, end_date = %s, available = %s WHERE id = %s", [properties.property_type, properties.description, properties.price, properties.location, properties.start_date, properties.end_date, properties.available, properties.id])
        return None   
    
    def delete(self, id):
        self._connection.execute("DELETE FROM Properties WHERE id = %s", [id])
        return None 