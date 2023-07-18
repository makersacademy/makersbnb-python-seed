from datetime import date

class Booking:
    def __init__(self, id, start_date, end_date, property_id, user_id):
        self.id = id
        self.start_date = start_date
        self.end_date = end_date
        self.property_id = property_id
        self.user_id = user_id

    def __repr__(self):
        return f"Booking({self.id}, {self.start_date}, {self.end_date}, {self.property_id}, {self.user_id})"
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def is_valid(self):
        
        list_of_properties = [self.start_date, self.end_date]
        if None in list_of_properties or "" in list_of_properties:
            return False
        else:
            start = date(int(self.start_date[0:4]), int(self.start_date[5:7]), int(self.start_date[8:]))
            end = date(int(self.end_date[0:4]), int(self.end_date[5:7]), int(self.end_date[8:]))
            if start > end:
                return False
            else:
                return True