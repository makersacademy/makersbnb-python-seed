from datetime import datetime
class Space():
    def __init__(self, id, title, start_date, end_date, userid,price):
            self.id = id
            self.title = title
            self.start_date = datetime.strptime(start_date, '%Y-%m-%d').date()
            self.end_date = datetime.strptime(end_date, '%Y-%m-%d').date()
            self.userid = userid
            self.price = price
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Space({self.id}, {self.title}, {self.start_date}, {self.end_date}, {self.userid}, {self.price})"
    
    def generate_errors(self):
        errors = []
        if self.title == None or self.title == "":
            errors.append("Title can't be blank!")
        # Space for description validation
        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)
        
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        # Space for description validation
        return True

    
