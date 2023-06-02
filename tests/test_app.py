from playwright.sync_api import Page, expect

# # Tests for your routes go here

# """
# We can render the index page
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")

# def test_get_login_page(page, test_web_address):
#     page.goto(f'http://{test_web_address}/login')
#     expect(page.locator(".name-input")).to_have_text("Username:")
#     expect(page.locator(".password-input")).to_have_text("Password:")

# def test_login_logs_in_with_correct_pw(page, test_web_address):
#     page.goto(f'http://{test_web_address}') 
#     div_tag = page.locator('.logged-in-status')
#     page.goto(f'http://{test_web_address}/login') 
#     page.fill("input[name='username']", "User1")
#     page.fill("input[name='password']", "Password1")
#     page.click("text=Submit")
#     expect(div_tag).to_have_text('Logged in as User1')   

# def test_login_fails_with_incorrect_pw(page, test_web_address):
#     page.goto(f'http://{test_web_address}/login') 
#     div_tag = page.locator('.logged-in-status')
#     page.click("text=Submit")
#     expect(div_tag).to_have_text("Unable to authenticate")   


# def test_create_listing(db_connection, page, test_web_address):
#     # Navigate to the create listing page
#     db_connection.seed("seeds/makersbnb.sql")
#     page.goto(f'http://{test_web_address}')
#     page.click("text=Create Your Listing")
#     page.fill("input[name='name']", "New Listing")
#     page.fill("textarea[name='description']", "A description for the new listing")
#     page.fill("input[name='price']", "100")
#     # Submit the form
#     page.click("input[type='submit']")
#     # Assert that the listing was created and redirected to the listings page
#     page.goto(f'http://{test_web_address}')
#     listing_text = "New Listing: A description for the new listing, $100.00"
#     card_row = page.locator('.preview-section')
#     card_row_html = card_row.inner_text()
#     assert listing_text in card_row_html
#     expect(card_row.inner_text()).to_include(listing_text)

# def test_create_user(db_connection, page, test_web_address):
#     # Navigate to the create listing page
#     db_connection.seed("seeds/makersbnb.sql")
#     page.goto(f'http://{test_web_address}/signup')
#     page.fill("input[name='signup-username']", "donutlover")
#     page.fill("input[name='actualname']", "Homer Simpson")
#     page.fill("input[name='email']", "donuts@springfield.com")
#     page.fill("input[name='signup-password']", "doh")
#     page.screenshot(path="before_submit_form.png")
#     page.click('button:has-text("Sign up")')
#     # # # Submit the form
#     success_message = "You have successfully signed up, please log in"
#     page_content = page.locator('.sign-up-message')
#     expect(page_content).to_have_text(success_message)
    

    # signup_message = page.locator("xpath=/html/body/div[2]")
    # # assert signup_message
    # expect(signup_message).to_have_text("You have successfully signed up, please log in")  
    # Assert that the listing was created and redirected to the listings page
    # page.goto(f'http://{test_web_address}')
    # listing_text = "New Listing: A description for the new listing, $100.00"
    # card_row = page.locator('.preview-section')
    # card_row_html = card_row.inner_text()
    # assert listing_text in card_row_html
