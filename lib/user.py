class User:
    #What does the user need to store? Their Reservations, their locations, password, username
    #What methods do we need for the user? View locations, view reservations
    def __init__(self,connection,username,password):
        self.connection = connection
        connection.execute('INSERT INTO USERS (name, password) VALUES (%s, %s)',
                        [username,password])
        self.id = connection.execute('SELECT id FROM USERS WHERE name = %s',[username])[0]['id']