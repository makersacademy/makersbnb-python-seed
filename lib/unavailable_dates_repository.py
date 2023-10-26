from lib.unavailable_dates import UnavailableDate

class UnavailableDatesRepository:
    def __init__(self, connection) -> None:
        self._connection = connection
    
    def all(self):
        rows = self._connection.execute('SELECT * FROM unavailable_dates')
        unavailable_dates = [UnavailableDate(row['space_id'], row['unavailable_date']) for row in rows]

        return unavailable_dates
    
    def find_all_unavailable_dates(self, space_id):
        return self._connection.execute(f'SELECT unavailable_date FROM unavailable_dates WHERE space_id = {space_id}')

    
    def create(self, unavailable_date):
        return self._connection.execute("INSERT INTO unavailable_dates (space_id, unavailable_date) VALUES (%s, %s) RETURNING id", [unavailable_date.space_id, unavailable_date.date]
        )
        #space.id = rows[0]['id']
    
    # def delete(self, space_id):
    #     self._connection.execute(f'DELETE FROM spaces WHERE id = {space_id}')