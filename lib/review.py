class Review:
    def __init__(self, id, listing_id, review_text, rating):
        self.id = id
        self.listing_id = listing_id
        self.review_text = review_text
        self.rating = rating

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Review:({self.id}, {self.listing_id}, {self.review_text}, {self.rating})"