from dataclasses import dataclass
from datetime import date

@dataclass
class Request:
    req_id:int
    user_id: int
    date_req: date
    status: str
