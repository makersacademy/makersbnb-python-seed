from datetime import date

class Booking:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, booking_start_date, booking_end_date, space_id):
        self.id = id
        self.booking_start_date = booking_start_date
        self.booking_end_date = booking_end_date
        self.space_id = space_id


    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return (self.id == other.id and
                str(self.booking_start_date) == str(other.booking_start_date) and
                str(self.booking_end_date) == str(other.booking_end_date) and
                self.space_id == other.space_id)

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Booking({self.id}, {self.booking_start_date}, {self.booking_end_date}, {self.space_id})"