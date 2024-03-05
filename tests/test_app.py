from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the / page
    page.goto(f"http://{test_web_address}")

    # We look at the <p> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "Makers BnB"
    expect(h1_tag).to_have_text("Makers BnB")

"""
We can render the places page
"""
def test_get_places(page, test_web_address):
    # We load a virtual browser and navigate to the /places page
    page.goto(f"http://{test_web_address}/places")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "Book a Place"
    expect(h1_tag).to_have_text("Book a Place")

"""
We can render the new place page
"""
def test_get_add_new_place(page, test_web_address):
    # We load a virtual browser and navigate to the /places page
    page.goto(f"http://{test_web_address}/places/new")

    # We look at the <h1> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "List a new Place"
    expect(h1_tag).to_have_text("List a new Place")

""" we can render the login page """

def test_get_login(page, test_web_address):
    # we go to the correct page within a virtual browser
    page.goto(f"http://{test_web_address}/login")

    # We check the <h1> tag on that page
    h1_tag = page.locator("h1")

    # we assert that we expect it to say "login"
    expect(h1_tag).to_have_text("Login")

"""We have username and password headers"""

def test_input_user_pass(page, test_web_address):
    # we go to the login page
    page.goto(f"http://{test_web_address}/login")

    # we check the label headers 
    label_tags = page.locator("label")

    # we asser that we expect it to say username and password
    expect(label_tags).to_have_text(["Username", "Password"])

"""Tests the login button redirects us to the main index page"""

def test_when_we_click_login_button(page, test_web_address):
    # we go to login page
    page.goto(f"http://{test_web_address}/login")

    # we click the button
    page.click("text='Login'")

    # we check new headers and assert we have been redirected
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Makers BnB")