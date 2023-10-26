from lib.date_repo import *
from lib.date import *
from datetime import datetime

def test_date_repo_init(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = DateRepo(db_connection)
    date_format = '%Y-%m-%d'
    assert repo.all() == [
        Date(datetime.strptime('2024-06-12', date_format), 1),
        Date(datetime.strptime('2024-06-13', date_format), 1),
        Date(datetime.strptime('2024-06-14', date_format), 1),
        Date(datetime.strptime('2024-06-15', date_format), 1),
        Date(datetime.strptime('2024-06-16', date_format), 1)       
    ]

def test_check_listing_availability_with_listing_id(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = DateRepo(db_connection)
    date_format = '%Y-%m-%d'
    assert repo.check_listing_availability_with_listing_id(1) == [
        Date(datetime.strptime('2024-06-12', date_format), 1),
        Date(datetime.strptime('2024-06-13', date_format), 1),
        Date(datetime.strptime('2024-06-14', date_format), 1),
        Date(datetime.strptime('2024-06-15', date_format), 1),
        Date(datetime.strptime('2024-06-16', date_format), 1)        
    ]    

    assert repo.check_listing_availability_with_listing_id(2) == []  


def test_date_repo_get_avail_for_date(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = DateRepo(db_connection)
    date_format = '%Y-%m-%d'
    date = datetime.strptime('2024-06-12', date_format)
    assert repo.get_availability_for_date(date, 1) == False
    date = datetime.strptime('2024-07-12', date_format)
    assert repo.get_availability_for_date(date, 1) == True