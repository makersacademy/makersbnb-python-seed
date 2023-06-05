from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the home page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /home page
    page.goto(f"http://{test_web_address}/home")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "Welcome to MakersBNB"
    expect(strong_tag).to_have_text("Welcome to MakersBNB")