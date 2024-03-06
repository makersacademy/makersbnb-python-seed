from playwright.sync_api import Page, TimeoutError, expect
import time


# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


"""
We can render the login page
"""
def test_get_login(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Login Details")


"""
We can render sign up page
"""
def test_get_sign_up(page, test_web_address):
    page.goto(f"http://{test_web_address}/sign_up")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Sign up below")

"""
We can render spaces page
"""
def test_get_spaces(page, test_web_address, db_connection):
    db_connection.seed('seeds/spaces.sql')
    page.goto(f"http://{test_web_address}/spaces")
    h1_tags = page.locator('h1')
    expect(h1_tags).to_have_text("SPACES")


"""
Check if sign up was unsuccessful - missing name
"""

def test_sign_up_unsuccessful_no_name(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/sign_up")
    page.fill("input[name='name']", "")
    page.fill("input[name='email']", 'user4@example.com')
    page.fill("input[name='password']", "abc1234")
    page.click("text = Submit")
    assert page.url == f"http://{test_web_address}/sign_up"


"""
Check if sign up was unsuccessful - missing email
"""

def test_sign_up_unsuccessful_no_email(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/sign_up")
    page.fill("input[name='name']", "user4")
    page.fill("input[name='email']", '')
    page.fill("input[name='password']", "abc1234")
    page.click("text = Submit")
    assert page.url == f"http://{test_web_address}/sign_up"

"""
Check if sign up was unsuccessful - missing password
"""

def test_sign_up_unsuccessful_no_password(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/sign_up")
    page.fill("input[name='name']", "user4")
    page.fill("input[name='email']", 'user4@example.com')
    page.fill("input[name='password']", "")
    page.click("text = Submit")
    assert page.url == f"http://{test_web_address}/sign_up"


"""
Check if sign up was successful - through to spaces page
"""

def test_sign_up_successful(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/sign_up")
    page.fill("input[name='name']", "user4")
    page.fill("input[name='email']", 'user4@example.com')
    page.fill("input[name='password']", "abc1234")

    page.click("text=Submit")

    final_url = page.url
    assert final_url == f"http://{test_web_address}/spaces"


"""
Test if sign up gets to database
"""

def test_sign_up_successful(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/sign_up")
    page.fill("input[name='name']", "user4")
    page.fill("input[name='email']", 'user4@example.com')
    page.fill("input[name='password']", "abc1234")
    page.click("text=Submit")

    user = db_connection.execute("""
        SELECT 1 AS found
        FROM users 
        WHERE email = %s
""", ("user4@example.com",))
    assert user is not None
    

"""
Check if error message appears on unsuccessful form fill
"""

def test_unsuccessful_error_message(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/sign_up")
    page.fill("input[name='name']", "")
    page.fill("input[name='email']", 'user4@example.com')
    page.fill("input[name='password']", "abc1234")
    page.click("input[type='submit']")
    error_message = page.locator(".t-errors")
    expect(error_message).to_have_text("There were errors with your submission: All fields are required.")


"""
We can check if a username exists 
"""

# def test_user_exists_sign_up(db_connection, page, test_web_address):
#     db_connection.seed("seeds/users.sql") 
#     page.goto(f"http://{test_web_address}/sign_up")
#     page.fill("input[name='name']", "user1")
#     page.fill("input[name='email']", 'user1@example.com')
#     page.fill("input[name='password']", "abc123")
#     page.click("text = Submit")
#     h1 = page.locator('h1')
#     # expect(h1).to_have_text("SPACES")
#     expect(h1).to_have_text("This user is already registered")


""" 
When we login with the correct username and password, we get redirected to the spaces page
"""
def test_successful_login(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='name']", "user3")
    page.fill("input[name='password']", "letmein!")
    page.click("text = Submit")
    h1 = page.locator('h1')
    expect(h1).to_have_text("SPACES")

def test_unsuccessful_login(db_connection, page, test_web_address):
    db_connection.seed("seeds/users.sql")
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='name']", "user2")
    page.fill("input[name='password']", "letmein!")
    page.click("text = Submit")
    h1 = page.locator("h1")
    expect(h1).to_have_text("Login Details")



"""
we are checking if we can create a new space
"""
def test_create_space(db_connection, page, test_web_address):
    db_connection.seed("seeds/spaces.sql")  
    page.goto(f"http://{test_web_address}/spaces/new")
    page.fill("input[name='name']", "London Bridge")
    page.fill("input[name='price']", "15.99")
    page.fill("input[name='description']", "It isnt the one you think it is")
    page.fill("input[name='user_id']", "1")
    page.click("text = List My Space")
    h1 = page.locator('h1')




    # # This time we click the link with the text 'Add a new book'
    # page.click("text=Add a new book")

    # # Then we fill out the field with the name attribute 'title'
    # page.fill("input[name='title']", "The Hobbit")

    # # And the field with the name attribute 'author_name'
    # page.fill("input[name='author_name']", "J.R.R. Tolkien")

    # # Finally we click the button with the text 'Create Book'
    # page.click("text=Create Book")

    # # Just as before, the virtual browser acts just like a normal browser and
    # # goes to the next page without us having to tell it to.

    # title_element = page.locator(".t-title")
    # expect(title_element).to_have_text("Title: The Hobbit")

    # author_element = page.locator(".t-author-name")
    # expect(author_element).to_have_text("Author: J.R.R. Tolkien")

