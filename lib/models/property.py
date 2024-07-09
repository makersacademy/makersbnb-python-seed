class Property():
    
<<<<<<< HEAD
    def __init__(self, id, name, price, description, available_from, available_to, owner_id) -> None:
=======
    def __init__(self, id, name,  description, price, available_from, available_to, owner_id) -> None:
>>>>>>> main
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.available_from = available_from
        self.available_to = available_to
        self.owner_id = owner_id
    
    def __repr__(self) -> str:
<<<<<<< HEAD
        return f'Property({self.id}, {self.name}, {self.price}, {self.description}, {self.available_from}, {self.available_to}, {self.owner_id})'
=======
        return f'Property({self.id}, {self.name},  {self.description}, {self.price}, {self.available_from}, {self.available_to}, {self.owner_id})'
>>>>>>> main
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__