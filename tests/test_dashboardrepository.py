from lib.Dashboard import Requests
from lib.DashboardRepository import DashboardRepository
from datetime import date

def test_list_req(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = DashboardRepository(db_connection)
    
    requests = repository.list_req(1)

    assert requests == [
       Requests(1, 2, date(2024, 1, 12), 'Approved', 'Test Title2', 25.0)
    ]

def test_list_approvals(db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    repository = DashboardRepository(db_connection)
    
    requests = repository.list_approvals(1)
    