from playwright.sync_api import Page, expect

# End to End Testing:
"""
We can render the index page
We can see all listings
"""
def test_get_homepage(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")
    # We look at the <p> tag
    title = page.locator(".t-title")
    # We assert that it has the text "This is the homepage."
    expect(title).to_have_text("MakersBnB")
    first_listing_name = page.locator(".t-listing-name-1")
    expect(first_listing_name).to_have_text("name")
    
'''
Test that the login page has input boxes and correct header
'''
def test_login_page(page, test_web_address):
    # Load a virtual browser and navigate to the login page
    page.goto(f"http://{test_web_address}/signup")
    # Check for the presence of the login box
    login_box = page.locator("input[name='login']")
    expect(login_box)
    # Check for the presence of the password box
    password_box = page.locator("input[name='password']")
    expect(password_box)
    # Check for the presence of the header "Sign Up"
    header = page.locator("h1")
    expect(header).to_have_text("Sign Up")