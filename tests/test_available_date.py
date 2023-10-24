from lib.available_date import AvailableDate
"""
test construction
"""
def test_init_method():
    first_available_date = AvailableDate("12/11/2003", 1)
    assert first_available_date.date == "12/11/2003"
    assert first_available_date.space_id == 1

"""

"""