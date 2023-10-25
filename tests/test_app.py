from playwright.sync_api import Page, expect

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    page.goto(f"http://{test_web_address}/")
    strong_tag = page.locator("p")
    expect(strong_tag).to_have_text("This is the homepage.")

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

def test_get_new_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/new-space")

    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Add a new space")


# TO DO - Once show page is created, can add the test below and ensure expected id match

# def test_create_space(page, test_web_address):
#     page.goto(f"http://{test_web_address}/")
#     page.fill("input[name='name']", "Beach house")
#     page.fill("input[name='description']", "Relaxing place")
#     page.fill("input[name='size']", "210")
#     page.fill("input[name='price']", "80")
#     page.click("text=Add space")

#     page.screenshot(path="screenshot.png", full_page=True)
#     print(page.content())

#     expect(page.locator("#name")).to_have_text("Beach house")
#     expect(page.locator("#description")).to_have_text("Relaxing place")
#     expect(page.locator("#size")).to_have_text("210")
#     expect(page.locator("#price")).to_have_text("80")
def test_get_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces/1")
    strong_tag = page.locator(".space_page > h1")
    expect(strong_tag).to_have_text("Beach House")
