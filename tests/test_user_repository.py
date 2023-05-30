from lib.user_repository import *
from lib.user import User

"""
When we call BookRepository#all
We get a list of Book objects reflecting the seed data.
"""
def test_get_all_users(db_connection):
    db_connection.seed("seeds/makersbnb.sql") # Seed our database with some test data
    repository = UserRepository(db_connection) # Create a new UserRepository

    users = repository.all() # Get all users

    # Assert on the results
    assert users == [
        User(1, "User1", "Actual Name 1", "Password1", "user1@email.com"),
        User(2, "User2", "Actual Name 2", "Password2", "user2@email.com"),
        User(3, "User3", "Actual Name 3", "Password3", "user3@email.com"),
    ]

def test_create_user(db_connection):
    db_connection.seed("seeds/makersbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "User4", "Actual Name 4", "Password4", "user4@email.com"))

    result = repository.all()
    assert result == [
        User(1, "User1", "Actual Name 1", "Password1", "user1@email.com"),
        User(2, "User2", "Actual Name 2", "Password2", "user2@email.com"),
        User(3, "User3", "Actual Name 3", "Password3", "user3@email.com"),
        User(4, "User4", "Actual Name 4", "Password4", "user4@email.com"),
    ]
# """
# When we call BookRepository#find
# We get a single Book object reflecting the seed data.
# """
# def test_get_single_record(db_connection):
#     db_connection.seed("seeds/book_store.sql")
#     repository = BookRepository(db_connection)

#     book = repository.find(3)
#     assert book == Book(3, "Bluets", "Maggie Nelson")

# """
# When we call BookRepository#create
# We get a new record in the database.
# """
# def test_create_record(db_connection):
#     db_connection.seed("seeds/book_store.sql")
#     repository = BookRepository(db_connection)

#     repository.create(Book(None, "The Great Gatsby", "F. Scott Fitzgerald"))

#     result = repository.all()
#     assert result == [
#         Book(1, "Invisible Cities", "Italo Calvino"),
#         Book(2, "The Man Who Was Thursday", "GK Chesterton"),
#         Book(3, "Bluets", "Maggie Nelson"),
#         Book(4, "No Place on Earth", "Christa Wolf"),
#         Book(5, "Nevada", "Imogen Binnie"),
#         Book(6, "The Great Gatsby", "F. Scott Fitzgerald"),
#     ]

# """
# When we call BookRepository#delete
# We remove a record from the database.
# """
# def test_delete_record(db_connection):
#     db_connection.seed("seeds/book_store.sql")
#     repository = BookRepository(db_connection)
#     repository.delete(3) # Apologies to Maggie Nelson fans

#     result = repository.all()
#     assert result == [
#         Book(1, "Invisible Cities", "Italo Calvino"),
#         Book(2, "The Man Who Was Thursday", "GK Chesterton"),
#         Book(4, "No Place on Earth", "Christa Wolf"),
#         Book(5, "Nevada", "Imogen Binnie"),
#     ]
