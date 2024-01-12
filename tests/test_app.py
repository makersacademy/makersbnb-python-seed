from playwright.sync_api import Page, expect
import pytest
from lib.user import User, UserRepo
from lib.space import Space
from lib.space_repository import SpaceRepository


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

# def test_create_new_space(page, test_web_address):
#     page.goto(f"http://{test_web_address}/")
#     page.fill("input[name='username']", "bob")
#     page.fill("input[name='email']", "bob@bob.com")
#     page.fill("input[name='password']", "bob")
#     page.fill("input[name='password-confirmation']", "bob")
#     page.click("input[name='signup']")
#     page.screenshot(path="screenshot.png", full_page = True)
#     page.click("text=List a space")
#     page.fill("input[name='space_name']", "new space")
#     page.fill("textarea[name='description']", "this is a new space")
#     page.fill("input[name='price']", "100")
#     page.fill("input[name='start_date']", "2025-01-01")
#     page.fill("input[name='end_date']", "2025-01-02")
#     page.click("input[name='list-space']")
#     page.screenshot(path="screenshot1.png", full_page = True)
    
    # CONFIRMED IT WORKS ON TABLE PLUS. NO MORE TIME ON THIS TEST!

#     # page.goto(f"http://{test_web_address}/new_space")

#     # page.get_by_role("textbox").fill("Peter")

