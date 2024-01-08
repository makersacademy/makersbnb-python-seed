from lib.space import Space

'''
test can construct space
'''
def test_can_construct():
    space = Space(1, "12 Norm Street N10 6MR", "2 Bedroom Cottage", 120, "A 2 bedroom cottage in a quiet area with lots of nature", "08/01/2023", "static/image1.jpeg", True)
    assert space.id == 1
    assert space.address == "12 Norm Street N10 6MR"
    assert space.price == 120
    assert space.description == "A 2 bedroom cottage in a quiet area with lots of nature"
    assert space.date_added == "08/01/2023"
    assert space.image == "static/image1.jpeg"
    assert space.availability == True

'''
test can format space
'''
def test_can_format():
    space = Space(1, "12 Norm Street N10 6MR", "2 Bedroom Cottage", 120, "A 2 bedroom cottage in a quiet area with lots of nature", "08/01/2023", "static/image1.jpeg", True)
    assert str(space) == "Space(1, 12 Norm Street N10 6MR, 2 Bedroom Cottage, 120, A 2 bedroom cottage in a quiet area with lots of nature, 08/01/2023, static/image1.jpeg, True)"