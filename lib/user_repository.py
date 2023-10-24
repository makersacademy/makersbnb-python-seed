from lib.user_class import User

class UserRepository:
    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection

    # Retrieve all users
    def all(self):
        userlist=[]
        response = self._connection.execute('SELECT  * FROM users')
        for ReturnedUser in response:
            user=User(ReturnedUser['id'],ReturnedUser['username'],ReturnedUser['name'],ReturnedUser['password'],ReturnedUser['email'],ReturnedUser['phone_number'])
            userlist.append(user)
        return userlist
    
    #Find a Specific User by their ID
    def all(self,id):
        ReturnedUser = self._connection.execute('SELECT * FROM users WHERE id = (%s)',[id])  
        user=User(ReturnedUser[0]['id'],ReturnedUser[0]['username'],ReturnedUser[0]['name'],ReturnedUser[0]['password'],ReturnedUser[0]['email'],ReturnedUser[0]['phone_number'])
        return user

    # Create a user
    def create(self,username,name,password,email,phone_number):
        self._connection.execute('INSERT INTO users (username,name,password,email,phone_number) VALUES (%s,%s,%s,%s,%s)', [username,name,password,email,phone_number])
        return None
    # Delete a User by their ID
    def delete_by_id(self,id):
        self._connection.execute('DELETE FROM users WHERE id = %s',[id]) 
        return None
