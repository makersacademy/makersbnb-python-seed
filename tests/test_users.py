from lib.user_repository import UserRepository
from lib.user_class import User

"""
Call all users

"""
def test_add_a_user(db_connection): # See conftest.py to learn what `db_connection` is.
    db_connection.seed("seeds/MAKERSBNB.sql") # Seed our database
    userrepo = UserRepository(db_connection) 
    userrepo.create('John Smith','Username','pass','user@mail.com','07752738279')
    All_Users=userrepo.all()
    assert All_Users == [
        User('Naomi Bloggs','Silvakippy369','782993a','Macicman@hotmail.com','01214960879', 1),
        User('Beata Ekkebert','Tomantning1789','A4$N61s','hir_ufizaxe52@yahoo.com','07700900186', 2),
        User('Rohese Clarity','Vegetebuck360','j=95J6','duha-gudedo63@outlook.com','01154960210', 3),
        User('Adolfo Dalit','Draffbrot1708','yuZY020#','jamixi_fajo87@yahoo.com','07700900191', 4),
        User('Apolónia Caelius','Mentalves26','XRy#14H6','rofenen-eya82@aol.com','07700900625', 5),
        User('Basu Eugenijus','Ajje04Mome','v9Q/l3~2','pizuye-xini98@aol.com','01314960681', 6),
        User('Inna Avital','Jockoman10245','^%41h6zW','reda-pajaru16@gmail.com','07700900485', 7),
        User('Anouk Verissimus','Bicornlian166',';628MGo','dox_epefize62@mail.com','03069990479', 8),
        User('Filipa Jyoti','Tiradepi280','uF#L6$89','gisuta-damo55@hotmail.com','07700900200', 9),
        User('Silas Narmer','Vaultynius39','PLd969;W','tule_piceyi54@yahoo.com','07700900239', 10),
        User('Cornelio Rozenn','Jossja0104','Zq07O0X','yaloki_saro39@aol.com','01214978789', 11),
        User('John Smith','Username','pass','user@mail.com','07752738279', 12)
        ]
    
def test_find_by_id(db_connection):
    db_connection.seed('seeds/MAKERSBNB.sql')
    user_repo = UserRepository(db_connection)
    print('HERE')
    print(user_repo.find_by_id(1))

def test_get_bookings(db_connection):
    db_connection.seed('seeds/MAKERSBNB.sql')
    user_repo = UserRepository(db_connection)
    print(user_repo.show_bookings(False, 1))

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