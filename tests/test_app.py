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

"""
We can get spaces from the /space page
"""

def test_get_space(page, test_web_address, db_connection):
    db_connection.seed("seeds/bnb.sql")
    #we load a virtual browser and navigate to the /space page
    page.goto(f"http://{test_web_address}/spaces")
    #we look at the h1 tag
    h3_tag = page.locator("h3")
    expect(h3_tag).to_have_text(['Bagend', 'Isengard', 'Minas Tirith'] )
    # p_tag = page.locator("p")
    # expect(p_tag).to_have_text(['Hobbit Hole', 'Wizards Tower', 'Big White City'])
    # p_tag = page.locator("p")
    # expect(p_tag).to_have_text([50, 150, 200])

"""
When calling /spaces/space_id
Takes user to page with space information
"""

def test_get_single_space(page, test_web_address, db_connection):
    db_connection.seed("seeds/bnb.sql")
    page.goto(f"http://{test_web_address}/single_space/1")
    h3_tag = page.locator("h3")
    expect(h3_tag).to_have_text('Bagend')
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(['Description: Hobbit Hole', 'Price: £50', 'Availability: 25-12-23 to 30-12-23'])
    # p_tag = page.locator("p")
    # expect(p_tag).to_have_text(['Price: £50'])

    page.goto(f"http://{test_web_address}/single_space/2")
    h3_tag = page.locator("h3")
    expect(h3_tag).to_have_text(['Isengard'])
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(['Description: Wizards Tower', 'Price: £150', 'Availability: 25-12-23 to 30-12-23'])
    # p_tag = page.locator("p")
    # expect(p_tag).to_have_text('Price: £'[150])

def test_add_new_space(page, test_web_address, db_connection, web_client):
    db_connection.seed("seeds/bnb.sql")
    page.goto(f"http://{test_web_address}/spaces/new_space")
    response = web_client.post('/spaces/new_space', data = {
        "name": "No Orcs Allowed",
        "description": "What it says on the tin",
        "price": 525,
        "start_date": "13-12-23",
        "end_date": "14-12-23"
        })
    assert response.status_code == 302
    redirected_url = response.headers["Location"]
    redirected_response = web_client.get(redirected_url)
    

    assert redirected_response.status_code == 200
    assert redirected_response.data.decode("utf-8").strip() == ""