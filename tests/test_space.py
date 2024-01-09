from lib.space import Space

'''
test can construct space
'''
def test_can_construct():
    space = Space(1, '123 Horse Lane', 'Wild horses', 56, '/images/lilkim.jpg', 'A light, warm, and modern space for a gathering.', '2020-10-22', '2024-06-22', 1)
    assert space.id == 1
    assert space.address == "123 Horse Lane"
    assert space.name == 'Wild horses'
    assert space.description == "A light, warm, and modern space for a gathering."
    assert space.price == 56
    assert space.date_added == "2020-10-22"
    assert space.date_available == "2024-06-22"
    assert space.image_path == "/images/lilkim.jpg"
    assert space.user_id == 1


'''
test can format space
'''
def test_can_format():
    space = Space(1, '123 Horse Lane', 'Wild horses', 56, '/images/lilkim.jpg', 'A light, warm, and modern space for a gathering.', '2020-10-22', '2024-06-22', 1)
    assert str(space) == "Space(1, 123 Horse Lane, Wild horses, 56, /images/lilkim.jpg, A light, warm, and modern space for a gathering., 2020-10-22, 2024-06-22, 1)"