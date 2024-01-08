import pytest
from lib.booking_parameters_validator import *

def test_is_valid():
    validator = BookingParametersValidator(1, '12-11-24', '16-11-24', 2)
    assert validator._is_valid() == True

def test_not_valid_with_empty_values():
    space_id_validator = BookingParametersValidator(None, '12-11-24', '16-11-24', 2)
    assert space_id_validator._is_valid() == False

    start_date_validator = BookingParametersValidator(1, None, '16-11-24', 2)
    assert start_date_validator._is_start_date_present() == False

    end_date_validator = BookingParametersValidator(1, '12-11-24', None, 2)
    assert end_date_validator._is_end_date_present() == False

    booker_id_validator = BookingParametersValidator(1, '12-11-24', '16-11-24', None)
    assert booker_id_validator._is_booker_id_present() == False

def test_generate_errors():
    validator = BookingParametersValidator(1, None, None, 2)
    assert validator.generate_errors() == [
        "Start date must not be blank",
        "End date must not be blank",
    ]

    validator_2 = BookingParametersValidator(1, None, 16-11-24, 2)
    assert validator_2.generate_errors() == [
        "Start date must not be blank",
    ]

def test_get_valid_space_id_if_space_id_valid():
    validator = BookingParametersValidator(1, '12-11-24', '16-11-24', 2)
    assert validator.get_valid_space_id() == 1

def test_get_valid_space_id_error_if_space_id_valid():
    validator = BookingParametersValidator(None, '12-11-24', '16-11-24', 2)
    with pytest.raises(ValueError) as err:
        validator.get_valid_space_id()
    assert str(err.value) == "Cannot get valid space"

def test_get_valid_start_date_if_start_date_valid():
    validator = BookingParametersValidator(1, '12-11-24', '16-11-24', 2)
    assert validator.get_valid_start_date() == '12-11-24'

def test_get_valid_start_date_error_if_start_date_valid():
    validator = BookingParametersValidator(1, None, 16-11-24, 2)
    with pytest.raises(ValueError) as err:
        validator.get_valid_start_date()
    assert str(err.value) == "Cannot get valid start date"

def test_get_valid_end_date_if_end_date_valid():
    validator = BookingParametersValidator(1, '12-11-24', '16-11-24', 2)
    assert validator.get_valid_end_date() == '16-11-24'

def test_get_valid_end_date_error_if_end_date_valid():
    validator = BookingParametersValidator(1, '12-11-24', None, 2)
    with pytest.raises(ValueError) as err:
        validator.get_valid_end_date()
    assert str(err.value) == "Cannot get valid end date"

def test_get_valid_booker_id_if_booker_id_valid():
    validator = BookingParametersValidator(1, '12-11-24', '16-11-24', 2)
    assert validator.get_valid_booker_id() == 2

def test_get_valid_price_error_if_booker_id_valid():
    validator = BookingParametersValidator(1, '12-11-24', '16-11-24', None)
    with pytest.raises(ValueError) as err:
        validator.get_valid_booker_id()
    assert str(err.value) == "Cannot get valid user"