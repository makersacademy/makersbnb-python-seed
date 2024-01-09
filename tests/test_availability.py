from lib.availability import Availability
from datetime import date

"""
Availability constructs with a space_id, date, status
"""
def test_constructs_availability():
    availability = Availability(1, date(2025,1,1), True)
    assert availability.space_id == 1
    assert availability.date == date(2025,1,1)
    assert availability.status == True

# """
# We can format availability to strings nicely
# """
def test_availability_format_nicely():
    availability = Availability(1, date(2025,1,1), True)
    assert availability == Availability(1, date(2025,1,1), True)

def test_availability_are_equal():
    availability1 = Availability(1, date(2025,1,1), True)
    availability2 = Availability(1, date(2025,1,1), True)
    assert availability1 == availability2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
