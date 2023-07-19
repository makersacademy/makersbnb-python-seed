from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    h1_tag = page.locator("h1")
    h2_tag = page.locator("h2")
    anchor_tag = page.locator("a")

    expect(h2_tag).to_have_text("Log in")
    expect(anchor_tag).to_have_text("Sign up")
    expect(h1_tag).to_have_text("Makers BnB")
"""
We can render the sign up page
"""
def test_get_signup(page, test_web_address):
    page.goto(f"http://{test_web_address}/sign-up")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Sign up")

"""
We can render the listings page
"""
def test_get_listings(page, test_web_address):
    page.goto(f"http://{test_web_address}/listings")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Listings")



"""
An existing user can log in with their correct email and password
and be redirected to the /listings page
"""
def test_existing_user_log_in(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "asha@example.com")
    page.fill("input[name='password']", "password1")
    page.get_by_role("button").click()
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Listings")

"""
A user without an account gets an error message when they try to log in
"""
def test_non_user_log_in_error(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.fill("input[name='email']", "notreal@example.com")
    page.fill("input[name='password']", "p@ssword")
    page.get_by_role("button").click()
    error_element = page.locator(".login-error")
    expect(error_element).to_have_text("User does not exist")

"""
When a user clicks the Sign up button they are redirected to /sign-up
"""
def test_sign_up_button_redirects(page, test_web_address, db_connection):
    db_connection.seed("seeds/makers_bnb_database.sql")
    page.goto(f"http://{test_web_address}/index")
    page.click("text=Sign up")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Sign up")
