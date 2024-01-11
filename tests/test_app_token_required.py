import pytest
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

def test_get_all_spaces(test_web_address, db_connection, browser):
    page = browser.new_page()
    db_connection.seed("seeds/makersbnb.sql")
    page = setup.login(page, test_web_address)
    expect(page).to_have_url(f"http://{test_web_address}/spaces")