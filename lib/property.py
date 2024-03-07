class Property:
    def __init__(self,  id, property_name , user_id, description, price_per_night):
        
        self._id = id
        self._property_name = property_name
        self._user_id = user_id
        self._description = description
        self._price_per_night = price_per_night 
        
        return None
    

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print a property
    def __repr__(self):
        return f"Property({self._id}, {self._property_name}, {self._user_id}, {self._description}, {self._price_per_night})"