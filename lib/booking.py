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
            #if the user has entered start and end date, we convert the strings into date format
            start = date(int(self.start_date[0:4]), int(self.start_date[5:7]), int(self.start_date[8:]))
            end = date(int(self.end_date[0:4]), int(self.end_date[5:7]), int(self.end_date[8:]))
            #check in if the start date is earlier than the end date, to validate
            if start > end:
                return False
            else:
                return True
            
    def generate_errors(self):
        errors = []
        if self.start_date == None or self.start_date == "":
            errors.append("start date")
        if self.end_date == None or self.end_date == "":
            errors.append("end date")
        if len(errors) == 0:
            #if the user has entered start and end date, we convert the strings into date format
            start = date(int(self.start_date[0:4]), int(self.start_date[5:7]), int(self.start_date[8:]))
            end = date(int(self.end_date[0:4]), int(self.end_date[5:7]), int(self.end_date[8:]))
            #check in if the start date is after than the end date, to show an error message
            if start > end:
                errors.append("a start date that is earlier than the end date")
            else:
                return None
        
        return "Please insert: "+", ".join(errors)
        
