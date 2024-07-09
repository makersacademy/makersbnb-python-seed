class BookingRequest: 

    def __init__(self, st_date, end_date, property_id, customer_id):
        self.start_date = st_date
        self.end_date = end_date
        # self.status = 'PENDING' # TODO  Another data type - need Charlie to look at modelling this in the database.
        self.property_id = property_id 
        self.customer_id = customer_id 

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def rejectRequest(self): 
        # Call this method if the owner doesn't want to accept this request.
        return True

    def approveRequest(self): 
        # Call this method if the owner wishes accept this request.
        return True