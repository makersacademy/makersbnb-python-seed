class Space:
    def __init__(self, name, description, size, price, owner_id, space_id = None) -> None:
        self.name = name
        self.description = description
        self.size = size
        self.price = price
        self.owner_id = owner_id
        self.space_id = space_id
        
    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__
    
    def __repr__(self) -> str:
        return f'Space({self.name}, {self.description}, {self.size}, {self.price})'