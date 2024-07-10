class Property:
    def __init__(self, id, property, description, location, cost, user_id):
        self.id = id
        self.property = property
        self.description = description
        self.location = location
        self.cost = cost
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Property({self.id}, {self.property}, {self.description}, {self.location}, {self.cost}, {self.user_id})"