import datetime
# This is an example of how to use the DatabaseConnection class

"""
When I seed the database
I get some records back
"""
def test_database_connection_can_read(db_connection):
    # Seed the database with some test data
    db_connection.seed("seeds/makersbnb_tables.sql")

    # Retrieve all records
    resultusers = db_connection.execute("SELECT * FROM users")
    resultspaces = db_connection.execute("SELECT * FROM spaces")
    resultsbookings = db_connection.execute("SELECT * FROM bookings")

    # Assert that the results are what we expect
    assert resultusers == [
    {"id": 1, "email": "mrtester@gmail.com", "password": "GudPass91!"},
    {"id": 2, "email": "vlad@hotmail.com", "password": "Coolguy4"}
    ]

    assert resultspaces == [
    {"id": 1, "name": "The Shack", "description": "A quaint little shed...", "price": 20.00, "available_from": datetime.date(2023, 1, 1), "available_to": datetime.date(2023, 12, 25), "user_id": 1},
    {"id": 2, "name": "24 Farm Street", "description": "The country aroma is strong...", "price": 40.00, "available_from": datetime.date(2023, 1, 1), "available_to": datetime.date(2023, 12, 25), "user_id": 1},
    {"id": 3, "name": "Castle Dracula", "description": "Dont let the dust put you off...", "price": 500.00, "available_from": datetime.date(2023, 1, 1), "available_to": datetime.date(2023, 12, 25), "user_id": 2},
    {"id": 4, "name": "London Bachelor Pad", "description": "You cant afford this place..", "price": 3000.00, "available_from": datetime.date(2023, 1, 1), "available_to": datetime.date(2023, 12, 25), "user_id": 2}]


    assert resultsbookings == [
    {"id": 1, "date_reserved": datetime.date(2023, 9, 1), "space_id": 1},
    {"id": 2, "date_reserved": datetime.date(2023, 9, 2), "space_id": 1},
    {"id": 3, "date_reserved": datetime.date(2023, 9, 3), "space_id": 1},
    {"id": 4, "date_reserved": datetime.date(2023, 9, 4), "space_id": 1},
    {"id": 5, "date_reserved": datetime.date(2023, 11, 15), "space_id": 2},
    {"id": 6, "date_reserved": datetime.date(2023, 11, 16), "space_id": 2},
    {"id": 7, "date_reserved": datetime.date(2023, 11, 17), "space_id": 2},
    {"id": 8, "date_reserved": datetime.date(2023, 11, 18), "space_id": 2}
    ]

def test_database_connection_can_write(db_connection):
    db_connection.seed("seeds/makersbnb_tables.sql")
    db_connection.execute("INSERT INTO users (email, password) VALUES ('added@hotmail.com', 'addpass')")
    resultusers = db_connection.execute("SELECT * FROM users")
    assert resultusers == [
    {"id": 1, "email": "mrtester@gmail.com", "password": "GudPass91!"},
    {"id": 2, "email": "vlad@hotmail.com", "password": "Coolguy4"},
    {"id": 3, "email": "added@hotmail.com", "password": "addpass"}]