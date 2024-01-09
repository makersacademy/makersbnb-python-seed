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

def test_get_logged_in_homepage(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/adminlogin")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("Logged in homepage")

def test_get_login_page(page, test_web_address):
    # We load a virtual browser and navigate to the /login2 page
    page.goto(f"http://{test_web_address}/login")

    # We look at the <h1> tag
    strong_tag = page.locator("h1")

    # We assert that it has the text "Log In"
    expect(strong_tag).to_have_text("Log In")


def test_login_redirect_when_submit_clicked(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name = 'name']", "Test Name")
    page.fill("input[name = 'email']", "Test Email")
    page.fill("input[name = 'password']", "TestPassword")
    page.click("text=submit")

    strong_tag = page.locator("h1")

    expect(strong_tag).to_have_text("Log In")
        
def test_login_redirect_when_hyperlink_clicked(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    page.click("text=Log In")

    strong_tag = page.locator("h1")

    expect(strong_tag).to_have_text("Log In")

def test_get_loggedin_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name = 'email']", "Test Email")
    page.fill("input[name = 'password']", "TestPassword")
    page.click("text=submit")

    strong_tag = page.locator("p")

    expect(strong_tag).to_have_text("Logged in homepage")

def test_get_book_space(page, test_web_address):
    #Sign Up
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name = 'name']", "Test Name")
    page.fill("input[name = 'email']", "Test Email")
    page.fill("input[name = 'password']", "TestPassword")
    #Submit New User
    page.click("text=submit")

    #Sign In
    page.fill("input[name = 'email']", "Test Email")
    page.fill("input[name = 'password']", "TestPassword")
    #Submit Details
    page.click("text=submit")

    #Click on book spaces
    page.click("text=Book a space")

    strong_tag = page.locator("h1")

    expect(strong_tag).to_have_text("Book your space")

def test_get_requests(page, test_web_address):
    #Sign Up
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name = 'name']", "Test Name")
    page.fill("input[name = 'email']", "Test Email")
    page.fill("input[name = 'password']", "TestPassword")
    #Submit New User
    page.click("text=submit")

    #Sign In
    page.fill("input[name = 'email']", "Test Email")
    page.fill("input[name = 'password']", "TestPassword")
    #Submit Details
    page.click("text=submit")

    #Click on book spaces
    page.click("text=View requests")

    strong_tag = page.locator("h1")

    expect(strong_tag).to_have_text("Requests")