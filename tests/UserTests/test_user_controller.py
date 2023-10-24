def test_user_controller(web_client):
    post_response = web_client.post("/signup", data = {
        "username": "benhurst1234",
        "email": "benhurst@123.co.uk",
        "password": "12345678",
        "phonenumber": "01234567891"
    })
    assert post_response.status_code == 200
    assert post_response.data.decode('utf-8') == ""
    
    # get_response = web_client.get("/signup")
    # assert get_response.status_code == 200
    # assert get_response.data.decode('utf-8') == ""