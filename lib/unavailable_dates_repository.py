from lib.unavailable_dates import unavailable_date

class unavailable_dates_repository:
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM unavailable_dates')
        unavailable_dates = [unavailable_date(row['spaces_id'], row['date']) for row in rows]

        return unavailable_dates
    
    def find_all_unavailable_dates(self, space_id):
        rows = self._connection.execute(f'SELECT unavailable_date FROM unavailable_dates WHERE space_id = {space_id}')
        dates = [date for date in rows]

        return dates
    
    def create(self, unavailable_date):
        self._connection.seed('seeds/airbnb.sql')
        rows = self._connection.execute(
            "INSERT INTO unavailable_dates (space_id, unavailable_date) VALUES (%s, %s) RETURNING id", 
            [unavailable_date.space_id, unavailable_date.date]
        )
        #space.id = rows[0]['id']
        return None
    
"""    def delete(self, space_id):
        self._connection.execute(f'DELETE FROM spaces WHERE id = {space_id}')"""