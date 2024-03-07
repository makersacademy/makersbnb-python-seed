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
    expect(strong_tag).to_have_text("This is the blueberries b&b homepage.")

"""
Test property information and booking page loads and has input fields with labels
"""

def test_get_property(page, test_web_address, db_connection):
    db_connection.seed("seeds/blueberries_bnb.sql")
    page.goto(f"http://{test_web_address}/properties/1")

    h1_tag = page.locator("h1")
    inputs = page.locator("input")
    labels = page.locator("label")
    button = page.get_by_role("button")

    expect(h1_tag).to_have_text("Burnaston Road")
    expect(inputs).to_have_count(3)
    expect(labels).to_have_count(2)
    expect(button).to_have_count(1)
