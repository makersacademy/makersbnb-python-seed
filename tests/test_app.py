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
Render listings page
"""

def test_get_listings(page, test_web_address,db_connection):
    db_connection.seed("seeds/spaces.sql")
    # We load a virtual browser and navigate to the /listings page
    page.goto(f"http://{test_web_address}/listings")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the listings page."
    expect(strong_tag).to_have_text(["Apartment 1", "Apartment 2"])