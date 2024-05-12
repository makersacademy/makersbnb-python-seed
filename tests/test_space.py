from lib.space import *


def test_space_eq_valid():
    space1 = Space(1, "Studio apartment", 100.0, '2024-05-20', '2025-05-20', 1)
    space2 = Space(1, "Studio apartment", 100.0, '2024-05-20', '2025-05-20', 1)
    # Space(2,"3 bedroom flat",'2024-05-10', '2024-12-10',1,250.0)

    assert space1 == space2


def test_space_eq_invalid():
    space1 = Space(1, "Buckingham Palace", 50.0, '2024-01-01', '2024-06-01', 1)
    space2 = Space(1, "Buckingham house", 60.0, '2024-01-01', '2024-06-01', 2)
    assert space1 != space2


def test_space_repr():
    space1 = Space(1, "Buckingham Palace", 50.0, '2024-01-01', '2024-06-01', 1)
    assert str(
        space1) == 'Space(1, Buckingham Palace, 2024-01-01, 2024-06-01, 1, 50.0)'


def test_isvalid_valid():
    space1 = Space(1, "Buckingham Palace", 50.0, '2024-01-01', '2024-06-01', 1)
    assert space1.is_valid() == True


def test_isvalid_notitle():
    space1 = Space(1, "", 50.0, '2024-01-01', '2024-06-01', 1)
    assert space1.is_valid() == False


def test_generateerrors_valid():
    space1 = Space(1, "Buckingham palace", 50.0, '2024-01-01', '2024-06-01', 1)
    assert space1.generate_errors() == None


def test_generateerrors_notitle():
    space1 = Space(1, "", 50.0, '2024-01-01', '2024-06-01', 1)
    assert space1.generate_errors() == "Title can't be blank"


def test_invalid_price_input():
    space = Space(1, "Buckingham palace", "", '2024-01-01', '2024-06-01', 1)
    assert space.generate_errors(
    ) == "Price can't be blank, Price has to be a number (up to 2 decimals)"


def test_invalid_start_date_input():
    space = Space(1, "Buckingham palace", 50, '', '2024-06-01', 1)
    assert space.generate_errors(
    ) == "Start date can't be blank"


def test_valid_price():
    space = Space(1, "Buckingham palace", 50.2, '2024-05-20', '2024-06-01', 1)
    assert space.is_valid() == True


def test_valid_error_message():
    space = Space(1, "Buckingham palace", 50, '2024-05-20', '2024-06-01', 1)
    assert space.is_valid() == True
