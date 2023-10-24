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

def test_get_new_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/new-space")

    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Add a new space")


# TO DO - Once show page is created, can add the test below and ensure expected id match

# def test_create_space(page, test_web_address):
#     page.goto(f"http://{test_web_address}/")
#     page.fill("input[name='name']", "Beach house")
#     page.fill("input[name='description']", "Relaxing place")
#     page.fill("input[name='size']", "210")
#     page.fill("input[name='price']", "80")
#     page.click("text=Add space")

#     page.screenshot(path="screenshot.png", full_page=True)
#     print(page.content())

#     expect(page.locator("#name")).to_have_text("Beach house")
#     expect(page.locator("#description")).to_have_text("Relaxing place")
#     expect(page.locator("#size")).to_have_text("210")
#     expect(page.locator("#price")).to_have_text("80")