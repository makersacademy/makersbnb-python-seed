class Property():
    
<<<<<<< HEAD
<<<<<<< HEAD
    def __init__(self, id, name, price, description, available_from, available_to, owner_id) -> None:
=======
    def __init__(self, id, name,  description, price, available_from, available_to, owner_id) -> None:
>>>>>>> main
=======
    def __init__(self, id, name,  description, price, available_from, available_to, owner_id) -> None:
>>>>>>> e3998440b4b4ac986f7155f490ddc71a50c54719
        self.id = id
        self.name = name
        self.price = price
        self.description = description
        self.available_from = available_from
        self.available_to = available_to
        self.owner_id = owner_id
    
    def __repr__(self) -> str:
<<<<<<< HEAD
<<<<<<< HEAD
        return f'Property({self.id}, {self.name}, {self.price}, {self.description}, {self.available_from}, {self.available_to}, {self.owner_id})'
=======
        return f'Property({self.id}, {self.name},  {self.description}, {self.price}, {self.available_from}, {self.available_to}, {self.owner_id})'
>>>>>>> main
=======
        return f'Property({self.id}, {self.name},  {self.description}, {self.price}, {self.available_from}, {self.available_to}, {self.owner_id})'
>>>>>>> e3998440b4b4ac986f7155f490ddc71a50c54719
    
    def __eq__(self, value: object) -> bool:
        return self.__dict__ == value.__dict__