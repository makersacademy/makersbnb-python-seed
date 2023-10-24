class Date():
    def __init__(self, id, date, available, space_id):
        self.id = id
        self.date = date
        self.available = available
        self.space_id = space_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Date({self.id}, {self.date}, {self.available}, {self.space_id})"