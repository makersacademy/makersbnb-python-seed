from lib.user import User
from lib.userRepository import UserRepository

# USER TESTS

def test_user_constructs():
    user = User(1, "testFirstName","testLastName", "testEmail", "testPassword")
    assert str(user) == "User(1, testFirstName, testLastName, testEmail, testPassword)"

def test_user_validity():
    assert User(1, "","", "", "").is_valid() == False
    assert User(1, "Aisha","Hasan", "aisha.com", "hello12345").is_valid() == False
    assert User(1, "Aisha","Hasan", "aisha@gmail", "hello12345").is_valid() == False
    assert User(1, "Aisha","Hasan", "aisha@gmail.com", "hello12").is_valid() == False
    assert User(1, "Aisha","Hasan","aisha@gmail.com", "hellooooooo").is_valid() == False
    assert User(1, "Aisha", "Hasan","aisha@gmail.com", "helloooo12").is_valid() == True

def test_user_errors():
    assert User(1, "Aisha","Hasan", "aisha.com", "hello12345").generate_errors() == "Invalid email"
    assert User(1, "", "", "", "").generate_errors() == "Name cannot be blank, Invalid email, Password has to be atleast 8 characters and contain atleast 1 number"
    assert User(1, "Aisha","Hasan", "aisha@gmail.com", "hello12").generate_errors() == "Password has to be atleast 8 characters and contain atleast 1 number"
    assert User(1, "Aisha","Hasan", "aisha@gmail.com", "helloooo12").generate_errors() == None



# USER REPOSITORY TESTS

def test_get_all_users(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = UserRepository(db_connection)

    users = repository.all()

    assert users == [
        User(1,'Leonardo', 'Leonardopoulos', 'leonar364@net.com','pug3&'),
        User(2, 'Donatello', 'Donatellis', 'donat5784@post.com', 'don9876&'),
        User(3, 'Michelangelo', 'Michelangelou', 'mich937@lst.gr','Poodlehd3&'),
        User(4, 'Raphael', 'Raphaelidis', 'raph086@pet.com', 'shitsugewv9%')
    ]

def test_get_single_user(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = UserRepository(db_connection)

    user = repository.find(1)

    assert user == User(1, 'Leonardo', 'Leonardopoulos', 'leonar364@net.com','pug3&')

def test_create_user(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = UserRepository(db_connection)

    repository.create(User(None, "Laiba","Ali", "laiba@gmail.com", "laiba1234"))
    
    result = repository.all()
    assert result == [
        User(1,'Leonardo', 'Leonardopoulos', 'leonar364@net.com','pug3&'),
        User(2, 'Donatello', 'Donatellis', 'donat5784@post.com', 'don9876&'),
        User(3, 'Michelangelo', 'Michelangelou', 'mich937@lst.gr','Poodlehd3&'),
        User(4, 'Raphael', 'Raphaelidis', 'raph086@pet.com', 'shitsugewv9%'),
        User(5, 'Laiba', 'Ali', 'laiba@gmail.com', 'laiba1234')
    ]

def test_delete_user(db_connection):
    db_connection.seed("seeds/airbnb.sql")
    repository = UserRepository(db_connection)

    repository.delete(3)

    result = repository.all()

    assert result == [
        User(1,'Leonardo', 'Leonardopoulos', 'leonar364@net.com','pug3&'),
        User(2, 'Donatello', 'Donatellis', 'donat5784@post.com', 'don9876&'),
        User(4, 'Raphael', 'Raphaelidis', 'raph086@pet.com', 'shitsugewv9%')
    ]