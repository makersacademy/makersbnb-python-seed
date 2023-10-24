class Space:
    def __init__(self,id,name,host_id,description,price_per_night,):
        self.id= id
        self.name = name
        self.host_id = host_id
        self.description = description
        self.price_per_night = price_per_night

    def __eq__(self,other):
        return self.__dict__==other.__dict__

    def __repr__(self):
        return (f'space {self.name}{self.name},{self.host_id},{self.description},{self.price_per_night})')