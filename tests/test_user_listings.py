from lib.space import *

def test_space_initialization():
    space = Space("London", "Smallest flat in the city with expensive rooms", 3000, "2024-03-24")
    assert space.name == "London"
    assert space.description == "Smallest flat"
    assert space.price_per_night == 3000
    assert space.availability == "2024-03-24"

