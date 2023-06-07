class Request:
    def __init__(self, id, owner_id, visitor_id, space_id, request_date, confirmed):
        self.id = id
        self.owner_id = owner_id
        self.visitor_id = visitor_id
        self.space_id = space_id
        self.request_date = request_date
        self.confirmed = confirmed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Request({self.id}, {self.owner_id}, {self.visitor_id}, {self.space_id}, {self.request_date}, {self.confirmed})"