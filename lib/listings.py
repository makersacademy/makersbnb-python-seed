class Listing:
    def __init__(self, id, name, description, price, user_id):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.user_id = user_id
        # self.available_dates = set()

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"listing({self.id}, {self.name}, {self.description}, {self.price}, {self.user_id})"
    def get_available_dates(self, connection):
        rows = connection.execute('SELECT available_date FROM availability WHERE listing_id = %s', [self.id])
        return [row['available_date'] for row in rows]
    def add_availability(self, connection, dates):
        for date in dates:
            connection.execute('INSERT INTO availability (listing_id, available_date) VALUES (%s, %s)', [self.id, date])    
