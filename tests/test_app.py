from playwright.sync_api import Page, expect
import time
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

# def test_signup(page, test_web_address):
#     page.goto(f"http://{test_web_address}/signup")

    

#     page.fill("input[name='firstName']", "testName")
#     page.fill("input[name='lastName']", "testLastName")
#     page.fill("input[name='email']", "test1111@gmail.com")
#     page.fill("input[name='password']", "testing123")

#     page.click("input[type='submit'][value='Create Account']")

#     login_element = page.locator('h1')
#     expect(login_element).to_have_text('Login')

# def test_signup_with_errors(page, test_web_address):
#     page.goto(f"http://{test_web_address}/signup")

#     page.fill("input[name='firstName']", "")
#     page.fill("input[name='lastName']", "testLastName")
#     page.fill("input[name='email']", "test@gmailcom")
#     page.fill("input[name='password']", "testing")

#     page.click("input[type='submit'][value='Create Account']")
    
#     list_errors = page.locator(".t-errors")

#     expect(list_errors).to_have_text(
#         "There were errors in your submission! Name cannot be blank, Invalid email, Password has to be atleast 8 character and contain atleast 1 number"
#         )