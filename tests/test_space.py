from lib.space import *

"""
construct space class,
id, space_name, description, price_per_night, user_id, start_date, end_date
"""
def test_construct_space_class():
    space = Space(1, "test_name", "test description", 30, 1)
    assert f"{space}" == "1, test_name, test description, 30, 1"
    space_2 = Space(1, "test_name", "test description", 30, 1)
    assert space == space_2

