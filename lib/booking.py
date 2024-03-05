class Booking:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, date, status, space_id, guest_id):
        self.id = id
        self.date = date
        self.status = status
        self.space_id = space_id
        self.guest_id = guest_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Booking({self.id}, {self.date}, {self.status}, {self.space_id}, {self.guest_id})"
    
     