from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository
from lib.user import *

# Tests for your routes go here

def test_create_user(page, test_web_address,db_connection):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/scar_bnb.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name=username]", "Test User")
    page.fill("input[name=email]", "testemail@test.com")
    page.fill("input[name=user_password]", "testpassword")
    page.click("text=Sign Up")
    # will test user details are displayed when redirected to next page

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")