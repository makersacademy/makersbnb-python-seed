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
    assert size_validator._is_size_present() == False
    size_validator_2 = SpaceParametersValidator("Beach house", "Relaxing space", None, "80")
    assert size_validator_2._is_size_present() == False

    price_validator = SpaceParametersValidator("Beach house", "Relaxing space", "210", "")
    assert price_validator._is_price_present() == False
    price_validator_2 = SpaceParametersValidator("Beach house", "Relaxing space", "210", None)
    assert price_validator_2._is_price_present() == False

def test_not_valid_with_size_not_digit():
    validator = SpaceParametersValidator("Beach house", "Relaxing space", "hello", "80")
    assert validator._is_size_digit() == False

def test_not_valid_with_price_not_digit():
    validator = SpaceParametersValidator("Beach house", "Relaxing space", "210", "hello")
    assert validator._is_price_digit() == False

def test_generate_errors():
    validator = SpaceParametersValidator("", "", "", "")
    assert validator.generate_errors() == [
        "Name must not be blank",
        "Description must not be blank",
        "Size must not be blank",
        "Price must not be blank"
    ]

    validator_2 = SpaceParametersValidator("Beach house", "", "", "80")
    assert validator_2.generate_errors() == [
        "Description must not be blank",
        "Size must not be blank"
    ]

    validator_3 = SpaceParametersValidator("Beach house", "Relaxing place", "", "")
    assert validator_3.generate_errors() == [
        "Size must not be blank",
        "Price must not be blank"
    ]

    validator_4 = SpaceParametersValidator("Beach house", "", "hello", "80")
    assert validator_4.generate_errors() == [
        "Description must not be blank",
        "Size must be a digit"
    ]

def test_get_valid_name_if_name_valid():
    validator = SpaceParametersValidator("Beach house", "Relaxing place", "210", "80")
    assert validator.get_valid_name() == "Beach house"

def test_get_valid_name_error_if_name_valid():
    validator = SpaceParametersValidator("", "Relaxing place", "210", "80")
    with pytest.raises(ValueError) as err:
        validator.get_valid_name()
    assert str(err.value) == "Cannot get valid name"

def test_get_valid_description_if_description_valid():
    validator = SpaceParametersValidator("Beach house", "Relaxing place", "210", "80")
    assert validator.get_valid_description() == "Relaxing place"

def test_get_valid_description_error_if_description_valid():
    validator = SpaceParametersValidator("Beach house", "", "210", "80")
    with pytest.raises(ValueError) as err:
        validator.get_valid_description()
    assert str(err.value) == "Cannot get valid description"

def test_get_valid_size_if_size_valid():
    validator = SpaceParametersValidator("Beach house", "Relaxing place", "210", "80")
    assert validator.get_valid_size() == "210"

def test_get_valid_size_error_if_size_valid():
    validator = SpaceParametersValidator("Beach house", "Relaxing place", "", "80")
    with pytest.raises(ValueError) as err:
        validator.get_valid_size()
    assert str(err.value) == "Cannot get valid size"

def test_get_valid_price_if_price_valid():
    validator = SpaceParametersValidator("Beach house", "Relaxing place", "210", "80")
    assert validator.get_valid_price() == "80"

def test_get_valid_price_error_if_price_valid():
    validator = SpaceParametersValidator("Beach house", "", "210", "")
    with pytest.raises(ValueError) as err:
        validator.get_valid_price()
    assert str(err.value) == "Cannot get valid price"