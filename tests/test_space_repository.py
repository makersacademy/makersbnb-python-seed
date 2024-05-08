from lib.space_repository import *
from lib.space import *
import pytest

def test_space_repo_all(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    spacerepo = SpaceRepository(db_connection)
    assert spacerepo.all() == [Space(1, 'Beach house','2024-06-01','2024-09-01',1,50.0), Space(2, 'Winter Lodge','2024-10-01','2025-01-01',2,60.0)]
    
def test_space_repo_find_by_id_valid(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    spacerepo = SpaceRepository(db_connection)
    assert spacerepo.find_by_id(1) == Space(1, 'Beach house','2024-06-01','2024-09-01',1,50.0)

def test_space_repo_find_by_id_invalid(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    spacerepo = SpaceRepository(db_connection)
    with pytest.raises(Exception) as e:
        spacerepo.find_by_id(3)
    error_message = str(e.value) 
    assert error_message == "Space not found!"

def test_space_repo_create_space(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    spacerepo = SpaceRepository(db_connection)
    newspace = Space(3,'The White House','2024-12-12','2025-12-12',2,75.0)
    spacerepo.create(newspace)
    assert spacerepo.find_by_id(3) ==  Space(3,'The White House','2024-12-12','2025-12-12',2,75.0)

def test_is_available_true(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    spacerepo = SpaceRepository(db_connection)
    assert spacerepo.is_available(1,'2002-12-20') ==True


def test_is_available_false(db_connection):
    db_connection.seed('seeds/temp_seed.sql')
    spacerepo = SpaceRepository(db_connection)
    assert spacerepo.is_available(1,'2024-05-07') == False