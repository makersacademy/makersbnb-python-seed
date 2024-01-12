class Space:
    # We initialise with all of our attributes
    # Each column in the table should have an attribute here
    def __init__(self, id, space_name, space_description, price, host_id, guest_id=0):
        self.id = id
        self.space_name = space_name
        self.space_description= space_description
        self.price = price
        self.host_id = host_id
        self.guest_id=guest_id

    # This method allows our tests to assert that the objects it expects
    # are the objects we made based on the database records.
    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # This method makes it look nicer when we print an Artist
    def __repr__(self):
        return f"Space({self.id}, {self.space_name}, {self.space_description}, {self.price}, {self.host_id})"