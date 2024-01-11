from dataclasses import dataclass
from datetime import date

@dataclass()
class Requests:
    req_id: int
    space_id: int
    date_req: date
    stat: str
    title: str
    price: float