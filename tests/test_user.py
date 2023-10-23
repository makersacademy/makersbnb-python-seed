from lib.user import *

"""
test init function
return correct username and spaces
"""

def test_construction_return_username():
    charlie = User("charliemeister649", ['mcdonalds'])
    assert charlie.username == "charliemeister649"
    assert charlie.spaces == ['mcdonalds']

"""
test nicer looking representation (repr function) 
"""

def test_repr_method(capfd):
    charlie = User("charliemeister649", ['mcdonalds'])
    print(charlie)
    out, err = capfd.readouterr()
    assert out == "User(charliemeister649, ['mcdonalds'])\n"
    

"""
test two user instances with identical dict (parameters) are ==
"""
def test_dict_method():
    charlie = User("charliemeister649", ['mcdonalds'])
    charlie_again = User("charliemeister649", ['mcdonalds'])
    assert charlie == charlie_again