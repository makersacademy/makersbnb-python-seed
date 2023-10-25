from lib.User.user_repository import UserRepository
from lib.User.user import User

def test_signup_page(web_client):
    response = web_client.get('/index')
    assert response.status_code == 200

def test_user_signup_integration(db_connection, web_client):

    json_data = {
        "username": "benhurst1234",
        "email": "benhurst@123.co.uk",
        "password": "12345678",
        "phonenumber": "01234567891"
    }

    post_response = web_client.post("/signuptwo", data = json_data)


    db_connection.seed("seeds/usertable_connection.sql")
    repository = UserRepository(db_connection)
    assert repository.check('benhurst1234') == True
    


def test_user_controller(web_client):
    json_data = {
        "username": "benhurst1234",
        "email": "benhurst@123.co.uk",
        "password": "12345678",
        "phonenumber": "01234567891"
    }

    post_response = web_client.post("/signuptwo", data = json_data)
    
    assert post_response == json_data