from playwright.sync_api import Page, expect

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


def test_login_path(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    # button = page.locator("a")
    # expect(button).to_have_url("This is a button")
    expect(page).to_have_url("http://localhost:4709/login")
  
"""
test web page has a login form
"""
def test_web_page_has_a_login_form(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    button = page.locator("button")
    expect(button).to_have_text("Button")

"""
test web page has a register form
"""

"""
test web page has a logout button
"""

"""
test web page has a logout button
"""

