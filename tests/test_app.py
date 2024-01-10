from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_spaces(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/spaces")

    # We look at the <p> tag
    h1_tag = page.locator("h1")

    # We assert that it has the text "This is the homepage."

    expect(h1_tag).to_have_text("Maker'sBNB")


"""def test_signup_successful(page, test_web_address):
    page.goto(f"http://{test_web_address}/signup")
    # Fill out the signup form
    page.fill('input[name="first_name"]', 'John')
    page.fill('input[name="last_name"]', 'Doe')
    page.fill('input[name="email"]', 'john.doe@example.com')
    page.fill('input[name="telephone_number"]', '1234567890')
    page.fill('input[name="password"]', 'testpassword')
        # Click the "Sign Up" button
    page.click("input[type='submit']")
        # Wait for an element indicating successful signup
    success_message = page.locator('body:has-text("Sign-up successful!")')
        # Assert that the success message is visible
    assert success_message.is_visible()



def test_email_exists(page, test_web_address):
    user = {
        'user_id': 3,
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'john.doe@example.com',
        'phone_number': '123456',
        'password': 'password',
    }
    page.goto(f"http://{test_web_address}/signup")
    page.fill('input[name="first_name"]', 'John')
    page.fill('input[name="last_name"]', 'Doe')
    page.fill('input[name="email"]', 'john.doe@example.com')
    page.fill('input[name="telephone_number"]', '1234567890')
    page.fill('input[name="password"]', 'testpassword')
    page.click("input[type='submit']")
    fail_message = page.locator('body:has-text("Email already exists. Please use a different Email.")')
    assert fail_message"""

def test_post_login(page, test_web_address):
    user = {
        'user_id': 3,
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'john.doe@example.com',
        'phone_number': '123456',
        'password': 'password',
    }
    page.goto(f"http://{test_web_address}/login")
    page.fill('input[name="email"]', 'john.doe@example.com')
    page.fill('input[name="password"]', 'password')
    page.click("button[type='submit']")
    assert page.goto(f"http://{test_web_address}/index")

def test_login_fail(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    page.fill('input[name="email"]', 'john.doe@example.com')
    page.fill('input[name="password"]', 'password')
    page.click("button[type='submit']")
    error_message = page.locator("h2")
    expect(error_message).to_have_text('No account has been made with this email. Please sign up.')


def test_wrong_password(page, test_web_address):
    user = {
        'user_id': 3,
        'first_name': 'first_name',
        'last_name': 'last_name',
        'email': 'email1@email.com',
        'phone_number': '123456',
        'password': 'password',
    }
    page.goto(f"http://{test_web_address}/login")
    page.fill('input[name="email"]', 'email1@email.com')
    page.fill('input[name="password"]', 'wrongpassword')
    page.click("button[type='submit']")
    error_message_tag = page.locator("h2")
    expect(error_message_tag).to_have_text("Incorrect password.")

def test_get_spaces(db_connection, page, test_web_address):
    db_connection.seed('seeds/makers_bnb.sql')
    page.goto(f'http://{test_web_address}/spaces')
    div_tags = page.locator('.t-property')
    expect(div_tags).to_have_text([
        '\nBeach House 1\n Description: A beautiful beach side property with a pool \n Price per night: £101\n',
        '\nBeach House 2\n Description: A beautiful beach side property with a pool \n Price per night: £102\n',
        '\nGlamping Pod 1\n Description: A glamping pod with all cooking facilities \n Price per night: £103\n',
        '\nGlamping Pod 2\n Description: A glamping pod with all cooking facilities \n Price per night: £104\n',
        '\nCountry escape 1\n Description: A luxury cottage in the middle of the countryside \n Price per night: £105\n',
        '\nCountry escape 2\n Description: A luxury cottage in the middle of the countryside \n Price per night: £106\n',
    ])

def test_create_space(db_connection, page, test_web_address):
    db_connection.seed('seeds/makers_bnb.sql')
    page.goto(f'http://{test_web_address}/spaces')
    page.click('text=Add New Space')
    page.fill("input[name='userID']",'1')
    page.fill("input[name='name']",'house')
    page.get_by_label("description").fill("a house")
    page.fill("input[name='pricepernight']",'110')
    page.fill("input[name='availablefrom']",'2024-01-29')
    page.fill("input[name='availableto']",'2024-01-30')
    page.click('text=Submit')
    div_tags = page.locator('.t-property')
    expect(div_tags).to_have_text([
        '\nBeach House 1\n Description: A beautiful beach side property with a pool \n Price per night: £101\n',
        '\nBeach House 2\n Description: A beautiful beach side property with a pool \n Price per night: £102\n',
        '\nGlamping Pod 1\n Description: A glamping pod with all cooking facilities \n Price per night: £103\n',
        '\nGlamping Pod 2\n Description: A glamping pod with all cooking facilities \n Price per night: £104\n',
        '\nCountry escape 1\n Description: A luxury cottage in the middle of the countryside \n Price per night: £105\n',
        '\nCountry escape 2\n Description: A luxury cottage in the middle of the countryside \n Price per night: £106\n',
        '\nhouse \n Description: a house\n Price per night: £110'
    ])

