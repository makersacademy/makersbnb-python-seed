from lib.Space import Space
class SpacesRepository:
    def __init__(self,connection):
        self._connection = connection

    def list_all(self):
        rows = self._connection.execute('SELECT * FROM Spaces')
        return_data = []
        for row in rows:
            data = Space(row['id'],row['title'],row['space_description'],row['price'],row['daterange'],row['user_id'])
            return_data.insert(0,data)
        return return_data
    
    def add(self,title,space_description,price,daterange,user_id):
        self._connection.execute('''INSERT INTO Spaces(
                                 title,space_description,price,daterange,user_id)
                                  VALUES (%s,%s,%s,%s,%s)''',[title,space_description,price,daterange,user_id])