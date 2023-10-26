from lib.date import *

class DateRepo():

    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT * FROM dates')
        dates = []
        for row in rows:
            date = Date(row['date'], row['listing_id'])
            dates.append(date)
        return dates

    def check_listing_availability_with_listing_id(self, listing_id):
        rows = self._connection.execute("SELECT * FROM dates WHERE listing_id = %i" % (int(listing_id)))
        dates = []
        for row in rows:
            date = Date(row['date'], row['listing_id'])
            dates.append(date)
        return dates

    def get_availability_for_date(self, checking_date, listing_id):
        rows = self._connection.execute("SELECT * FROM dates WHERE listing_id = %i" % (int(listing_id)))
        dates = []
        for row in rows:
            date = Date(row['date'], row['listing_id'])
            dates.append(date)
        
        for date in dates:
            if date.date == checking_date:
                return False
        
        return True