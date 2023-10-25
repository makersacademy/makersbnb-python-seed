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
            user=User(ReturnedUser['name'],ReturnedUser['username'],ReturnedUser['password'],ReturnedUser['email'],ReturnedUser['phone_number'],ReturnedUser['id'])
            userlist.append(user)
        return userlist
    
    #Find a Specific User by their ID
    def find_by_id(self, id):
        ReturnedUser = self._connection.execute('SELECT * FROM users WHERE id = (%s)',[id])  
        user=User(ReturnedUser[0]['name'],ReturnedUser[0]['username'],ReturnedUser[0]['password'],ReturnedUser[0]['email'],ReturnedUser[0]['phone_number'],ReturnedUser[0]['id'])
        return user

    def find_by_username(self, username):
        ReturnedUser = self._connection.execute('SELECT * FROM users WHERE username ILIKE (%s)',[username])
        if ReturnedUser == []:
            return None
        else:
            user=User(ReturnedUser[0]['name'],ReturnedUser[0]['username'],ReturnedUser[0]['password'],ReturnedUser[0]['email'],ReturnedUser[0]['phone_number'],ReturnedUser[0]['id'])
            return user
        

    # Create a user
    def create(self,name,username,password,email,phone_number):
        self._connection.execute('INSERT INTO users (name,username,password,email,phone_number) VALUES (%s,%s,%s,%s,%s)', [name,username,password,email,phone_number])
        return None
    # Delete a User by their ID
    def delete_by_id(self,id):
        self._connection.execute('DELETE FROM users WHERE id = %s',[id]) 
        return None
    
    #Show Owners property Bookings
    def show_bookings(self, approval,host_id):
        response = self._connection.execute('''SELECT availability.id, availability.date_not_available, users.username, spaces.name 
                                            FROM availability 
                                            JOIN spaces ON spaces.id = availability.spaces_id 
                                            JOIN users ON users.id = availability.requested_by_user_id 
                                            WHERE availability.approved = %s AND spaces.host_id = %s''', [approval,host_id])
        return (response)