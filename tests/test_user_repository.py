from lib.user_repository import UserRepository
from lib.user import User

def test_all(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, "Example User", "examplepassword", "exampleemail@email.com"),
        User(2, "Example User2", "examplepassword2", "exampleemail2@email.com")
    ]
def test_create_user(db_connection):
    db_connection.seed("seeds/scar_bnb.sql")
    repository = UserRepository(db_connection)
    repository.create(User(None, "Example user3", "examplepassword3", "exampleemail3@email.com"))
    result = repository.all()
    assert result == [
        User(1, "Example User", "examplepassword", "exampleemail@email.com"),
        User(2, "Example User2", "examplepassword2", "exampleemail2@email.com"),
        User(3, "Example user3", "examplepassword3", "exampleemail3@email.com")
    ]