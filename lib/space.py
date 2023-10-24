class Space:
    def __init__(self, name: str, description: str, size: str, owner_id: str) -> None:
        self.name = name
        self.description = description
        self.size = size
        self.owner_id = owner_id
        
    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__
    
    def __repr__(self) -> str:
        return f'Space({self.name}, {self.description}, {self.size})'