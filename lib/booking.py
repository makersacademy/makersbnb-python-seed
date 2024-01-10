class Booking:
    def __init__(self, id, night_id, user_id, status):
        self.id = id
        self.night_id = night_id
        self.user_id = user_id
        self.status = status
    
    def __repr__(self):
        return f'Booking({self.id}, {self.night_id}, {self.user_id}, {self.status})'

    def __eq__(self, other):
        return self.__dict__ == other.__dict__