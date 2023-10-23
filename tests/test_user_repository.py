from lib.user_repository import UserRepository
from lib.user import User

"""
When we call UserRepository#all
We get a list of all the User objects
"""
def test_list_all_users(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, 'name1@cmail.com', 'name1', 'password1'),
        User(2, 'name2@cmail.com', 'name2', 'password2'),
        User(3, 'name3@cmail.com', 'name3', 'password3')
    ]
    
"""
When we create a User object
It is reflected in the list when we call UserRepository#all
"""
def test_create_single_user(db_connection):
    db_connection.seed("seeds/makers_bnb_library.sql")
    repository = UserRepository(db_connection)
    user = User(None, "Test email", "Test Username", "Test Password")
    assert repository.create(user) == None
    assert repository.all() == [
        User(1, 'name1@cmail.com', 'name1', 'password1'),
        User(2, 'name2@cmail.com', 'name2', 'password2'),
        User(3, 'name3@cmail.com', 'name3', 'password3'),
        User(4, "Test email", "Test Username", "Test Password")
    ]


"""
When we call UserRepository#find with an id
We get the User object for that id
"""

"""
When we call UserRepository#update with a new password
It is reflected in the list when we call UserRepository#all
"""

"""
When we call UserRepository#delete with an id
That User object is no longer in the list when we call UserRepository#all
"""

