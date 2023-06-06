from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the home page
"""
def test_get_home(page, test_web_address):
    # We load a virtual browser and navigate to the /home page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    title_tag = page.locator(".t-title")

    # We assert that it has the text "Welcome to MakersBNB"
    expect(title_tag).to_have_text("Welcome to MakersBNB")



def test_signup(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/")
    page.click("text='Sign-up'")
    page.fill("input[name=first_name]", "Test First Name")
    page.fill("input[name=last_name]", "Test Last Name")
    page.fill("input[name=email]", "Test Email")
    page.fill("input[name=password]", "1234")
    page.click("text='Sign up'")

def test_login(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/")
    page.click("text='Log-in'")
    page.fill("input[name=email]", "Test Email")
    page.fill("input[name=password]", "1234")
    page.click("text='Log-in'")
    
def test_homepage_link(page, test_web_address):
    page.set_default_timeout(1000)
    page.goto(f"http://{test_web_address}/signup")
    page.click("text='Back to Homepage'")

"""
"""

def test_get_all_spaces(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_spaces.sql")
    page.goto(f"http://{test_web_address}/")
    space_item = page.locator(".space-item")

    expect(space_item).to_have_text([
        'test_title, test_description, $50.00, 2023-01-08',
        'test_title2, test_description2, $60.00, 2023-05-10'
    ])
