import pytest
from app import is_valid
from playwright.sync_api import Page, expect, sync_playwright

@pytest.fixture(scope="function")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch()
        yield browser
        browser.close()

class Setup:
    def __init__(self):
        pass

    def register(self, page, test_web_address):
        page.goto(f"http://{test_web_address}/")
        inputs = page.locator("input").all()
        values = [
            "TestUser4",
            "testuser@test.com",
            "TestUser4pass!",
            "TestUser4pass!"
        ]
        for input, value in zip(inputs[:-1], values):
            input.fill(value)
        inputs[-1].click()
        page.locator("a").all()[-1].click()
        return page
    
    def login(self, page, test_web_address):
        page = setup.register(page, test_web_address)
        inputs = page.locator("input").all()
        values = ["TestUser4", "TestUser4pass!"]
        for input, value in zip(inputs[:-1], values):
            input.fill(value)
        inputs[-1].click()
        return page

setup = Setup()

def test_password_is_valid():
    password = "passw0rd!"
    assert is_valid(password) == True
    password2 = "incorrect"
    assert is_valid(password2) == False    

def test_register_and_success(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page.goto(f"http://{test_web_address}/")
    inputs = page.locator("input").all()
    values = [
        "TestUser4",
        "testuser@test.com",
        "TestUser4pass!",
        "TestUser4pass!"
    ]
    for input, value in zip(inputs[:-1], values):
        input.fill(value)
    inputs[-1].click()
    # Token required here
    h1 = page.locator("h1")
    assert h1.inner_text() == "Registration Successful!"

def test_get_login(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page = setup.register(page, test_web_address)
    expect(page).to_have_url(f"http://{test_web_address}/login")
    inputs = page.locator("input").all()
    values = ["TestUser4", "TestUser4pass!"]
    for input, value in zip(inputs[:-1], values):
        input.fill(value)
    inputs[-1].click()
    expect(page).to_have_url(f"http://{test_web_address}/spaces")

def test_logout(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page = setup.login(page, test_web_address)
    links = page.locator("a").all()
    for link in links:
        if "Logout" in link.inner_text():
            link.click()
            break
    expect(page).to_have_url(f"http://{test_web_address}/logout")
    links = page.locator("a").all()
    for link in links:
        if link.get_attribute("href") == "/login":
            link.click()
            break
    assert page.url == f"http://{test_web_address}/login"
    cookies = page.context.cookies()
    assert not any(cookie["name"] == "token" and cookie["value"] for cookie in cookies)

def test_get_all_spaces(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page = setup.login(page, test_web_address)
    expect(page).to_have_url(f"http://{test_web_address}/spaces")
    h2_tags = page.locator("h2").all()
    assert "TestUser4" in h2_tags[0].inner_text()

def test_visit_a_space(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page = setup.login(page, test_web_address)
    a_tags = page.locator("a").all()
    for tag in a_tags:
        if tag.get_attribute("href") == f"/spaces/1":
            tag.click()
            break
    expect(page).to_have_url(f"http://{test_web_address}/spaces/1")

def test_list_a_new_space(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page = setup.login(page, test_web_address)
    buttons = page.locator(".button").all()
    for button in buttons:
        if button.get_attribute("href") == "spaces/new":
            button.click()
            break
    expect(page).to_have_url(f"http://{test_web_address}/spaces/new")
    all_inputs = page.locator("input").all()
    list_space_inputs = []
    for input in all_inputs:
        if input.get_attribute("name") in ["name", 
                                           "description", 
                                           "pricePerNight", 
                                           "availableFrom", 
                                           "availableTo"]:
            list_space_inputs.append(input)
        if input.get_attribute("value") == "List my Space":
            submit = input
    values = ["64 Zoo Lane", "Pet friendly detached house.", "25.00", "2024-02-01", "2024-02-05"]
    for input, value in zip(list_space_inputs, values):
        input.fill(value)
    submit.click()
    expect(page).to_have_url(f"http://{test_web_address}/spaces")
    space_button_texts = [tag.inner_text()
                     for tag in page.locator(".spacebutton").all()]
    assert "64 Zoo Lane" in space_button_texts

"""
We can render a requests index page
"""
def test_get_bookings(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page = setup.login(page, test_web_address)
    a_tags = page.locator("a").all()
    for tag in a_tags:
        if tag.get_attribute("href") == "/requests":
            tag.click()
            break
    expect(page).to_have_url(f"http://{test_web_address}/requests")

# """
# We can navigate to the booking page for a given space using /bookings POST
# """
# @pytest.mark.skip(reason="Relies on Space and SpaceRepository classes")
# def test_post_bookings(page, test_web_address, db_connection):
#     db_connection.seed("seeds/makersbnb.sql")
#     page.goto(f"http://{test_web_address}/bookings")
#     page.get_by_label("Space ID:").fill("1")
#     page.get_by_role("button").click()
#     expect(page).to_have_url(f"http://{test_web_address}/bookings/new/1")

# """
# We can render a page for creating new bookings
# """
# @pytest.mark.skip(reason="Test not written")
# def test_get_bookings_new(page, test_web_address, db_connection):
#     db_connection.seed("seeds/makersbnb.sql")
#     page.goto(f"http://{test_web_address}/bookings/new/1")

# """
# We can create a new booking using the new booking form
# """
# @pytest.mark.skip(reason="Test not written")
# def test_post_bookings_new(page, test_web_address, db_connection):
#     db_connection.seed("seeds/makersbnb.sql")
#     page.goto(f"http://{test_web_address}/bookings/new")

# """
# An error is generated if an attempt is made to book an unavailable date
# """
# @pytest.mark.skip(reason="Test not written")
# def test_post_bookings_new(page, test_web_address, db_connection):
#     db_connection.seed("seeds/makersbnb.sql")
#     page.goto(f"http://{test_web_address}/bookings/new")