
from lib.date import *

"""
Date constructs with id, date, confirmed and space_id
"""

def test_date_construct():
    date = Date(1, "2024-01-20", True, 1)
    assert date.id == 1
    assert date.date == "2024-01-20"
    assert date.confirmed == True
    assert date.space_id == 1

"""
We can format Date to a string
"""

def test_date_format():
    date = Date(1, "2024-01-20", True, 1)
    assert str(date) == "Date(1, 2024-01-20, True, 1)"

"""
We can compare two identical dates
And have them be equal
"""

def test_date_compare():
    date1 = Date(1, "2024-01-20", True, 1)
    date2 = Date(1, "2024-01-20", True, 1)
    assert date1 == date2
