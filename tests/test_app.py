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
"""
We can navigate to the spaces page
"""
def test_get_spaces_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")

    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Stay at any of these spaces.")
"""
The spaces page contains a list of spaces
"""