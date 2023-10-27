class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def check(self, username):
        return self._connection.execute(
            "SELECT * FROM users WHERE username=%s", [username]
        )

    def create(self, user):
        self._connection.execute(
            "INSERT INTO users "
            + "(id, username, email, passwordhash, phonenumber) "
            + "VALUES (%s, %s, %s, %s, %s)",
            [user.id, user.username, user.email, user.password_hash, user.phone_number],
        )

    def verify(self, username, passwordhash):
        print(
            self._connection.execute(
                "SELECT * FROM users WHERE username=%s AND passwordhash=%s",
                [username, passwordhash],
            )
        )
        return self._connection.execute(
            "SELECT * FROM users WHERE username=%s AND passwordhash=%s",
            [username, passwordhash],
        )
