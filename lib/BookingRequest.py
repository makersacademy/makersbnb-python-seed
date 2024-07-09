class BookingRequest: 

    def __init__(self, property_id, user_id, start_date, end_date):
        self.start_date = start_date
        self.end_date = end_date
        self.status = 'PENDING' # Todo Another data type?
        self.property_id = property_id
        self.user_id = user_id   

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def rejectRequest(self): 
        # Call this method if the owner doesn't want to accept this request.
        return True

    def approveRequest(self): 
        # Call this method if the owner wishes accept this request.
        return True