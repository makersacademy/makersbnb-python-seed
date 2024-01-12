from lib.Dashboard import Requests
from datetime import date


def test_equivilancy():
    req1 = Requests(1, 2, date(2024, 1, 12), 'Pending', "Josh's Crib", 100.00)
    req2 = Requests(1, 2, date(2024, 1, 12), 'Pending', "Josh's Crib", 100.00)
    assert req1 == req2