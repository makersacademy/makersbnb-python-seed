from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository
from lib.user import User

# Tests for your routes go here

"""
We can render the index page
"""


def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


def test_create_new_user(db_connection):
    db_connection.seed("makersbnb.sql")
    repository = UserRepository(db_connection)
    user = User(None, "Lola Li", "lola@lola.com", "password456")
    assert repository.create(user) is None
    assert repository.all() == [
        User(1, 'Liza L',  'liza@liza.com', 'password123'),
        User(1, 'Lola Li',  'lola@lola.com', 'password456')
    ]


def test_all(db_connection):
    db_connection.seed("makersbnb.sql")
    repository = UserRepository(db_connection)
    result = repository.all()
    assert result == [
        User(1, 'Liza L',  'liza@liza.com', 'password123'),
        User(1, 'Lola Li',  'lola@lola.com', 'password456')
    ]


# def test_booking(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/make_a_booking")

#     strong_tag = page.locator("p")

#     expect(strong_tag).to_have_text("This is the homepage.")
