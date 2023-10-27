class Date():

    def __init__(self, date, listing_id):
        self.date = date
        self.listing_id = listing_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"LISTING {self.listing_id} date: {self.formatted_time()}"

    
    def formatted_time(self):
        return self.date.strftime("%d/%m/%Y")