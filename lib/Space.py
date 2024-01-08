from dataclasses import dataclass

@dataclass()
class Space:
    id: int
    title: str
    space_description:str
    price: float
    daterange:str
    user_id: int
 
    

print(Space(1,'Test','Test desc',12.12,'somedates',1))


