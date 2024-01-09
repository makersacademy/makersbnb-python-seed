from lib.space_repository import SpaceRepository
from lib.space import Space


# # test get all spaces
def test_can_get_all_spaces(db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    repository = SpaceRepository(db_connection)
    assert repository.all() == [
Space(1, '123 Horse Lane', 'Wild horses', 56, '/images/lilkim.jpg', 'A light, warm, and modern space for a gathering.', '2020-10-22', 1),
Space(2, '5 Zoo lane', 'Zootropolis', 124, '/images/zoos.jpg', 'A nice warm bed amongst the animals', '2019-08-21', 2),
Space(3, '789 Starlight Street', 'Celestial Haven', 72, '/images/celestial_haven.jpg', 'Experience the tranquility under the stars in this celestial haven.', '2022-02-08', 3), 
Space(4, '101 Mountain View', 'Mountain Hideaway', 110, '/images/mountain_hideaway.jpg', 'Escape to the serene mountains and enjoy the breathtaking views.', '2023-01-17', 2),
Space(5, '222 Beachfront Road', 'Ocean Paradise Villa', 150, '/images/ocean_paradise.jpg', 'Relax by the beach in this luxurious oceanfront villa.', '2022-11-30', 1),
Space(6, '333 Skyline Tower', 'Cityscape Loft', 95, '/images/cityscape_loft.jpg', 'A modern loft with stunning views of the city skyline.', '2020-12-03', 3),
Space(7, '444 Lakeside Drive', 'Tranquil Lake Cottage', 80, '/images/lake_cottage.jpg', 'Escape to this cozy cottage by the lake for a peaceful retreat.', '2021-09-25', 2)
    ]
    


# # test create space


# #  test find space


# # test delete space


# # test update space