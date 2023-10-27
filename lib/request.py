class Request():

    def __init__(self, date, listing_id, requested_by, requested_from):
        self.date = date
        self.listing_id = listing_id
        self.requested_by_id = requested_by
        self.requested_from_id = requested_from

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Request(date: {self.formatted_time()} - listing: {self.listing_id} - requested_by: {self.requested_by_id} - requested_from: {self.requested_from_id})"
    
    def formatted_time(self):
        return self.date.strftime("%d/%m/%Y")