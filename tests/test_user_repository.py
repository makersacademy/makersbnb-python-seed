from lib.user_repository import *
from lib.user import *
from lib.database_connection import *
import pytest

def test_user_repo_all(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    user_repo = UserRepository(db_connection)
    assert user_repo.all() == [User(1, "harrydon725","password123"),User(2,"Jsanyang21",'1234')]

def test_user_repo_find_by_id_valid(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    user_repo = UserRepository(db_connection)
    assert user_repo.find_by_id(1) == User(1, "harrydon725","password123")

def test_user_repo_find_by_id_invalid(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    user_repo = UserRepository(db_connection)
    with pytest.raises(Exception) as e:
        user_repo.find_by_id(3)
    error_message = str(e.value) 
    assert error_message == "User not found!"

def test_user_repo_create_user(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    user_repo = UserRepository(db_connection)
    newuser = User(None,'JetSilv','thisispassword')
    user_repo.create(newuser)
    assert user_repo.find_by_id(3) == User(3,'JetSilv','thisispassword')


