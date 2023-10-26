from lib.request_repo import *
from lib.request import *
from datetime import datetime

def test_date_repo_get_all_requests_by_listing_id(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = RequestRepo(db_connection)
    date_format = '%Y-%m-%d'
    assert repo.get_all_requests_by_listing_id(5) == [
        Request(datetime.strptime('2024-07-12', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-13', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-14', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-15', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-16', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-12', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-13', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-14', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-15', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-16', date_format), 5, 6, 5)
    ]

    assert repo.get_all_requests_by_listing_id(6) == []


def test_date_repo_get_all_incoming_requests(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = RequestRepo(db_connection)
    date_format = '%Y-%m-%d'
    assert repo.get_all_incoming_requests(5) == [
        Request(datetime.strptime('2024-07-12', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-13', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-14', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-15', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-16', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-12', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-13', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-14', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-15', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-16', date_format), 5, 6, 5)
    ]

    assert repo.get_all_incoming_requests(6) == []

def test_date_repo_get_all_outgoing_requests(db_connection):
    db_connection.seed('seeds/bnb.sql')
    repo = RequestRepo(db_connection)
    date_format = '%Y-%m-%d'
    assert repo.get_all_outgoing_requests(6) == [
        Request(datetime.strptime('2024-07-12', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-13', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-14', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-15', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-07-16', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-12', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-13', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-14', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-15', date_format), 5, 6, 5),
        Request(datetime.strptime('2024-05-16', date_format), 5, 6, 5)
    ]

    assert repo.get_all_outgoing_requests(5) == []