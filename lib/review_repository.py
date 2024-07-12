from lib.review import Review
class ReviewRepository:
    def __init__(self, connection):
        self._connection = connection
    
    # This function creates a new review for a specific listing
    def create(self, review):
        rows = self._connection.execute('INSERT INTO reviews (listing_id, review_text, rating) VALUES (%s, %s, %s) RETURNING id', 
                                        [review.listing_id, review.review_text, review.rating])
        row = rows[0]
        review.id = row["id"]
        return review

    # This function returns all reviews for a specific listing by the LISTING id
    # This is what we want displayed on the single listing page
    def find_by_listing_id(self, listing_id):
        rows = self._connection.execute('SELECT * FROM reviews WHERE listing_id = %s', [listing_id])
        return [Review(row["id"], row["listing_id"], row["review_text"], row["rating"]) for row in rows]
    
    # This function lets us delete the review for a specific review id
    def delete(self, id):
        self._connection.execute('DELETE FROM reviews WHERE id = %s', [id])
        return None