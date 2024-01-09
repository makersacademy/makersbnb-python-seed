from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_spaces(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/spaces")

    # We look at the <p> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(h1_tag).to_have_text("Maker'sBNB")