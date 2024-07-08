class BookingRequest: 

    def __init__(self, st_date, end_date, property_id, customer_id):
        self.start_date = st_date
        self.end_date = end_date
        self.status = 'PENDING' # Todo Another data type?
        self.property_id = 1 # TODO : Placeholder.
        self.customer_id = 1 # TODO : Placeholder.

    def rejectRequest(self): 
        # Call this method if the owner doesn't want to accept this request.
        return True

    def approveRequest(self): 
        # Call this method if the owner wishes accept this request.
        return True