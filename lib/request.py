class Request():
    def __init__(self, id, user_id, space_id, date_to_book, request_status):
        self.id = id
        self.user_id = user_id
        self.space_id = space_id
        self.date_to_book = date_to_book
        self.request_status = request_status

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Request({self.id}, the persons id booking:{self.user_id}, the space_id:{self.space_id}, {self.date_to_book}, {self.request_status})"