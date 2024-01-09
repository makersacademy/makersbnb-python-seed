from lib.SpacesRepository import SpacesRepository
from lib.Space import Space


def test_list_all_returns_object_list(db_connection):
    db_connection.seed('seeds/SpacesTest.sql')
    repository = SpacesRepository(db_connection)
    result =repository.list_all()
    
    assert result == [
       Space(5,'Test Title5','This is some test description',1037.63,'2024-01-12-2024-01-19',3), 
       Space(4,'Test Title4','This is some test description',19.95,'2024-01-21-2024-01-31',2), 
       Space(3,'Test Title3','This is some test description',135.50,'2024-01-12-2024-02-05',2), 
       Space(2,'Test Title2','This is some test description',25.00,'2024-01-14-2024-01-29',1), 
       Space(1,'Test Title','This is some test description',65.75,'2024-01-12-2024-01-31',1)
    ]

def test_user_can_add_a_listing(db_connection):
    db_connection.seed('seeds/SpacesTest.sql')
    repository = SpacesRepository(db_connection)
    repository.add('Test Title6','This is some test description',45.75,'2024-01-23-2024-02-05',3)
    result = repository.list_all()
    assert result == [
       Space(6,'Test Title6','This is some test description',45.75,'2024-01-23-2024-02-05',3),
       Space(5,'Test Title5','This is some test description',1037.63,'2024-01-12-2024-01-19',3), 
       Space(4,'Test Title4','This is some test description',19.95,'2024-01-21-2024-01-31',2), 
       Space(3,'Test Title3','This is some test description',135.50,'2024-01-12-2024-02-05',2), 
       Space(2,'Test Title2','This is some test description',25.00,'2024-01-14-2024-01-29',1), 
       Space(1,'Test Title','This is some test description',65.75,'2024-01-12-2024-01-31',1)
    ]