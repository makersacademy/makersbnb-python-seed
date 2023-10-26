class UnavailableDate:
    def __init__(self, space_id, date):
        self.space_id = space_id
        self.date  = date 
        
    def __eq__(self, __value: object) -> bool:
        return self.__dict__ == __value.__dict__
    
    def __repr__(self) -> str:
        return f'unavailable_date({self.space_id}, {self.date})'
