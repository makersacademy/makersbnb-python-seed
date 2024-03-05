from datetime import datetime
import pandas as pd

class Space:
    def __init__(self, id, description, price, user_id, name, fromdate, todate):
        self.id = id
        self.description = description
        self.price = price
        self.user_id = user_id
        self.name = name
        self.free_dates = pd.date_range(start=fromdate,end=todate)
        self.free_dates = self.free_dates.strftime('%d-%m-%Y').tolist()


    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f'Space({self.id}, {self.description}, {self.price}, {self.user_id}, {self.name}, {self.free_dates})'

