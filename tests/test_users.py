from lib.user_repository import UserRepository
from lib.user_class import User

"""
Call all users

"""
def test_add_a_user(db_connection): # See conftest.py to learn what `db_connection` is.
    # db_connection.seed("seeds/seed.sql") # Seed our database
    userrepo = UserRepository(db_connection) 
    userrepo.create('Username','John Smith','pass','user@mail.com','07752738279')
    All_Users=userrepo.all()
    assert All_Users == ['User (username,John Smith,pass,user@mail.com.07752738279)']

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