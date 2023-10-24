import pytest
from lib.space_parameters_validator import *

def test_is_valid():
    validator = SpaceParametersValidator("Beach house", "Relaxing space", "210", "80")
    assert validator._is_valid() == True

def test_not_valid_with_empty_values():
    name_validator = SpaceParametersValidator("", "Relaxing space", "210", "80")
    assert name_validator._is_name_valid() == False
    name_validator_2 = SpaceParametersValidator(None, "Relaxing space", "210", "80")
    assert name_validator_2._is_name_valid() == False

    descr_validator = SpaceParametersValidator("Beach house", "", "210", "80")
    assert descr_validator._is_description_valid() == False
    descr_validator_2 = SpaceParametersValidator("Beach house", None, "210", "80")
    assert descr_validator_2._is_description_valid() == False

    size_validator = SpaceParametersValidator("Beach house", "Relaxing space", "", "80")
    assert size_validator._is_size_valid() == False
    size_validator_2 = SpaceParametersValidator("Beach house", "Relaxing space", False)
    assert size_validator_2._is_size_valid() == False

    price_validator = SpaceParametersValidator("Beach house", "Relaxing space", "210", "")
    assert price_validator._is_price_valid() == False
    price_validator_2 = SpaceParametersValidator("Beach house", "Relaxing space", False)
    assert price_validator_2._is_price_valid() == False

def test_not_valid_with_size_not_digit():
    validator = SpaceParametersValidator("Beach house", "Relaxing space", "hello")
    assert validator._is_size_valid() == False

def test_not_valid_with_price_not_digit():
    validator = SpaceParametersValidator("Beach house", "Relaxing space", "210", "hello")
    assert validator._is_price_valid() == False

def test_generate_errors():
    validator = SpaceParametersValidator("", "", "", "")
    assert validator.generate_errors() == [
        "Name must not be blank",
        "Description must not be blank",
        "Size must not be blank",
        "Price must not be blank"
    ]

    validator_2 = SpaceParametersValidator("Beack house", "", "", "80")
    assert validator_2.generate_errors() == [
        "Description must not be blank",
        "Size must not be blank"
    ]

    validator_3 = SpaceParametersValidator("Beack house", "Relaxing place", "", "")
    assert validator_3.generate_errors() == [
        "Size must not be blank",
        "Price must not be blank"
    ]

    validator_4 = SpaceParametersValidator("Beack house", "", "hello", "80")
    assert validator_4.generate_errors() == [
        "Description must not be blank",
        "Size must be a digit"
    ]

def test_get_valid_name_if_name_valid():
    validator = SpaceParametersValidator("Beack house", "Relaxing place", "210", "80")
    assert validator.get_valid_name == "Beack house"

def test_get_valid_name_error_if_name_valid():
    validator = SpaceParametersValidator("", "Relaxing place", "210", "80")
    with pytest.raises(ValueError) as err:
        validator.get_valid_name()
    assert str(err.value) == "Cannot get valid name"

def test_get_valid_description_if_description_valid():
    validator = SpaceParametersValidator("Beack house", "Relaxing place", "210", "80")
    assert validator.get_valid_description == "Relaxing place"

def test_get_valid_description_error_if_description_valid():
    validator = SpaceParametersValidator("Beack house", "", "210", "80")
    with pytest.raises(ValueError) as err:
        validator.get_valid_description()
    assert str(err.value) == "Cannot get valid description"

def test_get_valid_size_if_size_valid():
    validator = SpaceParametersValidator("Beack house", "Relaxing place", "210", "80")
    assert validator.get_valid_size == "Relaxing place"

def test_get_valid_size_error_if_size_valid():
    validator = SpaceParametersValidator("Beack house", "", "210", "80")
    with pytest.raises(ValueError) as err:
        validator.get_valid_size()
    assert str(err.value) == "Cannot get valid size"