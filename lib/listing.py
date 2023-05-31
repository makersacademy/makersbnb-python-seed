from dataclasses import dataclass

@dataclass
class Listing:
    id: int
    user_id: int
    price: int
    name: str
    description: str


