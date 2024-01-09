from playwright.sync_api import Page, expect
import pytest
from lib.user import User, UserRepo


# Tests for your routes go here

"""
We can render the index page
"""

@pytest.mark.skip(reason ="Skipped as not part of our testing Neil+Joe")
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")
    
def test_for_signup(page, test_web_address, db_connection):
    pass
