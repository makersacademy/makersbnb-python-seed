from lib.space import Space

"""
Initiating the space
and the properties are correct

"""
def test_properties_of_space():
    apartment1 = Space(1, 'Apartment 1', 'Description 1', 100, '2024-01-01', '2024-04-01', 1)
    apartment1.id == 1
    apartment1.name == "Apartment 1"
    apartment1.description == "Description 1"
    apartment1.price == 100
    apartment1.date_from == '2024-01-01'
    apartment1.date_to == '2024-04-01'
    apartment1.user_id == 1

"""
test the two space we make are equal

"""

def test_spaces_are_equal():
    apartment1 = Space(1, 'Apartment 1', 'Description 1', 100, '2024-01-01', '2024-04-01', 1)
    apartment2 = Space(1, 'Apartment 1', 'Description 1', 100, '2024-01-01', '2024-04-01', 1)
    assert apartment1 == apartment2


"""
the spaces formatted in a string
"""

def test_nice_format():
    apartment1 = Space(1, 'Apartment 1', 'Description 1', 100, '2024-01-01', '2024-04-01', 1)
    assert apartment1.nice_format() == "Apartment 1, Description 1, 100, 2024-01-01, 2024-04-01, 1"