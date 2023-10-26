from datetime import datetime, timedelta
from lib.date.Date import Date

class DateRepository:
    def __init__(self, connection):
        self._connection = connection

    def add(self, space): #space fields == name, owner_id, start_date, date_to

        start = space.start_date
        startObj = datetime.strptime(start, "%Y-%m-%d")

        end = space.end_date
        endObj = datetime.strptime(end, "%Y-%m-%d")

        current_date = startObj
        while current_date <= endObj:
            date_obj = Date(space.id, current_date.strftime("%Y-%m-%d"))
            self._connection.execute(
                'INSERT INTO dates (id, spaceId, date, isAvailable) ' +
                'VALUES (%s, %s, %s, %s)', [date_obj.id, date_obj.space_id, date_obj.date, date_obj.is_available]
            )
            current_date = current_date + timedelta(days = 1)

# start_date, end_date
# current_date = start_date
# add current_date to the table
# current_date + timedelta(days = 1)
# until we reach end_date