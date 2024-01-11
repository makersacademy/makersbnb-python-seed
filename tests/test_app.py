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

    expect(strong_tag).to_have_text("Welcome to MakersBnB.")
    
def test_mainpage_redirects_to_spaces(page,test_web_address):
    page.goto(f'http://{test_web_address}/')
    h1_tag = page.locator('h1')
    expect(h1_tag).to_have_text('Space Listings')
"""
We can render the login page
"""

def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/log_in")
    
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Please log in.")


def test_get_add_spaces(page, test_web_address,db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/index")
    
    # Then we fill out the field with the name attribute 'email'
    page.fill("input[name='email']", "test_user@mail.com")
    
    # And the field with the name attribute 'passw'
    page.fill("input[name='passw']", "testpassword123")

    page.fill("input[name='passw_conf']", "testpassword123")
    
    page.click("text=Submit")
    
    page.click('text=List new space')
    page.screenshot(path="screenshot.png", full_page=True)
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Create new listing")

def test_list_spaces(page,test_web_address,db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/spaces")
    h3_tag = page.locator('h3')
    expect(h3_tag).to_have_count(5)
    
def test_adding_a_space(page,test_web_address,db_connection):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/index")
    # Then we fill out the field with the name attribute 'email'
    page.fill("input[name='email']", "test_user@mail.com")
    # And the field with the name attribute 'passw'
    page.fill("input[name='passw']", "testpassword123")
    page.fill("input[name='passw_conf']", "testpassword123")
    page.click("text=Submit")
    page.click('text=List new space')
    page.fill('input[name=title]','Test Title6')
    page.fill('input[name=space_desc]','This is some description')
    page.fill('input[name=price]','1.234')
    page.fill('input[name=startdate]','2024-01-17')
    page.fill('input[name=enddate]','2024-01-31')
    page.click('text=Submit')
    page.click('text=Spaces')
    h3_tag = page.locator('h3')
    expect(h3_tag).to_have_count(6)

def test_create_user(db_connection, page, test_web_address):
    db_connection.seed("seeds/MasterTest.sql")
    page.goto(f"http://{test_web_address}/index")
    
    # Then we fill out the field with the name attribute 'email'
    page.fill("input[name='email']", "test_user@mail.com")
    
    # And the field with the name attribute 'passw'
    page.fill("input[name='passw']", "testpassword123")

    page.fill("input[name='passw_conf']", "testpassword123")
    
    page.click("text=Submit")
    
    strong_tag = page.locator("h1")
    expect(strong_tag).to_have_text("Space Listings")
    