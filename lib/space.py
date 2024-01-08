class Space:
    def __init__(self, id:None, name:None, desc:None, price:None):
        self.id = id
        self.name = name
        self.desc = desc
        self.price = price
    
    def __repr__(self):
        return f"id: {self.id}, name: {self.name}, desc: {self.desc}, price: {self.price}"