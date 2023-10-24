from playwright.sync_api import Page, expect

# Tests for your routes go here
"""
we want to render the spaces page
"""
def test_get_spaces(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces") 
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Spaces available.")




"""
we want to tests for lists of spaces available
"""
def test_get_list_of_spaces(page, test_web_address, db_connection):
    db_connection.seed('seeds/makersbnb.sql')
    page.goto(f"http://{test_web_address}/spaces") 
    space_id_li_tags = page.locator(".space-id")
    expect(space_id_li_tags).to_have_text(["id: 1", "id: 2"])



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
    
    
    
""" we want to render add new space page """
def test_add_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_space")
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text("Add a new space.")


"""
Test adding new space using webpage, then view all spaces once added
"""

def test_add_new_space(page, test_web_address):
    page.goto(f"http://{test_web_address}/add_space")
    
    page.fill("input[name=space_name]", "Test New Space Name")
    page.fill("input[name=description]", "Test description of said place")
    page.fill("input[name=price]", '200')
    page.fill("input[name=user_id]", '1')
    page.fill("input[name=available_date]", "24/10/2023")
    page.click("text=Add space")
    page.screenshot(path='screenshot_1.png', full_page=True)
    
    h1_tag = page.locator("h1")
    expect(h1_tag).to_have_text('Spaces available.')
    page.screenshot(path='screenshot_2.png', full_page=True)

    space_id_li_tags = page.locator(".space-id")
    expect(space_id_li_tags).to_have_text(["id: 1"])
