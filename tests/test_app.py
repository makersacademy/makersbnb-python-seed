from playwright.sync_api import Page, expect
import pytest
from lib.user import User, UserRepo


# Tests for your routes go here

"""
We can render the index page
"""

def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    heading_1 = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(heading_1).to_have_text("Space BnB")


def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")

    heading_3 = page.locator("h3")

    expect(heading_3).to_have_text("Log in to SpaceBnB")