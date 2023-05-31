from playwright.sync_api import Page, expect

"""
We can render the index page
We can see all listings
"""
def test_get_homepage(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    page.screenshot(path='screenshot.png')
    title = page.locator(".t-title")
    expect(title).to_have_text("MakersBnB")
    first_listing_name = page.locator("#t-listing-name-1")
    expect(first_listing_name).to_have_text("name")
    
'''
Test that the login page has input boxes and correct header
'''
def test_login_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    login_box = page.locator("input[name='login']")
    expect(login_box)
    password_box = page.locator("input[name='password']")
    expect(password_box)
    header = page.locator("h1")
    expect(header).to_have_text("Sign Up")