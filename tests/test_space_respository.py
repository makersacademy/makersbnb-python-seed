from lib.space_repository import SpaceRepository
from lib.space import Space

def test_get_all_spaces(db_connection):
    db_connection.seed("seeds/spaces.sql")
    repository = SpaceRepository(db_connection)

    spaces = repository.all()

    assert spaces == [
        Space('Cozy Corner', 'London', 120, 2, 'Warm and inviting space with a cozy atmosphere.'),
        Space('Serene Spot', 'Manchester', 95, 1, 'Tranquil setting for a peaceful and relaxing experience.'),
        Space('Tranquil Haven', 'Birmingham', 110, 3, 'A haven of tranquility with spacious and comfortable surroundings.'),
        Space('Peaceful Retreat', 'Edinburgh', 140, 2, 'Escape to a peaceful retreat with calming ambiance and serenity.'),
    ]