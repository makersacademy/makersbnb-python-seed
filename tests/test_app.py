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