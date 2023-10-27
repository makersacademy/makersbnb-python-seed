from lib.space.space import Space


class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        return self._connection.execute("SELECT * FROM spaces")

    def exists_already(self, name):
        if (
            len(self._connection.execute("SELECT * FROM spaces WHERE name=%s", [name]))
            > 0
        ):
            return True
        else:
            return False

    def add(self, space):
        self._connection.execute(
            "INSERT INTO spaces "
            + "(id, name, ownerid, description, startdate, enddate) "
            + "VALUES (%s, %s, %s, %s, %s, %s)",
            [
                space.id,
                space.name,
                space.owner_id,
                space.description,
                space.start_date,
                space.end_date,
            ],
        )
