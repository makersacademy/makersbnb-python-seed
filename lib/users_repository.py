from lib.user import *

class UsersRepository:

    def __init__(self, connection):
        self._connection = connection

    def find(self,email):
        rows = self._connection.execute("SELECT * FROM users WHERE email = %s", [email])
        try:
            row = rows[0]
        except:
            raise EmailNotFound("User not found")

        return User(row['id'],row['email'],row['forename'],row['surname'],row['phone_number'],row['password'],)

    def check_email_unique(self, credentials):
        user_credentials = credentials
        try:
            self.find(user_credentials.email)
            return False
        
        except EmailNotFound:
            return True

    def create(self,credentials):
        new_user = credentials
        if self.check_email_unique(new_user):
            self._connection.execute('INSERT INTO users (email,forename,surname,phone_number,password) VALUES (%s,%s,%s,%s,%s)', 
                                     [credentials.email,
                                      credentials.forename,
                                      credentials.surname,
                                      credentials.phone_number,
                                      credentials.password])
        else:
            raise AccountExists("Email already assigned to an account!")

class EmailNotFound(Exception):
    pass

class AccountExists(Exception):
    pass