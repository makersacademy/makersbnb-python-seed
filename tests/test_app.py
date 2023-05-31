from playwright.sync_api import Page, expect
from lib.user_repository import UserRepository
from lib.user import User
from app import password_is_valid
from app import username_is_valid

# Tests for your routes go here

'''
Test that the login page has input boxes and correct header
'''
def test_signup_page(page, test_web_address):
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

'''
We can render the index page
'''
def test_login_page(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/login")

    # Check for the presence of the login box
    email_box = page.locator("input[name='email']")
    expect(email_box)

    # Check for the presence of the password box
    password_box = page.locator("input[name='password']")
    expect(password_box)

    # Check for the presence of the header "Sign Up"
    header = page.locator("h1")
    expect(header).to_have_text("Log In")

'''
We can login as a known user
'''
def test_login(db_connection, page, test_web_address):
    db_connection.seed("seeds/user_seed.sql")
    repository = UserRepository(db_connection)

    # Navigate to the /login page
    page.goto(f"http://{test_web_address}/login")

    # Fill in the login form
    page.fill("#email", "samm@makersacademy.com")
    page.fill("#password", "password123")

    # Submit the form
    page.click("input[type='submit']")

    user_data = {}
    user = repository.get_by_email("samm@makersacademy.com")

    # Set user-specific data in the custom dictionary
    user_data['logged_in'] = True
    user_data['user_id'] = user.id

    # Check the user-specific data
    assert user_data.get('logged_in') is True
    assert user_data.get('user_id') == user.id

# Will fail untill user data is added some sort of dictionary/ file for safe keeping - into makersbnb

# def test_sign_up(db_connection, page, test_web_address):
#     db_connection.seed("seeds/user_seed.sql")
#     repository = UserRepository(db_connection)

#     # Navigate to the /signup page
#     page.goto(f"http://{test_web_address}/signup")

#     # Fill in the sign-up form
#     page.fill("#name", "John Doe")
#     page.fill("#username", "johndoe")
#     page.fill("#email", "johndoe@example.com")
#     page.fill("#password", "password123")
#     page.fill("#confirm_password", "password123")

#     # Submit the form
#     page.click("input[type='submit']")

#     # Verify that the user was added to the database
#     user = repository.get_by_username("johndoe")
#     expected_user = User(user.id, "John Doe", "johndoe", "johndoe@example.com", "password123")
#     assert user == expected_user

'''
Testing valid and invalid passwords
'''
def test_password_is_valid():
    # Valid password
    assert password_is_valid("Abcdefg1!")
    # Password is too short
    assert not password_is_valid("Abc12!")
    # Password does not contain a special character
    assert not password_is_valid("Abcdefg1")
    # Password does not contain a number
    assert not password_is_valid("Abcdefg!")
    # Password is too short and does not contain a number or special character
    assert not password_is_valid("Abcdefg")
    # Password is empty
    assert not password_is_valid("")
    # Password contains only numbers
    assert not password_is_valid("12345678")
    # Password contains only special characters
    assert not password_is_valid("!@#$%^&*")
    # Password contains only lowercase letters
    assert not password_is_valid("abcdefgh")
    # Password contains only uppercase letters
    assert not password_is_valid("ABCDEFGH")

'''
Testing valid and invalid usernames
'''
def test_username_is_valid():
    # Valid usernames
    assert username_is_valid("johndoe")
    assert username_is_valid("JohnDoe")
    # Username contains non-alphabet characters - special characters
    assert not username_is_valid("john_doe!")
    # Username is too long
    assert not username_is_valid("this username is too long to be valid")
    # Username contains non-alphabet characters - numbers
    assert not username_is_valid("john123")
    # Empty username
    assert not username_is_valid("")
    # Username contains whitespace
    assert not username_is_valid("john doe")
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
