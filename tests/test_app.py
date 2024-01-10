from playwright.sync_api import Page, expect, sync_playwright
from app import is_valid
import time

# Tests for your routes go here


# We can render the index page
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    strong_tag = page.locator("h1")
    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("Signup to MakersBnB")


# We can render the login page
def test_login_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    expect(page.locator("p")).to_have_text("Log in to MakersBnB")


# test password is valid
def test_password_is_valid():
    password = "passw0rd!"
    assert is_valid(password) == True
    password2 = "incorrect"
    assert is_valid(password2) == False
