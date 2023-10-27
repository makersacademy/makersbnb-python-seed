from lib.space import Space

def test_space_constructs():
    space = Space(1,"Test PLACE", "VERY NICE", 200, 1)
    assert  space.id == 1
    assert  space.name == "Test PLACE"
    assert  space.description == "VERY NICE"
    assert  space.price == 200
    assert  space.owner_id == 1


def test_books_are_equal():
    space1 = Space(1,"TEST PLACE", "VERY NICE", 200, 1)
    space2 = Space(1,"TEST PLACE", "VERY NICE", 200, 1)
    assert space1 == space2