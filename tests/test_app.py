from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."

    expect(strong_tag).to_have_text("Welcome to MakersBnB.")
    

"""
We can render the login page
"""

def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/log_in")
    
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Please log in.")


def test_get_add_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/newspace")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("This is for adding spaces.")

