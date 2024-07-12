class Review:
    def __init__(self, id, review_content, number_rating, listing_id):
        self.id = id
        self.review_content = review_content
        self.number_rating = number_rating
        self.listing_id = listing_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Review:({self.listing_id}, {self.review_content}, {self.number_rating}, {self.price_per_night}, {self.available_from}, {self.available_to})"