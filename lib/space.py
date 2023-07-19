class Space(): 
    def __init__(self, id, name, description, price, availability, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.availability = availability
        self.user_id = user_id

    def __eq__(self,other):
        return self.__dict__ == other.__dict__
