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

def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/session/new")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("Login page")

def test_get_new_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/new")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("Add a space")

def test_get_requests(page, test_web_address):
    page.goto(f"http://{test_web_address}/requests")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("Page for requests")

def test_get_space_by_id(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/1")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("Page for a specific space")

