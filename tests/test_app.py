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

def test_get_all_spaces(db_connection, page, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/users_spaces.sql")
    page.goto(f"http://{test_web_address}/")
    space_title_tag = page.locator(".space-title")
    # date_tag = page.locator(".date")
    #====todo=====
    #comments in this file are for next implementation with displaying date

    expect(space_title_tag).to_have_text(["test_title", "test_title2"])
    # expect(date_tag).to_have_text(["['2023-01-08', '2023-01-09']", "['2023-02-12', '2023-02-13']"])

def test_show_booking_page(db_connection, page, test_web_address):
    db_connection.seed("seeds/users_spaces.sql")
    page.goto(f"http://{test_web_address}/")
    
    page.click("text='test_title'")
    
    title_tag = page.locator(".space-title")
    expect(title_tag).to_have_text("test_title")

    pick_tag = page.locator(".dropbtn")
    expect(pick_tag).to_have_text("Pick a night")

    book_button_tag = page.locator(".book")
    expect(book_button_tag).to_have_text("Request to book")

def test_show_create_page(db_connection, page, test_web_address):
    page.set_default_timeout(1000)
    db_connection.seed("seeds/users_spaces.sql")
    page.goto(f"http://{test_web_address}/new-space")
    page.fill("input[name=email]", "test@gmail.com")
    page.fill("input[name=password]", "test123")
    page.click("text='Log-in'")
    page.click("text='Create new space'")
    page.fill("input[name=title]", "London")
    page.fill("input[name=description]", "A nice hotel")
    page.fill("input[name=price]", "$75")


    title_tag = page.locator(".space-title")
    expect(title_tag).to_have_text("Title:")

    description_tag = page.locator(".space-description")
    expect(description_tag).to_have_text("Description:")

    price_tag = page.locator(".space-price")
    expect(price_tag).to_have_text("Price:")

    page.click("text='Add Space'")


