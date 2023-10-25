from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("Sign Up")

def test_get_spaces(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/spaces")

    # We look at the <p> tag
    heading = page.locator("h1")

    # We assert that it has the text "This is the homepage."
    expect(heading).to_have_text("Book a space")

def test_signup_user(db_connection, page, test_web_address):
    db_connection.seed('seeds/bnb.sql')
    page.goto(f"http://{test_web_address}/index")

    page.fill("input[name='username']", "testuser")
    page.fill("input[name='email']", "testuser@email.com")
    page.fill("input[name='password']", "testpassword")

    page.click("text=Sign Up")
