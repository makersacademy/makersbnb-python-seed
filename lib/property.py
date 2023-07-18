
class Property:
    
    def __init__(self,id,name,description,price,user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
            return f"Property({self.id},{self.name},{self.description},{self.price:.2f},{self.user_id})"