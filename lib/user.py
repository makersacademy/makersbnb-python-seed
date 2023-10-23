class User:
    def __init__(s, username, spaces):
        s.username = username
        s.spaces = spaces
    def __repr__(s):
        return(f"User({s.username}, {s.spaces})")
    def __eq__(s, o):
        return s.__dict__ == o.__dict__