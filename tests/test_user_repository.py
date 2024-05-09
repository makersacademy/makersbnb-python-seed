from lib.user_repository import *
from lib.user import *
from lib.database_connection import *
import pytest
def test_user_repo_all(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    user_repo = UserRepository(db_connection)
    assert user_repo.all() == [User(1, 'matthew@gmail.com', '$2b$12$wuVZ7gFuaWwfeB8OdBsow.DrjAt30msLYkRMTlnSYZdhE5/Uwzp4.'),User(2,'myrto@hotmail.com', '6789@Gkx'), User(3, 'constantine@smith.net', 'Password123!'), User(4, 'john@yahoo.com', 'Hello67£'), User(5, 'alice@mail.com', 'Fdfdfd21$')]
def test_user_repo_find_by_id_valid(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    user_repo = UserRepository(db_connection)
    assert user_repo.find_by_id(1) == User(1, 'matthew@gmail.com', '$2b$12$wuVZ7gFuaWwfeB8OdBsow.DrjAt30msLYkRMTlnSYZdhE5/Uwzp4.')
def test_user_repo_find_by_id_invalid(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    user_repo = UserRepository(db_connection)
    with pytest.raises(Exception) as e:
        user_repo.find_by_id(6)
    error_message = str(e.value)
    assert error_message == "User not found!"
def test_user_repo_create_user(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    user_repo = UserRepository(db_connection)
    newuser = User(None,'JetSilv','thisispassword')
    user_repo.create(newuser)
    assert user_repo.find_by_id(6) == User(6,'JetSilv','thisispassword')