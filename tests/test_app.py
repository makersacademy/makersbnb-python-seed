from playwright.sync_api import Page, expect


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
    

def test_get_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/1")
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Test space")