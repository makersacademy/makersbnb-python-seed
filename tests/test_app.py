from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


"""
We can render the login page
"""
def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    h1 = page.locator("h1")
    expect(h1).to_have_text("This is login")


"""
We can render sign up page
"""
def test_get_sign_up(page, test_web_address):
    page.goto(f"http://{test_web_address}/sign_up")
    h1 = page.locator("h1")
    expect(h1).to_have_text("This is sign up")

"""
We can render spaces page
"""
def test_get_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    h1 = page.locator('h1')
    expect(h1).to_have_text("SPACES")

"""
We can check if a username exists 
"""

def test_user_exists(page, web_client):
    page.seeds("seeds/users.sql") # need updated database_connection.sql
    response_post = web_client.post("/sign_up", data={
        'name': 'user1',
        'email': 'user1@example.com',
        'password': 'abc123'
    })
    assert response_post.status_code == 409
    assert response_post.data.decode('utf-8') == "This user is already registered"



"""
Check if sign up was successful
"""

def test_sign_up_successful(web_client):
    response = web_client.post("/sign_")




def test_post_album(db_connection, web_client):
    db_connection.seed("seeds/record_store.sql")
    response_post = web_client.post("/albums", data={
        'title': "Voyage",
        'release_year': '2022',
        'artist_id': '2'
    })
    assert response_post.status_code == 200
    assert response_post.data.decode('utf-8') == ""

    response_get = web_client.get('/albums')
    assert response_get.status_code == 200
    assert response_get.data.decode('utf-8') == "" \
        "Album(1, PartyTime, 2003, 1)\n" \
        "Album(2, Voyage, 2022, 2)"


"""
Check if email/password is missing data
"""

