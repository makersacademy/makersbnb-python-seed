from dataclasses import dataclass
from datetime import date

@dataclass
class Request:
    req_id:int
    space_id: int
    date_req: date
    stat: str
