class User:
    def __init__(s, username, spaces, id=None):
        s.username = username
        s.spaces = spaces
        s.id = id
    def __repr__(s):
        return f"User({s.username}, {s.spaces}, {s.id})"
    def __eq__(s, o):
        return s.__dict__ == o.__dict__