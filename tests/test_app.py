from playwright.sync_api import Page, expect
from lib.user.user_repository import UserRepository

# Tests for your routes go here

"""
We can render the index page
"""


def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <h2> tag
    h2_tag = page.locator("h2")

    # We assert that it has the text "Sign up to Makers BnB"
    expect(h2_tag).to_have_text("Sign up to Makers BnB")


def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")

    h2_tag = page.locator("h2")

    expect(h2_tag).to_have_text("Log in to Makers BnB")


# """
# When: I make a POST request to /index
# And: I send a username, email, phone number, password and password confirmation as body parameters
# Then: I should get a 200 response and flask sets variable based on the input
# """

# def test_post_index(page, test_web_address):

#     page.goto(f'http://{test_web_address}/index')

#     page.fill('input[name="username"]', 'Username1')
#     page.fill('input[name="email"]', 'boberty@gmail.com')
#     page.fill('input[name="phone"]', '8675309')
#     page.fill('input[name="password"]', 'password2.')
#     page.fill('input[name="password_confirm"]', 'password2.')

#     page.click("text='Sign Up'")

"""
When a user fills out the form on the index page
a user is created in the database
"""


def test_integrated_sign_up(db_connection, page, test_web_address):
    db_connection.seed("seeds/usertable_connection.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill('input[name="username"]', "Username1")
    page.fill('input[name="email"]', "boberty@gmail.com")
    page.fill('input[name="phonenumber"]', "8675309")
    page.fill('input[name="password"]', "password2.")
    page.fill('input[name="password_confirm"]', "password2.")
    page.click("input[name='signup']")
    repo = UserRepository(db_connection)
    row = repo.check("Username1")
    assert row[0]["username"] == "Username1"
