from lib.makersbnb import MakersBnb

class MakersBnB_Repository:

    # We initialise with a database connection
    def __init__(self, connection):
        self._connection = connection    
        
    def all(self):
        rows = self._connection.execute("SELECT * FROM users")
        users = []
        for row in rows:
            user = MakersBnb(row["id"], row["email"], row["password"])
            users.append(user)
        return users
    
    def add_users(self):
        rows = self._connection.execute(
            'INSERT INTO users (email, password) VALUES (%s, %s)',
               [users.email, users.password]                    
               )
        
        
    
    """password validation
if user enters email already used, error message
once submitted, info gets saved to ‘users’ table"""

# from datetime import datetime

# class PasswordManager2():
#     def __init__(self):
#         self.passwords = {}
#         self.added_on = {}

#     def is_password_Valid(self, password):
#         if len(password) >= 8 and any(char in {'!', '@', '$', '%', '&'} for char in password) and not (password in self.passwords.values()):
#             return True
#         else:
#             return False
        
#
#     def update(self,service,password):
#         if service in self.passwords and self.is_password_Valid(password):
#             self.passwords[service] = password

#     def list_services(self):
#         return list(self.passwords.keys())
    
#     def sort_services_by(self, criterion, reverse=None):
#         if criterion == 'service':
#             sorted_services = sorted(self.passwords.keys())
#         elif criterion == 'added_on':
#             sorted_services = sorted(self.passwords.keys(), key=lambda x: self.added_on[x])
#         else:
#             raise ValueError("Invalid sorting criterion. Please use 'service' or 'added_on'.")

#         if reverse:
#             sorted_services.reverse()

#         return sorted_services
    
#     def get_for_service(self,service):
#         return self.passwords.get(service)
    
# password_manager = PasswordManager2()
# password_manager.add('gmail', '12ab5!678')   
# password_manager.add('facebook', '$abc1234') 
# password_manager.add('twitter', '12345678')  
# password_manager.list_services()
# password_manager.remove('facebook')
# password_manager.list_services()
# password_manager.update('gmail', '12345678')  
# password_manager.get_for_service('gmail')
# password_manager.update('gmail', '%21321415')  
# password_manager.get_for_service('gmail')
# password_manager.sort_services_by('service')
# password_manager.sort_services_by('added_on', 'reverse')