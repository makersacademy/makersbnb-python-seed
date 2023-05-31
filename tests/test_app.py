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

# def test_get_login_page(page, test_web_address):
#     page.goto(f'http://{test_web_address}/login')
#     expect(page.locator(".name-input")).to_have_text("Username:")
#     expect(page.locator(".password-input")).to_have_text("Password:")

# def test_login_logs_in_with_correct_pw(page, test_web_address):
#     page.goto(f'http://{test_web_address}/login') 
#     div_tag = page.locator('div')
#     page.fill("input[name='username']", "DynamicDante")
#     page.fill("input[name='password']", "spell456")
#     page.click("text=Submit")
#     expect(div_tag).to_have_text('You have logged in, welcome DynamicDante')   

# def test_login_fails_with_incorrect_pw(page, test_web_address):
#     page.goto(f'http://{test_web_address}/login') 
#     div_tag = page.locator('div')
#     page.click("text=Submit")
#     expect(div_tag).to_have_text('I was unable to authenticate your login details.')   
    