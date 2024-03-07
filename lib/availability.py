from datetime import date

class Availability:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, availability_from, availability_to, space_id):
        self.id = id
        self.availability_from = availability_from
        self.availability_to = availability_to
        self.space_id = space_id


    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Availability({self.id}, {self.availability_from}, {self.availability_to}, {self.space_id})"