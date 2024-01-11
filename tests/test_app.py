from playwright.sync_api import Page, expect

# Tests for your routes go here

# """
# We can render the index page ---> Test commented out as redundant 
# """
# def test_get_index(page, test_web_address):
#     # We load a virtual browser and navigate to the /index page
#     page.goto(f"http://{test_web_address}/index")

#     # We look at the <p> tag
#     strong_tag = page.locator("p")

#     # We assert that it has the text "This is the homepage."
#     expect(strong_tag).to_have_text("This is the homepage.")
"""
We can navigate to the spaces page
"""
def test_get_spaces_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")

    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Stay at any of these spaces.")
"""
The spaces page contains a list of spaces
"""
def test_spaces_page_shows_list(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    div_tags = page.locator("div")

    expect(div_tags).to_have_text([
        "Cozy Corner",
        "Serene Spot",
        "Tranquil Haven",
        "Peaceful Retreat"
    ])
"""
The spaces page displays the user's name
"""
def test_user_name_displays_on_page(page, test_web_address):
    page.goto(f"http://{test_web_address}/login")
    page.fill("input[name='email']", "test@test.com")
    page.fill("input[name='password']", "password1")
    page.click('input[type="submit"][value="Login"]') #Zak, I've fixed this
    
    b_tag = page.locator("b")

    expect(b_tag).to_have_text("You are logged in as test@test.com")

"""
Test that homepage appears
"""
def test_homepage_appears(page, test_web_address, web_client):
    page.goto(f"http://{test_web_address}/")
    response = web_client.get("/")
    h1_tag = page.locator("h1")

    expect(h1_tag).to_have_text("Welcome to MakersBnB")

    assert response.status_code == 200