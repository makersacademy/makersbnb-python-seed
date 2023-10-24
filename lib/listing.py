class Listing():

    def __init__(self, name, desc, price, user_id):
        self.listing_name = name
        self.listing_description = desc
        self.listing_price = price
        self.user_id = user_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"LISTING name: {self.listing_name} - desc: {self.listing_description} - price: {self.listing_price} - user_id: {self.user_id}"