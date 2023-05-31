class Availability:
    def __init__(self, id, listing_id, available_date):
        self.id = id
        self.listing_id = listing_id
        self.available_date = available_date

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    # # This method makes it look nicer when we print an availability
    def __repr__(self):
        return f"({self.id}, {self.listing_id}, {self.available_date})"
