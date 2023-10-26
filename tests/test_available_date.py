from lib.available_date import AvailableDate
"""
test construction
"""
def test_init_method():
    first_available_date = AvailableDate(2, "12/11/2003", 1)
    assert first_available_date.id == 2
    assert first_available_date.date_name == "12/11/2003"
    assert first_available_date.space_id == 1

"""
test repr method
"""
def test_repr_method(capfd):
    first_available_date = AvailableDate(2, "12/11/2003", 1)
    print(first_available_date)
    out, err = capfd.readouterr()
    assert out == "AvailableDate(2, 12/11/2003, 1)\n"