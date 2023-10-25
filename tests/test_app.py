from playwright.sync_api import Page, expect

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("This is the homepage.")
    

def test_get_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/1")
    strong_tag = page.locator(".space_page > h1")
    expect(strong_tag).to_have_text("Beach House")