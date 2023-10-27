class Space:
    def __init__(self,id, name,description,price,owner_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price 
        self.owner_id = owner_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

