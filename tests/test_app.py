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
    expect(strong_tag).to_have_text("Welcome to SSJBNB")


"""
Render listings page
"""

def test_get_listings(page, test_web_address,db_connection):
    db_connection.seed("seeds/spaces.sql")
    # We load a virtual browser and navigate to the /listings page
    page.goto(f"http://{test_web_address}/listings")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the listings page."
    expect(strong_tag).to_have_text(["Apartment 1", "Description 1", "Apartment 2", "Description 2"])


"""
test web page has a login form
"""
def test_web_page_has_a_login_form(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    # login = page.locator("button").first()
    # expect(login).to_have_text("Login")
    login = page.locator("id=1")
    expect(login).to_have_id("1")



"""
test web page has a register form
"""
def test_web_page_has_a_register_form(page, test_web_address):
    page.goto(f"http://{test_web_address}/index")
    sign_up = page.locator("id=2")
    expect(sign_up).to_have_id("2")

"""
test login button redirect to login page
"""
# def test_login_button_redirects_to_login_page(web_client, page, test_web_address):
#     response =  web_client.get('/login')
#     assert response.status_code == 200
#     page.goto(f"http://{test_web_address}/index")
#     # page.locator("a")
#     # link = page.click()
#     button = page.locator("id=1")
#     new_page = button.click()
#     expect(new_page).to_have_url(f"http://{test_web_address}/login")  
    
    


"""
test web page has a listing button 
"""
# def test_wep_page_has_listing_button(page, test_web_address):
#     page.goto(f"http://{test_web_address}/listings")
#     button = page.locator("Button")
#     expect(button).to_have_text("add a listing")



# def test_adding_a_listing_to_table_via_post_request(web_client):
#     response =  web_client.post('/listings', data={"Apartment 1", "Description 1", "Apartment 2", "Description 2"})
#     assert response.status_code == 200
#     assert response.data.decode == '"Apartment 1", "Description 1", "Apartment 2", "Description 2"'

def test_add(page, test_web_address, db_connection):
    db_connection.seed("seeds/spaces.sql")
    page.goto(f"http://{test_web_address}/listings") 
    page.fill("input[name=name]", "Apartment 3")
    page.fill("input[name=description]", "Description 3")
    page.fill("input[name=price]", "100")
    page.fill("input[name=date_from]", "25/10/2023")
    page.fill("input[name=date_to]", "25/10/2023")

    page.click("text='add a listing'")
    
    p_tag = page.locator("p")
    expect(p_tag).to_have_text(["Apartment 1", "Description 1", "Apartment 2", "Description 2", "Apartment 3", "Description 3"])
