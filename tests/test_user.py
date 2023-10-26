from lib.user import User

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

def test_repr_method():
    charlie = User("charliemeister649", ['mcdonalds'], id=1)
    assert str(charlie) == "User(charliemeister649, ['mcdonalds'], 1)"

"""
test two user instances with identical dict (parameters) are ==
"""
def test_dict_method():
    charlie = User("charliemeister649", ['mcdonalds'])
    charlie_again = User("charliemeister649", ['mcdonalds'])
    assert charlie == charlie_again