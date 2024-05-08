from playwright.sync_api import Page, expect, sync_playwright

# Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     p_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(p_tag).to_have_text("This is the homepage.")

def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    # Check if the page contains the expected text
    page.fill("input[name='email']",'test1@gmail.com')
    page.fill("input[name='password']",'password123')
    page.click("text='Login'")
    login_text = page.locator("h1")
    expect(login_text).to_have_text("Hello, test1@gmail.com! You are logged in.")
    
    

