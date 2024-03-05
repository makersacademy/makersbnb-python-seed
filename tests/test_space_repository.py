from lib.space_repository import SpaceRepository
from lib.space import Space

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [
        Space(1, 'Cozy Corner', 'London', 120, 2, 'Warm and inviting space with a cozy atmosphere.'),
        Space(2, 'Serene Spot', 'Manchester', 95, 1, 'Tranquil setting for a peaceful and relaxing experience.'),
        Space(3, 'Tranquil Haven', 'Birmingham', 110, 3, 'A haven of tranquility with spacious and comfortable surroundings.'),
        Space(4, 'Peaceful Retreat', 'Edinburgh', 140, 2, 'Escape to a peaceful retreat with calming ambiance and serenity.'),
    ]