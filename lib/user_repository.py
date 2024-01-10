from lib.user import User


class UserRepository:
    def __init__(self, connection):
        self._connection = connection

    def create_user(self, username, email, password):
        try:
            self._connection.execute(
                "INSERT into users (username, email, password) VALUES (%s, %s, %s)",
                [username, email, password],
            )
            return True
        except Exception as e:
            print("Error creating user")
            return False

    def all(self):
        rows = self._connection.execute(
            "SELECT username, email, password FROM users"  # security issue with calling password?
        )
        return [User(row["username"], row["email"], row["password"]) for row in rows]

    def find_user_by_username(self, username):
        rows = self._connection.execute(
            "SELECT username, email, password FROM users WHERE username = %s",
            [username],
        )
        if rows:
            user = rows[0]
            return User(user["username"], user["email"], user["password"])
        return None

    def password_hash():
        pass

    def login(self, username, password):
        rows = self._connection.execute(
            "SELECT id, username, email, password FROM users WHERE username = %s",
            [username],
        )
        if rows:
            user = rows[0]
            print(user)
            stored_username = user["username"]
            stored_password = user["password"]
            if stored_username == username and password == stored_password:
                return True
            else:
                print("Failed to login: Please check details")
                return None
        else:
            print("User not found")
            return None

    def request_space():
        pass

    def username_to_id(self, username):
        return self._connection.execute(
            """
            SELECT id FROM users WHERE username=%s;
            """, [username]
        )[0]['id']
    
    def id_to_username(self, id):
        return self._connection.execute(
            """
            SELECT username FROM users WHERE id=%s;
            """, [id]
        )[0]['username']
