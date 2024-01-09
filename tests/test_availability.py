from lib.availability import Availability

"""
Availability constructs with a space_id, date, status
"""
def test_constructs_availability():
    availability = Availability(1, "2025-01-01", True)
    assert availability.space_id == 1
    assert availability.date == "2025-01-01"
    assert availability.status == True

# """
# We can format availability to strings nicely
# """
# def test_availability_format_nicely():
#     availability = Availability(1, "2025-01-01", True)
#     assert str(availability) == Availability(1, "2025-01-01", True)

def test_artists_are_equal():
    artist1 = Availability(1, '2025-01-01', True)
    artist2 = Availability(1, '2025-01-01', True)
    assert artist1 == artist2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.
